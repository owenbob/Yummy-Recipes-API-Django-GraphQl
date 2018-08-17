# Yummy-Recipes-API-Django-GraphQl

[![Build Status](https://travis-ci.org/owenbob/Yummy-Recipes-API-Django-GraphQl.svg?branch=master)](https://travis-ci.org/owenbob/Yummy-Recipes-API-Django-GraphQl)

## Product overview 
 Yummy-Recipes-API-Django-GraphQl is a simple  API built with  Django and GraphQl.  Enables you to register a user,login. It aslo provides CRUD functionality for categories and recipes assigned to these categories. 

## Development set up
- Check that python 3, pip, virtualenv and postgres are installed

- Clone  Yummy-Recipes-API-Django-GraphQl  repo and cd into it
    ```
    git clone https://github.com/owenbob/Yummy-Recipes-API-Django-GraphQl.git
    ```
- Create virtual env
    ```
    virtualenv --python=python3 venv
    ```
- Activate virtual env
    ```
    source venv/bin/activate
    ```
- Install dependencies
    ```
    cd YummyRecipesApi
    ```
    ```
    pip install -r requirements.txt
    ```
- Create Application environment variables and save them in .env file
    ```
    export DBNAME='Your Database name'
    export DBPASSWORD='Your Database password'
    export DBUSER='Your Database user'
    ```
- Run command
    ```
    source .env
    ```
- Running migrations

     ```
     python manage.py migrate api
    ```
- Run application.
    ```
    python manage.py runserver
    ```

## Built with 
- Python version  3
- Django
- Graphql(Graphene)
- Postgres






