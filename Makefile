# Use -v and as many v's to increase verbosity
VERBOSITY += 

.PHONY: lint check test
lint:
	uv run --dev ruff format
check: lint
	uv run --dev ruff check --select I --fix
	uv run --dev ruff format
type: check
	uv run --dev ty check
test: type
	uv run --dev pytest ${VERBOSITY}
build: test
	uv build --clear -v .
setup:
	uv sync

