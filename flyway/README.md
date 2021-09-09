# Flyway

A pure SQL and command-line utility from the JVM world

Docs: https://flywaydb.org/documentation/

### Setup

#### Create two postgres docker containers

See [docker-compose.yml](../docker-compose.yml).

```bash
> docker compose up -d
```

#### Create the `migra` schema in both containers

```bash
> psql -h localhost -p 5432 -U prod -W -d prod -c 'CREATE SCHEMA IF NOT EXISTS flyway;'
> psql -h localhost -p 5400 -U dev -W -d dev -c 'CREATE SCHEMA IF NOT EXISTS flyway;'
```

### Installation

```bash
> brew install flyway
```

### Configuration

In the project's  home directory, create a file `flyway/flyway.conf` and enter the following content:
```properties
flyway.driver=org.postgresql.Driver
flyway.user=prod
flyway.password=prod
flyway.url=jdbc:postgresql://localhost:5432/prod
flyway.locations=filesystem:flyway/migrations
flyway.schemas=flyway
flyway.validateOnMigrate=true
```

### Create versioned migration scripts

Filename must follow this pattern: `V{number}_{description}.sql`

The versioned migrations must be listed in increasing order, e.g., :

* `V0001_create_person_table.sql` (gets executed first)
* `V0002_create_address_table.sql` (gets executed second)
* `V0003_create_person_read_view.sql` (gets executed third)

A popular versioning scheme is to use a timestamp: `V20210909090236__create_person_table.sql`

### Execute the migrations

You can execute the migrations with the following command

```bash
flyway -configFiles="./flyway/flyway.conf" migrate
```

### Bonus: Repeatable migrations

These can be used to add test data, temporary tables, etc.

```bash
 > flyway -configFiles="./flyway/flyway.conf" -locations="flyway/test-migrations" migrate
```

#### Clean up docker containers

```bash
> docker compose down -v
```