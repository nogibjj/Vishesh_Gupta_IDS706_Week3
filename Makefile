install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	ruff check *.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

test:
	python -m pytest -vv --nbval-lax -cov=mylib -cov=main test_*.py *.ipynb

all: install format lint test