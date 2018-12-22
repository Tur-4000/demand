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

*Добавить:*
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

*Закомментировать:* 
STATICFILES_DIRS
```
python3 manage.py collectstatic
```
На этом этапе можно запуститься в **dev** режиме 
```
python3 manage.py runserver 0.0.0.0:8000
```

### Настройка gunicorn
Проверить, что gunicorn установился корректно можно командой из виртуального окружения
```
gunicorn --bind 0.0.0.0:8000 config.wsgi
```
Дальше настраиваем от суперюзера

Создаём файл `gunicorn.service`
```
sudo vim /etc/systemd/system/gunicorn.service
```
Пишем
```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=demand
Group=www-data
WorkingDirectory=/home/demand/demand
ExecStart=/home/demand/demand/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/demand/demand/demand.sock config.wsgi:application

[Install]
WantedBy=multi-user.target
```
Дальше
```
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```
Проверяем
```
sudo systemctl status gunicorn
sudo journalctl -u gunicorn
```
Рестартуем
```
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```

### Настройка Nginx
Создаём конфиг
```
sudo nano /etc/nginx/sites-available/demand
```
```
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/demand/demand;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/demand/demand/demand.sock;
    }
}
```
Подключаем наш конфиг
```
sudo ln -s /etc/nginx/sites-available/demand /etc/nginx/sites-enabled
```
Проверяем и перезапускаем
```
sudo nginx -t
sudo systemctl restart nginx
```
Пользуемся!!!