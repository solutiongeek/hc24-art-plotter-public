# Variables
PYTHON := poetry run python
POETRY := poetry
SRC := src/  # Adjust this to your actual source directory
TEST_DIR := tests/

default: install

# Install dependencies
.PHONY: install
install:
	$(POETRY) install

# Remove virtual environment and caches (be careful with this)
.PHONY: clean
clean:
	$(POETRY) env remove --all
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -exec rm -f {} +

# Update dependencies
.PHONY: update
update:
	$(POETRY) update
