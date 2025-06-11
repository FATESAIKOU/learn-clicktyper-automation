.PHONY: install format lint check test clean help

help: ## Show this help message
	@echo "Available commands:"
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

install: ## Install project dependencies
	uv sync --dev

format: ## Format code with black and isort
	uv run black .
	uv run isort .

lint: ## Run linting checks (flake8, mypy)
	uv run flake8 .
	uv run mypy .

check: ## Run all checks (format, lint, test)
	uv run black --check .
	uv run isort --check-only .
	uv run flake8 .
	uv run mypy .
	uv run pytest

test: ## Run tests
	uv run pytest

clean: ## Clean cache and build artifacts
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

pre-commit: ## Run pre-commit hooks manually
	uv run pre-commit run --all-files

pre-commit-update: ## Update pre-commit hooks
	uv run pre-commit autoupdate
