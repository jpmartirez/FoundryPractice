# Foundry Practice

Small Python exercises for learning Azure AI, OpenAI-compatible clients, LangChain, document analysis, speech recognition, and agent-backed search. This repository is for practice, not a production application.

## Contents

- `CH-01-LLMS/` - basic Azure OpenAI and LangChain model calls.
- `CH-02-SERVICES/` - invoice/document analysis and microphone speech-to-text.
- `CH-03-AI-Search/` - ask questions through an Azure AI agent.
- `main.py` - minimal project scaffold.

## Setup

Requires Python `3.14+` and Azure resources with the relevant model or service deployments.

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows Git Bash
pip install -e .
```

Create a `.env` file in the project root. Depending on the exercise, provide:

```env
API_KEY=your_key
AZURE_OPENAI_ENDPOINT=your_openai_compatible_endpoint
PROJECT_ENDPOINT=your_content_understanding_endpoint
AZURE_SPEECH_ENDPOINT=your_speech_endpoint
AGENT_ENDPOINT=your_agent_endpoint
```

`API_KEY` is reused by the examples for their selected Azure service. Do not commit `.env` or real credentials.


