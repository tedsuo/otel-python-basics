import requests

from opentelemetry import baggage, trace
from opentelemetry.launcher import configure_opentelemetry
# from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.metrics import set_meter_provider
from opentelemetry.trace import set_tracer_provider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.context import attach, detach

set_tracer_provider(TracerProvider())

set_meter_provider(MeterProvider())


# example of getting the current span

# example of utilizing baggage

configure_opentelemetry(
    service_name="service-123",
    service_version="1.2.3",  # optional
    log_level="DEBUG",  # optional
    propagators="baggage,tracecontext",
)

tracer = trace.get_tracer(__name__)

span = trace.get_current_span()
print("current span: ", span)

with tracer.start_as_current_span("foo"):
    span = trace.get_current_span()
    print("current span: ", span)

    with tracer.start_as_current_span("add-attribute") as span:
        span.set_attribute("attr1", "valu1")

    ctx = baggage.set_baggage("projectID", "123")

    token = attach(ctx)

    print("val_ctx: ", baggage.get_baggage("projectID", ctx))
    print("val_no_ctx: ", baggage.get_baggage("projectID"))

    with tracer.start_as_current_span("bar"):

        url = "http://localhost:8000/hello"

        with tracer.start_as_current_span(
            "request to {}".format(url)
        ) as span:
            try:
                requests.get(url)
            except Exception as e:
                span.set_attribute("error", "true")
                span.record_exception(e)

        print("Hello world from OpenTelemetry Python!")
    detach(token)