import os
from dotenv import load_dotenv

# Load env variables at the absolute entry point
load_dotenv()

from curate import run_auto_applier

if __name__ == "__main__":
    run_auto_applier()