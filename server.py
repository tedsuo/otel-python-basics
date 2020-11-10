#!/usr/bin/env python3

from flask import Flask
from opentelemetry import trace, baggage
from time import sleep
from opentelemetry.launcher import configure_opentelemetry

PORT = 8000

app = Flask(__name__)
tracer = trace.get_tracer(__name__)

configure_opentelemetry(
    service_name="server-456",
    service_version="4.5.6",
    log_level="DEBUG",  # optional
    propagators="baggage,tracecontext",
)


@app.route("/hello")
def hello():

    # get the current span, created by flask instrumentation
    current_span = trace.propagation.get_current_span()

    # add more attributes to the server span
    current_span.set_attribute("http.route", "some_route")

    # pretend to do work and record the latency
    sleep(20 / 1000)

    with tracer.start_as_current_span("server_span") as span:

        # add a baggage value
        span.set_attribute("projectID", baggage.get_baggage("projectID"))

        # add an event
        span.add_event("event message", {"event_attributes": 1})

        # pretend to do work and record the latency
        sleep(30 / 1000)

        # record an exception
        try:
            1 / 0
        except ZeroDivisionError as error:
            span.record_exception(error)
            print("caught zero division error")

        return "hello"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
