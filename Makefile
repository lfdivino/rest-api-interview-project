install:
	pip install -e .

test:
	pytest tests/ -v --cov=api_interview

run:
	FLASK_APP=api_interview/app.py flask run