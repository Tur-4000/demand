- создать пользователя demand
- в домашнем каталоге demand выполнить:
```git
git clone https://github.com/Tur-4000/demand.git
```
- обновить pip и установить virtualenv:
```
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
```
- в папке ~/demand создать виртуальное окружение:
```
virtualenv --python=python3 venv
```
- запустить виртуальное окружение
```
source venv/bin/activate
```
- установить зависимости:
```
pip3 install -r requirements-prod.txt
```
### Подготовить базу данных (postgres)
```
sudo -u -i postgres
psql
```
```postgresql
CREATE DATABASE demand;
CREATE USER demanduser WITH PASSWORD 'P@ssw0rd';
GRANT ALL PRIVILEGES ON DATABASE demand TO demanduser;
GRANT ALL ON DATABASE demand to "demanduser";
ALTER USER demanduser CREATEDB;
ALTER ROLE demanduser SET client_encoding TO 'utf8';
ALTER ROLE demanduser SET default_transaction_isolation TO 'read committed';
ALTER ROLE demanduser SET timezone TO 'UTC';
```
```
python3 manage.py migrate
python3 manage.py createsuperuser
```

### settings.py
Проверить параметры:

ALLOWED_HOSTS

DATABASES

**Статика**

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```
python3 manage.py collectstatic
```
На этом этапе можно запуститься в **dev** режиме 
```
python3 manage.py runserver 0.0.0.0:8000
```

### Настройка gunicorn

