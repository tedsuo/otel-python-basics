# OpenTelemetry Python Basics

Just a basic client/server for playing with OpenTelemetry in Python.

Handy links:

* [Free Lightstep Developer Account](https://app.lightstep.com/signup/developer?signup_source=typythonbasics)
* OTel Python Launcher: https://github.com/lightstep/otel-launcher-python/
* Quickstart Guide: https://opentelemetry.lightstep.com/python
* OpenTelemetry Python: https://github.com/open-telemetry/opentelemetry-python

Define your Lightstep Access Token prior to running:

```sh
export LS_ACCESS_TOKEN=my-access-token-etc
```

## Installation
```
git clone https://github.com/tedsuo/otel-python-basics.git && cd otel-python-basics
mkdir new_virtual_environment
python3 -m venv new_virtual_environment
source new_virtual_environment/bin/activate
pip install -r requirements.txt
```

## Run

```
export LS_ACCESS_TOKEN=my-access-token-etc
export LS_SERVICE_NAME=hello-server
export OTEL_PYTHON_TRACER_PROVIDER=sdk_tracer_provider
opentelemetry-instrument python3 server.py
```

```
export LS_ACCESS_TOKEN=my-access-token-etc
export LS_SERVICE_NAME=hello-client
export OTEL_PYTHON_TRACER_PROVIDER=sdk_tracer_provider
opentelemetry-instrument python3 client.py
```
