![Code Climate coverage](https://www.code-inspector.com/project/14447/score/svg) ![Code Climate coverage](https://www.code-inspector.com/project/14447/status/svg)

# Django-backend-template
A good start point (from my humble opinion) to init a wherever kind of Backend project in Django. This proof of concept includes:

* A template with all necessary structure for inits a complete and robust backend project. We can find:

  * Directory to manage and maintain errors and exception handlings.
  * Directory to manage and maintain enums for model usage.
  * Directory to manage and maintain routers (urls) by a model entity.
  * Directory to manage and maintain signals.
  * The same with controllers, models, and views.
  * Setting by environment for an easy configuration.
  * Different mechanisms of deploy [Docker and ZAPPA (https://github.com/Miserlou/Zappa)] to use.
* JWT authentication mechanism.
* A little model (Student) as an example.
* Swagger Doc (http://127.0.0.1:8000/swagger/)
* ReDoc (http://127.0.0.1:8000/redoc/)
* Django Rest Framework documentation (http://127.0.0.1:8000/docs/)


## Setup
1. Copy / clone repo from github.

        git clone https://github.com/adosaa/Backend-Django-App.git

2. If you already have the repo, pull the latest version

        git checkout master
        git pull

3. Create a virtualenv. Note: supporting Pyhton 3.8.

        virtualenv -p python3.8 [DESIRED-NAME]-env
        source [DESIRED-NAME]/bin/activate

4. Switch to the project root and install requirements.

        pip install -r requirements.txt

5. create in project/secrets folder a .env file with the follow env. variables:

        SECRET_KEY=<secret_key_to_election>
        DB_NAME=django.db.backends.sqlite3

6. Migrate Django datamodels

        $ ./manage.py migrate

7. For easy use, we recommend load the initial data with fixtures

        $ ./manage.py loaddata auth_user_fixture

    The credentials of this users is:
    ```bash
    username: fvera
    password: 6-r6jC&5CRk3S$qVv
    ```

## Run

#### Subsequent runs

```bash
$ ./manage.py runserver
```

### Run test

```bash
$ ./manage.py test project/apps
```

## Usage
