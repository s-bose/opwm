# OPWM

OPWM, or Offline Password Manager is a complete Dockerized offline application made using `PostgreSQL` database, `FastAPI` server and `VueJS` frontend, for managing password credentials for various websites and applications.

All login passwords (called `Master Password` in this context) are stored after getting hashed twice (once in the server, and finally in the database).

All passwords are encrypted using logged-in user's master password hash before storage.

All database-level encryption/decryption and hashing are done using the `PGCRYPTO` extension from `PostgreSQL`.



## Features

1. Fully integrated frontend 

![frontend](./static/frontend_first.png)

2. SwaggerUI documentation for the APIs.

![swaggerui](./static/swaggerui.png)


3. Can be accessed via database management tools such as `pgadmin`

![pgadmin](./static/pgadmin.png)


## Setup

After cloning the repository, generate the `SECRET_KEY` to be used for this
application (requires `openssl`) and save it to some file.

```
openssl rand -hex 30 > ~/.config/.opwm_config
```

Copy the `.env.example` to a new `.env` file and paste the `SECRET_KEY` into
its corresponding key.

```
cd /backend

cp .env.example .env
```

Optionally, you can change the port numbers for the FastAPI server, the database
and the Vue application by editing the `docker-compose.yml`.

By default, these are:
```
database - 5400
backend  - 8000
frontend - 3333
```

To connect to the container database, use the following URL.
```
psql postgresql://postgres:postgres@localhost:5400/opwm
```

## Note

- Please note that this is by no means a safe or secure implementation of password managers. There are other well-established software like `BitWarden` or `KeePassXC` which provide a much better solution. 
This was created just to teach myself and showcase the basic structure of 
an end-to-end password storage software. Use it at your own risk.


---


