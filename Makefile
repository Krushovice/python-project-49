install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

run:
	poetry run brain-games

package-reinstall:
	pip install  --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games
