### Описание:
API для "социальной сети YaTube".
### Установка:
Клонировать репозиторий и перейти в него в командной строке:
- git clone https://github.com/yandex-praktikum/api_final_yatube.git

Cоздать и активировать виртуальное окружение:
- python3 -m venv venv source venv/bin/activate

Установить зависимости из файла requirements.txt:
- python3 -m pip install --upgrade pip pip install -r requirements.txt

Выполнить миграции:
- python3 manage.py migrate

Запустить проект:
- python3 manage.py runserver

### Примеры: 
- смотреть redoc.yaml
