# Métricas Prometheus

from prometheus_client import Counter

# Contador de requisições recebidas
REQUEST_COUNT = Counter("alert_requests_total", "Total de alertas recebidos")

# Contador de erros
ALERT_ERRORS = Counter("alert_errors_total", "Total de erros ao processar alertas")
