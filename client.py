import requests
from opentelemetry import baggage, trace
from opentelemetry.context import attach, detach
from opentelemetry.launcher import configure_opentelemetry

configure_opentelemetry(
    service_name="service-123",
    service_version="1.2.3",  # optional
    log_level="DEBUG",  # optional
    propagators="baggage,tracecontext",
)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("main"):
    span = trace.get_current_span()
    span.set_attribute("example", "attribute")

    # example of utilizing baggage
    ctx = baggage.set_baggage("projectID", "123")
    token = attach(ctx)

    requests.get("http://localhost:8000/hello")

    detach(token)
