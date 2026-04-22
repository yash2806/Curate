import json
import os

def get_board_tokens():
    """Reads the tracked companies from the JSON file."""
    try:
        # Get the project root directory (parent of src/)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        companies_file = os.path.join(project_root, "data", "companies.json")
        with open(companies_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found, try again..")
        return []

# ... keep your TARGET_KEYWORDS, EXCLUDED_KEYWORDS, CANDIDATE_DATA, etc. below ...
TARGET_KEYWORDS = [
    "backend", "software engineer", "sde", "distributed systems", 
    "systems engineer", "platform", "java", "c++", "core engineering", "senior software engineer",
    "senior engineer"
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