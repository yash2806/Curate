# job_filter.py
from config import TARGET_KEYWORDS, EXCLUDED_KEYWORDS

def is_relevant_role(job_title):
    """Filters jobs locally to save LLM API costs."""
    title_lower = job_title.lower()
    
    # 1. Hard Drop: If it contains an excluded word, reject immediately.
    for bad_word in EXCLUDED_KEYWORDS:
        if bad_word.lower() in title_lower:
            return False
            
    # 2. Match: If it contains a target word, approve it for LLM evaluation.
    for good_word in TARGET_KEYWORDS:
        if good_word.lower() in title_lower:
            return True
            
    # Default to False if it doesn't match our targets
    return False