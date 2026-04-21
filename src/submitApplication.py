import requests

def submit_application(board_token, job_id, candidate_data, resume_file_path):
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs/{job_id}/applications"
    
    # Standard fields required by Greenhouse
    data = {
        "first_name": candidate_data["first_name"],
        "last_name": candidate_data["last_name"],
        "email": candidate_data["email"],
        "phone": candidate_data["phone"],
        "mapped_url_tokens[LinkedIn]": candidate_data["linkedin"],
        "mapped_url_tokens[GitHub]": candidate_data["github"]
    }
    
    # Read the PDF resume
    with open(resume_file_path, "rb") as f:
        files = {
            "resume": (resume_file_path, f, "application/pdf")
        }
        
        # Make the POST request
        response = requests.post(url, data=data, files=files)
        
        if response.status_code == 200:
            print(f"Successfully applied to job {job_id}!")
        else:
            print(f"Failed to apply: {response.text}")