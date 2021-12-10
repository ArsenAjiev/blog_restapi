1. Установить библиотеку pip install pytest

2. создать файл pytest.ini
 Для того что бы запускать все тесты

[pytest]
DJANGO_SETTINGS_MODULE = blog_restapi.settings

blog_restapi - это имя проекта!


3. pytest
Запуск тестов

4. pytest tests/api/test_api.py
Запуск конкретного теста

5. pytest -vv
робробная информация о тестах

