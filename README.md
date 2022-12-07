# protest
technical test

### Requirements ###

* Python 3.8.15
* Postgres 12


### Enviroments ###

    # Database Postgres SQL 
    export DB_NAME=protest
    export DB_USER=admin
    export DB_PASSWORD=admin
    export DB_HOST=localhost
    export DB_PORT=5432

    # Configuration
    export ALLOWED_HOSTS=*
    
### Installation
    ### make a virtual enviroment ###
    virtualenv -p python3 venv
     source venv/bn/activate

    # Install RabbitMQ
    sudo apt-get install rabbitmq-server
    sudo apt-get install -y erlang

    # Check RabbitMQ is running
    service rabbitmq-server  status
    
    pip install -r requirements.txt
    

### Execute celery 
    Note: Eexecute in other terminal
    source venv/bin/activate
    source vars.sh
    celery -A protest worker -l INFO
