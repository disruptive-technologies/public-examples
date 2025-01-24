PYTHON?=python3.13
PIP?=pip3
VENV?=venv

SHELL := /bin/bash

.PHONY: docs build venv VENV

venv: $(VENV)/bin/activate

$(VENV)/bin/activate: Makefile requirements.txt
	@test -d $(VENV) || $(PYTHON) -m venv $(VENV)
	${VENV}/bin/python -m pip install --upgrade pip -r requirements.txt
	@touch $(VENV)/bin/activate

marimo: venv
	source $(VENV)/bin/activate && cd notebooks && marimo edit . --headless

clean:
	rm -rf $(VENV)