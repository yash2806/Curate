from setuptools import setup, find_packages

setup(
    name="curate",
    version="1.0.0",
    description="An AI-powered CLI tool to auto-apply to jobs via Greenhouse.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "requests",
        "langchain-core",
        "langchain-openai",
        "langchain-anthropic",
        "langchain-google-genai",
        "pydantic",
        "python-dotenv"
    ],
    # This is the magic part that creates the terminal command
    entry_points={
        "console_scripts": [
            "curate=cli:main", 
        ],
    },
)