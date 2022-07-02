## Проект тестового задания для приема на работу в ОО Айтек
Для запуска и настройки понадобится:

> - python 3.8+
> - Соединение с интернетом
> - руки хоть чуточку прямее моих
> - docker (Опционально)

Прежде чем начать, склонируйте проект:
```shell
git clone git@github.com:artur1214/aitech_tz.git
cd aitech_tz
```

## Как запускать?
Для начала необходимо создать .env файл в корне проекта. 
Содержимое .env файла можно взять из .env.sample, который уже есть в репозитории

Думаю, по названию переменных и так понятно, какая за что отвечает.


Теперь проект необходимо запустить:
### DOCKER:
При работе в docker вам нужно лишь запустить docker-compose.
```shell
docker-compose build
docker-compose up
```
Докер автоматически сделает миграции и установит зависимости.
Изменения в проекте так же автоматически подтянутся в docker.

Запускать `docker-compose build` нужно будет только в случае изменений в static
файлах и в случае изменения списка зависимостей.

Перезапускать контейнер (`docker-composer up`) нужно при изменении .env файла и изменении структуры БД,
потому что миграции выполняются только при запуске контейнера (не делать же их при каждом
малейшем изменении кода)

**Примечание:** Вместе с приложением поднимается контейнер postgres. В env файле
для подключения к БД (раз вы работаете с docker'ом) используйте
`DB_HOST=tz_postgres`

**Еще одно примечание:** В docker запускается только контейнер с postgres.
Если вы хотите использовать mysql, настраивать подключение к нему вам нужно будет самостоятельно 
(можно использовать любую удаленную БД MySQL или самостоятельно поднять и настроить подключение в docker контейнер)

После того как все запущенно, приложение будет доступно по 
`http://localhost:5000`

### NO DOCKER:
Первым делом необходимо установить зависимости 
(Предварительно советую создать виртуальную среду)

```shell
pip install -r requirements.txt
```
Теперь переходим в папку приложения (папка `app`)

И запускаем миграции:
```shell
python manage.py makemigrations
python manage.py migrate
```

Не забудьте, что ничего не получится, если вы неправильно указали данные для
подключения к базе. 

В таком режиме работы, я бы советовал использовать `sqlite` в качестве типа БД
(название файла БД sqlite3 все также нужно будет указать в переменной окружения `DB_NAME`, или удалить эту переменную, тогда по умолчанию будет `db1.sqlite`)

Теперь остается лишь запустить проект:

```shell
python manage.py runserver 0.0.0.0:5000
``` 
После того как все запущенно, приложение будет доступно по 
`http://localhost:5000`
(Порт вы можете выбрать самостоятельно)

## Тесты

Для приложения написано несколько простых тестов (в `app/core/tests.py`) 

Для их запуска вам нужно запустить команду 
```shell
python manage.py test
```
Однако это сработает, только если вы настраивали проект без docker'a. Если же
вы хотите запустить тесты с docker'ом, то вам нужно сделать это внутри самого контейнера:

```shell
docker exer -it tz-app /bin/bash
```
И теперь, уже внутри самого контейнера нужно запустить тесты:
```shell
python manage.py test
```

## OpenAPI

При запуске в debug режиме (Переменная окружения `DEBUG=1`) Вам кроме основных URL
будут так же доступны url для получения автоматически сгенерированной openAPI схемы.

 http://localhost:5000/api/schema/ - YAML 

 http://localhost:5000/api/schema/swagger-ui/ - swagger-ui

http://localhost:5000/api/schema/redoc/ - Документация

**Примечание:** Если вы изменили порт запуска, не забудьте поменять и здесь :)

## По всем вопросам:
https://vk.com/avartur92
