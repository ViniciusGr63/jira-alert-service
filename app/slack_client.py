# Integração Slack

import requests, os

def enviar_alerta_slack(mensagem):
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    payload = {"text": mensagem}
    response = requests.post(webhook, json=payload)
    if response.status_code != 200:
        raise Exception(f"Erro ao enviar mensagem Slack: {response.text}")
