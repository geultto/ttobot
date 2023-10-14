run-server:
	ENV=prod uvicorn app:app --host 0.0.0.0 --port 8000

dev:
	ENV=dev uvicorn app:app --host 0.0.0.0 --port 8000 --reload

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt
