# REST API для YATUBE

### Описание

Сервис выполняет CRUD-операции со всеми эндпоинтами модели Yatube.

### Функционал

- Создание, редактирование и удаление записи.
- Подписка, отписка на автора.
- Создание, редактирование и удаление комментариев.
- Добавление публикации к группе.
- Фильтрация по группам, подпискам и поиск.
- Авторизация по JWT-токенам (Djoser).
- Доступна документация.

### Стек
 Python, Django, DRF, Djoser, Sqlite3

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/kristina-pachi/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Script/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры

GET http://127.0.0.1:8000/api/v1/posts/

Получит все посты из базы данных

Пример ответа:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

Получит все комментарии по определенному посту

Пример ответа:
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
POST http://127.0.0.1:8000/api/v1/posts/

Создание поста

Пример REQUEST BODY:

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Пример ответа:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
