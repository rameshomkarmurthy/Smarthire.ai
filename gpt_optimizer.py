import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def improve_summary(resume_text, job_description):
    prompt = f"""Rewrite this resume summary to better match the following job description:

Job Description:
{job_description}

Resume Summary:
{resume_text}

Make it more professional, ATS-friendly, and aligned with the job requirements.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
