.PHONY: test

setup:
	pip install -r requirements.txt
	pre-commit install

test:
	pytest
