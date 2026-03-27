"""
final2_questions.py — أسئلة الفاينل 2
50 سؤال
"""

import os, json
from database import Database
os.makedirs("/data", exist_ok=True)
db = Database("/data/quiz_bot.db")

# امسح هذا السكشن فقط
with db._connect() as c:
    c.execute("PRAGMA foreign_keys = OFF")
    c.execute("DELETE FROM questions WHERE section_id IN (SELECT id FROM sections WHERE name='الفاينل 2 — Final Exam 2')")
    c.execute("DELETE FROM sections WHERE name='الفاينل 2 — Final Exam 2'")
    c.execute("PRAGMA foreign_keys = ON")
print('🗑️ تم مسح الأسئلة القديمة')

QUESTIONS = [
    {
        "section": "الفاينل 2 — Final Exam 2",
        "section_emoji": "📋",
        "section_description": "أسئلة الفاينل — بهلاثم — Microbiology I",
        "question": "What is a virus composed of?",
        "a": "DNA only",
        "b": "RNA only",
        "c": "Genetic material and a protein shell",
        "d": "Lipids and carbohydrates",
        "answer": "C",
        "explanation": "All viruses consist of genetic material (DNA or RNA) enclosed in a protein coat (capsid)."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Viruses are considered:",
        "a": "Cellular organisms",
        "b": "Acellular particles",
        "c": "Prokaryotic cells",
        "d": "Eukaryotic cells",
        "answer": "B",
        "explanation": "Viruses are acellular — they have no cell structure, organelles, or cytoplasm."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Which of the following is NOT a characteristic of viruses?",
        "a": "Obligate intracellular parasites",
        "b": "Possession of metabolic enzymes",
        "c": "Very small genomes",
        "d": "Limited protein production",
        "answer": "B",
        "explanation": "Viruses do NOT have metabolic enzymes — they depend entirely on the host cell's machinery."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Viruses that have a lipid membrane are called:",
        "a": "Naked viruses",
        "b": "Enveloped viruses",
        "c": "Complex viruses",
        "d": "RNA viruses",
        "answer": "B",
        "explanation": "Enveloped viruses have a lipid bilayer membrane derived from the host cell membrane."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Which of the following is NOT a basic viral form?",
        "a": "Complex",
        "b": "Naked",
        "c": "Filamentous",
        "d": "Enveloped",
        "answer": "C",
        "explanation": "Basic viral forms: icosahedral, helical, and complex. Filamentous is not a standard viral morphology category."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "In viral taxonomy, what suffix is commonly used for virus families?",
        "a": "-virus",
        "b": "-pathogen",
        "c": "-viridae",
        "d": "-bacteria",
        "answer": "C",
        "explanation": "Virus family names end in -viridae (e.g., Herpesviridae, Retroviridae, Picornaviridae)."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "The first step in the viral life cycle, where the virus attaches to the host cell, is called:",
        "a": "Penetration",
        "b": "Adsorption",
        "c": "Uncoating",
        "d": "Assembly",
        "answer": "B",
        "explanation": "Adsorption (attachment) is the first step — virus binds to specific receptors on the host cell surface."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "What is the origin of the word 'virus'?",
        "a": "Latin for germ",
        "b": "Greek for poison",
        "c": "Latin for infectious",
        "d": "Word for toxoplasma",
        "answer": "B",
        "explanation": "The word 'virus' originates from Latin/Greek meaning poison or venom."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Viruses reproduce:",
        "a": "Outside cells",
        "b": "Inside living cells",
        "c": "In soil",
        "d": "In water",
        "answer": "B",
        "explanation": "Viruses can only replicate inside living host cells — they are obligate intracellular parasites."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Which metabolic pathway produces ATP through substrate-level phosphorylation?",
        "a": "Glycolysis",
        "b": "Electron Transport Chain",
        "c": "Krebs Cycle",
        "d": "Photosynthesis",
        "answer": "A",
        "explanation": "Glycolysis produces 2 ATP net via substrate-level phosphorylation in the cytoplasm."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Enzymes are best described as:",
        "a": "Structural proteins",
        "b": "Biological catalysts",
        "c": "Energy sources",
        "d": "Hormones",
        "answer": "B",
        "explanation": "Enzymes are biological catalysts that lower activation energy without being consumed."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Which of the following metabolic processes is catabolic?",
        "a": "Protein synthesis",
        "b": "Breakdown of glucose for energy",
        "c": "Lipid biosynthesis",
        "d": "DNA replication",
        "answer": "B",
        "explanation": "Catabolism = breaking down complex molecules to release energy. Glucose breakdown is classic catabolism."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Which of the following categories of microorganisms uses light as an energy source?",
        "a": "Chemotrophs",
        "b": "Phototrophs",
        "c": "Chemoorganotrophs",
        "d": "Autotrophs",
        "answer": "B",
        "explanation": "Phototrophs use light as their primary energy source through photosynthesis."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "What type of organism uses chemicals for energy but organic molecules as a carbon source?",
        "a": "Phototroph",
        "b": "Chemolithotroph",
        "c": "Chemoorganotroph",
        "d": "Autotroph",
        "answer": "C",
        "explanation": "Chemoorganotrophs: energy from chemicals + organic carbon source (e.g., most bacteria, all animals)."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Which of the following factors can denature enzymes?",
        "a": "Exposure to light",
        "b": "Changes in temperature and pH",
        "c": "Presence of enzyme inhibitors",
        "d": "None of the above",
        "answer": "B",
        "explanation": "High temperature and extreme pH disrupt enzyme 3D structure → denaturation → loss of function."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Which enzyme is responsible for transferring functional groups between molecules?",
        "a": "Oxidoreductase",
        "b": "Transferase",
        "c": "Hydrolase",
        "d": "Isomerase",
        "answer": "B",
        "explanation": "Transferase enzymes transfer functional groups from one molecule to another."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Isomerase is responsible for:",
        "a": "Oxidation-reduction",
        "b": "Hydrolysis",
        "c": "Rearrangement of atoms",
        "d": "Joining molecules",
        "answer": "C",
        "explanation": "Isomerase catalyzes rearrangement of atoms within a molecule to form isomers."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "What is the main product of glycolysis?",
        "a": "Glucose",
        "b": "Pyruvic acid",
        "c": "Lactic acid",
        "d": "Acetyl-CoA",
        "answer": "B",
        "explanation": "Glycolysis: 1 glucose → 2 pyruvate + 2 ATP (net) + 2 NADH."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "What is the primary purpose of the Krebs cycle?",
        "a": "To generate ATP and electron carriers",
        "b": "To synthesize glucose",
        "c": "To break down nucleotides",
        "d": "To store energy in the cell",
        "answer": "A",
        "explanation": "Krebs cycle produces NADH, FADH2, and GTP (ATP) — electron carriers that feed into the ETC."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "What is the main function of the electron transport chain?",
        "a": "DNA replication",
        "b": "ATP production",
        "c": "Protein synthesis",
        "d": "Lipid breakdown",
        "answer": "B",
        "explanation": "The ETC generates ATP through oxidative phosphorylation using the proton gradient."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "In aerobic respiration, which molecule serves as the final electron acceptor?",
        "a": "Water",
        "b": "Oxygen",
        "c": "Glucose",
        "d": "ATP",
        "answer": "B",
        "explanation": "O2 is the final electron acceptor in aerobic respiration, being reduced to water (H2O)."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "What type of fermentation produces only lactic acid?",
        "a": "Alcohol fermentation",
        "b": "Mixed acid fermentation",
        "c": "Homolactic fermentation",
        "d": "Heterolactic fermentation",
        "answer": "C",
        "explanation": "Homolactic fermentation produces ONLY lactic acid (e.g., Lactobacillus)."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Lactic acid fermentation produces:",
        "a": "Only ethyl alcohol",
        "b": "Only lactic acid",
        "c": "Both lactic acid and other compounds",
        "d": "Carbon dioxide and water",
        "answer": "B",
        "explanation": "Homolactic fermentation produces only lactic acid from pyruvate."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Alcohol fermentation produces:",
        "a": "Lactic acid",
        "b": "Ethyl alcohol and CO2",
        "c": "Pyruvic acid",
        "d": "NADH only",
        "answer": "B",
        "explanation": "Alcohol fermentation: pyruvate → acetaldehyde → ethanol + CO2."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Which metabolic process does NOT require oxygen and does NOT involve the Krebs cycle?",
        "a": "Aerobic respiration",
        "b": "Fermentation",
        "c": "Anaerobic respiration",
        "d": "Oxidative phosphorylation",
        "answer": "B",
        "explanation": "Fermentation: no O2, no Krebs cycle, no ETC — uses organic final electron acceptor."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Heterolactic fermentation produces:",
        "a": "Lactic acid only",
        "b": "Ethyl alcohol only",
        "c": "Lactic acid and other compounds",
        "d": "CO2 only",
        "answer": "C",
        "explanation": "Heterolactic fermentation produces lactic acid + ethanol + CO2 (mixed products)."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Photosynthesis converts light energy into:",
        "a": "Mechanical energy",
        "b": "Chemical energy (ATP)",
        "c": "Thermal energy",
        "d": "Kinetic energy",
        "answer": "B",
        "explanation": "Photosynthesis converts light energy into chemical energy stored in ATP and glucose."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "The light-independent reaction of photosynthesis is also called:",
        "a": "Light reaction",
        "b": "Calvin-Benson cycle",
        "c": "Krebs cycle",
        "d": "Glycolysis",
        "answer": "B",
        "explanation": "The Calvin-Benson cycle = dark (light-independent) reactions that fix CO2 into organic molecules."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Phototrophs use _______ as an energy source:",
        "a": "Chemicals",
        "b": "Light",
        "c": "Organic compounds",
        "d": "Inorganic ions",
        "answer": "B",
        "explanation": "Phototrophs use light as their energy source (photosynthesis)."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "The mutation that occurs due to occasional mistakes in DNA replication is called:",
        "a": "Induced mutation",
        "b": "Spontaneous mutation",
        "c": "Frameshift mutation",
        "d": "Missense mutation",
        "answer": "B",
        "explanation": "Spontaneous mutations occur naturally from DNA replication errors without any external agent."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Transcription proceeds in which direction?",
        "a": "3' → 5'",
        "b": "5' → 3'",
        "c": "Both directions",
        "d": "Random",
        "answer": "B",
        "explanation": "Transcription proceeds in the 5' to 3' direction (RNA polymerase reads template 3'→5')."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Genetics is defined as the study of:",
        "a": "Cell metabolism",
        "b": "Genes and how information is carried, expressed, and replicated",
        "c": "Protein synthesis only",
        "d": "Cell membrane structure",
        "answer": "B",
        "explanation": "Genetics = study of genes, heredity, and how genetic information is stored, expressed, and transmitted."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "What is a gene?",
        "a": "A segment of RNA",
        "b": "A segment of DNA encoding a functional product",
        "c": "A protein molecule",
        "d": "A lipid component of the cell membrane",
        "answer": "B",
        "explanation": "A gene is a DNA sequence that encodes a functional product — usually a protein or functional RNA."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Genetic information is stored in:",
        "a": "Proteins",
        "b": "DNA base sequence",
        "c": "Lipids",
        "d": "Carbohydrates",
        "answer": "B",
        "explanation": "Genetic information is encoded in the sequence of nitrogenous bases in DNA."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "What does environmental microbiology study?",
        "a": "Microorganisms in artificial lab environments",
        "b": "Microorganisms in their natural habitats",
        "c": "Microorganisms used in medical research",
        "d": "Only harmful microorganisms",
        "answer": "B",
        "explanation": "Environmental microbiology studies microorganisms in natural environments and their ecological roles."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Translation of mRNA begins at start codon _______ and terminates at stop codon _______.",
        "a": "AUG and UTA, UAG, UGA",
        "b": "AUG and UAA, UAG, UGA",
        "c": "AUU and UAA, UAG, UGA",
        "d": "AGG and UAA, UAG, UGA",
        "answer": "B",
        "explanation": "Start codon = AUG (methionine). Stop codons = UAA, UAG, UGA (no amino acid)."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "The light-independent reaction of photosynthesis is also called: (Q37)",
        "a": "Light reaction",
        "b": "Calvin-Benson cycle",
        "c": "Krebs cycle",
        "d": "Glycolysis",
        "answer": "B",
        "explanation": "The Calvin-Benson cycle fixes CO2 into organic molecules using ATP and NADPH from light reactions."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Oxygenic photosynthesis produces:",
        "a": "H2S",
        "b": "O2",
        "c": "CO2",
        "d": "NH3",
        "answer": "B",
        "explanation": "Oxygenic photosynthesis (plants, cyanobacteria) splits water → releases O2 as a byproduct."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "All genetic material in a cell is called:",
        "a": "One gene",
        "b": "RNA molecules",
        "c": "Genome",
        "d": "Ribosomes",
        "answer": "C",
        "explanation": "Genome = the complete set of all genetic material (DNA) in a cell or organism."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Hydrogen bonds in DNA occur between:",
        "a": "Sugar and phosphate",
        "b": "Nitrogenous bases",
        "c": "Amino acids",
        "d": "Lipids",
        "answer": "B",
        "explanation": "Hydrogen bonds form between complementary nitrogenous bases (A-T: 2 bonds, G-C: 3 bonds)."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Mutations can be classified as:",
        "a": "Only harmful",
        "b": "Only beneficial",
        "c": "Neutral, beneficial, or harmful",
        "d": "Only neutral",
        "answer": "C",
        "explanation": "Mutations can be harmful (disrupts function), beneficial (improves function), or neutral (no effect)."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "An agent that causes mutations is called:",
        "a": "Enzyme",
        "b": "Mutagen",
        "c": "Antigen",
        "d": "Catalyst",
        "answer": "B",
        "explanation": "A mutagen is any physical or chemical agent that causes mutations in DNA."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Which of the following is an example of a mutagen?",
        "a": "Oxygen",
        "b": "UV radiation",
        "c": "Water",
        "d": "Glucose",
        "answer": "B",
        "explanation": "UV radiation causes thymine dimers (T=T) in DNA — a classic mutagenic effect."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Which of the following is a chemical mutagen?",
        "a": "X-rays",
        "b": "Gamma rays",
        "c": "Nitrous acid",
        "d": "Heat",
        "answer": "C",
        "explanation": "Nitrous acid is a chemical mutagen that deaminates bases, causing mutations. X-rays and gamma rays are physical mutagens."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Ionizing radiation can cause mutations by:",
        "a": "Increasing enzyme activity",
        "b": "Forming ions that react with DNA",
        "c": "Stabilizing DNA structure",
        "d": "Enhancing replication accuracy",
        "answer": "B",
        "explanation": "Ionizing radiation (X-rays, gamma rays) creates reactive ions that damage DNA bases and backbone."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Damage to the deoxyribose-phosphate backbone by radiation may result in:",
        "a": "Improved replication",
        "b": "Chromosome breakage",
        "c": "Increased protein synthesis",
        "d": "Neutral mutation only",
        "answer": "B",
        "explanation": "Radiation damage to the sugar-phosphate backbone can cause single or double-strand breaks → chromosome breakage."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Oxygen levels in moist soils are typically:",
        "a": "Higher than dry soils",
        "b": "Lower than dry soils",
        "c": "Equal to dry soils",
        "d": "Absent completely",
        "answer": "B",
        "explanation": "Water fills soil pores in moist soil → restricts gas exchange → lower O2 than dry soil."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Microorganisms in soil are distributed based on:",
        "a": "Soil texture only",
        "b": "Nutrient availability and environmental factors",
        "c": "Wind direction",
        "d": "Soil color",
        "answer": "B",
        "explanation": "Microbial distribution in soil depends on nutrients, moisture, pH, O2, temperature, and organic matter."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Which of the following is NOT a common soil microorganism?",
        "a": "Bacteria",
        "b": "Archaea",
        "c": "Fungi",
        "d": "Mammals",
        "answer": "D",
        "explanation": "Mammals are macroorganisms — not microorganisms. Common soil microbes: bacteria, archaea, fungi, protozoa, algae."
    },
    {
        "section": "الفاينل 2 — Final Exam 2",
        "question": "Soil microorganisms help in decomposition by:",
        "a": "Producing oxygen",
        "b": "Degrading dead organisms",
        "c": "Increasing temperature",
        "d": "Reducing moisture",
        "answer": "B",
        "explanation": "Soil microorganisms decompose dead organic matter, releasing nutrients back into the soil."
    }
]

db.import_questions(QUESTIONS)
print(f'✅ تم إضافة {len(QUESTIONS)} سؤال في سكشن الفاينل 2 📋')
