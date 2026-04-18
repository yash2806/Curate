# Import External Tooling
from fetchJobs import fetch_greenhouse_jobs, check_can_auto_apply
from langchainEvaluator import evaluate_job
from submitApplication import submit_application

# Import Internal Modules
from config import get_board_tokens, CANDIDATE_DATA, RESUME_FILE_PATH, CV_FILE_PATH
from jobFilter import is_relevant_role
from storage import already_applied, mark_as_applied, load_cv_text

def run_auto_applier():
    # Load your CV context from config path
    my_cv_text = load_cv_text(CV_FILE_PATH)
    if not my_cv_text:
        print("Aborting: CV text could not be loaded.")
        return

    for token in get_board_tokens():
        print(f"\nScanning job board: {token.upper()}...")
        jobs = fetch_greenhouse_jobs(token)
        
        for job in jobs:
            job_id = str(job["id"])
            job_title = job.get("title", "Unknown Title")
            
            # Step A: Local Keyword Filter
            if not is_relevant_role(job_title):
                print(f"Skipping (Filter): {job_title}")
                continue

            # Step B: Duplicate Check
            if already_applied(job_id):
                continue
                
            print(f"\nAnalyzing: {job_title} ({job_id})")
            
            # Step C: Pre-flight check for custom fields
            if not check_can_auto_apply(token, job_id):
                continue
                
            # Step D: Agentic Evaluation
            evaluation = evaluate_job(job.get("content", ""), my_cv_text)
            print(f"  Match: {evaluation['is_match']} | Score: {evaluation['confidence_score']}")
            print(f"  Reasoning: {evaluation['reasoning']}")
            
            # Step E: Execute Application
            if evaluation["is_match"] and evaluation["confidence_score"] >= 85:
                print("  => High match detected. Applying...")
                
                # Uncomment the line below to send requests..
                # submit_application(token, job_id, CANDIDATE_DATA, RESUME_FILE_PATH)
                
                mark_as_applied(job_id)

