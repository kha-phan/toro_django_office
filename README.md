<h2> Toro Django Office </h2>

<p align="left">
    <a href="#">
        <img src="https://img.shields.io/badge/python-%3E=v3.10-brightgreen">
    </a>
</p>
<hr/>

### Prerequisite & Dependencies
- Python `3.10`
- MySQL `8`

## Install pip packages:
```bash
pip3 install -r requirements.txt
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
python3 manage.py migrate
```

## Create a super admin user
```bash
python3 manage.py createsuperuser
```

## Start Django app
```bash
python3 manage.py runserver 8000
```
