# cli.py
import argparse
import json
import os
from dotenv import set_key
from main import run_auto_applier

COMPANIES_FILE = "companies.json"
ENV_FILE = ".env"

# --- Helper Functions ---
def load_companies():
    if not os.path.exists(COMPANIES_FILE):
        return []
    with open(COMPANIES_FILE, "r") as f:
        return json.load(f)

def save_companies(companies):
    with open(COMPANIES_FILE, "w") as f:
        json.dump(companies, f, indent=4)

# --- Command Logic ---
def configure_llm(args):
    """Sets the LLM credentials in the .env file."""
    # Ensure .env exists
    if not os.path.exists(ENV_FILE):
        open(ENV_FILE, 'w').close()

    if args.provider:
        set_key(ENV_FILE, "LLM_PROVIDER", args.provider)
        print(f"✅ Provider set to: {args.provider}")
    if args.model:
        set_key(ENV_FILE, "LLM_MODEL", args.model)
        print(f"✅ Model set to: {args.model}")
    if args.key:
        set_key(ENV_FILE, "LLM_API_KEY", args.key)
        print(f"✅ API Key updated.")

def add_company(args):
    """Adds a new company token to the tracking list."""
    companies = load_companies()
    company = args.name.lower().strip()
    
    if company in companies:
        print(f"⚠️  '{company}' is already in your tracking list.")
    else:
        companies.append(company)
        save_companies(companies)
        print(f"✅ Added '{company}' to tracking list. Total: {len(companies)}")

def remove_company(args):
    """Removes a company token from the tracking list."""
    companies = load_companies()
    company = args.name.lower().strip()
    
    if company in companies:
        companies.remove(company)
        save_companies(companies)
        print(f"🗑️  Removed '{company}' from tracking list. Total: {len(companies)}")
    else:
        print(f"⚠️  '{company}' was not found in your list.")

def list_companies(args):
    """Displays all currently tracked companies."""
    companies = load_companies()
    print("\n🏢 Currently Tracked Companies:")
    print("-" * 30)
    for i, company in enumerate(companies, 1):
        print(f"{i}. {company}")
    print("-" * 30)

def execute_run(args):
    """Triggers the main auto-applier loop."""
    print("🚀 Starting Smart Auto-Applier...\n")
    run_auto_applier()

# --- CLI Setup ---
def main():
    parser = argparse.ArgumentParser(description="Smart Auto-Applier CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Command: run
    parser_run = subparsers.add_parser("run", help="Start the auto-applier loop")
    parser_run.set_defaults(func=execute_run)

    # Command: config
    parser_config = subparsers.add_parser("config", help="Configure LLM provider and API keys")
    parser_config.add_argument("--provider", type=str, choices=["openai", "anthropic", "google"], help="Which LLM provider to use")
    parser_config.add_argument("--model", type=str, help="The model name (e.g., gpt-4o-mini, claude-3-5-sonnet-20240620)")
    parser_config.add_argument("--key", type=str, help="Your API key")
    parser_config.set_defaults(func=configure_llm)

    # Command: add
    parser_add = subparsers.add_parser("add", help="Add a company to track")
    parser_add.add_argument("name", type=str, help="The Greenhouse board token (e.g., 'anthropic')")
    parser_add.set_defaults(func=add_company)

    # Command: remove
    parser_remove = subparsers.add_parser("remove", help="Stop tracking a company")
    parser_remove.add_argument("name", type=str, help="The Greenhouse board token to remove")
    parser_remove.set_defaults(func=remove_company)

    # Command: list
    parser_list = subparsers.add_parser("list", help="List all tracked companies")
    parser_list.set_defaults(func=list_companies)

    # Execute
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()