#Установка poetry
install:
	poetry install

#Сборка
build:
	poetry build

#Публикация
publish:
	poetry publish --dry-run

#Установка или переустановка с флагом --force-reinstall
package-install:
	python3 -m pip install --user dist/* --force-reinstall

#Проверка линтера
lint:
	poetry run flake8 brain_games

#Запуск brain-games
brain-games:
	poetry run brain-games

#запуск brain-even
brain-even:
	poetry run brain-even

#запуск brain-calc
brain-calc:
	poetry run brain-calc

#запуск brain-gcd
brain-gcd:
	poetry run brain-gcd

#запуск brain-progression
brain-progression:
	poetry run brain-progression