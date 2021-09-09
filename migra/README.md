# DEMO: `migra`

### Setup

#### Create two postgres docker containers

See [docker-compose.yml](../docker-compose.yml).

```bash
> docker compose up -d
```

#### Create the `migra` schema in both containers

```bash
> psql -h localhost -p 5432 -U prod -W -d prod -c 'CREATE SCHEMA IF NOT EXISTS migra;'
> psql -h localhost -p 5400 -U dev -W -d dev -c 'CREATE SCHEMA IF NOT EXISTS migra;'
```

#### Install `migra`

```bash
> python -m pip install migra[pg]
```

#### Create the development environment

```bash
> psql -h localhost -p 5400 -U dev -W -d dev -f migra/migra_base.sql
```

#### Generate the schema diff

```bash
> migra --schema migra postgresql://prod:prod@localhost:5432/prod postgresql://dev:dev@localhost:5400/dev > migra/migrate.sql
```

_CLEAN UP_ `migra/migration.py` as necessary

#### Apply the changes to the production server

```bash
> psql -h localhost -p 5432 -U prod -W -d prod -f migra/migrate.sql
```

#### Clean up docker containers

```bash
> docker compose down -v
```