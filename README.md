# 📈 Observability Export — Stack de Observabilidade com OpenTelemetry

Este repositório contém a infraestrutura necessária para uma stack de **observabilidade moderna**, com foco em **logs**, **métricas** e **traces**, utilizando ferramentas open source e compatíveis com o ecossistema OpenTelemetry.

---

## ⚙️ Visão Geral da Arquitetura

- 🐍 **Aplicação Python** com OpenTelemetry (logs + traces)
- 📦 **OpenTelemetry Collector** para ingestão e roteamento de dados
- 📊 **Grafana** para visualização centralizada
- 📦 **Loki** como backend de logs
- 📉 **Prometheus** como backend de métricas
- 🔍 **Jaeger** para visualização de traces distribuídos

---

## 🌐 Infraestrutura

| Serviço         | Porta  | Função                     |
|-----------------|--------|----------------------------|
| Grafana         | `3000` | Dashboard unificado        |
| Loki            | `3100` | Coletor de logs            |
| Prometheus      | `9090` | Coletor de métricas        |
| OTEL Collector  | `4317/4318` | Ingestor OTLP         |
| Jaeger          | `16686` | Visualização de traces     |

---

## 📁 Estrutura do Projeto

observability/
├── configs/
│ ├── otel-collector-config.yaml # Configuração atual do OTEL Collector
│ └── otel-collector-with-jaeger.yaml # Config com exportador Jaeger ativado
│
├── docs/
│ └── grafana-queries.md # Exemplos de queries no Grafana/Loki
│
├── python-app/
│ ├── app.py # App Python instrumentado com OpenTelemetry
│ ├── app_production.py # Variante com config de produção
│ ├── Dockerfile # Dockerfile da aplicação
│ ├── requirements.txt # Dependências Python
│ └── .env # Variáveis de ambiente
│
├── scripts/
│ └── install-jaeger.sh # Script para subir o Jaeger via Docker
│
└── README.md # Documentação principal do projeto
