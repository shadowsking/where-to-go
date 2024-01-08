# where-to-go

Интерактивная карта Москвы с известными видами активного отдыха.


## Установка

Для запуска сайта необходимо установить python 3.10.

Скачайте код
```bash
git clone https://github.com/shadowsking/where-to-go.git
cd where-to-go
```

Создайте виртуальное окружение
```bash
python -m venv venv
source venv/scripts/activate
```

Установите зависимости
```bash
pip install -r requirements.txt
```

## Запуск
Создайте базу данных
```bash
python manage.py migrate
```

Запустите сервер
```bash
python manage.py runserver
```

## Переменные окружения
- DEBUG — [режим отладки](https://docs.djangoproject.com/en/3.1/ref/settings/#debug)
- SECRET_KEY — [секретный ключ проекта ](https://docs.djangoproject.com/en/3.1/ref/settings/#secret-key)
- DATABASE_FILEPATH — путь к файлу базы данных SQLite
- ALLOWED_HOSTS — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
