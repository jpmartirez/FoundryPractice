from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.environ["AGENT_ENDPOINT"]
api_key = os.environ["API_KEY"]

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)
my_agent = "elated-agent-bz968stwq4"
my_version = "2"
deployment_name = "gpt-4.1-mini"

question = input("Enter your question: ")

response = client.responses.create(
    model=deployment_name,
    input=question,
    extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
)


print(f"\nAnswer: {response.output_text}")
