import requests

def fetch_greenhouse_jobs(board_token):
    """Fetches all active jobs with their full HTML descriptions."""
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs?content=true"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get("jobs", [])
    return []

def check_can_auto_apply(board_token, job_id):
    """
    Pre-flight check: Fetches the specific job's application form.
    Returns True if we can safely auto-apply, or False if there are custom 
    mandatory questions (e.g., Visa status, Cover Letter) we can't answer yet.
    """
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs/{job_id}?questions=true"
    response = requests.get(url)
    
    if response.status_code != 200:
        return False
        
    job_data = response.json()
    questions = job_data.get("questions", [])
    
    # Standard fields Greenhouse uses that our POST request handles
    standard_fields = {"first_name", "last_name", "email", "phone", "resume"}
    
    for q in questions:
        if q.get("required"):
            # Greenhouse groups inputs in a "fields" array per question
            fields = q.get("fields", [])
            for field in fields:
                field_name = field.get("name", "")
                
                # If a required field is NOT in our standard list, flag it
                if field_name not in standard_fields:
                    print(f"  [!] Skipping {job_id}: Requires custom field '{q.get('label')}'")
                    return False
                    
    return True