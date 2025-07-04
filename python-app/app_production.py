import time
import sys
import logging

# Tracing
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

# Logging
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter

# Configurar resource com labels
resource = Resource.create({
    "service.name": "teste-otel-python",
    "service.version": "1.0.0",
    "environment": "production"
})

# --- Tracer ---
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(
        OTLPSpanExporter(
            endpoint="http://54.172.252.227:4318/v1/traces",
            timeout=60
        ),
        max_queue_size=200,
        max_export_batch_size=50,
        schedule_delay_millis=5000,
        export_timeout_millis=60000
    )
)

# --- Logger ---
logger_provider = LoggerProvider(resource=resource)
set_logger_provider(logger_provider)
logger_provider.add_log_record_processor(
    BatchLogRecordProcessor(
        OTLPLogExporter(
            endpoint="http://54.172.252.227:4318/v1/logs",
            timeout=60
        ),
        max_queue_size=200,
        max_export_batch_size=50,
        schedule_delay_millis=5000,
        export_timeout_millis=60000
    )
)

otel_handler = LoggingHandler(level=logging.INFO, logger_provider=logger_provider)
stdout_handler = logging.StreamHandler(sys.stdout)

logger = logging.getLogger("otel-test")
logger.addHandler(otel_handler)
logger.addHandler(stdout_handler)
logger.setLevel(logging.INFO)

# --- Loop de teste ---
counter = 0
while True:
    counter += 1
    with tracer.start_as_current_span("loop-span") as span:
        # Obter trace_id e span_id do contexto atual
        span_context = span.get_span_context()
        trace_id = format(span_context.trace_id, '032x')
        span_id = format(span_context.span_id, '016x')
        
        # Adicionar atributos ao span
        span.set_attribute("counter", counter)
        span.set_attribute("operation", "periodic_log")
        
        # Log com trace_id manual para correlação
        log_message = f"[trace_id={trace_id}] [span_id={span_id}] Log #{counter} via OpenTelemetry funcionando!"
        logger.info(log_message)
        
        # Log adicional com informações estruturadas
        logger.info("Operação concluída com sucesso", extra={
            "trace_id": trace_id,
            "span_id": span_id,
            "counter": counter,
            "status": "success"
        })
        
        time.sleep(15)
