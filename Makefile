dev-up:
	fastapi dev main.py

check:
	ruff check && ruff format
