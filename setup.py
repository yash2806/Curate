from setuptools import setup, find_packages

setup(
    name="curate",
    version="1.0.0",
    description="AI-powered CLI tool for autonomous job application evaluation",
    author="Yash Malani",
    packages=find_packages(),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "langchain-core",
        "langchain-openai",
        "langchain-anthropic",
        "langchain-google-genai",
        "pydantic",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "curate=cli:main",
        ],
    },
    python_requires=">=3.9",
)