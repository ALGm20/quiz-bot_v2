"""
bot.py — Final Exam Quiz Bot v2
"""
import logging, asyncio, os, random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes, ConversationHandler)
from database import Database

logging.basicConfig(format="%(asctime)s — %(levelname)s — %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
os.makedirs("/data", exist_ok=True)
db = Database("/data/quiz_bot.db")
WAITING_NAME = 1

# ══════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════

def shuffle_options(q_obj: dict, user_seed: int) -> dict:
    """خلط الخيارات لكل طالب بشكل مختلف — anti-cheat"""
    opts = [("A",q_obj["option_a"]),("B",q_obj["option_b"]),
            ("C",q_obj["option_c"]),("D",q_obj["option_d"])]
    correct_text = q_obj[f"option_{q_obj['correct_answer'].lower()}"]
    rng = random.Random(user_seed + q_obj["id"])
    rng.shuffle(opts)
    letters = ["A","B","C","D"]
    new_q = dict(q_obj)
    new_q["option_a"] = opts[0][1]
    new_q["option_b"] = opts[1][1]
    new_q["option_c"] = opts[2][1]
    new_q["option_d"] = opts[3][1]
    for i,(_, txt) in enumerate(opts):
        if txt == correct_text:
            new_q["correct_answer"] = letters[i]
            break
    return new_q

def question_keyboard(q_obj):
    qid = q_obj["id"]
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(f"🔵  A)  {q_obj['option_a']}", callback_data=f"ans_A_{qid}")],
        [InlineKeyboardButton(f"🟢  B)  {q_obj['option_b']}", callback_data=f"ans_B_{qid}")],
        [InlineKeyboardButton(f"🟡  C)  {q_obj['option_c']}", callback_data=f"ans_C_{qid}")],
        [InlineKeyboardButton(f"🔴  D)  {q_obj['option_d']}", callback_data=f"ans_D_{qid}")],
    ])

def sections_menu(student_id: int):
    sections = db.get_sections()
    rows = []
    for sec in sections:
        cnt = db.count_q(sec["id"])
        prog = db.get_section_progress(student_id, sec["id"])
        emoji = sec["emoji"] or "📖"
        badge = f"✅ {prog['pct']}%" if (prog and prog["assessed"]) else "📝 لم يُقيَّم"
        rows.append([InlineKeyboardButton(
            f"{emoji}  {sec['name']}   ┃   {badge}   ┃   {cnt}س",
            callback_data=f"sec_{sec['id']}")])
    return InlineKeyboardMarkup(rows)

async def notify_teacher(ctx, text: str):
    ids_str = os.environ.get("TEACHER_CHAT_ID","")
    if not ids_str: return
    for tid in ids_str.split(","):
        tid = tid.strip()
        if tid:
            try: await ctx.bot.send_message(chat_id=tid, text=text)
            except Exception as e: logger.warning(f"Notify failed {tid}: {e}")

# ══════════════════════════════════════════════════════════════════
# /start
# ══════════════════════════════════════════════════════════════════

async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    student = db.get_student_by_telegram(uid)
    if student:
        await update.message.reply_text(
            f"👋 *أهلاً {student['full_name']}!*\n\nاختر سكشناً 👇\n"
            f"_(✅ = تم التقييم   |   📝 = لم يُقيَّم)_",
            parse_mode="Markdown", reply_markup=sections_menu(student["id"]))
        return ConversationHandler.END
    await update.message.reply_text(
        "🎓 *مرحباً بك في بوت الاختبارات!*\n\nأرسل *اسمك الثلاثي* للتسجيل:",
        parse_mode="Markdown")
    return WAITING_NAME

async def receive_name(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    name = update.message.text.strip()
    uid  = update.effective_user.id
    if db.get_student_by_telegram(uid):
        await update.message.reply_text("أنت مسجّل مسبقاً. /start")
        return ConversationHandler.END
    if len(name) < 5 or any(c.isdigit() for c in name):
        await update.message.reply_text("⚠️ أدخل اسمك الثلاثي بشكل صحيح.\nمثال: `أحمد محمد علي`",
                                        parse_mode="Markdown")
        return WAITING_NAME
    db.register_new_student(name, uid)
    student = db.get_student_by_telegram(uid)
    await update.message.reply_text(
        f"✅ *تم التسجيل!* أهلاً *{name}* 🎉\n\nاختر سكشناً للبدء 👇",
        parse_mode="Markdown", reply_markup=sections_menu(student["id"]))
    return ConversationHandler.END

async def cmd_cancel(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم الإلغاء. /start")
    return ConversationHandler.END

# ══════════════════════════════════════════════════════════════════
# SECTIONS
# ══════════════════════════════════════════════════════════════════

async def cb_section(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    uid = update.effective_user.id
    student = db.get_student_by_telegram(uid)
    if not student:
        await q.edit_message_text("يرجى التسجيل /start"); return

    sec_id = int(q.data.split("_")[1])
    section = db.get_section(sec_id)
    cnt = db.count_q(sec_id)
    prog = db.get_section_progress(student["id"], sec_id)
    emoji = section["emoji"] or "📖"

    if not prog or not prog["assessed"]:
        await q.edit_message_text(
            f"{emoji} *{section['name']}*\n\n📝 لم تُجرِ التقييم بعد.\nابدأ الاختبار لمعرفة مستواك!",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"🎯 ابدأ التقييم ({cnt} سؤال)", callback_data=f"assess_{sec_id}")],
                [InlineKeyboardButton("🔙 رجوع", callback_data="back_sections")],
            ]))
    else:
        pct = prog["pct"]; score = prog["score"]; total = prog["total_q"]
        bar = "█"*round(pct/10) + "░"*(10-round(pct/10))
        can, days_left = db.can_reassess(student["id"], sec_id)
        reassess_btn = (InlineKeyboardButton("🔄 أعد التقييم", callback_data=f"reassess_{sec_id}")
                       if can else
                       InlineKeyboardButton(f"⏳ إعادة التقييم بعد {days_left} يوم", callback_data="blocked"))
        await q.edit_message_text(
            f"{emoji} *{section['name']}*\n\n📊 نتيجتك:\n`{bar}` {pct}%  ({score}/{total})\n\nاختر:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⚡️ 10 أسئلة عشوائية", callback_data=f"train_{sec_id}_10")],
                [InlineKeyboardButton("📋 كل الأسئلة",        callback_data=f"train_{sec_id}_all")],
                [reassess_btn],
                [InlineKeyboardButton("🔙 رجوع",              callback_data="back_sections")],
            ]))

async def cb_back_sections(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    uid = update.effective_user.id
    student = db.get_student_by_telegram(uid)
    if not student:
        await q.edit_message_text("يرجى التسجيل /start"); return
    await q.edit_message_text(
        f"📚 *اختر السكشن — {student['full_name']}*",
        parse_mode="Markdown", reply_markup=sections_menu(student["id"]))

async def cb_blocked(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("⏳ لم يحن وقت إعادة التقييم بعد!", show_alert=True)

# ══════════════════════════════════════════════════════════════════
# ASSESSMENT
# ══════════════════════════════════════════════════════════════════

async def cb_assess_section(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    uid = update.effective_user.id
    student = db.get_student_by_telegram(uid)
    if not student:
        await q.edit_message_text("يرجى التسجيل /start"); return
    sec_id = int(q.data.split("_")[1])
    section = db.get_section(sec_id)
    questions = list(db.get_questions(sec_id))
    random.shuffle(questions)
    db.save_session(uid, "assessment", sec_id, questions, 0, 0, len(questions))
    await q.edit_message_text(
        f"{section['emoji'] or '📖'} *تقييم: {section['name']}*\n\n📝 {len(questions)} سؤال\n\nابدأ! 💪",
        parse_mode="Markdown")
    await asyncio.sleep(0.6)
    await _send_question(update, ctx)

async def cb_reassess_section(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    uid = update.effective_user.id
    student = db.get_student_by_telegram(uid)
    if not student:
        await q.edit_message_text("يرجى التسجيل /start"); return
    sec_id = int(q.data.split("_")[1])
    can, days_left = db.can_reassess(student["id"], sec_id)
    if not can:
        await q.answer(f"⏳ يمكنك إعادة التقييم بعد {days_left} يوم", show_alert=True); return
    section = db.get_section(sec_id)
    questions = list(db.get_questions(sec_id))
    random.shuffle(questions)
    db.save_session(uid, "assessment", sec_id, questions, 0, 0, len(questions))
    await q.edit_message_text(
        f"{section['emoji'] or '📖'} *إعادة تقييم: {section['name']}*\n\n📝 {len(questions)} سؤال\n\nابدأ! 💪",
        parse_mode="Markdown")
    await asyncio.sleep(0.6)
    await _send_question(update, ctx)

# ══════════════════════════════════════════════════════════════════
# TRAINING
# ══════════════════════════════════════════════════════════════════

async def cb_train_section(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    uid = update.effective_user.id
    student = db.get_student_by_telegram(uid)
    if not student:
        await q.edit_message_text("يرجى التسجيل /start"); return
    parts = q.data.split("_")
    sec_id = int(parts[1])
    limit = None if parts[2]=="all" else int(parts[2])
    questions = list(db.get_questions(sec_id, limit))
    random.shuffle(questions)
    db.save_session(uid, "training", sec_id, questions, 0, 0, len(questions))
    section = db.get_section(sec_id)
    await q.edit_message_text(
        f"{section['emoji'] or '📖'} *{section['name']}*\n\n🎯 {len(questions)} سؤال — ابدأ! 🚀",
        parse_mode="Markdown")
    await asyncio.sleep(0.6)
    await _send_question(update, ctx)

# ══════════════════════════════════════════════════════════════════
# SEND QUESTION
# ══════════════════════════════════════════════════════════════════

async def _send_question(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    sess = db.get_session(uid)
    if not sess:
        try: await update.callback_query.edit_message_text("⚠️ انتهت الجلسة. /start")
        except: pass
        return

    idx = sess["idx"]; total = sess["total"]
    if idx >= total:
        if sess["mode"] == "assessment": await _finish_assessment(update, ctx, sess)
        else: await _finish_training(update, ctx, sess)
        return

    q_obj = sess["qs"][idx]
    shuffled = shuffle_options(q_obj, uid)
    filled = round((idx/total)*10) if total else 0
    bar = "█"*filled + "░"*(10-filled)
    pct = round((idx/total)*100)
    icon = "🎯" if sess["mode"]=="assessment" else "📚"
    text = f"{icon}  *سؤال {idx+1} من {total}*\n`{bar}` {pct}%\n\n❓ *{q_obj['question_text']}*"

    try:
        await update.callback_query.edit_message_text(
            text, parse_mode="Markdown", reply_markup=question_keyboard(shuffled))
    except Exception as e:
        logger.warning(f"edit failed: {e}")
        try:
            await update.effective_chat.send_message(
                text, parse_mode="Markdown", reply_markup=question_keyboard(shuffled))
        except Exception as e2:
            logger.error(f"send failed: {e2}")

# ══════════════════════════════════════════════════════════════════
# ANSWER
# ══════════════════════════════════════════════════════════════════

async def cb_answer(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    uid = update.effective_user.id
    sess = db.get_session(uid)
    if not sess:
        await q.edit_message_text("⚠️ انتهت الجلسة. /start",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 رجوع", callback_data="back_sections")]])); return

    parts = q.data.split("_")
    user_ans = parts[1].upper()
    idx = sess["idx"]
    q_obj = sess["qs"][idx]
    shuffled = shuffle_options(q_obj, uid)
    correct = shuffled["correct_answer"].upper()
    is_right = (user_ans == correct)

    new_score = sess["score"] + (1 if is_right else 0)
    new_idx = idx + 1
    db.update_session(uid, new_idx, new_score)

    color = {"A":"🔵","B":"🟢","C":"🟡","D":"🔴"}
    opt = {"A":shuffled["option_a"],"B":shuffled["option_b"],"C":shuffled["option_c"],"D":shuffled["option_d"]}

    if is_right:
        result = f"✅ *صحيح!*\n{color[correct]}  {correct})  {opt[correct]}"
    else:
        result = (f"❌ *خطأ!*\nاخترت: {color[user_ans]}  {user_ans})  {opt[user_ans]}\n\n"
                  f"✅ الصحيحة: {color[correct]}  {correct})  {opt[correct]}")

    exp = q_obj.get("explanation","") or ""
    exp_line = f"\n\n💡 _{exp}_" if exp else ""
    remaining = sess["total"] - new_idx
    btn = f"التالي ← ({new_idx+1}/{sess['total']})" if remaining>0 else "عرض النتيجة 🏁"

    await q.edit_message_text(
        f"❓ *{q_obj['question_text']}*\n\n{'─'*18}\n\n{result}{exp_line}",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(btn, callback_data="next_q")]]))

async def cb_next_q(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    uid = update.effective_user.id
    sess = db.get_session(uid)
    if not sess:
        await q.edit_message_text("⚠️ انتهت الجلسة. /start"); return
    if sess["idx"] >= sess["total"]:
        if sess["mode"]=="assessment": await _finish_assessment(update, ctx, sess)
        else: await _finish_training(update, ctx, sess)
    else:
        await _send_question(update, ctx)

# ══════════════════════════════════════════════════════════════════
# FINISH ASSESSMENT
# ══════════════════════════════════════════════════════════════════

async def _finish_assessment(update: Update, ctx: ContextTypes.DEFAULT_TYPE, sess: dict):
    uid = update.effective_user.id
    student = db.get_student_by_telegram(uid)
    sec_id = sess["sec_id"]
    db.delete_session(uid)

    score = sess["score"]; total = sess["total"]
    pct = round((score/total)*100) if total else 0
    db.save_section_assessment(student["id"], sec_id, score, total)

    section = db.get_section(sec_id)
    emoji = section["emoji"] or "📖"

    if pct>=90: grade,icon = "ممتاز 🏆","🌟"
    elif pct>=75: grade,icon = "جيد جداً 🥈","✅"
    elif pct>=60: grade,icon = "جيد 🥉","👍"
    elif pct>=50: grade,icon = "مقبول 📘","⚠️"
    else: grade,icon = "يحتاج مراجعة 📖","❗"

    filled = round(pct/10)
    bar = "█"*filled + "░"*(10-filled)
    stars = "⭐"*max(1, round(pct/20))

    uname = update.effective_user.username
    uname_txt = f"@{uname}" if uname else "لا يوجد"
    divider = "──────────────────────"
    await notify_teacher(ctx,
        f"📋 نتيجة تقييم جديدة\n{divider}\n"
        f"👤 الاسم: {student['full_name']}\n"
        f"🔗 الحساب: {uname_txt}\n{divider}\n"
        f"{emoji} السكشن: {section['name']}\n"
        f"📊 النتيجة: {score}/{total} ({pct}%)\n"
        f"التقدير: {grade}")

    student_obj = db.get_student_by_telegram(uid)
    await update.callback_query.edit_message_text(
        f"{icon} *انتهى التقييم: {section['name']}*\n\n"
        f"`{bar}` {pct}%\n\n"
        f"✅ صحيح: *{score}*   ❌ خطأ: *{total-score}*\n"
        f"📊 *{score}/{total}*\n\n{stars}  *{grade}*\n\n"
        f"تم الحفظ ✅ — اختر سكشناً للتدريب 👇",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⚡️ تدريب الآن",    callback_data=f"train_{sec_id}_10")],
            [InlineKeyboardButton("📚 سكشن آخر",      callback_data="back_sections")],
        ]))

# ══════════════════════════════════════════════════════════════════
# FINISH TRAINING
# ══════════════════════════════════════════════════════════════════

async def _finish_training(update: Update, ctx: ContextTypes.DEFAULT_TYPE, sess: dict):
    uid = update.effective_user.id
    db.delete_session(uid)
    score = sess["score"]; total = sess["total"]
    pct = round((score/total)*100) if total else 0
    if pct==100: grade="ممتاز 🏆"
    elif pct>=90: grade="ممتاز 🥇"
    elif pct>=75: grade="جيد جداً 🥈"
    elif pct>=60: grade="جيد 🥉"
    else: grade="راجع المادة 📖"
    filled = round(pct/10)
    bar = "█"*filled + "░"*(10-filled)
    stars = "⭐"*max(1,round(pct/20))
    sec_id = sess.get("sec_id")
    rows = []
    if sec_id: rows.append([InlineKeyboardButton("🔄 أعد التدريب", callback_data=f"train_{sec_id}_10")])
    rows.append([InlineKeyboardButton("📚 سكشن آخر", callback_data="back_sections")])
    await update.callback_query.edit_message_text(
        f"🎉 *انتهى التدريب!*\n\n`{bar}` {pct}%\n\n"
        f"✅ صحيح: *{score}*   ❌ خطأ: *{total-score}*\n"
        f"📊 *{score}/{total}*\n\n{stars}  *{grade}*",
        parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(rows))

# ══════════════════════════════════════════════════════════════════
# ADMIN
# ══════════════════════════════════════════════════════════════════

async def cmd_myid(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    uname = update.effective_user.username or "لا يوجد"
    await update.message.reply_text(
        f"🆔 *معلوماتك:*\n\nالـ ID: `{uid}`\nاليوزرنيم: @{uname}\n\n"
        f"أضفه في Railway:\n`TEACHER_CHAT_ID` = `{uid}`",
        parse_mode="Markdown")

async def cmd_stats(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    st = db.stats()
    url = os.environ.get("RAILWAY_PUBLIC_DOMAIN","")
    url = f"https://{url}" if url else "—"
    await update.message.reply_text(
        f"📊 *إحصائيات:*\n\n👥 طلاب: {st['students']}\n"
        f"📦 سكشنات: {st['sections']}\n❓ أسئلة: {st['questions']}\n\n"
        f"🌐 الداشبورد: {url}", parse_mode="Markdown")

async def guard(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if not db.get_student_by_telegram(update.effective_user.id):
        await update.message.reply_text("يرجى التسجيل /start")

# ══════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════

def main():
    TOKEN = os.environ.get("BOT_TOKEN","PUT_YOUR_TOKEN_HERE")
    app = Application.builder().token(TOKEN).build()
    conv = ConversationHandler(
        entry_points=[CommandHandler("start", cmd_start)],
        states={WAITING_NAME:[MessageHandler(filters.TEXT & ~filters.COMMAND, receive_name)]},
        fallbacks=[CommandHandler("cancel", cmd_cancel)])
    app.add_handler(conv)
    app.add_handler(CommandHandler("stats", cmd_stats))
    app.add_handler(CommandHandler("myid",  cmd_myid))
    app.add_handler(CallbackQueryHandler(cb_section,         pattern=r"^sec_\d+$"))
    app.add_handler(CallbackQueryHandler(cb_back_sections,   pattern="^back_sections$"))
    app.add_handler(CallbackQueryHandler(cb_assess_section,  pattern=r"^assess_\d+$"))
    app.add_handler(CallbackQueryHandler(cb_reassess_section,pattern=r"^reassess_\d+$"))
    app.add_handler(CallbackQueryHandler(cb_train_section,   pattern=r"^train_\d+_(all|\d+)$"))
    app.add_handler(CallbackQueryHandler(cb_answer,          pattern=r"^ans_[AaBbCcDd]_\d+$"))
    app.add_handler(CallbackQueryHandler(cb_next_q,          pattern="^next_q$"))
    app.add_handler(CallbackQueryHandler(cb_blocked,         pattern="^blocked$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, guard))
    logger.info("Bot v2 started ✅")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
