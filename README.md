# Vertebra Test
technical test

### Requirements ###

* Python 3.8.15
* Postgres 12
* rabbitmq-server


### Enviroments ###

    ### Database Postgres SQL ### 
    export DB_NAME=protest
    export DB_USER=admin
    export DB_PASSWORD=admin
    export DB_HOST=localhost
    export DB_PORT=5432

    # Configuration
    export ALLOWED_HOSTS=*
    export LOG_PATH='<str_path>/debug.log'
    export STATIC_ROOT='<str_path>/statics'
    export MEDIA_ROOT='<str_path>/media'
    
### Installation
    ### make a virtual enviroment ###
    virtualenv -p python3 venv
    source venv/bn/activate

    ### Install RabbitMQ ###
    sudo apt-get install rabbitmq-server
    sudo apt-get install -y erlang

    ### Check RabbitMQ is running ###
    service rabbitmq-server  status

    ### Install the requirements ###
    pip install -r requirements.txt
    

### Execute celery 
    Note: Eexecute in other terminal
    source venv/bin/activate

    ### Load enviroment ###
    source vars.sh

    ### Run celery ###
    celery -A protest worker -l INFO

### Migrate Database ###
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic

### Create User ####
    python manage.py createsuperuser
        - username: admin
        - password: admin
