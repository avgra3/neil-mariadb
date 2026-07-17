# Use -v and as many v's to increase verbosity
VERBOSITY += 

.PHONY: lint check
lint:
	uv run --dev ruff format
check: lint
	uv run --dev ruff check --fix
type: check
	uv run --dev ty check
test: type
	uv run --dev pytest ${VERBOSITY}
build: test
	uv build --clear -v .

