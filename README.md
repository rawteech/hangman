# HANGMAN API
This is the API part of the hangman game

## Setup
To get up and running clone the project first then follow the steps below:

* Create a virtual environment for the project and activate
```
$ virtualenv -p python3 hangman
$ source ./hangman/bin/activate
```

* Install the requirements
```
pip install -r requirements.txt
```

* Rename the `.env.example` to `.env`

* Generate a [secrete key](https://www.miniwebtool.com/django-secret-key-generator/) and paste it into the `SECRET_KEY` variable in the `.env` file

* Run the migrations
```
./manage.py migrate
```

* Create a superuser
```
./manage.py createsuperuser
```

* Finally start the development server
```
./manage.py runserver
```

* Follow the instructions in this repo to setup the User Interface

