"""
populate_db.py — أسئلة الفاينل (زمن 2 مشترك)
شغّله مرة واحدة فقط
"""
import os
from database import Database
os.makedirs("/data", exist_ok=True)
db = Database("/data/quiz_bot.db")

# مسح القديم لتجنب التكرار
with db._connect() as c:
    c.execute("PRAGMA foreign_keys = OFF")
    c.execute("DELETE FROM questions")
    c.execute("DELETE FROM sections")
    c.execute("PRAGMA foreign_keys = ON")
print("🗑️ تم مسح الأسئلة القديمة")

QUESTIONS = [

    # ══ سكشن الفيروسات 🦠 ══
    {"section":"الفيروسات — Virology","section_emoji":"🦠",
     "section_description":"Virus structure, classification, life cycle, transmission",
     "question":"'Virus' is from the Greek meaning 'poison' and was initially described by Edward Jenner in 1798.",
     "a":"Virus","b":"Bacteria","c":"Fungi","d":"Mollicutes",
     "answer":"A","explanation":"The term virus comes from Latin/Greek meaning poison. Edward Jenner described it in 1798."},

    {"section":"الفيروسات — Virology",
     "question":"A virus is a package of genetic information protected by a protein shell for delivery into a host cell.",
     "a":"Genetic material and protein shell","b":"Genetic material and envelope",
     "c":"DNA and protein shell","d":"RNA and protein shell",
     "answer":"A","explanation":"Viruses consist of genetic information (DNA or RNA) protected by a protein shell (capsid)."},

    {"section":"الفيروسات — Virology",
     "question":"Poxviruses is:",
     "a":"Complex","b":"Naked","c":"Enveloped","d":"Both A and C",
     "answer":"A","explanation":"Poxviruses have a complex irregular morphology — neither icosahedral nor helical."},

    {"section":"الفيروسات — Virology",
     "question":"Which virus has complex capsid head and tail structures?",
     "a":"Bacteriophages","b":"Coronavirus","c":"HIV","d":"Poxvirus",
     "answer":"A","explanation":"Bacteriophages have complex structures with a head (icosahedral) and tail apparatus."},

    {"section":"الفيروسات — Virology",
     "question":"Which type of virus has a capsid that directly contains DNA or RNA with no envelope?",
     "a":"Naked","b":"Complex","c":"Enveloped","d":"Both A and C",
     "answer":"A","explanation":"Naked viruses have only a capsid enclosing the nucleic acid — no lipid envelope."},

    {"section":"الفيروسات — Virology",
     "question":"Structural subunits containing several proteins that aggregate to produce the viral capsid are called:",
     "a":"Proteins","b":"Capsomeres","c":"Amino acids","d":"Both A and C",
     "answer":"B","explanation":"Capsomeres are the protein subunits that self-assemble to form the complete viral capsid."},

    {"section":"الفيروسات — Virology",
     "question":"Linking of viral capsid with nucleic acid results in:",
     "a":"Cell membrane","b":"Nucleocapsid","c":"Amino acids","d":"Both A and C",
     "answer":"B","explanation":"Nucleocapsid = capsid (protein coat) + nucleic acid (genome) combined together."},

    {"section":"الفيروسات — Virology",
     "question":"Viral lipid envelopes are derived from:",
     "a":"Viral cellular membranes","b":"Host cellular membranes",
     "c":"Cell wall","d":"Viral capsid",
     "answer":"B","explanation":"The viral envelope is derived from the host cell membrane during the budding process."},

    {"section":"الفيروسات — Virology",
     "question":"Herpesviridae is _______, while Coxsackie is _______.",
     "a":"Class and phylum","b":"Family and species",
     "c":"Family and virus","d":"Species and genus",
     "answer":"C","explanation":"Herpesviridae is a family (-viridae suffix). Coxsackievirus is a specific virus within Picornaviridae."},

    {"section":"الفيروسات — Virology",
     "question":"Poliovirus is _______, while Herpesvirus is _______.",
     "a":"ssDNA and dsRNA","b":"dsRNA and ssDNA",
     "c":"ssDNA and dsDNA","d":"Circular DNA and dsDNA",
     "answer":"C","explanation":"Poliovirus (Picornaviridae) has ssRNA genome. Herpesvirus (Herpesviridae) has dsDNA genome."},

    {"section":"الفيروسات — Virology",
     "question":"'Human lung cells - Influenza virus' is _______, while 'Various cells of all mammals - Rabies' is _______.",
     "a":"Intermediate and Restricted","b":"Tropisms and Intermediate",
     "c":"Restricted and Broad","d":"Broad and Intermediate",
     "answer":"C","explanation":"Influenza has restricted tropism (lung cells). Rabies has broad tropism (various mammalian cells)."},

    {"section":"الفيروسات — Virology",
     "question":"HIV, Hepatitis B and C, CMV are transmitted by _______, while HAV by _______.",
     "a":"Vector and fomites","b":"Airborne and foodborne",
     "c":"Parenteral and foodborne","d":"Direct contact and vector",
     "answer":"C","explanation":"HIV/HBV/HCV/CMV = parenteral (blood, sexual). HAV = foodborne/fecal-oral route."},

    {"section":"الفيروسات — Virology",
     "question":"In the viral life cycle, binding of virus with host cell is called _______, and digest capsid is called _______.",
     "a":"Adsorption and release","b":"Adsorption and assembly",
     "c":"Adsorption and uncoating","d":"Penetration and release",
     "answer":"C","explanation":"Step 1: Adsorption (attachment). Step 3: Uncoating (removal of capsid to release genome)."},

    {"section":"الفيروسات — Virology",
     "question":"Copying of genome and protein synthesis occurs during which stage of viral replication?",
     "a":"Adsorption","b":"Penetration","c":"Replication","d":"Release",
     "answer":"C","explanation":"During the replication/biosynthesis stage, viral genomes and proteins are synthesized using host machinery."},

    {"section":"الفيروسات — Virology",
     "question":"Viral capsid reforms and packaging of genome occurs during:",
     "a":"Adsorption","b":"Penetration","c":"Assembly","d":"Release",
     "answer":"C","explanation":"Assembly is when new capsids are formed and viral genomes are packaged inside them."},

    # ══ سكشن الأيض ⚗️ ══
    {"section":"العمليات الأيضية — Metabolism","section_emoji":"⚗️",
     "section_description":"Metabolism, Enzymes, Glycolysis, Krebs, ETC, Fermentation",
     "question":"A sequence of enzymatically catalyzed chemical reactions in a cell is called:",
     "a":"Anabolism","b":"Catabolism","c":"Replication","d":"Metabolic pathway",
     "answer":"D","explanation":"A metabolic pathway is a series of enzymatically catalyzed reactions leading to a specific product."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"_______ is energy-releasing processes, while _______ is energy-using processes.",
     "a":"Oxidation and reduction","b":"Metabolism and anabolism",
     "c":"Anabolism and metabolism","d":"Catabolism and anabolism",
     "answer":"D","explanation":"Catabolism = energy-releasing (breakdown). Anabolism = energy-using (synthesis)."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"Simple molecules include _______, while complex molecules include _______.",
     "a":"Amino acids and fatty acids","b":"Glucose and amino acids",
     "c":"Lipids and proteins","d":"Glucose and proteins",
     "answer":"A","explanation":"Simple molecules: amino acids, glucose, fatty acids. Complex: proteins, polysaccharides, lipids."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"The collision theory states that chemical reactions can occur when atoms, ions, and molecules:",
     "a":"Are oxidized","b":"Are reduced","c":"Are replicated","d":"Collide",
     "answer":"D","explanation":"Collision theory: reactions occur when molecules collide with sufficient energy (≥ activation energy)."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"The frequency of collisions with enough energy to bring about a reaction is called:",
     "a":"Oxidation rate","b":"Reduction rate","c":"Inhibition rate","d":"Reaction rate",
     "answer":"D","explanation":"Reaction rate = frequency of effective collisions that result in a chemical reaction."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"Apoenzyme plus cofactor produces:",
     "a":"Coenzyme","b":"Holoenzyme","c":"Cofactor","d":"Apoenzyme",
     "answer":"B","explanation":"Holoenzyme = Apoenzyme (protein part) + Cofactor (non-protein part) = fully active enzyme."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"_______ is removal of atoms without hydrolysis. _______ is joining of molecules using ATP.",
     "a":"Lyase and Ligase","b":"Hydrolase and Isomerase",
     "c":"Isomerase and Transferase","d":"Ligase and Lyase",
     "answer":"A","explanation":"Lyase = removes atoms without hydrolysis. Ligase = joins molecules using ATP."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"Temperature and pH can denature:",
     "a":"Enzymes","b":"Proteins","c":"Amino acids","d":"All of the above",
     "answer":"A","explanation":"Extreme temperature and pH change disrupt enzyme 3D structure → denaturation → loss of function."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"Oxidation is removal of electrons, while Reduction is gain of electrons.",
     "a":"Anabolism and catabolism","b":"Reduction and Oxidation",
     "c":"Enzyme and proteins","d":"Oxidation and Reduction",
     "answer":"D","explanation":"Oxidation = loss of electrons (or H). Reduction = gain of electrons (or H). Together = redox reaction."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"A redox reaction is:",
     "a":"Only an oxidation reaction","b":"Only a reduction reaction",
     "c":"A metabolic reaction","d":"An oxidation reaction paired with a reduction reaction",
     "answer":"D","explanation":"Redox reactions always occur in pairs — one molecule is oxidized while another is reduced."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"The breakdown of carbohydrates to release energy is carried out through which processes?",
     "a":"Glycolysis","b":"Krebs cycle","c":"Electron transport chain","d":"All of the above",
     "answer":"D","explanation":"Carbohydrate catabolism = Glycolysis + Krebs cycle + Electron transport chain (all three)."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"The oxidation of glucose to pyruvic acid producing ATP and NADH is:",
     "a":"Glycolysis","b":"Krebs cycle","c":"Electron transport chain","d":"All of the above",
     "answer":"A","explanation":"Glycolysis: glucose → 2 pyruvate + 2 ATP (net) + 2 NADH in the cytoplasm."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"Net energy (ATP) produced from glycolysis is:",
     "a":"10 ATP","b":"2 ATP","c":"8 ATP","d":"4 ATP",
     "answer":"B","explanation":"Glycolysis net = 2 ATP (4 produced - 2 consumed = 2 net ATP)."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"Energy consumed (used) during glycolysis is:",
     "a":"10 ATP","b":"2 ATP","c":"8 ATP","d":"4 ATP",
     "answer":"B","explanation":"Glycolysis uses 2 ATP in the preparatory phase (energy investment phase)."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"Lipids are converted to fatty acids by _______, while proteins are converted to amino acids by _______.",
     "a":"Oxidase and reductase","b":"Protease and lipase",
     "c":"Lipase and proteases","d":"Lipase and reductase",
     "answer":"C","explanation":"Lipase breaks down lipids → glycerol + fatty acids. Proteases break down proteins → amino acids."},

    {"section":"العمليات الأيضية — Metabolism",
     "question":"Lipids enter the Krebs cycle via:",
     "a":"Pyruvic acids","b":"Glucophosphate","c":"Acetyl CoA","d":"Pyruvate",
     "answer":"C","explanation":"Fatty acids → beta-oxidation → Acetyl CoA → enters Krebs cycle directly."},

    # ══ سكشن الوراثة 🧬 ══
    {"section":"علم الوراثة — Genetics","section_emoji":"🧬",
     "section_description":"Genetics, DNA, RNA, Replication, Transcription, Translation",
     "question":"The molecular study of genomes is called:",
     "a":"Genomics","b":"Genome","c":"Genetics","d":"Heredity",
     "answer":"A","explanation":"Genomics = molecular study of genomes including structure, function, and evolution."},

    {"section":"علم الوراثة — Genetics",
     "question":"Conversion of RNA to DNA in HIV is done by:",
     "a":"Reverse translation","b":"Transcription",
     "c":"Reverse transcription","d":"Replication",
     "answer":"C","explanation":"HIV uses reverse transcriptase to convert its RNA genome into DNA (reverse transcription)."},

    {"section":"علم الوراثة — Genetics",
     "question":"Conversion of mRNA to protein is done by:",
     "a":"Translation","b":"Transcription","c":"Reverse transcription","d":"Replication",
     "answer":"A","explanation":"Translation = converting mRNA code into a protein sequence at the ribosome."},

    {"section":"علم الوراثة — Genetics",
     "question":"DNA consists of bases and:",
     "a":"Sugar + phosphate","b":"Adenine + cytosine",
     "c":"Sugar + guanine","d":"Phosphate + thymine",
     "answer":"A","explanation":"DNA = 4 nitrogenous bases + deoxyribose sugar + phosphate group (forming nucleotides)."},

    # ══ سكشن البيئة 🌍 ══
    {"section":"الأحياء الدقيقة والبيئة — Environmental","section_emoji":"🌍",
     "section_description":"Environmental microbiology, soil, ecology, nitrogen fixation, UV",
     "question":"Study of the interrelationships among microorganisms and the environment is called:",
     "a":"Environmental Microbiology","b":"Microbial Ecology",
     "c":"Ecosystem","d":"Both A and B",
     "answer":"D","explanation":"Environmental microbiology and microbial ecology both study microorganism-environment relationships."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"Organisms adapted to extremely harsh conditions are called:",
     "a":"Ecology","b":"Adaptation","c":"Extremophobic","d":"Extremophilic",
     "answer":"D","explanation":"Extremophiles (extremophilic) thrive in extreme conditions: heat, cold, acid, high pressure, salinity."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"Biodiversity is held in balance by various checks including:",
     "a":"Competition","b":"Cooperation","c":"Antagonism","d":"All of the above",
     "answer":"D","explanation":"Biodiversity is maintained through competition, cooperation, antagonism, and other ecological interactions."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"Soil arising from weathering of rocks and microbial actions is studied under:",
     "a":"Aquatic microbiology","b":"Food microbiology",
     "c":"Air microbiology","d":"Soil microbiology",
     "answer":"D","explanation":"Soil microbiology studies microorganisms in soil, their roles in soil formation and nutrient cycling."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"Environmental factors affecting microbial abundance in soils include:",
     "a":"Moisture content","b":"pH","c":"Weather","d":"Both A and B",
     "answer":"D","explanation":"Key factors: moisture content, pH, temperature, nutrient availability, oxygen levels."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"Most soil organisms are:",
     "a":"Thermophobic","b":"Thermophiles","c":"Both A and B","d":"Mesophiles",
     "answer":"D","explanation":"Most soil microorganisms are mesophiles — optimally grow at moderate temperatures (20-45°C)."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"Moist soils are lower in _______ than dry soils.",
     "a":"CO2","b":"O2","c":"SO4","d":"NO3",
     "answer":"B","explanation":"Water fills soil pores in moist soil, restricting gas exchange → lower O2 than dry soil."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"The relation between nutrients/microbial numbers and soil depth is:",
     "a":"Reversible","b":"Irreversible","c":"Negative","d":"Both A and C",
     "answer":"D","explanation":"As depth increases, nutrients and microbial numbers decrease — negative and reversible relationship."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"Microbial populations present in soil include:",
     "a":"Bacteria","b":"Fungi","c":"Archaea","d":"All of the above",
     "answer":"D","explanation":"Soil contains all major microbial groups: bacteria, fungi, archaea, protozoa, algae."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"Compounds released from moribund (dying) cells during autolysis are called:",
     "a":"Secretions","b":"Lysates","c":"Exudates","d":"Plant mucilage",
     "answer":"B","explanation":"Lysates = compounds released when dead or dying cells break down (lyse) in the rhizosphere."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"The beneficial aspect of root-microbe interactions includes:",
     "a":"Biological nitrogen fixation","b":"Soil drying",
     "c":"Root damage","d":"Plant damage",
     "answer":"A","explanation":"Root-microbe interactions benefit plants through nitrogen fixation, nutrient solubilization, and growth promotion."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"Beneficial relationships between two living organisms is called:",
     "a":"Parasitic","b":"Symbiotic","c":"Saprophytic","d":"Both A and C",
     "answer":"B","explanation":"Symbiosis = mutually beneficial relationship between two organisms (e.g., Rhizobium-legume)."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"Symbiotic nitrogen fixation gives _______ kg/hectare/crop.",
     "a":"250","b":"100","c":"1000","d":"25",
     "answer":"B","explanation":"Symbiotic nitrogen fixation (Rhizobium in legume nodules) produces ~100 kg N/hectare/crop."},

    {"section":"الأحياء الدقيقة والبيئة — Environmental",
     "question":"T=T (thymine dimer) formation is a result of:",
     "a":"X-ray","b":"UV radiation","c":"Gamma ray","d":"Chemical exposure",
     "answer":"B","explanation":"UV radiation causes thymine dimers (T=T) — covalent bonds between adjacent thymines in DNA, causing mutations."},
]

db.import_questions(QUESTIONS)

from collections import Counter
counts = Counter(q["section"] for q in QUESTIONS)
print(f"\n✅ تم إضافة {len(QUESTIONS)} سؤال:\n")
for sec, cnt in counts.items():
    emoji = next((q.get("section_emoji","📖") for q in QUESTIONS if q["section"]==sec), "📖")
    print(f"   {emoji} {sec}: {cnt} سؤال")
print("\n🚀 شغّل البوت: python run.py")
