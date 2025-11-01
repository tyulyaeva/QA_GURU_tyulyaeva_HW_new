help:
	@echo "Makefile commands:"
	@echo "make install    - Установить зависимости"
	@echo "make run_test   - Запустить все автотесты (pytest -v)"
	@echo "make test_only  - Запустить тесты с меткой (по умолчанию: only)"
	@echo "make linter     - Отформатировать и проверить код (isort, black, flake8)"
	@echo "make hooks      - Установить/обновить pre-commit хуки"
	@echo "make clean      - Очистить кеши/отчёты"


linter:
	isort .
	black .
	flake8 .


run_test:
	python -m pytest -v


install:
	python -m pip install -r requirements.txt