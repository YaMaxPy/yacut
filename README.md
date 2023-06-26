# Проект YaCut

## Описание

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

### Запуск приложения:
1. Склонируйте репозиторий:

```
git clone git@github.com:YaMaxPy/yacut.git
```

2. Перейдите в директорию с проектом:

```
cd yacut
```

3. Создайте и активируйте вирутальное окружение:

```
python -m venv venv
```
```
Если у вас Linux/macOS: source venv/bin/activate
Если у вас Windows: source venv/Scripts/activate
```

4. Установите зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

5. Создайте в корневой директории файл .env со следующим наполнением:

```
FLASK_APP=yacut
FLASK_ENV=development или production
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=<ваш_секретный_ключ>
```

6. Создать базу данных и выполнить миграции:

```
flask db upgrade
```

### Управление:
Для локального запуска выполните команду:
```
flask run
```
Сервис будет запущен и доступен по следующим адресам:
- http://localhost/ - главная страница сервиса;

    * Если не заполнить поле для короткой ссылки, она будет сгенерирована автоматически.
    * Короткая ссылка должна быть не длиннее 16 символов (цифры и латинские буквы в любом регистре).

### Работа с API:
- http://localhost/api/id/ - эндпоинт, принимающий POST-запросы;

    * Схема POST-запроса:
        ```json
        {
        "url": "string",
        "custom_id": "string" * (необязательное поле)
        }
        ```
    * Схема ответа на POST-запрос:
        ```json
        {
        "url": "string",
        "short_link": "string"
        }
        ```

- http://localhost/api/id/short_id/ - эндпоинт, принимающий GET-запросы.
    
    В адресе вместо <short_id> должна быть указана введённая или сгенерированная короткая ссылка.

    * Схема ответа на GET-запрос:
        ```json
        {
        "url": "string"
        }
        ```

Полная спецификация API доступна в репозитории - файл openapi.yml

#### Ключевые технологии и библиотеки:
- [Python](https://www.python.org/);
- [Flask](https://pypi.org/project/Flask/);
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/);

#### Автор
- [Радченко Максим](https://github.com/YaMaxPy "GitHub аккаунт")