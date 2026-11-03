VENV := .venv
PIP := $(VENV)/bin/pip

.PHONY: all clean re

all: $(VENV)
	@echo "Run: source $(VENV)/bin/activate"

$(VENV):
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install requests beautifulsoup4

clean:
	rm -rf $(VENV)

re: clean all
