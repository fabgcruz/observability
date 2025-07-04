#!/bin/bash
# Instalar Jaeger via Docker

echo "Instalando Jaeger..."

# Parar se já estiver rodando
docker stop jaeger 2>/dev/null || true
docker rm jaeger 2>/dev/null || true

# Instalar Jaeger all-in-one
docker run -d --name jaeger \
  --restart unless-stopped \
  -p 16686:16686 \
  -p 14268:14268 \
  -p 6831:6831/udp \
  -p 6832:6832/udp \
  -p 5778:5778 \
  -p 14250:14250 \
  jaegertracing/all-in-one:latest

echo "Aguardando Jaeger inicializar..."
sleep 10

# Verificar se está funcionando
if curl -s http://localhost:16686 > /dev/null; then
    echo "✅ Jaeger instalado com sucesso!"
    echo "🌐 Acesse: http://54.172.252.227:16686"
else
    echo "❌ Erro na instalação do Jaeger"
fi

echo "📊 Para configurar no Grafana:"
echo "   Data Sources → Add → Jaeger"
echo "   URL: http://localhost:16686"
