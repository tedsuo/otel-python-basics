import requests
from opentelemetry import baggage, trace
from opentelemetry.context import attach, detach

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("main"):
    span = trace.get_current_span()
    span.set_attribute("example", "attribute")

    # example of utilizing baggage
    ctx = baggage.set_baggage("projectID", "123")
    token = attach(ctx)

    requests.get("http://localhost:8000/hello")
    
    detach(token)