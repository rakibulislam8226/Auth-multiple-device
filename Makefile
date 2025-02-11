pys:
	python3 manage.py runserver 0.0.0.0:8000

pym:
	python3 manage.py migrate

pymm:
	python3 manage.py makemigrations

nrd:
	npm run dev

celery:
	python -m celery -A conf worker --loglevel=info
	python -m celery -A conf beat --loglevel=info
	python -m celery -A conf flower --port=5555


