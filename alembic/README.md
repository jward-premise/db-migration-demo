# Alembic Demo

#### Create two postgres docker containers

See [docker-compose.yml](../docker-compose.yml). 

```bash
> docker compose up -d
```

#### Create the `alembic` schema in both containers

```bash
> psql -h localhost -p 5432 -U prod -W -d prod -c 'CREATE SCHEMA IF NOT EXISTS alembic;'
> psql -h localhost -p 5400 -U dev -W -d dev -c 'CREATE SCHEMA IF NOT EXISTS alembic;'
```

### Installation 

```bash
> python -m pip install alembic sqlalchemy psycopg2
```


### Create `alembic` folder

Create the migration directory and the `alembic.ini` configuration file.

```bash
> alembic init alembic
```

Adjust the `alembic.ini`, `env.py`, and `script.py.mako` as necessary for the project.

### Creating a migration file

Create a new migration file with the following:

```bash
> alembic revision -m "create person table"
```

This will produce a version file such as `./alembic/versions/20210908141253_08ebf4a91c1b_create_person_table.py`. In this file, entry the "upgrade" and "downgrade" logic.

### Execute migration

To advance to the most recent migration:
```bash
> alembic upgrade head
```

To undo the last two revisions:
```bash
> alembic downgrade -2
```

To upgrade one revision (if not already at head):
```bash
> alembic upgrade +1
```

To reset the database back to the beginning state:
```bash
> alembic downgrade base
```

#### Clean up docker containers

```bash
> docker compose down -v
```



