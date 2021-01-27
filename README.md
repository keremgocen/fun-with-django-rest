# fun-with-django-rest
A REST API endpoint example using Django

### Exposed endpoints
```
customers/ # used to view and create user pin_code values
api/customer_login/ # used to valued user pin_code values
````

### Running it locally
```
# Python 3
$ pip3 install virtualenv
$ python3 -m venv env
$ source env/bin/activate

$ pip install -r requirements.txt

$ python ./manage.py migrate
$ python ./manage.py createsuperuser
$ python ./manage.py runserver
```

### Creating a user to validate pin_code

```
http://127.0.0.1:8000/admin -- Django Admin
or
http://127.0.0.1:8000/customers/ -- Web browsable API
```

### Using cURL locally to test api/customer_login endpoint
```
$ curl --location --request POST 'http://127.0.0.1:8000/api/customer_login/' \
--form 'pin_code="00000"'
```
