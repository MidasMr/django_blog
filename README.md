# django_blog

### Описание проетка:

```
django-blog - это проект-тестовое задание простого блога.
```

### Установка:

Клонировать репозиторий и перейти в него:

```
git@github.com:MidasMr/django_blog.git
```

```
cd django_blog
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
Windows
source venv/Scripts/activate
Linux, Mac OS
source venv/bin/activate
```

Обновить pip до последней версии
```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

### Шаблон заполненния .env файла
```
SECRET_KEY= <Секретный ключ django>
```

### Запуск приложения

Запуск backend django

Перейти в директорию
```
cd backend/django_blog
```

Теперь нужно последовательно выполнить команды:

Выполняем миграции
```
python manage.py migrate
```

Создаем суперпользователя
```
python manage.py createsuperuser
```

Запускаем dev сервер
```
python manage.py runserver
```

Запуск frontend vue:

Создаем новое окно терминала

Переходим в директорию с проектом

Переходим в директорию с frontend vue

```
cd frontend
```

Setup vue
```
npm install
```

Запустить приложение в dev режиме
```
npm run serve
```

Перейти в браузере по ссылке
```
http://localhost:8080/ 
```