# import re
# from huggingface_api import get_resume_score

# # A more reliable way to find sections using keywords
# def find_sections(resume_text: str) -> set:
#     """
#     Finds common resume sections using a flexible regex search.
#     This is more reliable than NER for finding section headers.
#     """
#     found_sections = set()
    
#     # This dictionary holds the section name and the regex pattern to find it.
#     # We look for optional spaces at the start, various keywords, and optional punctuation.
#     section_patterns = {
#         "Skills": r"^\s*(skills|technical skills|proficiencies)",
#         "Experience": r"^\s*(experience|work experience|professional experience|employment history)",
#         "Education": r"^\s*(education|academic qualifications)",
#         "Certifications": r"^\s*(certifications|licenses|professional development)",
#         "Projects": r"^\s*(projects|personal projects|portfolio)"
#     }

#     for section, pattern in section_patterns.items():
#         # re.IGNORECASE: Matches "Skills", "skills", "SKILLS", etc.
#         # re.MULTILINE: Allows '^' to match the start of each new line.
#         if re.search(pattern, resume_text, re.IGNORECASE | re.MULTILINE):
#             found_sections.add(section)
            
#     return found_sections

# # The rest of your score_resume function remains the same.
# def score_resume(resume_text: str):
#     score = get_resume_score(resume_text)
    
#     EXPECTED_SECTIONS = {"Skills", "Experience", "Education", "Certifications", "Projects"}
#     present_sections = find_sections(resume_text)
    
#     suggestions = []
#     strengths = []
    
#     for section in EXPECTED_SECTIONS:
#         if section in present_sections:
#             strengths.append(f"Includes a clear <b>{section}</b> section.")
#         else:
#             suggestions.append(f"Consider adding a dedicated <b>{section}</b> section.")

#     improvements = []
#     if "Skills" not in present_sections:
#         improvements.append("No 'Skills' section was clearly identified.")

#     return {
#         "score": score,
#         "suggestions": suggestions,
#         "strengths": strengths,
#         "improvements": improvements
#     }

#Other
# import re
# import spacy
# from collections import Counter
# import textstat

# # Load the spaCy model
# try:
#     nlp = spacy.load("en_core_web_sm")
# except OSError:
#     print("Downloading 'en_core_web_sm' model. Please wait...")
#     from spacy.cli import download
#     download("en_core_web_sm")
#     nlp = spacy.load("en_core_web_sm")

# # --- Lists for Analysis ---
# ACTION_VERBS = ['achieved', 'administered', 'advised', 'analyzed', 'authored', 'automated', 'built', 'centralized', 'chaired', 'collaborated', 'conceived', 'conducted', 'created', 'customized', 'designed', 'developed', 'directed', 'documented', 'drove', 'engineered', 'enhanced', 'established', 'executed', 'expanded', 'facilitated', 'founded', 'generated', 'guided', 'identified', 'implemented', 'improved', 'increased', 'initiated', 'innovated', 'instituted', 'integrated', 'launched', 'led', 'leveraged', 'managed', 'mentored', 'negotiated', 'orchestrated', 'organized', 'oversaw', 'pioneered', 'planned', 'produced', 'proposed', 'ran', 'recommended', 'redesigned', 'reduced', 're-engineered', 'researched', 'resolved', 'revamped', 'saved', 'scaled', 'secured', 'solved', 'spearheaded', 'standardized', 'streamlined', 'strengthened', 'supervised', 'systematized', 'tested', 'trained', 'transformed', 'upgraded', 'validated']
# CLICHE_LIST = ['team player', 'hard worker', 'results-oriented', 'self-motivated', 'go-getter', 'synergy', 'proactive', 'dynamic', 'detail-oriented', 'think outside the box', 'problem solver', 'highly motivated']

# # ▼▼▼ NEW KEYWORD LISTS FOR PERFECTED SCORING ▼▼▼
# HARD_SKILLS = ['python', 'java', 'c++', 'javascript', 'sql', 'mysql', 'postgresql', 'mongodb', 'react', 'angular', 'vue', 'node.js', 'django', 'flask', 'html', 'css', 'aws', 'azure', 'google cloud', 'docker', 'kubernetes', 'git', 'jenkins', 'excel', 'tableau', 'power bi', 'tensorflow', 'pytorch', 'scikit-learn', 'numpy', 'pandas', 'matplotlib', 'autocad', 'solidworks', 'matlab', 'photoshop', 'illustrator', 'figma', 'jira']
# SOFT_SKILLS = ['leadership', 'communication', 'teamwork', 'collaboration', 'problem solving', 'critical thinking', 'creativity', 'adaptability', 'time management', 'work ethic', 'interpersonal skills', 'conflict resolution', 'negotiation', 'mentorship']


# # --- Analysis Functions ---

# def analyze_contact_info(text):
#     # This function remains the same
#     results = {'found': [], 'missing': []}
#     if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text): results['found'].append('Email')
#     else: results['missing'].append('Email')
#     if re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text): results['found'].append('Phone Number')
#     else: results['missing'].append('Phone Number')
#     if re.search(r'(https?:\/\/)?(www\.)?linkedin\.com\/in\/[a-zA-Z0-9\-\_]+', text, re.I): results['found'].append('LinkedIn Profile')
#     else: results['missing'].append('LinkedIn Profile')
#     return results

# def analyze_sections(text):
#     # This function remains the same
#     section_patterns = {"Summary": r"^\s*(summary|objective|profile)", "Experience": r"^\s*(experience|work experience|professional experience|employment history|internship|internships)", "Education": r"^\s*(education|academic qualifications)", "Skills": r"^\s*(skills|technical skills|proficiencies)", "Projects": r"^\s*(projects|personal projects|portfolio)"}
#     present = {section for section, pattern in section_patterns.items() if re.search(pattern, text, re.I | re.M)}
#     missing = set(section_patterns.keys()) - present
#     return {'present': list(present), 'missing': list(missing)}

# def analyze_action_verbs(text):
#     # This function remains the same
#     experience_pattern = r"(experience|work experience|professional experience|employment history|internship|internships)(.*)"
#     experience_text_match = re.search(experience_pattern, text, re.I | re.DOTALL)
#     if not experience_text_match: return {'score': 0, 'feedback': "Could not find an 'Experience' or 'Internships' section to analyze verb usage."}
#     experience_text = experience_text_match.group(2)
#     bullet_points = re.findall(r"^\s*[\*•-]\s+(.*)", experience_text, re.M)
#     if not bullet_points: return {'score': 0, 'feedback': 'No bullet points found in the Experience/Internships section to analyze.'}
#     action_verb_count = sum(1 for point in bullet_points if point.split(' ')[0].lower().strip() in ACTION_VERBS)
#     score = int((action_verb_count / len(bullet_points)) * 100) if bullet_points else 0
#     return {'score': score, 'feedback': f"Used strong action verbs in {action_verb_count} out of {len(bullet_points)} bullet points ({score}%)."}

# def analyze_quantification(text):
#     # This function remains the same
#     experience_pattern = r"(experience|work experience|professional experience|employment history|internship|internships)(.*)"
#     experience_text_match = re.search(experience_pattern, text, re.I | re.DOTALL)
#     if not experience_text_match: return {'count': 0, 'feedback': "Could not find an 'Experience' or 'Internships' section to analyze quantification."}
#     experience_text = experience_text_match.group(2)
#     numbers = re.findall(r'(\d{1,3}(,\d{3})*(\.\d+)?|\d+)', experience_text)
#     percentages = re.findall(r'\d+%', experience_text)
#     dollars = re.findall(r'\$\d+', experience_text)
#     count = len(numbers) + len(percentages) + len(dollars)
#     return {'count': count, 'feedback': f"Found {count} instances of quantifiable data."}

# def analyze_cliches(text):
#     # This function remains the same
#     found_cliches = [cliche for cliche in CLICHE_LIST if re.search(r'\b' + re.escape(cliche) + r'\b', text, re.I)]
#     return {'count': len(found_cliches), 'found': list(set(found_cliches))}

# def analyze_tense_consistency(text):
#     # This function remains the same
#     experience_pattern = r"(experience|work experience|professional experience|employment history|internship|internships)(.*)"
#     experience_text_match = re.search(experience_pattern, text, re.I | re.DOTALL)
#     if not experience_text_match: return {'consistent': True, 'feedback': "Could not find an Experience/Internships section to analyze tense."}
#     experience_text = experience_text_match.group(2)
#     bullet_points = re.findall(r"^\s*[\*•-]\s+(.*)", experience_text, re.M)
#     past_tense_verbs = 0
#     present_tense_verbs = 0
#     for point in bullet_points:
#         first_token = nlp(point)[0]
#         if first_token.pos_ == 'VERB':
#             if first_token.tag_ == 'VBD': past_tense_verbs += 1
#             elif first_token.tag_ in ['VBP', 'VBZ']: present_tense_verbs += 1
#     if past_tense_verbs > 0 and present_tense_verbs > 0: return {'consistent': False, 'feedback': "Found a mix of past and present tense verbs in bullet points. Use past tense for past roles and present tense for current roles."}
#     return {'consistent': True, 'feedback': "Verb tenses in bullet points appear consistent."}

# # --- NEW AND UPDATED ANALYSIS FUNCTIONS ---

# def analyze_clarity(text):
#     """Calculates a transformed, positive readability score (out of 10)."""
#     flesch_score = textstat.flesch_reading_ease(text)
#     clarity_score = 0
#     if flesch_score >= 70: clarity_score = 10
#     elif flesch_score >= 60: clarity_score = 9
#     elif flesch_score >= 50: clarity_score = 7
#     elif flesch_score >= 30: clarity_score = 5
#     else: clarity_score = 3
#     return {'score': clarity_score, 'feedback': f"Your resume's clarity score is {clarity_score}/10."}

# def analyze_skill_keywords(text):
#     """Finds and categorizes hard and soft skills."""
#     text_lower = text.lower()
#     found_hard_skills = {skill for skill in HARD_SKILLS if re.search(r'\b' + re.escape(skill) + r'\b', text_lower)}
#     found_soft_skills = {skill for skill in SOFT_SKILLS if re.search(r'\b' + re.escape(skill) + r'\b', text_lower)}
#     return {
#         'hard_skills': list(found_hard_skills),
#         'soft_skills': list(found_soft_skills)
#     }

# # --- NEW "PERFECTED" SCORING LOGIC ---

# def calculate_professional_score(analysis_data):
#     """Calculates a detailed, rubric-based score out of 100."""
#     scores = {}

#     # 1. Core Components Score (Max 30 points)
#     core_score = 0
#     # Contact Info (5 pts)
#     if 'Email' in analysis_data['contact_info']['found']: core_score += 2
#     if 'Phone Number' in analysis_data['contact_info']['found']: core_score += 2
#     if 'LinkedIn Profile' in analysis_data['contact_info']['found']: core_score += 1
#     # Sections (10 pts) - weighted for students
#     section_points = {'Education': 3, 'Experience': 3, 'Skills': 2, 'Projects': 2}
#     for section in analysis_data['sections']['present']:
#         if section in section_points:
#             core_score += section_points[section]
#     # Clarity & Conciseness (15 pts)
#     core_score += analysis_data['clarity']['score'] # Readability (10 pts)
#     core_score += max(5 - analysis_data['cliches']['count'], 0) # Cliché penalty (5 pts)
#     scores['core_score'] = int(core_score)

#     # 2. Experience & Impact Score (Max 45 points)
#     impact_score = 0
#     # Action verbs score (20 pts)
#     impact_score += (analysis_data['action_verbs']['score'] / 100.0) * 20
#     # Quantification score (15 pts) - capped at 5 metrics
#     impact_score += min((analysis_data['quantification']['count'] / 5.0) * 15, 15)
#     # Tense consistency (10 pts)
#     if analysis_data['tenses']['consistent']:
#         impact_score += 10
#     scores['impact_score'] = int(impact_score)

#     # 3. Skills & Keywords Score (Max 25 points)
#     skills_score = 0
#     # Dedicated skills section (5 pts)
#     if 'Skills' in analysis_data['sections']['present']:
#         skills_score += 5
#     # Keyword mix (20 pts)
#     hard_skill_score = min((len(analysis_data['skill_keywords']['hard_skills']) / 10.0) * 15, 15)
#     soft_skill_score = min((len(analysis_data['skill_keywords']['soft_skills']) / 5.0) * 5, 5)
#     skills_score += hard_skill_score + soft_skill_score
#     scores['skills_score'] = int(skills_score)
    
#     # Calculate Total Score
#     total_score = int(scores['core_score'] + scores['impact_score'] + scores['skills_score'])
#     scores['total_score'] = total_score
    
#     return scores

# def professional_analysis(resume_text):
#     """Runs all analysis modules and compiles the final, perfected results."""
#     analysis_results = {
#         "contact_info": analyze_contact_info(resume_text),
#         "sections": analyze_sections(resume_text),
#         "action_verbs": analyze_action_verbs(resume_text),
#         "quantification": analyze_quantification(resume_text),
#         "cliches": analyze_cliches(resume_text),
#         "tenses": analyze_tense_consistency(resume_text),
#         "clarity": analyze_clarity(resume_text),
#         "skill_keywords": analyze_skill_keywords(resume_text),
#     }

#     # Calculate the detailed score using the new rubric
#     score_breakdown = calculate_professional_score(analysis_results)
#     analysis_results["score_breakdown"] = score_breakdown
    
#     return analysis_results


# import re
# import spacy
# from collections import Counter
# import textstat

# # Load the spaCy model
# try:
#     nlp = spacy.load("en_core_web_sm")
# except OSError:
#     print("Downloading 'en_core_web_sm' model. Please wait...")
#     from spacy.cli import download
#     download("en_core_web_sm")
#     nlp = spacy.load("en_core_web_sm")

# # --- Lists & Dictionaries for Elite Analysis ---
# ACTION_VERBS = ['achieved', 'administered', 'advised', 'analyzed', 'authored', 'automated', 'built', 'centralized', 'chaired', 'collaborated', 'conceived', 'conducted', 'created', 'customized', 'designed', 'developed', 'directed', 'documented', 'drove', 'engineered', 'enhanced', 'established', 'executed', 'expanded', 'facilitated', 'founded', 'generated', 'guided', 'identified', 'implemented', 'improved', 'increased', 'initiated', 'innovated', 'instituted', 'integrated', 'launched', 'led', 'leveraged', 'managed', 'mentored', 'negotiated', 'orchestrated', 'organized', 'oversaw', 'pioneered', 'planned', 'produced', 'proposed', 'ran', 'recommended', 'redesigned', 'reduced', 're-engineered', 'researched', 'resolved', 'revamped', 'saved', 'scaled', 'secured', 'solved', 'spearheaded', 'standardized', 'streamlined', 'strengthened', 'supervised', 'systematized', 'tested', 'trained', 'transformed', 'upgraded', 'validated']
# CLICHE_LIST = ['team player', 'hard worker', 'results-oriented', 'self-motivated', 'go-getter', 'synergy', 'proactive', 'dynamic', 'detail-oriented', 'think outside the box', 'problem solver', 'highly motivated']

# # ▼▼▼ NEW: TIERED SKILL SYSTEM FOR MORE GRANULAR SCORING ▼▼▼
# SKILL_TIERS = {
#     "Tier 1 (Advanced/High-Impact)": ['tensorflow', 'pytorch', 'kubernetes', 'aws', 'azure', 'gcp', 'docker', 'scikit-learn', 'go', 'rust', 'scala'],
#     "Tier 2 (Core/Intermediate)": ['python', 'java', 'c++', 'c#', 'sql', 'mysql', 'postgresql', 'mongodb', 'react', 'angular', 'vue', 'node.js', 'django', 'flask', 'git', 'jenkins', 'tableau', 'power bi', 'matlab', 'swift', 'kotlin'],
#     "Tier 3 (Foundational)": ['html', 'css', 'javascript', 'excel', 'photoshop', 'illustrator', 'figma', 'jira', 'trello', 'canva']
# }

# # --- Analysis Functions (Some are new or heavily modified) ---

# def analyze_contact_info(text):
#     results = {'found': [], 'missing': []}
#     if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text): results['found'].append('Email')
#     else: results['missing'].append('Email')
#     if re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text): results['found'].append('Phone Number')
#     else: results['missing'].append('Phone Number')
#     if re.search(r'(https?:\/\/)?(www\.)?linkedin\.com\/in\/[a-zA-Z0-9\-\_]+', text, re.I): results['found'].append('LinkedIn Profile')
#     else: results['missing'].append('LinkedIn Profile')
#     return results

# def analyze_sections(text):
#     section_patterns = {"Summary": r"^\s*(summary|profile)", "Experience": r"^\s*(experience|work experience|professional experience|employment history|internship|internships)", "Education": r"^\s*(education|academic qualifications)", "Skills": r"^\s*(skills|technical skills|proficiencies)", "Projects": r"^\s*(projects|personal projects|portfolio)", "Objective": r"^\s*(objective)"}
#     present = {section for section, pattern in section_patterns.items() if re.search(pattern, text, re.I | re.M)}
#     return {'present': list(present)}

# # ▼▼▼ NEW: PER-BULLET-POINT IMPACT ANALYSIS ▼▼▼
# def analyze_experience_impact(text):
#     experience_pattern = r"(experience|work experience|professional experience|employment history|internship|internships)(.*)"
#     experience_text_match = re.search(experience_pattern, text, re.I | re.DOTALL)
#     if not experience_text_match: return {'bullet_count': 0, 'impact_score': 0, 'feedback': "No 'Experience' section found."}
    
#     experience_text = experience_text_match.group(2)
#     bullet_points = re.findall(r"^\s*[\*•-]\s+(.*)", experience_text, re.M)
#     if not bullet_points: return {'bullet_count': 0, 'impact_score': 0, 'feedback': 'No bullet points found in Experience section.'}

#     total_score = 0
#     max_score_per_bullet = 5 # Verb(1) + Metric(2) + Length(1) + Synergy Bonus(1) = 5
    
#     for point in bullet_points:
#         bullet_score = 0
#         # 1. Action Verb Check (+1 pt)
#         if point.split(' ')[0].lower().strip() in ACTION_VERBS:
#             bullet_score += 1
#         # 2. Quantification Check (+2 pts)
#         if re.search(r'\d', point):
#             bullet_score += 2
#         # 3. Optimal Length Check (+1 pt)
#         if 10 <= len(point.split()) <= 25:
#             bullet_score += 1
#         # 4. Synergy Bonus (+1 pt) - The "perfect" bullet
#         if (point.split(' ')[0].lower().strip() in ACTION_VERBS) and (re.search(r'\d', point)):
#              bullet_score += 1
        
#         total_score += bullet_score
        
#     avg_bullet_score = total_score / len(bullet_points)
#     impact_score_scaled = (avg_bullet_score / max_score_per_bullet) * 100
    
#     return {'bullet_count': len(bullet_points), 'impact_score': int(impact_score_scaled), 'feedback': f"Your {len(bullet_points)} bullet points have an average impact score of {int(impact_score_scaled)}/100."}

# # ▼▼▼ NEW: TIERED SKILL ANALYSIS ▼▼▼
# def analyze_skill_tiers(text):
#     text_lower = text.lower()
#     found_skills = {}
#     for tier, skills in SKILL_TIERS.items():
#         found = {skill for skill in skills if re.search(r'\b' + re.escape(skill) + r'\b', text_lower)}
#         if found:
#             found_skills[tier] = list(found)
#     return found_skills

# # --- Penalty and Final Score Calculation ---

# def calculate_penalties(text, analysis_data):
#     penalties = []
#     # Length Penalty (approximated by character count for a 1-page resume)
#     if len(text) > 4000:
#         penalties.append({'reason': "Resume exceeds recommended 1-page length for students.", 'points': -5})
#     # Cliché Penalty
#     found_cliches = [cliche for cliche in CLICHE_LIST if re.search(r'\b' + re.escape(cliche) + r'\b', text, re.I)]
#     if found_cliches:
#         penalties.append({'reason': f"Use of clichés ({', '.join(found_cliches)}) weakens professional tone.", 'points': -2 * len(found_cliches)})
#     # Outdated "Objective" Section Penalty
#     if "Objective" in analysis_data['sections']['present']:
#         penalties.append({'reason': "Contains an outdated 'Objective' section. A 'Summary' is preferred.", 'points': -3})
    
#     return penalties

# # ▼▼▼ NEW "ELITE" SCORING RUBRIC ▼▼▼
# def elite_score_calculation(analysis_data, penalties):
#     scores = {}
    
#     # I. Structure & Clarity (20 points)
#     structure_score = 0
#     if 'Email' in analysis_data['contact_info']['found']: structure_score += 2
#     if 'Phone Number' in analysis_data['contact_info']['found']: structure_score += 2
#     if 'LinkedIn Profile' in analysis_data['contact_info']['found']: structure_score += 1
#     clarity_score = textstat.flesch_reading_ease(analysis_data['raw_text'])
#     if clarity_score > 60: structure_score += 10
#     elif clarity_score > 40: structure_score += 7
#     elif clarity_score > 20: structure_score += 4
#     section_points = {'Experience': 2, 'Skills': 2, 'Education': 1, 'Projects': 1}
#     for section in analysis_data['sections']['present']:
#         if section in section_points: structure_score += section_points.get(section, 0)
#     scores['structure_score'] = int(min(structure_score, 20)) # Cap at 20

#     # II. Experience & Impact (50 points)
#     impact_score = (analysis_data['experience_impact']['impact_score'] / 100.0) * 50
#     scores['impact_score'] = int(impact_score)

#     # III. Skills & Competencies (30 points)
#     skills_score = 0
#     skill_tiers = analysis_data['skill_tiers']
#     if 'Tier 1 (Advanced/High-Impact)' in skill_tiers:
#         skills_score += min(len(skill_tiers['Tier 1 (Advanced/High-Impact)']) * 5, 15)
#     if 'Tier 2 (Core/Intermediate)' in skill_tiers:
#         skills_score += min(len(skill_tiers['Tier 2 (Core/Intermediate)']) * 2, 10)
#     if 'Tier 3 (Foundational)' in skill_tiers:
#         skills_score += min(len(skill_tiers['Tier 3 (Foundational)']) * 1, 5)
#     scores['skills_score'] = int(skills_score)
    
#     # Calculate Final Score
#     base_score = scores['structure_score'] + scores['impact_score'] + scores['skills_score']
#     total_penalty = sum(p['points'] for p in penalties)
#     final_score = max(0, base_score + total_penalty) # Ensure score doesn't go below 0
#     scores['total_score'] = final_score
    
#     return scores

# def elite_analysis(resume_text):
#     """The main function to run all elite analysis modules."""
#     analysis_results = {
#         "raw_text": resume_text, # Store raw text for multiple uses
#         "contact_info": analyze_contact_info(resume_text),
#         "sections": analyze_sections(resume_text),
#         "experience_impact": analyze_experience_impact(resume_text),
#         "skill_tiers": analyze_skill_tiers(resume_text)
#     }
    
#     penalties = calculate_penalties(resume_text, analysis_results)
#     analysis_results["penalties"] = penalties
    
#     score_breakdown = elite_score_calculation(analysis_results, penalties)
#     analysis_results["score_breakdown"] = score_breakdown
    
#     return analysis_results

# # Renamed professional_analysis to elite_analysis to reflect the change
# professional_analysis = elite_analysis
import re
import spacy
from collections import Counter
import textstat

# Load the spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading 'en_core_web_sm' model. Please wait...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# --- Lists & Dictionaries for Elite Analysis ---
ACTION_VERBS = ['achieved', 'administered', 'advised', 'analyzed', 'authored', 'automated', 'built', 'centralized', 'chaired', 'collaborated', 'conceived', 'conducted', 'created', 'customized', 'designed', 'developed', 'directed', 'documented', 'drove', 'engineered', 'enhanced', 'established', 'executed', 'expanded', 'facilitated', 'founded', 'generated', 'guided', 'identified', 'implemented', 'improved', 'increased', 'initiated', 'innovated', 'instituted', 'integrated', 'launched', 'led', 'leveraged', 'managed', 'mentored', 'negotiated', 'orchestrated', 'organized', 'oversaw', 'pioneered', 'planned', 'produced', 'proposed', 'ran', 'recommended', 'redesigned', 'reduced', 're-engineered', 'researched', 'resolved', 'revamped', 'saved', 'scaled', 'secured', 'solved', 'spearheaded', 'standardized', 'streamlined', 'strengthened', 'supervised', 'systematized', 'tested', 'trained', 'transformed', 'upgraded', 'validated']
CLICHE_LIST = ['team player', 'hard worker', 'results-oriented', 'self-motivated', 'go-getter', 'synergy', 'proactive', 'dynamic', 'detail-oriented', 'think outside the box', 'problem solver', 'highly motivated']

SKILL_TIERS = {
    "Tier 1 (Advanced/High-Impact)": ['tensorflow', 'pytorch', 'kubernetes', 'aws', 'azure', 'gcp', 'docker', 'scikit-learn', 'go', 'rust', 'scala'],
    "Tier 2 (Core/Intermediate)": ['python', 'java', 'c++', 'c#', 'sql', 'mysql', 'postgresql', 'mongodb', 'react', 'angular', 'vue', 'node.js', 'django', 'flask', 'git', 'jenkins', 'tableau', 'power bi', 'matlab', 'swift', 'kotlin'],
    "Tier 3 (Foundational)": ['html', 'css', 'javascript', 'excel', 'photoshop', 'illustrator', 'figma', 'jira', 'trello', 'canva']
}

# --- Analysis Functions ---

def analyze_contact_info(text):
    results = {'found': [], 'missing': []}
    if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text): results['found'].append('Email')
    else: results['missing'].append('Email')
    if re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text): results['found'].append('Phone Number')
    else: results['missing'].append('Phone Number')
    if re.search(r'(https?:\/\/)?(www\.)?linkedin\.com\/in\/[a-zA-Z0-9\-\_]+', text, re.I): results['found'].append('LinkedIn Profile')
    else: results['missing'].append('LinkedIn Profile')
    return results

def analyze_sections(text):
    section_patterns = {"Summary": r"^\s*(summary|profile)", "Experience": r"^\s*(experience|work experience|professional experience|employment history|internship|internships)", "Education": r"^\s*(education|academic qualifications)", "Skills": r"^\s*(skills|technical skills|proficiencies)", "Projects": r"^\s*(projects|personal projects|portfolio)", "Objective": r"^\s*(objective)"}
    present = {section for section, pattern in section_patterns.items() if re.search(pattern, text, re.I | re.M)}
    return {'present': list(present)}

def analyze_experience_impact(text):
    experience_pattern = r"(experience|work experience|professional experience|employment history|internship|internships)(.*)"
    experience_text_match = re.search(experience_pattern, text, re.I | re.DOTALL)
    if not experience_text_match: return {'bullet_count': 0, 'impact_score': 0, 'feedback': "No 'Experience' section found."}
    
    experience_text = experience_text_match.group(2)
    bullet_points = re.findall(r"^\s*[\*•-]\s+(.*)", experience_text, re.M)
    if not bullet_points: return {'bullet_count': 0, 'impact_score': 0, 'feedback': 'No bullet points found in Experience section.'}

    total_score = 0
    max_score_per_bullet = 5 # Verb(1) + Metric(2) + Length(1) + Synergy Bonus(1) = 5
    
    for point in bullet_points:
        bullet_score = 0
        if point.split(' ')[0].lower().strip() in ACTION_VERBS: bullet_score += 1
        if re.search(r'\d', point): bullet_score += 2
        if 10 <= len(point.split()) <= 25: bullet_score += 1
        if (point.split(' ')[0].lower().strip() in ACTION_VERBS) and (re.search(r'\d', point)): bullet_score += 1
        total_score += bullet_score
        
    avg_bullet_score = total_score / len(bullet_points)
    impact_score_scaled = (avg_bullet_score / max_score_per_bullet) * 100
    
    return {'bullet_count': len(bullet_points), 'impact_score': int(impact_score_scaled), 'feedback': f"Your {len(bullet_points)} bullet points have an average impact score of {int(impact_score_scaled)}/100."}

def analyze_skill_tiers(text):
    text_lower = text.lower()
    found_skills = {}
    for tier, skills in SKILL_TIERS.items():
        found = {skill for skill in skills if re.search(r'\b' + re.escape(skill) + r'\b', text_lower)}
        if found:
            found_skills[tier] = list(found)
    return found_skills

def calculate_penalties(text, analysis_data):
    penalties = []
    if len(text) > 4000:
        penalties.append({'reason': "Resume exceeds recommended 1-page length for students.", 'points': -5})
    found_cliches = [cliche for cliche in CLICHE_LIST if re.search(r'\b' + re.escape(cliche) + r'\b', text, re.I)]
    if found_cliches:
        penalties.append({'reason': f"Use of clichés ({', '.join(found_cliches)}) weakens professional tone.", 'points': -2 * len(found_cliches)})
    if "Objective" in analysis_data['sections']['present']:
        penalties.append({'reason': "Contains an outdated 'Objective' section. A 'Summary' is preferred.", 'points': -3})
    return penalties

def elite_score_calculation(analysis_data):
    scores = {}
    
    # I. Structure & Clarity (20 points)
    structure_score = 0
    if 'Email' in analysis_data['contact_info']['found']: structure_score += 2
    if 'Phone Number' in analysis_data['contact_info']['found']: structure_score += 2
    if 'LinkedIn Profile' in analysis_data['contact_info']['found']: structure_score += 1
    clarity_score = textstat.flesch_reading_ease(analysis_data['raw_text'])
    if clarity_score > 60: structure_score += 10
    elif clarity_score > 40: structure_score += 7
    elif clarity_score > 20: structure_score += 4
    section_points = {'Experience': 2, 'Skills': 2, 'Education': 1, 'Projects': 1}
    for section in analysis_data['sections']['present']:
        structure_score += section_points.get(section, 0)
    scores['structure_score'] = int(min(structure_score, 20))

    # II. Experience & Impact (50 points)
    impact_score = (analysis_data['experience_impact']['impact_score'] / 100.0) * 50
    scores['impact_score'] = int(impact_score)

    # III. Skills & Competencies (30 points)
    skills_score = 0
    skill_tiers = analysis_data['skill_tiers']
    if 'Tier 1 (Advanced/High-Impact)' in skill_tiers:
        skills_score += min(len(skill_tiers['Tier 1 (Advanced/High-Impact)']) * 5, 15)
    if 'Tier 2 (Core/Intermediate)' in skill_tiers:
        skills_score += min(len(skill_tiers['Tier 2 (Core/Intermediate)']) * 2, 10)
    if 'Tier 3 (Foundational)' in skill_tiers:
        skills_score += min(len(skill_tiers['Tier 3 (Foundational)']) * 1, 5)
    scores['skills_score'] = int(skills_score)
    
    # Calculate Final Score
    base_score = scores['structure_score'] + scores['impact_score'] + scores['skills_score']
    total_penalty = sum(p['points'] for p in analysis_data['penalties'])
    final_score = max(0, base_score + total_penalty)
    scores['total_score'] = final_score
    
    return scores

def elite_analysis(resume_text):
    """The main function to run all elite analysis modules."""
    analysis_results = {
        "raw_text": resume_text,
        "contact_info": analyze_contact_info(resume_text),
        "sections": analyze_sections(resume_text),
        "experience_impact": analyze_experience_impact(resume_text),
        "skill_tiers": analyze_skill_tiers(resume_text)
    }
    
    penalties = calculate_penalties(resume_text, analysis_results)
    analysis_results["penalties"] = penalties
    
    # ▼▼▼ THE CHANGE IS HERE ▼▼▼
    # Calculate the score and merge the score dictionary into the main results
    score_breakdown = elite_score_calculation(analysis_results)
    analysis_results["score_breakdown"] = score_breakdown
    # ▲▲▲ END OF CHANGE ▲▲▲
    
    return analysis_results

# Maintain compatibility with the old function name for bot.py
professional_analysis = elite_analysis