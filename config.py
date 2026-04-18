import json
import os

def get_board_tokens():
    """Reads the tracked companies from the JSON file."""
    try:
        with open("companies.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# ... keep your TARGET_KEYWORDS, EXCLUDED_KEYWORDS, CANDIDATE_DATA, etc. below ...
TARGET_KEYWORDS = [
    "backend", "software engineer", "sde", "distributed systems", 
    "systems engineer", "platform", "java", "c++", "core engineering"
]

EXCLUDED_KEYWORDS = [
    "frontend", "ui", "ux", "mobile", "ios", "android", "sales", 
    "marketing", "hr", "recruiter", "manager", "product manager", 
    "intern", "data scientist", "support", "qa", "sdet"
]

# --- File Paths ---
CV_FILE_PATH = "data/cv.md"
RESUME_FILE_PATH = "resumes/Yash_Malani_Resume_2.pdf"

# --- Candidate Details ---
CANDIDATE_DATA = {
    "first_name": "Yash",
    "last_name": "Malani",
    "email": "yashmalani340@gmail.com",
    "phone": "+91-79766-40069",
    "linkedin": "linkedin.com/in/yashmalani340",
    "github": "github.com/yashmalani"
}