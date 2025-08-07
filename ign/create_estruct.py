
import os

# Defina a estrutura e conteúdo inicial (vazio ou exemplo)
structure = {
    "jira-alert-service": {
        "app": {
            "main.py": "# Código principal aqui\n",
            "jira_client.py": "# Integração Jira\n",
            "slack_client.py": "# Integração Slack\n",
            "logger.py": "# Configuração de logs\n",
            "metrics.py": "# Métricas Prometheus\n",
            "models.py": "# Schemas Pydantic\n",
        },
        ".env": "# Variáveis de ambiente\n",
        "requirements.txt": "# Dependências do projeto\n",
        "README.md": "# Documentação do projeto\n",
    }
}

def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    create_structure(".", structure)
    print("Estrutura de projeto criada com sucesso!")
