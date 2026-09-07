VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

.PHONY: run clean

$(VENV):
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install requests

run: $(VENV)
	$(PYTHON) request.py $(ARGS)

clean:
	rm -rf $(VENV)