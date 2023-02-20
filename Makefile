install:
	poetry install

run:
	poetry run brain-games

lint:
	poetry run flake8 brain_games

build:
	poetry build

publish:
	poetry publish --dry-run

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=brain_games/ --cov-report xml

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	pip install  --force-reinstall dist/*.whl
