#!/usr/bin/env python3

from flask import Flask
from opentelemetry.launcher import configure_opentelemetry
from opentelemetry.trace import set_tracer_provider
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry import trace
from time import sleep
from opentelemetry import baggage

set_tracer_provider(TracerProvider())


PORT = 8000
configure_opentelemetry(
    service_name="server-456",
    service_version="4.5.6",
    propagators="baggage,tracecontext",
)

app = Flask(__name__)
tracer = trace.get_tracer(__name__)


@app.route("/hello")
def hello():

    current_span = trace.propagation.get_current_span()

    current_span.set_attribute("http.route", "some_route")

    with tracer.start_as_current_span("server_span") as span:

        span.set_attribute("projectID", baggage.get_baggage("projectID"))
#        span.add_event("the_event", {"the_event_attribute": 1})
        sleep(30 / 1000)
        return "hello"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)