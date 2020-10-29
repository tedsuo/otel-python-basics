# OpenTelemetry Python Basics

Just a basic client/server for playing with OpenTelemetry in Python.

Handy links:

* Free Lightstep Developer Account: https://bit.ly/otel-workshop
* OTel Python Launcher: https://github.com/lightstep/otel-launcher-python/
* Quickstart Guide: https://opentelemetry.lightstep.com/python
* OpenTelemetry Python: https://github.com/open-telemetry/opentelemetry-python

Define your Lightstep Access Token prior to running:

```sh
export LS_ACCESS_TOKEN=my-access-token-etc
```

## Installation
```
python3 -m venv .
source bin/activate
pip3 install opentelemetry-launcher
pip3 install requests
pip3 install flask
opentelemetry-bootstrap -a install
```

## Run

```
export LS_ACCESS_TOKEN=my-access-token-etc
export LS_SERVICE_NAME=hello-server
opentelemetry-instrument python3 server.py
```

```
export LS_ACCESS_TOKEN=my-access-token-etc
export LS_SERVICE_NAME=hello-client
opentelemetry-instrument python3 client.py
```