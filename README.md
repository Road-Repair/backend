### Как запустить проект:

Клонировать проект
```
git clone https://github.com/Road-Repair/backend.git
```

Переименовать файл .env.example и изменить содержимое на актуальные данные.
```
mv .env.example .env
```

Запустить контейнер c проектом
```
docker-compose up -d
```

Выполнить миграции:
```
docker-compose exec backend python manage.py migrate
```

# Проект будет доступен на 8000 порту.

# Swager доступен по адресу:
```
http://localhost:8000/api/v1/docs/
```

Если отсутствуют статические файлы, то выполнить
```
docker-compose exec backend python manage.py collectstatic --no-input
```
