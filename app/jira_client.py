# Integração Jira

import requests, os
from dotenv import load_dotenv

load_dotenv()

def criar_ticket_jira(titulo, descricao):
    url = f"{os.getenv('JIRA_BASE_URL')}/rest/api/3/issue"
    auth = (os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))

    payload = {
        "fields": {
            "project": {"key": os.getenv("JIRA_PROJECT_KEY")},
            "summary": titulo,
            "description": descricao,
            "issuetype": {"name": "Incident"}
        }
    }

    response = requests.post(url, json=payload, auth=auth)
    response.raise_for_status()
    return response.json()["key"]
