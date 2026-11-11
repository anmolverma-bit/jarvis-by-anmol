import streamlit as st
import re

# ============================================================
# JARVIS BY ANMOL - CAREER GUIDANCE
# Each career has its own guide. Information is India-focused.
# Verify changing admission rules, age limits, fees and salaries
# from the linked official authority before making decisions.
# ============================================================

st.set_page_config(
    page_title="Jarvis by Anmol",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

CAREERS = {
    "Technology & Coding": [
        "BCA", "B.Tech Computer Science", "B.Sc Computer Science",
        "Software Developer", "Web Developer", "Data Scientist"
    ],
    "Medical & Healthcare": [
        "MBBS", "BDS", "B.Sc Nursing", "Pharmacy", "Physiotherapy"
    ],
    "Business & Finance": [
        "B.Com", "BBA", "Chartered Accountant (CA)",
        "Company Secretary (CS)", "Banking", "Entrepreneur"
    ],
    "Government Jobs": [
        "SSC CGL", "SSC CHSL", "UPSC", "Banking Exams",
        "Railway Exams", "NDA"
    ],
    "Arts & Creativity": [
        "Graphic Designing", "Animation", "Fashion Designing",
        "Journalism", "Hotel Management"
    ],
    "Law": ["BA LLB", "BBA LLB", "LLB", "Legal Studies"],
    "Sports & Athletics": ["Cricketer", "Footballer", "Athlete", "Sports Coach"],
    "Social Media & Digital Careers": [
        "YouTuber", "Content Creator", "Social Media Manager",
        "Video Editor", "Digital Marketer"
    ],
    "Science & Research": [
        "Scientist", "Research Scientist", "Space Scientist",
        "Environmental Scientist"
    ],
    "Politics & Public Service": [
        "Politician", "Political Analyst", "Public Administration", "Social Worker"
    ]
}

# A separate record is provided for EVERY career listed above.
# No category-level generic guide is used as a fallback.
GUIDES = {
"BCA": {
"intro":"Bachelor of Computer Applications is an undergraduate degree focused on computer applications, programming and IT systems.",
"qualification":"Usually Class 12 from a recognised board. Mathematics requirements vary by university; check each college prospectus.",
"age":"There is no single all-India age limit. Individual universities may publish age or year-of-passing conditions.",
"admission":"Admission may be merit-based or through a university/institute entrance test. Apply through the institution's official admission portal.",
"exam":"University-specific tests may cover English, mathematics, logical reasoning and computer awareness. CUET-UG is accepted by some participating universities, not all.",
"syllabus":["Programming fundamentals","C/Python/Java as prescribed","Data structures","Database management systems","Operating systems","Computer networks","Web technologies","Software engineering"],
"resources":["NCERT Mathematics (where relevant)","Python documentation: https://docs.python.org/3/","NPTEL: https://nptel.ac.in/","SWAYAM: https://swayam.gov.in/"],
"strategy":["Compare university eligibility and curriculum before applying.","Learn one programming language well.","Practise problem solving and SQL.","Build small projects and document them.","Look for internships and maintain a project portfolio."],
"skills":["Programming","Logical reasoning","Database basics","Communication","Teamwork"],
"opportunities":"Junior software developer, web developer, QA tester, technical support, database assistant or further study such as MCA/MSc, depending on eligibility.",
"salary":"No fixed starting salary. It varies by skills, projects, city, employer and experience; check current job postings rather than relying on a guaranteed figure.",
"official":["University admission portal of the chosen college","https://cuet.nta.nic.in/","https://www.ugc.gov.in/"]
},
"B.Tech Computer Science": {
"intro":"A four-year engineering degree covering computer science theory, software, hardware and engineering problem-solving.",
"qualification":"Class 12 with Physics and Mathematics and other subjects required by the institution; minimum marks and subject combinations vary.",
"age":"No universal age limit for every engineering college. Entrance and counselling rules can include year-of-passing or age conditions; verify the current brochure.",
"admission":"Common routes include JEE Main followed by JoSAA/CSAB counselling for participating institutes, or state/private university processes.",
"exam":"JEE Main tests Physics, Chemistry and Mathematics. Some institutes conduct their own examinations or use other accepted scores.",
"syllabus":["Engineering Mathematics","Programming and data structures","Algorithms","Computer organisation","Operating systems","Database systems","Computer networks","Theory of computation","AI and electives"],
"resources":["JEE Main official site: https://jeemain.nta.nic.in/","JoSAA: https://josaa.nic.in/","NPTEL: https://nptel.ac.in/","SWAYAM: https://swayam.gov.in/"],
"strategy":["Check the latest entrance and counselling information.","Prepare PCM concepts and solve timed practice questions.","Compare accredited colleges, fees and course curriculum.","Build programming projects alongside coursework.","Seek internships and practise technical interviews."],
"skills":["Mathematics","Programming","Algorithms","Teamwork","Technical communication"],
"opportunities":"Software engineering, systems, cybersecurity, cloud, data/AI, research or postgraduate study. Roles depend on skills and employer requirements.",
"salary":"Varies widely by institute, skills, location and employer; placements are not guaranteed.",
"official":["https://jeemain.nta.nic.in/","https://josaa.nic.in/","https://www.aicte-india.org/"]
},
"B.Sc Computer Science": {
"intro":"A science degree focused on computing foundations, programming, mathematics and computer systems.",
"qualification":"Class 12 with subject requirements set by the university; Mathematics is required or preferred by many programmes.",
"age":"University-specific; there is no single national age limit for all BSc Computer Science admissions.",
"admission":"Merit-based or entrance-based admission, including CUET-UG at participating universities.",
"exam":"Where required, entrance tests may assess mathematics, reasoning, English and domain subjects.",
"syllabus":["Discrete mathematics","Programming","Data structures","Computer architecture","Operating systems","Database systems","Networks","Software engineering"],
"resources":["CUET: https://cuet.nta.nic.in/","NPTEL: https://nptel.ac.in/","Python: https://docs.python.org/3/","SWAYAM: https://swayam.gov.in/"],
"strategy":["Check whether the course requires Mathematics.","Strengthen mathematical and programming basics.","Complete practical lab work and projects.","Explore internships and research opportunities.","Consider MSc, MCA or specialised certifications if useful."],
"skills":["Programming","Mathematical reasoning","Research","Problem solving","Technical writing"],
"opportunities":"IT support, junior programming, QA, data support, research assistance or higher studies; role requirements differ.",
"salary":"Depends on role, skills, further qualifications, location and employer.",
"official":["https://cuet.nta.nic.in/","https://www.ugc.gov.in/"]
},
"Software Developer": {
"intro":"Software developers design, build, test, maintain and improve applications and software systems.",
"qualification":"A CS/IT degree is common but not universally mandatory; demonstrable skills and employer-specific requirements matter.",
"age":"No general profession-wide age limit. Employer hiring rules apply.",
"admission":"Not a single degree admission route. Learn through a degree, diploma, structured courses and practical projects.",
"exam":"No universal entrance exam. Hiring commonly includes coding tests, technical interviews and project discussions.",
"syllabus":["One programming language","Data structures and algorithms","Object-oriented programming","Databases and SQL","APIs and version control","Testing and debugging","Software design basics"],
"resources":["Git: https://git-scm.com/doc","MDN: https://developer.mozilla.org/","Python: https://docs.python.org/3/","NPTEL: https://nptel.ac.in/"],
"strategy":["Choose a development area and one language.","Learn Git and debugging.","Build progressively harder original projects.","Study data structures and algorithms.","Prepare a clear portfolio and practise interviews."],
"skills":["Programming","Debugging","Problem solving","Collaboration","Clear documentation"],
"opportunities":"Frontend, backend, full-stack, mobile, embedded, QA automation, DevOps or software testing roles.",
"salary":"Highly variable by skill level, location, company and experience; no salary is guaranteed.",
"official":["https://www.ncs.gov.in/","https://www.nptel.ac.in/"]
},
"Web Developer": {
"intro":"Web developers create and maintain websites and browser-based applications.",
"qualification":"No single mandatory degree for all roles. Relevant computer education and a strong portfolio can help.",
"age":"No universal age limit; employer or apprenticeship conditions may apply.",
"admission":"Can be learned through formal IT courses, college programmes or structured self-study.",
"exam":"No universal entrance exam. Hiring may involve portfolio review, practical tasks and interviews.",
"syllabus":["HTML structure","CSS and responsive design","JavaScript","Accessibility","Browser and HTTP basics","Frontend framework concepts","Backend/API and database basics","Security and testing"],
"resources":["MDN Web Docs: https://developer.mozilla.org/","W3C: https://www.w3.org/","Git: https://git-scm.com/doc/"],
"strategy":["Learn HTML, CSS and JavaScript foundations.","Build accessible responsive pages.","Use Git and publish projects.","Learn APIs and basic security.","Test on different screen sizes and browsers."],
"skills":["HTML/CSS/JavaScript","Design awareness","Debugging","Accessibility","Communication"],
"opportunities":"Frontend developer, backend developer, full-stack developer, CMS developer or web application tester.",
"salary":"Depends on portfolio, framework knowledge, employer, location and experience.",
"official":["https://developer.mozilla.org/","https://www.ncs.gov.in/"]
},
"Data Scientist": {
"intro":"Data scientists use statistics, programming and domain knowledge to analyse data and build predictive models.",
"qualification":"A degree in mathematics, statistics, computer science, engineering, economics or a related area is useful; advanced roles may require postgraduate study.",
"age":"No universal profession-wide age limit.",
"admission":"Relevant bachelor's or master's programmes; university-specific entrance and admission rules apply.",
"exam":"There is no single national data-scientist entrance exam. Academic admissions and employer assessments vary.",
"syllabus":["Statistics and probability","Linear algebra","Python or R","SQL","Data cleaning","Machine learning","Data visualisation","Ethics and privacy"],
"resources":["Kaggle Learn: https://www.kaggle.com/learn","NPTEL: https://nptel.ac.in/","Python: https://docs.python.org/3/","R: https://www.r-project.org/"],
"strategy":["Build mathematics and statistics foundations.","Learn Python or R and SQL.","Practise cleaning and visualising real datasets.","Study model evaluation and limitations.","Publish reproducible projects with clear explanations."],
"skills":["Statistics","Programming","Critical thinking","Data storytelling","Ethical handling of data"],
"opportunities":"Data analyst, business analyst, machine-learning associate, data scientist or research roles, depending on qualifications.",
"salary":"Varies substantially by role, education, technical depth, location and employer.",
"official":["https://www.ncs.gov.in/","https://www.nptel.ac.in/"]
},
"MBBS": {
"intro":"MBBS is the primary undergraduate medical qualification for training as a doctor in modern medicine in India.",
"qualification":"Class 12 with Physics, Chemistry, Biology/Biotechnology and English, meeting the current NMC/NEET eligibility and marks rules.",
"age":"NEET-UG eligibility has a minimum age requirement; current upper-age and other rules must be checked in the latest NTA/NMC documents.",
"admission":"NEET-UG score followed by counselling through the relevant central or state counselling authority. Seat allotment and category rules apply.",
"exam":"NEET-UG covers Physics, Chemistry and Biology (Botany and Zoology); use the current official syllabus.",
"syllabus":["NEET-UG Physics","NEET-UG Chemistry","NEET-UG Biology","During MBBS: anatomy","Physiology and biochemistry","Pathology, pharmacology and microbiology","Clinical and community medicine"],
"resources":["NTA NEET: https://neet.nta.nic.in/","NMC: https://www.nmc.org.in/","Medical Counselling Committee: https://mcc.nic.in/","NCERT: https://ncert.nic.in/"],
"strategy":["Read the current NEET information bulletin and syllabus.","Study NCERT Biology and core Physics/Chemistry concepts.","Practise questions and analyse mistakes.","Use official counselling information only.","Understand the long clinical training pathway and professional responsibilities."],
"skills":["Biological science","Patient communication","Clinical reasoning","Empathy","Professional ethics"],
"opportunities":"After the degree and required internship/registration formalities, doctors may pursue clinical practice, postgraduate specialisation, public health or research.",
"salary":"Depends on internship/residency, employer, location, specialty and experience; no fixed salary applies to all doctors.",
"official":["https://neet.nta.nic.in/","https://www.nmc.org.in/","https://mcc.nic.in/"]
},
"BDS": {
"intro":"Bachelor of Dental Surgery trains students in oral health, dental diagnosis and dental treatment.",
"qualification":"Class 12 with Physics, Chemistry, Biology/Biotechnology and English, satisfying current NEET-UG and counselling eligibility.",
"age":"Follow current NEET-UG bulletin and applicable dental admission regulations; do not rely on an old age-rule summary.",
"admission":"NEET-UG followed by applicable All India or state counselling for recognised dental seats.",
"exam":"NEET-UG: Physics, Chemistry and Biology. Dental course subjects are taught after admission.",
"syllabus":["NEET Physics, Chemistry and Biology","Dental anatomy","Oral pathology","General medicine and surgery","Conservative dentistry","Oral surgery","Prosthodontics and orthodontics"],
"resources":["https://neet.nta.nic.in/","Dental Council of India: https://dciindia.gov.in/","https://mcc.nic.in/","https://ncert.nic.in/"],
"strategy":["Prepare for NEET using the current syllabus.","Verify college recognition and counselling rules.","Understand clinical training and internship requirements.","Develop patient communication and careful practical skills.","Check current registration rules before practice."],
"skills":["Manual precision","Oral-health knowledge","Patient communication","Clinical judgement","Ethics"],
"opportunities":"Dental surgeon after required qualification, internship and registration; further specialisation, public health, teaching or research may follow.",
"salary":"Depends on practice setting, location, experience, patient base and specialisation.",
"official":["https://dciindia.gov.in/","https://neet.nta.nic.in/","https://mcc.nic.in/"]
},
"B.Sc Nursing": {
"intro":"BSc Nursing is a professional undergraduate programme preparing students for nursing care, health education and clinical practice.",
"qualification":"Usually Class 12 with Physics, Chemistry, Biology and English; exact marks and other eligibility are set by the institution and current nursing regulations.",
"age":"Age conditions can vary by admission authority and programme; check the current prospectus and INC/state rules.",
"admission":"Admission may be through a national, state or university entrance test, or merit, depending on the institution.",
"exam":"No single admission exam applies to every college. Tests may include Physics, Chemistry, Biology, English and general ability.",
"syllabus":["Anatomy and physiology","Nutrition and biochemistry","Nursing foundations","Medical-surgical nursing","Community health nursing","Child health nursing","Mental health nursing","Midwifery and practical clinical training"],
"resources":["Indian Nursing Council: https://indiannursingcouncil.org/","University/state nursing admission prospectus","https://ncert.nic.in/"],
"strategy":["Check recognition and clinical training facilities.","Prepare the subjects named in the college prospectus.","Build communication and patient-care knowledge.","Take clinical placements seriously under supervision.","Check registration requirements after graduation."],
"skills":["Patient care","Communication","Observation","Teamwork","Professional ethics"],
"opportunities":"Staff nurse, community health, hospitals, education, administration and further nursing specialisation, subject to registration and rules.",
"salary":"Depends on public/private employer, state, experience, role and allowances.",
"official":["https://indiannursingcouncil.org/"]
},
"Pharmacy": {
"intro":"Pharmacy covers medicines, their formulation, safe use, dispensing, quality and related healthcare services.",
"qualification":"Routes include D.Pharm and B.Pharm. Subject eligibility differs; many BPharm routes require Class 12 with Physics and Chemistry plus Mathematics or Biology.",
"age":"No single universal age limit across all pharmacy courses; check the institution and state admission rules.",
"admission":"Admission may be merit-based or through state/university tests. Verify the course and institution's approval.",
"exam":"No one national entrance test for every pharmacy programme. Some states and universities use their own processes.",
"syllabus":["Pharmaceutics","Pharmaceutical chemistry","Pharmacology","Pharmacognosy","Pharmaceutical analysis","Pharmacy practice","Medicinal and regulatory topics"],
"resources":["Pharmacy Council of India: https://pci.nic.in/","State admission authority prospectus","NPTEL: https://nptel.ac.in/"],
"strategy":["Compare DPharm and BPharm pathways.","Verify PCI approval and course details.","Study chemistry and biology foundations.","Develop accuracy and medicine-safety awareness.","Check registration requirements for the intended role."],
"skills":["Chemistry","Accuracy","Medicine knowledge","Communication","Ethics"],
"opportunities":"Community/hospital pharmacy, pharmaceutical industry, quality control, regulatory affairs, research or further study.",
"salary":"Depends on qualification, registration, employer, role and experience.",
"official":["https://pci.nic.in/"]
},
"Physiotherapy": {
"intro":"Physiotherapy focuses on movement, rehabilitation, function and helping people manage physical limitations.",
"qualification":"BPT admission commonly requires Class 12 science subjects, often Physics, Chemistry and Biology; exact requirements vary by institution and current rules.",
"age":"Institution-specific; check the current admission prospectus.",
"admission":"Merit or entrance-based admission depending on state and university. Confirm course recognition and clinical placement arrangements.",
"exam":"There is no single national entrance exam for all BPT colleges.",
"syllabus":["Anatomy","Physiology","Biomechanics","Exercise therapy","Electrotherapy","Orthopaedics","Neurology","Cardiorespiratory and clinical practice"],
"resources":["University curriculum and prospectus","NPTEL health-related courses: https://nptel.ac.in/","Ministry of Health: https://mohfw.gov.in/"],
"strategy":["Verify course duration and clinical exposure.","Build biology and anatomy foundations.","Learn evidence-based rehabilitation principles.","Develop supervised practical skills.","Check current professional registration requirements."],
"skills":["Anatomy knowledge","Observation","Patient communication","Movement assessment","Empathy"],
"opportunities":"Hospital, rehabilitation centre, sports setting, community care, private practice or postgraduate specialisation, subject to applicable rules.",
"salary":"Varies by location, employer, experience, specialisation and practice model.",
"official":["https://mohfw.gov.in/"]
},
"B.Com": {
"intro":"Bachelor of Commerce develops foundations in accounting, finance, taxation, business and economics.",
"qualification":"Class 12 from a recognised board; mathematics/accountancy requirements depend on the university.",
"age":"No single national age limit; university rules apply.",
"admission":"Merit-based or entrance-based, including CUET-UG at participating universities.",
"exam":"Some universities use CUET-UG or their own admission process; check the institution's current notice.",
"syllabus":["Financial accounting","Business law","Corporate accounting","Economics","Taxation","Cost accounting","Auditing","Finance and statistics"],
"resources":["CUET: https://cuet.nta.nic.in/","NCERT: https://ncert.nic.in/","SWAYAM: https://swayam.gov.in/"],
"strategy":["Strengthen accounting and basic mathematics.","Understand the university's subject combination.","Practise numerical problems consistently.","Learn spreadsheet skills.","Explore internships and professional qualifications."],
"skills":["Accounting","Numeracy","Excel/spreadsheets","Business communication","Analysis"],
"opportunities":"Accounts assistant, finance operations, tax support, banking operations, audit support or further study such as MCom/MBA/CA pathways.",
"salary":"Depends on role, skills, city, employer and additional qualifications.",
"official":["https://cuet.nta.nic.in/","https://www.ugc.gov.in/"]
},
"BBA": {
"intro":"Bachelor of Business Administration introduces management, marketing, finance, operations and organisational behaviour.",
"qualification":"Class 12 from a recognised board; subject and minimum-mark rules vary by institution.",
"age":"Institution-specific; no single universal age limit.",
"admission":"Merit or entrance test, with CUET-UG or university-specific tests accepted by some institutions.",
"exam":"May assess English, quantitative aptitude, reasoning, general awareness and business awareness.",
"syllabus":["Principles of management","Marketing","Accounting and finance","Business economics","Human resources","Operations","Business law","Entrepreneurship"],
"resources":["CUET: https://cuet.nta.nic.in/","SWAYAM: https://swayam.gov.in/","NPTEL: https://nptel.ac.in/"],
"strategy":["Compare course curriculum and internships.","Build communication and spreadsheet skills.","Take part in case studies and team projects.","Explore a specialisation through projects.","Consider MBA or work experience based on goals."],
"skills":["Communication","Teamwork","Numeracy","Planning","Presentation"],
"opportunities":"Sales, marketing, operations, HR, business development, management trainee roles or postgraduate study.",
"salary":"Varies by college, role, industry, location and experience; a degree alone does not guarantee a management job.",
"official":["https://cuet.nta.nic.in/","https://www.ugc.gov.in/"]
},
"Chartered Accountant (CA)": {
"intro":"The CA qualification in India is awarded by the Institute of Chartered Accountants of India and covers accounting, audit, taxation and finance.",
"qualification":"Entry is generally through Foundation after Class 10/12 registration, or eligible direct-entry routes for specified graduates/postgraduates. Check current ICAI rules.",
"age":"ICAI course regulations and registration rules apply; check the current official scheme rather than assuming a general age limit.",
"admission":"Register with ICAI for the applicable entry route and follow the current course, examination and practical training requirements.",
"exam":"Foundation, Intermediate and Final examinations under the applicable ICAI scheme, with required practical training and other course components.",
"syllabus":["Accounting","Business laws","Quantitative aptitude/economics at Foundation","Taxation","Auditing and assurance","Financial management","Strategic management","Advanced accounting and reporting"],
"resources":["ICAI: https://www.icai.org/","ICAI BOS: https://boslive.icai.org/"],
"strategy":["Read the current ICAI scheme and registration cut-offs.","Use official study material and announcements.","Make a subject-wise study and revision plan.","Practise ICAI question papers and mock tests.","Track training and exam eligibility requirements."],
"skills":["Accounting","Tax knowledge","Audit","Ethical judgement","Attention to detail"],
"opportunities":"Audit, taxation, financial reporting, corporate finance, consulting, practice or senior finance roles.",
"salary":"Highly dependent on experience, role, location, practice and employer; no fixed package is assured.",
"official":["https://www.icai.org/","https://boslive.icai.org/"]
},
"Company Secretary (CS)": {
"intro":"The Company Secretary qualification focuses on company law, corporate governance, compliance and secretarial practice.",
"qualification":"ICSI's current entry routes and exemptions apply. Check eligibility for CSEET or direct registration under the current rules.",
"age":"Follow current ICSI registration and examination regulations; do not assume a universal age limit.",
"admission":"Register through the Institute of Company Secretaries of India for the route applicable to your qualification.",
"exam":"CSEET where applicable, followed by Executive and Professional stages under the current ICSI syllabus and training requirements.",
"syllabus":["Business communication","Legal aptitude and logical reasoning","Company law","Securities laws","Economic and commercial laws","Corporate accounting","Governance and compliance"],
"resources":["ICSI: https://www.icsi.edu/","ICSI student portal and official study material"],
"strategy":["Check the latest ICSI course structure.","Study official modules and amendments.","Practise case-based legal questions.","Track examination and training requirements.","Develop precise drafting and compliance skills."],
"skills":["Company law","Legal research","Drafting","Governance","Accuracy"],
"opportunities":"Company secretarial departments, compliance, governance, legal support, listed-company compliance or independent practice subject to rules.",
"salary":"Depends on qualification, membership, role, organisation, location and experience.",
"official":["https://www.icsi.edu/"]
},
"Banking": {
"intro":"Banking includes customer service, operations, credit, finance, risk and specialist roles in public and private banks.",
"qualification":"Clerical and officer recruitment commonly requires graduation; specialist posts may require relevant professional qualifications. Exact rules differ by notification.",
"age":"Post-specific. IBPS, SBI and other recruiters publish separate age limits and category relaxations in each notification.",
"admission":"Apply to the recruiting bank or examination body when the official recruitment notice is released.",
"exam":"IBPS/SBI patterns vary by post. Common stages include preliminary and main exams, and interview for some officer roles.",
"syllabus":["Reasoning","Quantitative aptitude","English","General/economy/banking awareness","Computer aptitude","Professional knowledge for specialist posts"],
"resources":["IBPS: https://www.ibps.in/","SBI Careers: https://sbi.co.in/web/careers","RBI Opportunities: https://opportunities.rbi.org.in/"],
"strategy":["Choose a specific bank and post.","Read that year's official notification.","Practise sectional tests and previous papers.","Follow financial and banking news.","Prepare documents and interview knowledge where required."],
"skills":["Numeracy","Customer communication","Accuracy","Digital literacy","Integrity"],
"opportunities":"Clerk, probationary officer, specialist officer, operations, credit, risk and managerial progression.",
"salary":"Pay and allowances vary by bank, cadre, location and current wage agreements.",
"official":["https://www.ibps.in/","https://sbi.co.in/web/careers","https://opportunities.rbi.org.in/"]
},
"Entrepreneur": {
"intro":"An entrepreneur identifies a problem or opportunity and builds an organisation or venture to serve customers.",
"qualification":"No single mandatory degree. Business, finance, technology or domain education can help, depending on the venture.",
"age":"Legal capacity, business registration and sector-specific rules apply. Minors need appropriate adult/legal support for contracts and formal registrations.",
"admission":"No standard admission process. Learn the market, validate a problem and understand legal and financial obligations before launching.",
"exam":"No universal entrance exam. Incubators and funding programmes may have their own selection processes.",
"syllabus":["Customer discovery","Business models","Market research","Basic accounting","Pricing and cash flow","Marketing and sales","Operations","Business law and compliance"],
"resources":["Startup India: https://www.startupindia.gov.in/","MSME: https://msme.gov.in/","Udyam: https://udyamregistration.gov.in/"],
"strategy":["Identify a real customer problem.","Interview potential users and test assumptions.","Prepare a simple cost and revenue model.","Start with a small, safe prototype.","Understand registrations, tax and consumer obligations.","Seek mentors and keep financial records."],
"skills":["Problem solving","Communication","Financial literacy","Planning","Adaptability"],
"opportunities":"Small business, technology startup, social enterprise, family business or independent professional venture.",
"salary":"There is no guaranteed salary or profit; a venture can earn revenue, break even or lose money.",
"official":["https://www.startupindia.gov.in/","https://msme.gov.in/"]
},
"SSC CGL": {
"intro":"SSC Combined Graduate Level examination recruits for notified Group B and Group C posts in central government departments and organisations.",
"qualification":"Bachelor's degree is generally required. Certain statistical, finance or other posts specify additional subject/qualification conditions.",
"age":"Varies by post and notification; common bands include 18–27, 18–30, 18–32 and 20–30. Relaxations apply as notified.",
"admission":"Apply online through the official SSC website during the notification window. Post preferences and document verification rules matter.",
"exam":"Current scheme uses Tier-I and Tier-II computer-based examinations; modules and qualifying tests depend on the latest notification and post.",
"syllabus":["Mathematical abilities","Reasoning and general intelligence","English comprehension","General awareness","Computer knowledge","Data entry speed test where applicable","Statistics/Finance papers for specified posts"],
"resources":["SSC: https://ssc.gov.in/","NCERT: https://ncert.nic.in/","Previous-year papers and official notices on SSC portal"],
"strategy":["Read the latest CGL notification and post-wise age/qualification table.","Prepare maths, reasoning, English and general awareness.","Practise previous-year papers under time limits.","Prepare computer and DEST requirements where applicable.","Check post preferences, physical/medical standards if any, and document rules."],
"skills":["Quantitative aptitude","Reasoning","English","General awareness","Accuracy"],
"opportunities":"Posts such as Assistant Section Officer, Inspector, Auditor, Accountant and other notified roles; actual allocation depends on merit, preferences and vacancies.",
"salary":"Pay level and allowances differ by post, department and posting; use the current notification/pay rules.",
"official":["https://ssc.gov.in/"]
},
"SSC CHSL": {
"intro":"SSC Combined Higher Secondary Level examination recruits for notified posts such as LDC/JSA and Data Entry Operator.",
"qualification":"Class 12 or equivalent is generally required. Some DEO posts require specified subjects or qualifications as stated in the notice.",
"age":"Usually 18–27 in recent notices, with relaxations as per rules; verify the relevant examination year's notification.",
"admission":"Apply online through SSC during the official application period.",
"exam":"The current scheme includes Tier-I and Tier-II computer-based stages, with typing/skill tests for applicable posts.",
"syllabus":["Mathematical abilities","Reasoning","English language","General awareness","Computer knowledge","Typing test or data entry skill test as applicable"],
"resources":["SSC: https://ssc.gov.in/","NCERT: https://ncert.nic.in/","Official SSC CHSL notice and previous papers"],
"strategy":["Check post-specific qualification and age conditions.","Practise arithmetic, reasoning and English daily.","Revise general awareness from reliable sources.","Practise typing accurately and consistently for relevant posts.","Use timed mock tests and read skill-test rules."],
"skills":["Typing","Computer basics","English","Reasoning","Accuracy"],
"opportunities":"LDC, JSA and DEO posts as notified, with progression under the relevant department's service rules.",
"salary":"Depends on the allotted post, pay level, department and allowances.",
"official":["https://ssc.gov.in/"]
},
"UPSC": {
"intro":"The Civil Services Examination conducted by UPSC recruits for IAS, IPS, Indian Foreign Service and other notified services.",
"qualification":"A recognised bachelor's degree is generally required; final-year candidates may be eligible subject to proof and rules in the notification.",
"age":"For the general category, the usual range is 21–32 on the specified cut-off date. Category and other relaxations are governed by the current notice.",
"admission":"Apply online through UPSC. Candidates must satisfy nationality, age, education, attempt and other conditions.",
"exam":"Preliminary examination, Main written examination and Personality Test. Prelims GS Paper II (CSAT) is qualifying under the notified threshold.",
"syllabus":["Prelims GS: history, geography, polity, economy, environment, science and current affairs","CSAT: comprehension, reasoning and numeracy","Mains Essay","GS I: culture, history, society, geography","GS II: governance, constitution, polity, social justice, IR","GS III: economy, science, environment, security, disaster management","GS IV: ethics","Optional subject papers and qualifying language/English papers"],
"resources":["UPSC: https://upsc.gov.in/","NCERT: https://ncert.nic.in/","PIB: https://pib.gov.in/","PRS: https://prsindia.org/"],
"strategy":["Read the current UPSC notification and syllabus.","Build foundations using NCERT and standard sources.","Practise answer writing and previous papers.","Prepare optional subject carefully.","Revise current affairs and take balanced mock tests."],
"skills":["Analytical thinking","Writing","Decision making","Awareness","Ethical reasoning"],
"opportunities":"Service-specific administrative, police, diplomatic, revenue and other public responsibilities; allocation depends on rank, preferences, vacancies and rules.",
"salary":"Depends on service, pay level, posting and allowances under current government rules.",
"official":["https://upsc.gov.in/"]
},
"Banking Exams": {
"intro":"Bank recruitment examinations select candidates for clerical, probationary officer and specialist roles in participating banks.",
"qualification":"Graduation is common for IBPS/SBI clerk and PO roles; specialist posts may require specific degrees or certifications.",
"age":"Varies by post, bank and notification. Category relaxations are specified in the official notice.",
"admission":"Apply separately for the relevant IBPS, SBI or other bank recruitment notification.",
"exam":"May include prelims, mains and interview for officer roles; exact stages differ between recruitments.",
"syllabus":["Reasoning ability","Quantitative aptitude","English language","General and banking awareness","Computer aptitude","Professional knowledge for specialist roles"],
"resources":["IBPS: https://www.ibps.in/","SBI Careers: https://sbi.co.in/web/careers","RBI Opportunities: https://opportunities.rbi.org.in/"],
"strategy":["Select the exact exam and post.","Study its official pattern and sectional timing.","Practise speed and accuracy.","Follow banking/economic current affairs.","Prepare interview and document verification where applicable."],
"skills":["Numeracy","Reasoning","Communication","Financial awareness","Accuracy"],
"opportunities":"Clerk, PO, specialist officer and bank operations/management roles.",
"salary":"Depends on recruiting bank, cadre, posting, allowances and current wage rules.",
"official":["https://www.ibps.in/","https://sbi.co.in/web/careers"]
},
"Railway Exams": {
"intro":"Railway recruitment covers technical and non-technical posts in Indian Railways through different RRB/RRC notifications.",
"qualification":"Varies: some posts require Class 10/ITI, Class 12, diploma or graduation; technical posts may require specific trade/discipline.",
"age":"Post-specific and notification-specific, with relaxations as published by the recruiting board.",
"admission":"Apply only through the official RRB/RRC portal named in the notification.",
"exam":"Different recruitments include RRB NTPC, Group D, ALP, Technician and JE; stages and aptitude/skill tests differ.",
"syllabus":["Mathematics","General intelligence and reasoning","General awareness/current affairs","General science","Technical trade/discipline knowledge for relevant posts","Aptitude or skill tests where applicable"],
"resources":["Indian Railways: https://indianrailways.gov.in/","RRB portal links from official railway site","NCERT: https://ncert.nic.in/"],
"strategy":["Identify the exact railway post.","Read the official notification for qualification, age and medical standards.","Study the notified syllabus only.","Practise previous papers and mock tests.","Prepare required trade, aptitude or physical standards where applicable."],
"skills":["Reasoning","Numeracy","Technical knowledge where required","Safety awareness","Discipline"],
"opportunities":"Operational, technical, clerical, station, maintenance and supervisory roles depending on recruitment.",
"salary":"Varies by post, pay level, allowances and railway zone.",
"official":["https://indianrailways.gov.in/"]
},
"NDA": {
"intro":"The National Defence Academy route trains eligible candidates for officer careers in the Army, Navy and Air Force, subject to service selection.",
"qualification":"Class 12 or equivalent. Army wing accepts the notified subjects; Air Force and Naval wings require Physics, Chemistry and Mathematics as specified.",
"age":"A narrow birth-date window is prescribed in each UPSC NDA notice; check the exact dates for the examination cycle.",
"admission":"UPSC written examination followed by Services Selection Board assessment, medical examination and final merit/allocation.",
"exam":"Written Mathematics and General Ability Test, followed by SSB selection and medical standards.",
"syllabus":["Mathematics","English","Physics","Chemistry","General science","History and geography","Current events","SSB psychological, group and interview assessments"],
"resources":["UPSC NDA: https://upsc.gov.in/","Join Indian Army: https://joinindianarmy.nic.in/","Indian Navy: https://www.joinindiannavy.gov.in/","AFCAT/IAF: https://afcat.cdac.in/"],
"strategy":["Check exact date-of-birth and subject conditions.","Prepare Mathematics and GAT from the notified syllabus.","Build general fitness safely and consistently.","Understand SSB stages and officer-like qualities.","Read medical standards and service preferences carefully."],
"skills":["Academic foundations","Teamwork","Communication","Leadership","Responsible fitness"],
"opportunities":"Training and commissioning into the respective service subject to merit, medical fitness and service allocation.",
"salary":"Military pay, rank and allowances follow current government and service rules after commissioning; training-stage conditions differ.",
"official":["https://upsc.gov.in/","https://joinindianarmy.nic.in/","https://www.joinindiannavy.gov.in/"]
},
"Graphic Designing": {
"intro":"Graphic designers communicate ideas visually through layouts, typography, images and digital or print design.",
"qualification":"A design degree/diploma can help, but many roles assess portfolio, practical ability and software knowledge.",
"age":"No universal profession-wide age limit; institute admission rules may set conditions.",
"admission":"Design institutes may use entrance tests, studio tasks, interviews or portfolio reviews.",
"exam":"NID DAT, UCEED or institute-specific tests may be relevant to particular design programmes; they are not mandatory for every job.",
"syllabus":["Visual communication","Typography","Colour theory","Composition","Brand identity","Image editing","Layout and publication design","Design history and research"],
"resources":["NID: https://www.nid.edu/","UCEED: https://uceed.iitb.ac.in/","Adobe tutorials: https://helpx.adobe.com/"],
"strategy":["Learn design principles before relying on software.","Practise typography, layout and visual hierarchy.","Create original briefs and portfolio case studies.","Learn feedback and revision workflows.","Check licensing and accessibility of assets."],
"skills":["Visual thinking","Typography","Creativity","Software proficiency","Client communication"],
"opportunities":"Graphic designer, brand designer, publication designer, UI visual designer, packaging designer or freelance work.",
"salary":"Depends on portfolio, specialisation, location, employer and experience.",
"official":["https://www.nid.edu/","https://uceed.iitb.ac.in/"]
},
"Animation": {
"intro":"Animation creates moving visual stories for films, games, advertising, education and digital media.",
"qualification":"Relevant degree/diploma is useful but portfolio and demonstrable skills are important; institute requirements vary.",
"age":"No universal profession-wide age limit.",
"admission":"Animation institutes may admit through merit, aptitude tests, interviews or portfolio review.",
"exam":"No single national animation entrance exam for all programmes.",
"syllabus":["Drawing and observation","Storyboarding","Timing and movement","2D/3D principles","Modelling","Texturing and lighting","Rigging","Compositing and editing"],
"resources":["Blender: https://www.blender.org/","Autodesk Education: https://www.autodesk.com/education/","NPTEL: https://nptel.ac.in/"],
"strategy":["Practise drawing and observation.","Learn animation principles and one tool.","Create short exercises before large projects.","Build a showreel with your own work.","Study feedback, teamwork and production pipelines."],
"skills":["Visual storytelling","Observation","Patience","3D/2D tools","Collaboration"],
"opportunities":"2D/3D animator, modeller, rigger, storyboard artist, VFX/compositing artist or game artist.",
"salary":"Varies by specialisation, showreel, studio, project type and experience.",
"official":["https://www.blender.org/","https://www.autodesk.com/education/"]
},
"Fashion Designing": {
"intro":"Fashion design involves researching, designing and developing clothing, accessories and related products.",
"qualification":"Relevant fashion degree/diploma; Class 12 subject and marks requirements depend on the institute.",
"age":"Institute-specific admission conditions apply.",
"admission":"NIFT and other institutes may use entrance tests, situation tests, interviews or portfolio components as notified.",
"exam":"NIFT entrance process for NIFT programmes; other institutes have their own admission systems.",
"syllabus":["Design fundamentals","Drawing and illustration","Textiles","Pattern making","Garment construction","Fashion history","Trend research","Merchandising and sustainability"],
"resources":["NIFT: https://www.nift.ac.in/","NID: https://www.nid.edu/"],
"strategy":["Check the current institute admission brochure.","Practise observation, drawing and creative problem-solving.","Learn fabrics and garment construction.","Build a process-based portfolio.","Understand sourcing, costing and sustainable design."],
"skills":["Creativity","Drawing","Textile knowledge","Research","Communication"],
"opportunities":"Fashion designer, assistant designer, stylist, merchandiser, textile designer, costume designer or entrepreneur.",
"salary":"Depends on portfolio, brand, location, role and experience.",
"official":["https://www.nift.ac.in/","https://www.nid.edu/"]
},
"Journalism": {
"intro":"Journalism gathers, verifies and communicates information through print, broadcast, digital and audio-visual media.",
"qualification":"A journalism/mass communication degree can help; some entry roles accept graduates from other disciplines with strong reporting skills.",
"age":"No universal profession-wide age limit; university admission rules apply.",
"admission":"BA Journalism/Mass Communication or postgraduate programmes through merit or institution-specific entrance tests.",
"exam":"No single national exam for all journalism courses or jobs.",
"syllabus":["News writing","Reporting","Media law and ethics","Editing","Broadcast journalism","Digital journalism","Fact-checking","Media research"],
"resources":["Press Council of India: https://presscouncil.nic.in/","Reuters Handbook: https://www.reuters.com/","SWAYAM: https://swayam.gov.in/"],
"strategy":["Read diverse credible news sources.","Practise clear, accurate writing.","Learn verification and source protection principles.","Create sample reports and multimedia work.","Understand media law, ethics and corrections."],
"skills":["Writing","Interviewing","Research","Verification","Deadline management"],
"opportunities":"Reporter, sub-editor, producer, digital journalist, researcher, correspondent or communications roles.",
"salary":"Varies by organisation, platform, location, beat and experience.",
"official":["https://presscouncil.nic.in/"]
},
"Hotel Management": {
"intro":"Hotel management prepares students for hospitality operations in hotels, restaurants, resorts, events and related services.",
"qualification":"Class 12 is commonly required for undergraduate hospitality programmes; exact subject and marks rules vary.",
"age":"Institute and entrance-notice specific.",
"admission":"NCHM JEE is used for participating central IHMs; other institutes may have separate admission processes.",
"exam":"NCHM JEE commonly tests numerical ability, reasoning, general knowledge, English and service aptitude as per current bulletin.",
"syllabus":["Food production","Food and beverage service","Front office","Housekeeping","Hospitality accounting","Hotel operations","Communication","Customer service"],
"resources":["NCHM JEE: https://exams.nta.ac.in/NCHM/","NCHMCT: https://nchm.gov.in/"],
"strategy":["Check current NCHM JEE and institute rules.","Practise English, reasoning and numerical basics.","Understand practical training and internships.","Build customer-service and teamwork skills.","Compare institute facilities and placement information carefully."],
"skills":["Communication","Service orientation","Organisation","Teamwork","Problem solving"],
"opportunities":"Front office, food production, food and beverage, housekeeping, events, travel, revenue or hotel operations.",
"salary":"Depends on property, department, location, role and experience.",
"official":["https://nchm.gov.in/","https://exams.nta.ac.in/NCHM/"]
},
"BA LLB": {
"intro":"BA LLB is an integrated five-year undergraduate law degree combining arts/social science subjects with legal education.",
"qualification":"Class 12 or equivalent; minimum marks and other eligibility depend on the university and current admission rules.",
"age":"Follow the current university/consortium prospectus and applicable legal education regulations; do not assume one age rule for all institutions.",
"admission":"CLAT for participating NLUs, AILET for NLU Delhi and other university-specific routes.",
"exam":"CLAT UG commonly includes English, current affairs, legal reasoning, logical reasoning and quantitative techniques; check current pattern.",
"syllabus":["Political science and sociology foundations","Legal methods","Constitutional law","Contract law","Criminal law","Torts","Civil procedure","Evidence","Moot court and internships"],
"resources":["CLAT: https://consortiumofnlus.ac.in/","NLU Delhi AILET: https://nationallawuniversitydelhi.in/","Bar Council of India: https://www.barcouncilofindia.org/"],
"strategy":["Compare NLU and other college admission routes.","Read the current CLAT/AILET pattern.","Build reading comprehension and reasoning.","Follow legal current affairs.","Use internships, moots and research to explore practice areas."],
"skills":["Reading","Legal reasoning","Research","Writing","Public speaking"],
"opportunities":"Advocacy after required enrolment and rules, litigation, corporate law, policy, legal research or higher studies.",
"salary":"Varies greatly by institution, practice area, employer, city and experience.",
"official":["https://consortiumofnlus.ac.in/","https://nationallawuniversitydelhi.in/","https://www.barcouncilofindia.org/"]
},
"BBA LLB": {
"intro":"BBA LLB is an integrated five-year law degree combining business/management studies with legal education.",
"qualification":"Class 12 or equivalent; minimum marks and subject conditions depend on the institution.",
"age":"Check the current admission prospectus and applicable legal education rules.",
"admission":"CLAT, AILET or university-specific admission processes depending on the college.",
"exam":"CLAT UG or the institution's own test may apply; common areas include English, current affairs, legal and logical reasoning, and quantitative techniques.",
"syllabus":["Management principles","Business economics","Accounting basics","Constitutional law","Contract law","Company law","Taxation","Corporate and commercial law","Moot court and internships"],
"resources":["https://consortiumofnlus.ac.in/","https://nationallawuniversitydelhi.in/","https://www.barcouncilofindia.org/"],
"strategy":["Check the university's curriculum and admission rules.","Prepare for the applicable law entrance test.","Build business and legal reading habits.","Take part in moots, research and internships.","Explore corporate/commercial law through supervised learning."],
"skills":["Legal research","Business awareness","Drafting","Negotiation","Communication"],
"opportunities":"Corporate legal teams, law firms, compliance, contracts, litigation or policy roles, subject to qualifications and enrolment rules.",
"salary":"Depends on institution, employer, specialisation, location and experience.",
"official":["https://consortiumofnlus.ac.in/","https://www.barcouncilofindia.org/"]
},
"LLB": {
"intro":"The three-year LLB is a graduate-entry professional law degree for students who already hold a bachelor's degree.",
"qualification":"A recognised bachelor's degree; minimum marks and eligibility vary by university.",
"age":"Check the current university admission rules and applicable legal education regulations.",
"admission":"University entrance tests or merit-based admissions, depending on the institution.",
"exam":"No single national entrance exam for every three-year LLB programme.",
"syllabus":["Constitutional law","Contract law","Criminal law","Torts","Family law","Property law","Civil procedure","Evidence","Professional ethics and practical training"],
"resources":["University admission portal","Bar Council of India: https://www.barcouncilofindia.org/","India Code: https://www.indiacode.nic.in/"],
"strategy":["Compare recognised institutions and current eligibility.","Prepare for the specific university entrance test.","Read statutes and legal cases carefully.","Practise legal writing and research.","Check enrolment and bar examination requirements for practice."],
"skills":["Legal analysis","Research","Writing","Advocacy","Ethical judgement"],
"opportunities":"Advocacy, legal research, corporate legal work, compliance, public policy or further legal study.",
"salary":"Varies by employer, practice area, location and experience.",
"official":["https://www.barcouncilofindia.org/","https://www.indiacode.nic.in/"]
},
"Legal Studies": {
"intro":"Legal studies is an academic pathway exploring law, legal institutions, rights, governance and justice; it is not automatically a professional licence to practise law.",
"qualification":"Requirements depend on whether the programme is a certificate, BA, integrated law degree or postgraduate course.",
"age":"Institution-specific.",
"admission":"University-specific merit or entrance process.",
"exam":"No single entrance examination applies to all legal studies programmes.",
"syllabus":["Legal systems","Constitution and rights","Criminal justice","Public law","International law basics","Legal research","Society and law","Policy analysis"],
"resources":["India Code: https://www.indiacode.nic.in/","Supreme Court of India: https://www.sci.gov.in/","Bar Council of India: https://www.barcouncilofindia.org/"],
"strategy":["Identify whether the goal is academic study or qualifying as a lawyer.","Check programme recognition and award title.","Develop reading, research and writing skills.","Study primary legal materials and case analysis.","For legal practice, verify the required recognised law degree and enrolment route."],
"skills":["Research","Critical reading","Writing","Policy analysis","Communication"],
"opportunities":"Policy research, legal research support, public administration, compliance support or further professional law study; role eligibility varies.",
"salary":"Depends on the exact qualification and job; this broad subject does not guarantee a particular legal role.",
"official":["https://www.indiacode.nic.in/","https://www.barcouncilofindia.org/"]
},
"Cricketer": {
"intro":"A professional cricketer develops sport-specific skills and progresses through organised club, district, state, domestic and potentially national cricket.",
"qualification":"No academic degree is required to play professionally. Continue education alongside sport; selection is based on cricketing performance and eligibility.",
"age":"No single age limit for all cricket careers. BCCI/state association age-group competitions have specific birth-date and documentation rules.",
"admission":"Join a reputable academy or club, register with the relevant district/state association and take part in recognised competitions and trials.",
"exam":"No standard written entrance exam. Selection is based on trials, match performance, fitness and team requirements.",
"syllabus":["Batting or bowling technique","Fielding and wicketkeeping","Cricket laws","Match tactics","Physical preparation under qualified coaches","Teamwork and sportsmanship"],
"resources":["BCCI: https://www.bcci.tv/","State cricket association official website","ICC: https://www.icc-cricket.com/"],
"strategy":["Find qualified, reputable coaching.","Learn fundamentals and safe training habits.","Play age-appropriate local and recognised competitions.","Keep performance records and accept coaching feedback.","Balance education, rest and sport."],
"skills":["Batting/bowling","Fielding","Game awareness","Teamwork","Discipline"],
"opportunities":"Club, district, state, age-group, domestic, franchise and potentially national cricket; progression is competitive and not guaranteed.",
"salary":"No fixed salary. Match fees, contracts and sponsorships depend on selection level, performance and agreements.",
"official":["https://www.bcci.tv/","https://www.icc-cricket.com/"]
},
"Footballer": {
"intro":"A footballer trains and competes in organised football, progressing through local clubs, academies, leagues and representative teams.",
"qualification":"No specific academic degree is required; education should continue alongside sport.",
"age":"Academy and youth competitions have age-group rules. Senior professional opportunities depend on competition regulations and selection.",
"admission":"Trials and scouting through recognised clubs or academies; check coaching credentials and safeguarding arrangements.",
"exam":"No standard written entrance examination. Selection is based on technical ability, match performance, fitness and team needs.",
"syllabus":["Ball control and passing","Dribbling and shooting","Defending and positioning","Tactical awareness","Rules of football","Teamwork and safe conditioning"],
"resources":["AIFF: https://www.the-aiff.com/","FIFA: https://www.fifa.com/","Recognised state football association"],
"strategy":["Learn fundamentals under qualified coaches.","Play organised age-appropriate matches.","Develop tactical understanding and teamwork.","Use safe, balanced training and recovery.","Keep school/college education progressing."],
"skills":["Ball skills","Tactical awareness","Teamwork","Communication","Discipline"],
"opportunities":"Club football, state/national age-group pathways, leagues, coaching or sports-related roles.",
"salary":"Highly variable; contracts depend on club, league, level, performance and sponsorship.",
"official":["https://www.the-aiff.com/","https://www.fifa.com/"]
},
"Athlete": {
"intro":"An athlete trains and competes in an individual sport such as athletics, swimming, badminton, wrestling or another recognised discipline.",
"qualification":"No universal academic degree is required for competition. Education and sport can be pursued together.",
"age":"Age-group categories and competition eligibility are sport-specific.",
"admission":"Join a recognised sports club, district association or academy and participate in official competitions.",
"exam":"No common written exam. Selection uses event performance, trials, rankings and qualification standards.",
"syllabus":["Sport-specific technique","Rules and event formats","Movement skills","Tactics","Safe conditioning and recovery","Competition preparation"],
"resources":["Sports Authority of India: https://sportsauthorityofindia.nic.in/","Indian Olympic Association: https://olympic.ind.in/","Relevant national sports federation"],
"strategy":["Choose a sport and qualified coach.","Learn the official rules and age categories.","Build technique progressively and safely.","Compete in recognised events and track results.","Balance training, rest, nutrition and education with adult/coach support."],
"skills":["Sport technique","Focus","Discipline","Resilience","Competition awareness"],
"opportunities":"Club, district, state, national and international competition; later coaching, officiating or sports administration.",
"salary":"Not guaranteed; depends on performance, selection, contracts, awards and sponsorship.",
"official":["https://sportsauthorityofindia.nic.in/","https://olympic.ind.in/"]
},
"Sports Coach": {
"intro":"Sports coaches teach sport skills, plan training, support athlete development and promote safe participation.",
"qualification":"Sport-specific coaching certifications, recognised qualifications and practical experience may be required by employer/federation.",
"age":"No universal profession-wide age limit; course and recruitment rules apply.",
"admission":"Coaching courses and certifications are offered by recognised sports bodies and institutions.",
"exam":"Certification assessments may include theory, practical coaching and evaluation; requirements vary by sport.",
"syllabus":["Sport rules and technique","Coaching methodology","Training principles","Basic sports science","Injury prevention and safeguarding","Communication and athlete development"],
"resources":["Sports Authority of India: https://sportsauthorityofindia.nic.in/","National sports federation for the chosen sport","NPTEL: https://nptel.ac.in/"],
"strategy":["Build experience in a chosen sport.","Check recognised certification routes.","Learn age-appropriate coaching and safeguarding.","Gain supervised practical experience.","Keep qualifications and first-aid knowledge current."],
"skills":["Teaching","Communication","Sport expertise","Planning","Safeguarding awareness"],
"opportunities":"Academy coach, school/college coach, club coach, fitness/sport programme instructor or high-performance pathway with further qualifications.",
"salary":"Depends on certification, employer, sport, location and experience.",
"official":["https://sportsauthorityofindia.nic.in/"]
},
"YouTuber": {
"intro":"A YouTuber plans, creates and publishes original video content for an audience on YouTube.",
"qualification":"No specific degree is required. Research, communication, storytelling and production skills are useful.",
"age":"YouTube account and monetisation rules have age and guardian requirements. Under-18 users should involve a parent/guardian where required; check current platform terms.",
"admission":"No formal admission. Learn production, plan a responsible channel concept and follow platform rules.",
"exam":"No entrance examination. Monetisation depends on current YouTube Partner Programme eligibility, review and policy compliance.",
"syllabus":["Topic research","Script and storytelling","Recording and editing","Thumbnail and title design","Audience analytics","Copyright and privacy","Community guidelines and monetisation policies"],
"resources":["YouTube Creator Academy: https://creatoracademy.youtube.com/","YouTube Help: https://support.google.com/youtube/","YouTube policies: https://www.youtube.com/howyoutubeworks/policies/"],
"strategy":["Choose a topic you understand and can cover responsibly.","Make original, useful videos without exposing private information.","Learn basic scripting, recording and editing.","Follow copyright, safety and community rules.","Review analytics and improve content quality; do not assume income."],
"skills":["Communication","Research","Storytelling","Editing","Consistency"],
"opportunities":"Video production, education, media, brand work and independent creator work; audience and income are uncertain.",
"salary":"No fixed salary. Revenue depends on eligibility, audience, content, advertiser demand and other permitted income streams.",
"official":["https://creatoracademy.youtube.com/","https://support.google.com/youtube/"]
},
"Content Creator": {
"intro":"Content creators produce written, visual, audio or video material for audiences, organisations or digital platforms.",
"qualification":"No universal degree requirement; subject knowledge, communication and a portfolio are useful.",
"age":"Platform terms and contract rules apply. Minors should involve a parent/guardian for agreements and account requirements.",
"admission":"No standard admission route; build skills through practice, courses and original portfolio work.",
"exam":"No universal entrance exam. Employers/clients may assess samples and practical tasks.",
"syllabus":["Audience research","Content strategy","Writing and storytelling","Photography/video basics","Editing","Accessibility","Copyright and platform policies"],
"resources":["SWAYAM: https://swayam.gov.in/","YouTube Creator Academy: https://creatoracademy.youtube.com/","Canva Design School: https://www.canva.com/designschool/"],
"strategy":["Choose a clear subject area.","Research facts and cite reliable sources.","Create original sample work.","Learn accessible formatting and basic editing.","Protect privacy and follow copyright/platform rules."],
"skills":["Writing","Creativity","Research","Communication","Editing"],
"opportunities":"Writer, creator, producer, community educator, content strategist or freelance work.",
"salary":"Varies by employer, clients, audience, platform and experience; independent income is not guaranteed.",
"official":["https://swayam.gov.in/","https://creatoracademy.youtube.com/"]
},
"Social Media Manager": {
"intro":"Social media managers plan, publish and evaluate an organisation's social media communication.",
"qualification":"Marketing, communications or business education can help; portfolio and platform skills are important.",
"age":"No universal profession-wide age limit; employment rules apply.",
"admission":"Relevant degree/diploma or online learning; no single mandatory qualification.",
"exam":"No standard national entrance exam. Employers may use practical assignments and interviews.",
"syllabus":["Content calendars","Brand voice","Platform formats","Community moderation","Analytics","Campaign planning","Copyright and advertising disclosure","Crisis communication"],
"resources":["Meta Blueprint: https://www.facebook.com/business/learn","Google Skillshop: https://skillshop.withgoogle.com/","LinkedIn Learning: https://www.linkedin.com/learning/"],
"strategy":["Learn how different platforms work.","Practise planning a sample content calendar.","Understand analytics and reporting.","Learn moderation, privacy and disclosure rules.","Build case studies showing goals and results honestly."],
"skills":["Writing","Planning","Analytics","Communication","Judgement"],
"opportunities":"Social media executive, community manager, digital communications specialist or marketing strategist.",
"salary":"Depends on organisation, city, account scope, skills and experience.",
"official":["https://www.facebook.com/business/learn","https://skillshop.withgoogle.com/"]
},
"Video Editor": {
"intro":"Video editors shape recorded footage into coherent videos for film, education, advertising, news and online media.",
"qualification":"A media degree/diploma can help, but a strong showreel and editing ability are often important.",
"age":"No universal profession-wide age limit; training institute rules apply.",
"admission":"Media courses may use merit, entrance tests or portfolios. Independent learning is also possible.",
"exam":"No single national exam for video-editing jobs.",
"syllabus":["Editing principles","Story structure","Audio editing","Colour correction","Titles and graphics","Export formats","File management","Copyright and permissions"],
"resources":["DaVinci Resolve: https://www.blackmagicdesign.com/products/davinciresolve","Adobe tutorials: https://helpx.adobe.com/","Blender: https://www.blender.org/"],
"strategy":["Learn one editing application.","Practise cuts, pacing, sound and captions.","Create a short showreel using permitted footage.","Learn file organisation and export settings.","Respect music, footage and image licences."],
"skills":["Visual storytelling","Timing","Audio awareness","Software proficiency","Attention to detail"],
"opportunities":"Assistant editor, video editor, post-production assistant, social video editor or freelance editor.",
"salary":"Depends on portfolio, project complexity, employer, location and experience.",
"official":["https://www.blackmagicdesign.com/products/davinciresolve","https://helpx.adobe.com/"]
},
"Digital Marketer": {
"intro":"Digital marketers plan and evaluate online campaigns across search, websites, email, social media and paid advertising.",
"qualification":"Marketing, business or communications education is useful but not mandatory for every entry role.",
"age":"No universal profession-wide age limit.",
"admission":"Degree, diploma or structured online learning; employers assess practical knowledge.",
"exam":"No single national entrance exam. Some platforms offer optional certifications.",
"syllabus":["Marketing fundamentals","SEO","Search and social ads","Content marketing","Email marketing","Web analytics","Conversion measurement","Privacy and advertising rules"],
"resources":["Google Skillshop: https://skillshop.withgoogle.com/","Google Search Central: https://developers.google.com/search","Meta Blueprint: https://www.facebook.com/business/learn"],
"strategy":["Learn marketing fundamentals first.","Practise SEO and analytics on a sample project.","Understand audience research and campaign objectives.","Learn privacy, consent and ad disclosure rules.","Build a portfolio with transparent results."],
"skills":["Analysis","Writing","Creativity","Communication","Data literacy"],
"opportunities":"SEO executive, performance marketer, content marketer, email marketer, campaign analyst or marketing manager.",
"salary":"Depends on specialisation, measurable experience, employer, location and industry.",
"official":["https://skillshop.withgoogle.com/","https://developers.google.com/search"]
},
"Scientist": {
"intro":"A scientist investigates questions systematically using evidence, research methods and discipline-specific knowledge.",
"qualification":"Usually a relevant bachelor's degree followed by master's/PhD for many research roles; requirements vary by discipline and employer.",
"age":"No universal age limit for the profession. Specific fellowships and recruitment notices may set age criteria.",
"admission":"Choose a science discipline and enter recognised undergraduate/postgraduate programmes; research pathways vary.",
"exam":"Possible routes include university entrance tests, CSIR-UGC NET, GATE, institutional tests and recruitment exams depending on field and role.",
"syllabus":["Core subject foundations","Mathematics/statistics as relevant","Research methods","Experimental design","Data analysis","Scientific writing","Research ethics"],
"resources":["CSIR HRDG: https://csirhrdg.res.in/","UGC: https://www.ugc.gov.in/","NPTEL: https://nptel.ac.in/","INFLIBNET: https://www.inflibnet.ac.in/"],
"strategy":["Choose a subject based on genuine interest and strengths.","Build deep undergraduate fundamentals.","Learn research methods and statistics.","Seek supervised projects and research internships.","Read papers critically and learn ethical research practice."],
"skills":["Critical thinking","Research design","Data analysis","Writing","Persistence"],
"opportunities":"Research assistant, project fellow, academic researcher, laboratory scientist or specialist roles in public/private institutions.",
"salary":"Depends on qualification, funding, institution, discipline, role and experience.",
"official":["https://csirhrdg.res.in/","https://www.ugc.gov.in/"]
},
"Research Scientist": {
"intro":"Research scientists design and conduct specialised studies, analyse results and communicate findings in academic, government or industry settings.",
"qualification":"A relevant master's degree is common; many independent research scientist roles require a PhD and research record.",
"age":"No universal career age limit; fellowships and project vacancies may impose their own age rules.",
"admission":"Study a relevant subject, pursue postgraduate research and apply to laboratories, universities or funded projects.",
"exam":"Depending on discipline: CSIR-UGC NET, GATE, DBT/ICMR-related fellowships, university PhD tests or institute-specific selection.",
"syllabus":["Advanced discipline knowledge","Research methodology","Statistics and data analysis","Laboratory/field methods","Literature review","Research ethics","Scientific communication"],
"resources":["CSIR: https://www.csir.res.in/","CSIR HRDG: https://csirhrdg.res.in/","ICMR: https://www.icmr.gov.in/","DBT: https://dbtindia.gov.in/"],
"strategy":["Identify a research field and suitable labs.","Build a strong subject foundation.","Learn methods and research ethics.","Develop a research proposal and seek supervised experience.","Read current papers and practise presenting results."],
"skills":["Experimental design","Analysis","Technical writing","Collaboration","Research integrity"],
"opportunities":"Postdoctoral researcher, scientist, principal investigator pathway, R&D specialist or academic roles, depending on experience and openings.",
"salary":"Varies by funding scheme, institute, seniority, discipline and appointment type.",
"official":["https://www.csir.res.in/","https://www.icmr.gov.in/","https://dbtindia.gov.in/"]
},
"Space Scientist": {
"intro":"Space scientists study astronomy, planetary science, atmospheric science, space physics, remote sensing or develop space technology.",
"qualification":"Relevant degrees in physics, astronomy, mathematics, aerospace, electronics, computer science or related fields; research roles often require postgraduate study.",
"age":"No universal age limit. Specific ISRO recruitment, fellowship and project notices set their own criteria.",
"admission":"Pursue a relevant science/engineering degree, then specialise through postgraduate study or research.",
"exam":"Depending on role: JEE-based engineering admission, university tests, GATE or ISRO recruitment selection; there is no one exam for all space scientists.",
"syllabus":["Physics and mathematics","Orbital mechanics where relevant","Electronics/instrumentation","Programming and data analysis","Remote sensing or astrophysics","Research methods"],
"resources":["ISRO: https://www.isro.gov.in/","IISc: https://iisc.ac.in/","IUCAA: https://www.iucaa.in/","NPTEL: https://nptel.ac.in/"],
"strategy":["Build strong mathematics and physics foundations.","Choose science research or engineering pathway.","Learn programming and data analysis.","Explore recognised universities and research institutes.","Check specific ISRO/institute recruitment criteria."],
"skills":["Physics","Mathematics","Programming","Research","Teamwork"],
"opportunities":"Space research, satellite systems, mission analysis, astrophysics, remote sensing, instrumentation or academic research.",
"salary":"Depends on institute, role, qualification, pay scale and experience.",
"official":["https://www.isro.gov.in/","https://iisc.ac.in/","https://www.iucaa.in/"]
},
"Environmental Scientist": {
"intro":"Environmental scientists study ecosystems, pollution, climate, natural resources and environmental impacts.",
"qualification":"Relevant degrees include environmental science, biology, chemistry, geology, geography or engineering; specialist roles may require postgraduate study.",
"age":"No universal profession-wide age limit; recruitment and fellowship notices may specify limits.",
"admission":"University merit or entrance routes vary by course and institution.",
"exam":"Some postgraduate programmes use university tests; government research roles have separate recruitment processes.",
"syllabus":["Ecology","Environmental chemistry","Climate science","Biodiversity","Pollution monitoring","GIS/remote sensing","Environmental laws","Statistics and field methods"],
"resources":["MoEFCC: https://moef.gov.in/","CPCB: https://cpcb.nic.in/","NPTEL: https://nptel.ac.in/"],
"strategy":["Build biology, chemistry and geography foundations.","Learn field sampling and data interpretation.","Study environmental laws and impact assessment.","Gain supervised field or lab experience.","Develop GIS and scientific writing skills."],
"skills":["Field research","Data analysis","Scientific writing","Observation","Environmental awareness"],
"opportunities":"Environmental consultant, EIA support, pollution monitoring, conservation, sustainability, research or government projects.",
"salary":"Depends on qualification, employer, project funding, location and experience.",
"official":["https://moef.gov.in/","https://cpcb.nic.in/"]
},
"Politician": {
"intro":"An elected politician represents constituents and participates in democratic decision-making and public policy.",
"qualification":"There is no general minimum educational qualification for Lok Sabha or State Legislative Assembly candidates; constitutional and statutory eligibility conditions still apply.",
"age":"Generally at least 25 for Lok Sabha/State Assembly and 30 for Rajya Sabha/State Legislative Council, subject to other legal conditions.",
"admission":"No course admission or standard recruitment process. Candidates must satisfy election law, nomination and scrutiny requirements.",
"exam":"No competitive entrance examination for elected office. Election is by the relevant electoral process.",
"syllabus":["Indian Constitution","Parliament and state legislatures","Election law","Public policy","Economics","Local governance","Public finance","Constituency issues"],
"resources":["Election Commission of India: https://www.eci.gov.in/","India Code: https://www.indiacode.nic.in/","Parliament of India: https://sansad.in/"],
"strategy":["Study constitutional democracy and election laws.","Understand local issues through lawful community engagement.","Develop evidence-based communication.","Respect democratic processes and diverse communities.","Verify nomination and disqualification rules with ECI materials."],
"skills":["Public communication","Listening","Policy analysis","Leadership","Ethical judgement"],
"opportunities":"Local bodies, state legislature, Parliament and party/public policy roles; election outcomes are not guaranteed.",
"salary":"Honorarium, salary and allowances depend on the elected office and applicable law.",
"official":["https://www.eci.gov.in/","https://www.indiacode.nic.in/","https://sansad.in/"]
},
"Political Analyst": {
"intro":"Political analysts research political institutions, elections, public opinion, policy and government decisions.",
"qualification":"Political science, public policy, economics, sociology, statistics, journalism or related degrees are useful; research roles may prefer postgraduate study.",
"age":"No universal profession-wide age limit.",
"admission":"University programmes in political science, public policy, international relations or data/social research.",
"exam":"University admission tests may apply. There is no single national political analyst exam.",
"syllabus":["Political theory","Indian polity","Comparative politics","Public policy","Research methods","Statistics and polling literacy","International relations","Political communication"],
"resources":["PRS Legislative Research: https://prsindia.org/","Election Commission: https://www.eci.gov.in/","SWAYAM: https://swayam.gov.in/"],
"strategy":["Build foundations in political science and research methods.","Learn to evaluate data and polling claims critically.","Read legislation and policy documents.","Write balanced research briefs with sources.","Develop statistics and data visualisation skills."],
"skills":["Research","Writing","Data literacy","Critical thinking","Neutral analysis"],
"opportunities":"Policy researcher, legislative researcher, political risk analyst, campaign research, journalism or think-tank roles.",
"salary":"Depends on employer, research skills, location, project and experience.",
"official":["https://prsindia.org/","https://www.eci.gov.in/"]
},
"Public Administration": {
"intro":"Public administration studies how public institutions design, implement and evaluate government programmes and services.",
"qualification":"Relevant degrees include public administration, political science, economics, law or management; requirements depend on the target role.",
"age":"No universal age limit for the subject. Government recruitment roles have separate post-specific age rules.",
"admission":"BA/MA or related programmes through university merit or entrance procedures.",
"exam":"UPSC and State PSC exams recruit for certain administrative services, but studying public administration itself does not require one universal exam.",
"syllabus":["Administrative theory","Indian administration","Public policy","Governance","Public finance","Personnel administration","Local government","Development administration"],
"resources":["UPSC: https://upsc.gov.in/","PRS: https://prsindia.org/","DARPG: https://darpg.gov.in/","SWAYAM: https://swayam.gov.in/"],
"strategy":["Study administrative institutions and constitutional framework.","Understand policy design and implementation.","Read government reports and budgets.","Develop research, writing and data skills.","For civil-service roles, separately prepare for the relevant recruitment exam."],
"skills":["Policy analysis","Organisation","Writing","Research","Public communication"],
"opportunities":"Policy research, programme management, public-sector projects, NGOs, consulting or competitive public-service roles.",
"salary":"Depends on whether the role is government, research, NGO or private-sector and on its pay structure.",
"official":["https://upsc.gov.in/","https://darpg.gov.in/","https://prsindia.org/"]
},
"Social Worker": {
"intro":"Social workers support individuals and communities, connect people with services and work on social welfare and development issues.",
"qualification":"BSW is a common undergraduate route; MSW is useful or required for many specialised roles. Employer requirements vary.",
"age":"No universal profession-wide age limit; course and job requirements apply.",
"admission":"BSW/MSW admission through merit or university-specific entrance processes.",
"exam":"No single national entrance exam for all social work courses or jobs.",
"syllabus":["Social work foundations","Human behaviour","Community organisation","Social policy","Counselling basics","Case work","Research methods","Fieldwork and ethics"],
"resources":["Ministry of Social Justice: https://socialjustice.gov.in/","SWAYAM: https://swayam.gov.in/","University social work department resources"],
"strategy":["Compare accredited programmes and fieldwork placements.","Build communication and listening skills.","Learn confidentiality, safeguarding and professional boundaries.","Gain supervised field experience.","Understand local welfare systems and referral pathways."],
"skills":["Empathy","Communication","Community engagement","Documentation","Ethical judgement"],
"opportunities":"NGOs, hospitals, schools, community programmes, child/family services, development projects and policy organisations.",
"salary":"Depends on organisation, funding, qualification, location and experience.",
"official":["https://socialjustice.gov.in/"]
}
}

# ----------------------------- Theme -----------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "Light"
if "show_report" not in st.session_state:
    st.session_state.show_report = False
if "selected_career" not in st.session_state:
    st.session_state.selected_career = None
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

theme_choice = st.session_state.theme
if theme_choice == "Dark":
    bg, card, fg, muted, border, input_bg, accent = (
        "#11121C", "rgba(35,36,53,.92)", "#F5F3FF", "#C0BDD3",
        "#44435E", "#25263A", "#A88AFF"
    )
else:
    bg, card, fg, muted, border, input_bg, accent = (
        "#F2F0FA", "rgba(255,255,255,.88)", "#252044", "#625D7B",
        "#E1DCEF", "#FFFFFF", "#7546D8"
    )

st.markdown(f"""
<style>
.stApp {{background-color:{bg}; color:{fg};}}
.block-container {{max-width:1350px;padding-top:1.5rem;padding-bottom:2rem;}}
h1,h2,h3,h4,p,label,span,li {{color:{fg};}}
[data-testid="stMarkdownContainer"] p {{color:{fg};}}
div[data-testid="stVerticalBlockBorderWrapper"] {{
 background:{card};border:1px solid {border};border-radius:20px;
 box-shadow:0 8px 25px rgba(70,50,120,.08);
}}
div[data-baseweb="select"] > div {{background:{input_bg};border:1px solid {border};border-radius:12px;}}
div[data-baseweb="select"] * {{color:{fg}!important;}}
div[role="listbox"],div[data-baseweb="popover"] {{background:{input_bg};}}
div[role="option"] {{color:{fg}!important;}}
.stButton > button {{
 background:{accent};color:white!important;border:0;border-radius:12px;
 min-height:44px;font-weight:650;
}}
.stButton > button:hover {{opacity:.86;border:1px solid {accent};}}
.brand {{font-size:37px;font-weight:850;color:{accent}!important;}}
.subtitle {{color:{muted}!important;font-size:15px;}}
.small-note {{color:{muted}!important;font-size:13px;}}
.footer {{text-align:center;color:{muted}!important;padding:25px;}}
a {{color:{accent}!important;}}
</style>
""", unsafe_allow_html=True)

def reset_form():
    for key, value in {
        "student_class": "Select Class",
        "subject": "Select Subject",
        "interest": "Select Interest",
        "goal": "Select Goal",
    }.items():
        st.session_state[key] = value
    st.session_state.show_report = False
    st.session_state.selected_career = None
    st.session_state.selected_category = None

# ----------------------------- Header -----------------------------
h1, h2 = st.columns([3, 1])
with h1:
    st.markdown('<div class="brand">🧠 Jarvis by Anmol</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Your Smart Study & Career Companion</div>', unsafe_allow_html=True)
with h2:
    chosen_theme = st.selectbox("Appearance", ["Light", "Dark"],
                                index=0 if st.session_state.theme == "Light" else 1,
                                key="theme_picker")
    if chosen_theme != st.session_state.theme:
        st.session_state.theme = chosen_theme
        st.rerun()
st.divider()

# ----------------------------- Student form -----------------------------
st.markdown("## 👋 Welcome to Your Future")
st.markdown('<p class="subtitle">Tell us about yourself to explore suitable career paths.</p>', unsafe_allow_html=True)

with st.container(border=True):
    st.subheader("📚 Student Information")
    c1, c2 = st.columns(2)
    with c1:
        st.selectbox("Select Your Class",
            ["Select Class", "Class 8", "Class 9", "Class 10", "Class 11",
             "Class 12", "After 12th", "College Student"], key="student_class")
        st.selectbox("Favourite Subject",
            ["Select Subject", "Mathematics", "Science", "Biology", "Commerce",
             "English", "Computer Science", "Arts"], key="subject")
    with c2:
        st.selectbox("Your Interest", ["Select Interest"] + list(CAREERS.keys()), key="interest")
        st.selectbox("Your Goal",
            ["Select Goal", "Government Job", "Private Job", "Business",
             "Higher Studies", "Not Decided"], key="goal")
    b1, b2 = st.columns([3, 1])
    with b1:
        get_future = st.button("🚀 GET MY FUTURE", use_container_width=True)
    with b2:
        st.button("↻ RESET", use_container_width=True, on_click=reset_form)

if get_future:
    st.session_state.show_report = True
    st.session_state.selected_career = None
    st.session_state.selected_category = None

if st.session_state.show_report:
    vals = [st.session_state.student_class, st.session_state.subject,
            st.session_state.interest, st.session_state.goal]
    if any(v.startswith("Select ") for v in vals):
        st.warning("Please fill in all four options.")
    else:
        category = st.session_state.interest
        st.success("Your Future Study Report is Ready!")
        with st.container(border=True):
            st.header("📋 Your Future Study Report")
            r1, r2 = st.columns(2)
            with r1:
                st.write("**Your Class:**", st.session_state.student_class)
                st.write("**Favourite Subject:**", st.session_state.subject)
            with r2:
                st.write("**Your Interest:**", category)
                st.write("**Your Goal:**", st.session_state.goal)
            st.divider()
            st.subheader("🎯 Recommended Careers")
            st.caption("Select a career to open its own detailed guide.")
            cols = st.columns(2)
            for i, career in enumerate(CAREERS[category]):
                with cols[i % 2]:
                    if st.button(f"📖 Explore {career} →", key=f"recommend_{career}",
                                 use_container_width=True):
                        st.session_state.selected_career = career
                        st.session_state.selected_category = category
                        st.rerun()
            st.divider()
            st.subheader("📖 Suggested next steps")
            for i, step in enumerate([
                "Read the individual guide and note its eligibility requirements.",
                "Check the current official admission or recruitment notification.",
                "Compare course duration, fees, location and recognition.",
                "Discuss important decisions with a teacher, parent or qualified counsellor."
            ], 1):
                st.write(f"{i}. {step}")

# ----------------------------- Explore careers -----------------------------
st.divider()
st.header("🌍 Explore All Career Options")
st.markdown('<p class="subtitle">Every career below opens a separate profession-specific guide.</p>', unsafe_allow_html=True)
selected_category = st.selectbox("Choose a Career Category", list(CAREERS.keys()), key="explore_category")
career_cols = st.columns(3)
for i, career in enumerate(CAREERS[selected_category]):
    with career_cols[i % 3]:
        if st.button(f"📘 {career}", key=f"explore_{career}", use_container_width=True):
            st.session_state.selected_career = career
            st.session_state.selected_category = selected_category
            st.rerun()

# ----------------------------- Individual career guide -----------------------------
career = st.session_state.selected_career
if career:
    st.divider()
    st.header(f"🎓 {career} — Complete Career Guide")
    if st.button("← Back to Career Exploration", key="back_to_explore"):
        st.session_state.selected_career = None
        st.session_state.selected_category = None
        st.rerun()

    guide = GUIDES.get(career)
    if guide is None:
        st.error("This career guide is not available yet. Please report this issue.")
    else:
        st.info(guide["intro"])
        sections = [
            ("1. Educational Qualification", "qualification"),
            ("2. Age Criteria", "age"),
            ("3. Admission / Entry Process", "admission"),
            ("4. Entrance Examination / Selection", "exam"),
            ("5. Syllabus / Important Topics", "syllabus"),
            ("6. Free Learning Resources & Official Links", "resources"),
            ("7. Preparation / Career-Building Strategy", "strategy"),
            ("8. Important Skills", "skills"),
            ("9. Career Opportunities & Growth", "opportunities"),
            ("10. Salary & Earnings", "salary"),
            ("11. Official Authorities / Websites", "official"),
        ]
        for title, key in sections:
            with st.container(border=True):
                st.subheader(title)
                value = guide[key]
                if isinstance(value, list):
                    for item in value:
                        if key in ("resources", "official") and item.startswith("http"):
                            st.markdown(f"- [{item}]({item})")
                        else:
                            st.markdown(f"- {item}")
                else:
                    st.write(value)

        st.warning(
            "Important: Admission rules, age limits, exam patterns, fees, recognition "
            "and salaries can change. This guide is an orientation, not an official "
            "notification. Verify the latest details with the linked authority and "
            "the specific college/employer before applying."
        )



# ------------------------- Free Career Chat Assistant -------------------------
st.divider()
st.header("🤖 Jarvis Career Assistant")
st.markdown(
    '<p class="subtitle">Ask about careers already covered on this website. '
    'Works without an API key or paid subscription.</p>',
    unsafe_allow_html=True
)

def _jarvis_guide_text(career_name, guide):
    parts = [career_name, guide.get("intro", "")]
    for key, value in guide.items():
        if isinstance(value, list):
            parts.extend(str(item) for item in value)
        else:
            parts.append(str(value))
    return " ".join(parts).lower()

def _jarvis_find_careers(question):
    """Find the most relevant career guides using the website's own data."""
    query = question.lower()
    stop_words = {
        "what", "which", "where", "when", "how", "can", "could", "should",
        "tell", "about", "explain", "guide", "career", "careers", "job",
        "jobs", "the", "for", "and", "with", "from", "after", "best",
        "mujhe", "batao", "btao", "kya", "kaise", "hai", "hain", "ke",
        "ki", "ka", "me", "mein", "aur", "koi", "options", "guide"
    }
        if len(token) > 1 and token not in stop_words

    scores = []
    for category, careers in CAREERS.items():
        for career in careers:
            guide = GUIDES.get(career)
            if not guide:
                continue
            haystack = _jarvis_guide_text(career, guide)
            score = 0
            name_tokens = set(re.findall(r"[a-zA-Z0-9+#.]+", career.lower()))
            score += 5 * len(tokens & name_tokens)
            score += sum(1 for token in tokens if token in haystack)
            if career.lower() in query:
                score += 20
            if category.lower() in query:
                score += 4
            if score:
                scores.append((score, category, career, guide))

    scores.sort(key=lambda item: item[0], reverse=True)
    return scores

def _jarvis_answer(question):
    q = question.lower().strip()

    if any(word in q for word in ["hello", "hi", "hey", "namaste", "नमस्ते"]):
        return (
            "Namaste! Main Jarvis Career Assistant hoon. 😊\n\n"
            "Main is website ke career guides se eligibility, exams, skills, "
            "preparation aur resources dhoondh sakta hoon. Kisi career ka naam "
            "likhkar poochho, jaise **BCA**, **UPSC**, **MBBS** ya **Cricketer**."
        ), []

    if any(word in q for word in ["category", "categories", "career options", "all careers", "sabhi career"]):
        category_lines = []
        for category, careers in CAREERS.items():
            category_lines.append(
                f"**{category}:** " + ", ".join(careers)
            )
        return "Website par ye career categories available hain:\n\n" + "\n\n".join(category_lines), []

    results = _jarvis_find_careers(q)
    if not results:
        return (
            "Is sawaal ka jawab abhi meri built-in career library mein nahi mila. "
            "Kisi listed career ka naam likho, jaise **B.Tech Computer Science**, "
            "**NDA**, **CA**, **Graphic Designing** ya **YouTuber**.\n\n"
            "Note: Main abhi live internet search ya general-purpose AI model use nahi karta."
        ), []

    top_results = results[:2]
    answer_parts = []
    sources = []
    for score, category, career, guide in top_results:
        answer_parts.append(f"## {career}\n*Category: {category}*")
        answer_parts.append(guide.get("intro", ""))

        # Return the most useful sections based on what the user asked.
        requested_sections = []
        if any(word in q for word in ["eligib", "qualification", "12th", "12th ke baad", "subject", "marks"]):
            requested_sections += ["qualification", "age", "admission"]
        if any(word in q for word in ["exam", "entrance", "test", "syllabus", "paper"]):
            requested_sections += ["exam", "syllabus"]
        if any(word in q for word in ["resource", "website", "link", "study", "prepare", "preparation"]):
            requested_sections += ["resources", "strategy"]
        if any(word in q for word in ["salary", "income", "earning", "package", "paisa"]):
            requested_sections += ["salary", "opportunities"]
        if any(word in q for word in ["skill", "skills", "ability"]):
            requested_sections += ["skills"]
        if not requested_sections:
            requested_sections = [
                "qualification", "admission", "exam", "skills",
                "opportunities", "resources"
            ]

        labels = {
            "qualification": "Eligibility",
            "age": "Age criteria",
            "admission": "Admission process",
            "exam": "Entrance / selection",
            "syllabus": "Syllabus",
            "resources": "Learning resources",
            "strategy": "Preparation strategy",
            "salary": "Salary",
            "opportunities": "Career opportunities",
            "skills": "Important skills",
        }

        seen = set()
        for key in requested_sections:
            if key in seen or key not in guide:
                continue
            seen.add(key)
            value = guide[key]
            if isinstance(value, list):
                formatted = "\n".join(f"- {item}" for item in value)
                answer_parts.append(f"**{labels[key]}**\n{formatted}")
                if key == "resources":
                    for item in value:
                        match = re.search(r"https?://\S+", str(item))
                        if match:
                            url = match.group(0).rstrip(".,)")
                            sources.append((career + " resource", url))
            else:
                answer_parts.append(f"**{labels[key]}:** {value}")

        for item in guide.get("official", []):
            if isinstance(item, str) and item.startswith("http"):
                sources.append((career + " official source", item))

    unique_sources = []
    seen_urls = set()
    for title, url in sources:
        if url not in seen_urls:
            seen_urls.add(url)
            unique_sources.append((title, url))

    answer_parts.append(
        "\n**Important:** Eligibility, age limits, exam dates, fees and salaries "
        "can change. Latest details ke liye official authority ki notification check karein."
    )
    return "\n\n".join(answer_parts), unique_sources

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

with st.container(border=True):
    left_col, right_col = st.columns([3, 1])
    with left_col:
        st.caption("🟢 Free mode • No API key • No usage charges")
    with right_col:
        if st.button("🗑️ Clear chat", use_container_width=True, key="clear_jarvis_chat"):
            st.session_state.chat_messages = []
            st.rerun()

    st.info(
        "Main tumhari website ke 49 career guides mein se information nikaal sakta hoon. "
        "Yeh built-in assistant hai—live web search aur open-ended AI chat abhi available nahi hain."
    )

    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message.get("sources"):
                with st.expander("🔗 Official links and resources"):
                    for title, url in message["sources"]:
                        st.markdown(f"- [{title}]({url})")

    user_prompt = st.chat_input(
        "Career, eligibility, exam ya skills ke baare mein poochho...",
        key="jarvis_chat_input"
    )

    if user_prompt:
        st.session_state.chat_messages.append({
            "role": "user",
            "content": user_prompt
        })
        with st.chat_message("user"):
            st.markdown(user_prompt)

        with st.chat_message("assistant"):
            with st.spinner("Jarvis tumhari career library check kar raha hai..."):
                answer, sources = _jarvis_answer(user_prompt)
                st.markdown(answer)
                if sources:
                    with st.expander("🔗 Official links and resources"):
                        for title, url in sources:
                            st.markdown(f"- [{title}]({url})")

        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": answer,
            "sources": sources
        })
        # Keep the session history compact.
        st.session_state.chat_messages = st.session_state.chat_messages[-20:]


# ----------------------------- Footer -----------------------------
st.divider()
st.markdown("""
<div class="footer">
    🧠 Jarvis by Anmol<br>
    Learn • Grow • Achieve<br><br>
    Made with ❤️ by Anmol Verma
</div>
""", unsafe_allow_html=True)
