### Toro Django Office

### Prerequisite & Dependencies
- Python `3.10`
- MySQL `8`

## Install pip packages:
```bash
pip install -r requirements.txt
```

## Database
```mysql
CREATE DATABASE <database-name> CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
```

## Configuration
- Clone .env.sample and rename it to .env
- Modify the environment variables name in .env to match your setup.

## Migration
```bash
python manage.py migrate
```

## Create a super admin user
```bash
python manage.py createsuperuser
```

## Start Django app
```bash
python manage.py runserver 8000
```
