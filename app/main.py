# Código principal aqui

from fastapi import FastAPI
from app.models import Alerta
from app.jira_client import criar_ticket_jira
from app.slack_client import enviar_alerta_slack
from app.logger import logger
from app.metrics import REQUEST_COUNT, ALERT_ERRORS
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()

@app.post("/alerta")
async def receber_alerta(alerta: Alerta):
    REQUEST_COUNT.inc()
    try:
        logger.info(f"Recebido alerta: {alerta.titulo}")
        ticket = criar_ticket_jira(alerta.titulo, alerta.descricao)
        enviar_alerta_slack(f"🔔 Novo alerta: {alerta.titulo}\n📋 Ticket: {ticket}")
        return {"status": "ok", "ticket": ticket}
    except Exception as e:
        ALERT_ERRORS.inc()
        logger.error(f"Erro ao processar alerta: {e}")
        return {"status": "erro", "mensagem": str(e)}

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

#uvicorn app.main:app --reload