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
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall

#Проверка линтера
make lint:
	poetry run flake8 brain_games

#Запуск проекта
brain-games:
	poetry run brain-games

