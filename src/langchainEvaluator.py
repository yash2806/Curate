# langchainEvaluator.py
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

# 1. Define the expected output structure
class JobEvaluation(BaseModel):
    is_match: bool = Field(description="True if the candidate is a strong fit for the role")
    confidence_score: int = Field(description="Score from 0 to 100 on how well the profile matches")
    reasoning: str = Field(description="Brief explanation of the score")

parser = JsonOutputParser(pydantic_object=JobEvaluation)

# 2. Build the Prompt
prompt = PromptTemplate(
    template="""You are an expert technical recruiter evaluating a candidate for a role.
    
    Candidate Profile (YAML):
    {candidate_profile}
    
    Job Description:
    {job_description}
    
    Evaluate if this candidate is a strong fit for this specific job.
    {format_instructions}
    """,
    input_variables=["candidate_profile", "job_description"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# 3. The LLM Factory
def get_llm():
    """Dynamically loads the LLM based on .env configuration."""
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    model_name = os.getenv("LLM_MODEL", "gpt-4o-mini")
    api_key = os.getenv("LLM_API_KEY")
    
    if not api_key:
        raise ValueError("LLM_API_KEY is missing from your .env file.")

    if provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(temperature=0, model=model_name, api_key=api_key)
        
    elif provider == "anthropic":
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(temperature=0, model=model_name, api_key=api_key)
        
    elif provider == "google":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(temperature=0, model=model_name, api_key=api_key)
        
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: '{provider}'. Please use 'openai', 'anthropic', or 'google'.")

# 4. Create the Chain dynamically
def evaluate_job(job_description_text, profile_yaml_string):
    # Initialize the LLM on the fly based on current environment variables
    llm = get_llm()
    chain = prompt | llm | parser
    
    result = chain.invoke({
        "candidate_profile": profile_yaml_string,
        "job_description": job_description_text
    })
    return result