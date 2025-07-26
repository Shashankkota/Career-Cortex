# def deduplicate(items: list[str]) -> list[str]:
#     """Removes duplicates from a list while preserving order."""
#     seen = set()
#     result = []
#     for item in items:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result

# def format_bullets(items: list[str]) -> str:
#     """Formats a list of items as bullet points for the message."""
#     if not items:
#         return ""
#     # Use HTML for better formatting in Telegram
#     return "\n" + "\n".join(f"  • {item.strip()}" for item in items if item)

# def build_output_message(score: int, suggestions: list, strengths: list, improvements: list) -> str:
#     """Builds the final formatted message to send to the user."""
    
#     # Determine emoji based on score
#     if score >= 85:
#         emoji = "🚀"
#     elif score >= 70:
#         emoji = "✅"
#     else:
#         emoji = "💡"

#     message = f"{emoji} <b>Your Resume Score: {score}/100</b>\n\n"

#     if strengths:
#         message += "<b>📈 Strengths:</b>"
#         message += format_bullets(strengths)
#         message += "\n\n"

#     if improvements:
#         message += "<b>⚠️ Areas for Improvement:</b>"
#         message += format_bullets(improvements)
#         message += "\n\n"
        
#     if suggestions:
#         message += "<b>💡 Suggestions:</b>"
#         message += format_bullets(suggestions)
#         message += "\n"

#     message += "\n<i>Disclaimer: This is an automated analysis.</i>"

#     return message.strip()
# def build_professional_output(data: dict) -> str:
#     """Builds a professional, good-looking, and detailed resume analysis report."""
    
#     score = data['overall_score']
    
#     # Determine emoji and summary based on score
#     if score >= 85:
#         summary_emoji = "🚀"
#         summary_text = "<b>Excellent!</b> Your resume is well-structured, impactful, and ready for applications."
#     elif score >= 70:
#         summary_emoji = "✅"
#         summary_text = "<b>Good foundation.</b> Your resume is solid, with a few key areas for improvement to maximize its impact."
#     else:
#         summary_emoji = "💡"
#         summary_text = "<b>Needs improvement.</b> Your resume has potential, but requires significant updates to be competitive."

#     # --- Start Building the Message ---
#     message = f"{summary_emoji} <b><u>Resume Analysis Complete</u></b> {summary_emoji}\n\n"
#     message += f"<b>Overall ATS Score: {score}/100</b>\n"
#     message += f"<i>{summary_text}</i>\n\n"
#     message += "---" * 8 + "\n\n"

#     # --- Section 1: ATS & Readability ---
#     message += "<b><u>1. ATS & Readability</u></b>\n"
#     message += "<i>How easily can a system parse your resume?</i>\n\n"
    
#     # Contact Info
#     contact = data['contact_info']
#     message += "<b>Contact Information:</b>\n"
#     if not contact['missing']:
#         message += "  ✅ All key contact details (Email, Phone, LinkedIn) were found.\n"
#     else:
#         for item in contact['missing']:
#             message += f"  ❌ <b>Missing:</b> A standard {item} could not be found.\n"
            
#     # Section Presence
#     sections = data['sections']
#     message += "\n<b>Standard Sections:</b>\n"
#     for section in sections['present']:
#         message += f"  ✅ Found: <b>{section}</b>\n"
#     for section in sections['missing']:
#         message += f"  ⚠️ Missing: Consider adding a dedicated <b>{section}</b> section.\n"
#     message += "\n"
#     message += "---" * 8 + "\n\n"

#     # --- Section 2: Core Keywords ---
#     keywords = data['keywords']['top_keywords']
#     message += "<b><u>2. Core Keywords & Competencies</u></b>\n"
#     message += "<i>These are the key terms that define your expertise, extracted from your resume.</i>\n\n"
#     if keywords:
#         keyword_str = ", ".join(f"<code>{kw}</code>" for kw in keywords)
#         message += f"<b>Identified Keywords:</b> {keyword_str}\n\n"
#         message += "<b>Recommendation:</b> Ensure these keywords are prominently featured and align with the roles you are targeting.\n"
#     else:
#         message += "Could not extract a significant number of keywords. Ensure your skills and technologies are clearly listed.\n"
#     message += "\n"
#     message += "---" * 8 + "\n\n"

#     # --- Section 3: Impact & Achievements ---
#     message += "<b><u>3. Impact & Achievements</u></b>\n"
#     message += "<i>This section analyzes how well you showcase your accomplishments.</i>\n\n"

#     # Action Verbs
#     verbs = data['action_verbs']
#     message += f"<b>Action Verbs Analysis:</b>\n  - {verbs['feedback']}\n"
#     if verbs['score'] < 80:
#         message += "  - <b>Tip:</b> Start every bullet point in your experience section with a strong action verb like 'Managed', 'Developed', or 'Achieved' to create a more dynamic tone.\n"
        
#     # Quantification
#     quant = data['quantification']
#     message += f"\n<b>Quantification Analysis:</b>\n  - {quant['feedback']}\n"
#     if quant['count'] < 3:
#         message += "  - <b>Tip:</b> Strengthen your resume by adding numbers to describe your accomplishments. For example, instead of 'Managed a team', try 'Managed a team of 5'. Use percentages (%), currency ($), and numbers to show scale and impact.\n"
#     message += "\n"
#     message += "---" * 8 + "\n\n"

#     # --- Section 4: Final Recommendations ---
#     message += "<b><u>4. Final Recommendations</u></b>\n"
#     message += "  • <b>Proofread Thoroughly:</b> Check for any spelling or grammar errors. A clean document is crucial.\n"
#     message += "  • <b>File Naming:</b> Name your file something professional, like 'FirstName-LastName-Resume.pdf'.\n"
#     message += "  • <b>Consistency:</b> Ensure formatting (dates, fonts, spacing) is consistent throughout the document.\n\n"
    
#     message += "<i>Disclaimer: This is an automated analysis designed to provide guidance. Tailor your resume for each specific job application.</i>"

#     return message.strip()
# def build_professional_output(data: dict) -> str:
#     """Builds the perfected, professional, and detailed resume analysis report."""
    
#     score_data = data['score_breakdown']
#     total_score = score_data['total_score']
    
#     if total_score >= 85:
#         summary_emoji = "🚀"
#         summary_text = "<b>Excellent!</b> A highly competitive and well-crafted resume."
#     elif total_score >= 70:
#         summary_emoji = "✅"
#         summary_text = "<b>Solid Resume.</b> A strong foundation with clear opportunities for enhancement."
#     else:
#         summary_emoji = "💡"
#         summary_text = "<b>Good Start.</b> Needs key improvements to meet professional standards."

#     # --- Start Building the Message ---
#     message = f"{summary_emoji} <b><u>Professional Resume Analysis</u></b> {summary_emoji}\n\n"
    
#     # --- Score Breakdown Section ---
#     message += "<b><u>Overall ATS Score</u></b>\n"
#     message += f"<b>TOTAL: {total_score} / 100</b>\n"
#     message += f"<i>{summary_text}</i>\n\n"
    
#     # Detailed rubric
#     message += f"  • <b>Core Components:</b> {score_data['core_score']} / 30\n"
#     message += f"  • <b>Experience & Impact:</b> {score_data['impact_score']} / 45\n"
#     message += f"  • <b>Skills & Keywords:</b> {score_data['skills_score']} / 25\n\n"
#     message += "---" * 8 + "\n\n"

#     # --- Detailed Analysis Sections ---
#     message += "<b><u>Detailed Breakdown & Recommendations</u></b>\n\n"

#     # 1. Core Components
#     message += "<b>1. Core Components Analysis</b>\n"
#     contact = data['contact_info']
#     if not contact['missing']:
#         message += "  ✅ <b>Contact Info:</b> All key contact details found.\n"
#     else:
#         message += f"  ❌ <b>Contact Info:</b> Missing: {', '.join(contact['missing'])}.\n"
            
#     sections = data['sections']
#     if len(sections['missing']) <= 1: # Allow missing summary
#         message += "  ✅ <b>Sections:</b> All critical sections are present.\n"
#     else:
#         message += f"  ⚠️ <b>Sections:</b> Consider adding: {', '.join(sections['missing'])}.\n"
    
#     message += f"  ✅ <b>Clarity & Conciseness:</b> {data['clarity']['feedback']} No confusing jargon detected.\n"
#     cliches = data['cliches']
#     if cliches['count'] > 0:
#         message += f"  ❌ <b>Buzzwords:</b> Detected {cliches['count']} cliché(s) like <code>{cliches['found'][0]}</code>. Replace with specific examples of your achievements.\n\n"
#     else:
#         message += "  ✅ <b>Buzzwords:</b> Excellent! Your language is specific and professional.\n\n"

#     # 2. Experience & Impact
#     message += "<b>2. Experience & Impact Analysis</b>\n"
#     message += f"  ✅ <b>Action Verbs:</b> {data['action_verbs']['feedback']}\n"
#     if data['action_verbs']['score'] < 80:
#         message += "      - <b>Tip:</b> Start each bullet point with a strong verb (e.g., 'Developed', 'Managed') to show you as the primary actor.\n"
        
#     message += f"  ✅ <b>Quantification:</b> {data['quantification']['feedback']} Using numbers to show the scale of your work is crucial for impact.\n"
#     if data['quantification']['count'] < 3:
#         message += "      - <b>Tip:</b> Add more metrics. How many people were on your team? By what percentage did you improve a process? How much money did you save?\n"
    
#     tenses = data['tenses']
#     if tenses['consistent']:
#         message += "  ✅ <b>Tense Consistency:</b> Verb tenses appear consistent.\n\n"
#     else:
#         message += f"  ❌ <b>Tense Consistency:</b> {tenses['feedback']}\n\n"

#     # 3. Skills & Keywords
#     message += "<b>3. Skills & Keywords Analysis</b>\n"
#     skills = data['skill_keywords']
#     if skills['hard_skills']:
#         message += f"  ✅ <b>Hard Skills Found:</b> " + ", ".join(f"<code>{s}</code>" for s in skills['hard_skills'][:10]) + "\n"
#     else:
#         message += "  ❌ <b>Hard Skills:</b> No specific technical skills were identified. Ensure you have a detailed skills section.\n"
    
#     if skills['soft_skills']:
#         message += f"  ✅ <b>Soft Skills Found:</b> " + ", ".join(f"<code>{s}</code>" for s in skills['soft_skills']) + "\n"
#     else:
#         message += "  ⚠️ <b>Soft Skills:</b> While important, these are best demonstrated through your experience bullet points rather than just listing them.\n"
#     message += "\n"

#     # --- Final Recommendations ---
#     message += "<b><u>Final Recommendations</u></b>\n"
#     message += "  • <b>Proofread:</b> Double-check for any spelling or grammar errors.\n"
#     message += "  • <b>File Format:</b> Always submit as a PDF to preserve formatting.\n"
#     message += "  • <b>Tailor Your Resume:</b> For real applications, adjust your keywords and bullet points to match the specific job description.\n\n"
    
#     message += "<i>Disclaimer: This automated analysis provides guidance based on general best practices.</i>"

#     return message.strip()

# In utils.py

def build_professional_output(data: dict) -> str:
    """Builds the elite, professional, and highly detailed resume analysis report."""
    
    score_data = data['score_breakdown']
    total_score = score_data['total_score']
    
    if total_score >= 90:
        summary_emoji = "🏆"
        summary_text = "<b>Exceptional!</b> This is a top-tier, elite resume that meets the highest professional standards."
    elif total_score >= 75:
        summary_emoji = "🚀"
        summary_text = "<b>Very Strong.</b> A highly competitive resume with excellent structure and impact."
    elif total_score >= 60:
        summary_emoji = "✅"
        summary_text = "<b>Solid Foundation.</b> A good resume with clear, actionable areas for improvement."
    else:
        summary_emoji = "💡"
        summary_text = "<b>Needs Significant Improvement.</b> Requires substantial updates to be competitive."

    # --- Start Building the Message ---
    message = f"{summary_emoji} <b><u>Elite Resume Analysis</u></b> {summary_emoji}\n\n"
    
    # --- Score Breakdown Section ---
    message += "<b><u>Overall ATS & Quality Score</u></b>\n"
    message += f"<b>FINAL SCORE: {total_score} / 100</b>\n"
    message += f"<i>{summary_text}</i>\n\n"
    
    message += f"  • <b>Structure & Clarity:</b> {score_data['structure_score']} / 20\n"
    message += f"  • <b>Experience & Impact:</b> {score_data['impact_score']} / 50\n"
    message += f"  • <b>Skills & Competencies:</b> {score_data['skills_score']} / 30\n\n"

    # Penalties Section
    penalties = data['penalties']
    if penalties:
        message += "<b>Penalties Applied:</b>\n"
        for p in penalties:
            message += f"  - <code>{p['points']} pts</code> for: <i>{p['reason']}</i>\n"
        message += "\n"

    message += "---" * 8 + "\n\n"
    message += "<b><u>Detailed Breakdown & Recommendations</u></b>\n\n"

    # 1. Experience & Impact Analysis
    impact = data['experience_impact']
    message += f"<b>1. Experience & Impact Analysis (Score: {score_data['impact_score']}/50)</b>\n"
    message += f"  - {impact['feedback']}\n"
    if impact['impact_score'] < 75:
        message += "  - <b>Tip:</b> A perfect bullet point starts with an action verb, contains a number/metric, and is 10-25 words long. Focus on showcasing measurable results.\n\n"
    else:
        message += "  - ✅ Your bullet points are consistently impactful and well-written.\n\n"
    
    # 2. Skills & Competencies Analysis
    message += f"<b>2. Skills & Competencies (Score: {score_data['skills_score']}/30)</b>\n"
    skills = data['skill_tiers']
    if not skills:
        message += "  - ❌ No technical or professional skills were clearly identified. This is a critical area for improvement.\n"
    for tier, skill_list in skills.items():
        message += f"  - <b>{tier}:</b> " + ", ".join(f"<code>{s}</code>" for s in skill_list) + "\n"
    message += "\n"

    # 3. Structure & Clarity Analysis
    message += f"<b>3. Structure & Clarity (Score: {score_data['structure_score']}/20)</b>\n"
    contact = data['contact_info']
    if not contact['missing']:
        message += "  - ✅ All essential contact information found.\n"
    else:
        message += f"  - ❌ Missing contact details: {', '.join(contact['missing'])}.\n"
    
    # Final Recommendations
    message += "\n<b><u>Final Recommendations</u></b>\n"
    message += "  • <b>Review Penalties:</b> Address any points deducted in the 'Penalties' section above.\n"
    message += "  • <b>Tailor Keywords:</b> For real applications, research the target company and role, and ensure your Tier 1 and Tier 2 skills align with their needs.\n"
    message += "  • <b>Proofread Meticulously:</b> One small typo can undermine a perfect score.\n\n"
    
    message += "<i>Disclaimer: This automated analysis provides guidance based on general best practices.</i>"

    # Invitation to the new Q&A feature
    message += "\n\n" + "---" * 8 + "\n\n"
    message += "🤖 **You can now ask me questions!**\nType any question about your resume, or ask for general career advice. (Type `/end` to finish)."

    return message.strip()