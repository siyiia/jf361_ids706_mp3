install:
	pip install -r requirements.txt
	mkdir -p output/
lint:
	pylint --disable=R,C  src/*.py
format:
	black src/*.py
test:
	python src/main.py
