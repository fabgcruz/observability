# 📈 Observability Export — Stack de Observabilidade com OpenTelemetry

Este repositório contém a infraestrutura necessária para uma stack de **observabilidade moderna**, com foco em **logs**, **métricas** e **traces**, utilizando ferramentas open source e compatíveis com o ecossistema OpenTelemetry.

---
## ⚙️ Visão Geral da Arquitetura

- 🐍 **Aplicação Python** com OpenTelemetry (logs + traces)
- 🚛 **OpenTelemetry Collector** para ingestão e roteamento de dados
- 📊 ![Grafana](https://img.shields.io/badge/Grafana-3000-orange?logo=grafana&logoColor=white) Visualização centralizada
- 📦 ![Loki](https://img.shields.io/badge/Loki-3100-green?logo=loki&logoColor=white) Backend de logs
- 📉 ![Prometheus](https://img.shields.io/badge/Prometheus-9090-red?logo=prometheus&logoColor=white) Backend de métricas
- 🔍 ![Jaeger](https://img.shields.io/badge/Jaeger-16686-blue?logo=jaeger&logoColor=white) Visualização de traces distribuídos

---
## 🌐 Infraestrutura

| Serviço         | Porta  | Função                     |
|-----------------|--------|----------------------------|
| Grafana         | `3000` | Dashboard unificado        |
| Loki            | `3100` | Coletor de logs            |
| Prometheus      | `9090` | Coletor de métricas        |
| OTEL Collector  | `4317/4318` | Ingestor OTLP         |
| Jaeger          | `16686` | Visualização de traces     |



