## Use this project

```
git clone git@github.com:makan-dianka/wplogin.git

cd wplogin
```

 ## Create dotenv file

```
sudo nano .env
```

add those env variables

```
EMAIL_HOST_USER="gmail"
EMAIL_HOST_PASSWORD="gmail token"

RECIPIENT="recipient email"

DEBUG=0

ALLOWED_HOSTS="192.168.1.42,127.0.0.1"
```

## Create conf.json file

```
sudo nano conf.json
```

add those values

```
TARGET_URL=
```

## create virtualenv and activate

```
python -m venv .venv

. .venv/bin/activate
```

## Install dependencies

```
pip install --upgrade pip

pip install -r requirements.txt
```


## Run server

```python manage.py runserver```

## Go to webpage

127.0.0.1:8000/wp-login
