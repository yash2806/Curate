# storage.py

# Simple mock database to prevent duplicate applications
APPLIED_JOBS_DB = set()

def already_applied(job_id):
    return job_id in APPLIED_JOBS_DB

def mark_as_applied(job_id):
    APPLIED_JOBS_DB.add(job_id)

def load_cv_text(filepath):
    """Loads the CV text to feed into the LangChain agent."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Could not find CV at {filepath}")
        return ""