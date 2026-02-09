dev-up:
	fastapi dev app/main.py

check:
	ruff check && ruff format
