# Configuração Atual - Observability Stack

## EC2 Observability (IP:)
- **RAM**: 8GB
- **OS**: Ubuntu
- **Serviços rodando**:
  - Grafana (porta 3000)
  - Loki (porta 3100) 
  - Prometheus (porta 9090)
  - OpenTelemetry Collector (4317/4318)

## EC2 Python App (IP:)
- **App**: Python com OpenTelemetry
- **Instrumentação**: Logs + Traces
- **Target**: EC2 Observability

## Status
- ✅ Logs funcionando (Grafana → Loki)
- ✅ Trace IDs nos logs
- ⏳ Jaeger pendente (para traces)
- ✅ Drilldown básico funcionando

## Próximos passos
1. Instalar Jaeger
2. Configurar trace backend
3. Correlação completa logs ↔ traces
