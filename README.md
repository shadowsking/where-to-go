# where-to-go

[Интерактивная карта Москвы](https://gowheretogo.pythonanywhere.com/) с известными видами активного отдыха.


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

Соберите статические файлы
```bash
python manage.py collectstatic
```

Создайте админа
```bash
python manage.py createsuperuser
```

Запустите сервер
```bash
python manage.py runserver
```

Добавление локации
```bash
python manage.py load_place <URL>.json
```

JSON файл имеет следующую струкутуру:
```
{
    "title": "Останкинская телебашня",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e3b20361050ae13b3aaf7ddcef76e7c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/adc544d7acc9be889cfec73064bcfb06.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6338bf58897bb4bef5c6ef1483c357de.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e5efbafdfc29423e361df0ee81145b7.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/99c1cb7ba5ccf948767524876edf27c8.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/67b694871a431460745668d686770f54.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/e6ef6f4f3a7df07cb8881d4ed0c44b6e.jpg"
    ],
    "description_short": "Останкинская телебашня — одна из главных достопримечательностей Москвы и символ отечественного  телерадиовещания. Здесь проводятся экскурсии с подъёмом на высоту более трёхсот метров, а уникальный мультимедийный комплекс знакомит посетителей с устройством этого удивительного сооружения. ",
    "description_long": "<p>За последнее время внутри башни многое изменилось. Теперь это не только главная точка  телерадиовещания  в стране, но и туристический комплекс, побывать в котором может любой желающий.</p><p>На экскурсиях посетители познакомятся с историей строительства этого чуда инженерной мысли и смогут узнать, с какими сложностями пришлось столкнуться его создателям. В башне устроен интерактивный мультимедийный комплекс, в который также можно попасть во время экскурсии. Здесь гости услышат о технологических особенностях башни, познакомятся с «квакшами» и картой гроз в Москве. Оказывается, башня умеет петь и танцевать, а её шпиль значительно отклоняется под порывами ветра. За этими отклонениями можно будет проследить в реальном времени. Участники экскурсии выяснят, почему башня не падает, и поучаствуют в формировании рейтинга своего любимого телеканала.</p><p>Также для посещения доступна площадка на высоте 85 метров, где видно все 145 тросов, придающих башне гибкость и устойчивость. А с площадки на высоте 337 метров можно полюбоваться на панораму Москвы. Гостей ждёт и легендарный ресторан «Седьмое небо». Его полы вращаются, описывая полный оборот за 50 минут.</p><p>Узнать подробности можно на <a class=\"external-link\" href=\"https://www.tvtower.ru/\" target=\"_blank\">официальном сайте</a>, <a class=\"external-link\" href=\"https://vk.com/tv_tower\" target=\"_blank\">ВКонтакте</a> и в <a class=\"external-link\" href=\"https://www.instagram.com/ostankino_tvtower/\" target=\"_blank\">Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.61171499999998",
        "lat": "55.81972699999998"
    }
}
```


## Переменные окружения
- DEBUG — [режим отладки](https://docs.djangoproject.com/en/3.1/ref/settings/#debug)
- SECRET_KEY — [секретный ключ проекта ](https://docs.djangoproject.com/en/3.1/ref/settings/#secret-key)
- DATABASE_FILEPATH — путь к файлу базы данных SQLite
- ALLOWED_HOSTS — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
