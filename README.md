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


