.PHONY: setup create-venv update-deps start test coverage clean

VENV_NAME := .venv
PYTHON := $(VENV_NAME)/bin/python
PIP := $(VENV_NAME)/bin/pip
MAIN_FILE := main.py
APP_POKE_MODULE := app.main:app
TESTS_POKE_DIR := tests


setup: create-venv update-deps

create-venv:
	@echo "🔨 Creating a virtual environment..."
	python3 -m venv $(VENV_NAME)

update-deps:
	@echo "🚀 Updating the virtual environment..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

start:
	@echo "🏁 Serving FastAPI..."
	$(PYTHON) $(MAIN_FILE)

test:
	@echo "🧪 Running the tests..."
	$(PYTHON) -m pytest $(TESTS_POKE_DIR)

coverage:
	@echo "📊 Running the test coverage..."
	$(PYTHON) -m pytest --cov=app --cov-report=html $(TESTS_POKE_DIR)

clean:
	@echo "🧹 Cleaning up..."
	rm -rf $(VENV_NAME)
	find . -name "*.pyc" -delete