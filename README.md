# Neil
![neil-the-seal][neil the seal image]
A simple tool to handle MariaDB queries and reduce friction when interacting with query results.

## NOTES

1. This project is in its early stages and likely has bugs or issues.
2. This relies on the Python MariaDB connector version less than 2.0, thus does not have any asynchronous features.

## Prerequisites

You will need the [MariaDB Connector C][mariadb-connector-c] library in order to use this library. Please use the install guide for your machines.

## Installing

To quickly install to your machine using UV, use the following command.

```bash
uv add git+https://github.com/avgra3/neil-mariadb.git@main
```

If you are using Pip, use the command below.

```bash
pip install --upgrade  git+https://github.com/avgra3/neil-mariadb.git@main
```

## Features
### SQL Cleaning
Before running any SQL, all commented lines are removed in order to prevent accidental running of invalid SQL.

### Errors
Errors are handled with a `NeilError` object which contains essentially the MariaDB errors which normally come as a tuple, as a usable object broken into the error message, SQL state, and error number which corresponds to what the MariaDB database would return to the user.

### Results
Result objects that gives back the sql statement ran, updated rows, returned data (if any), metadata, warnings, and errors.

### Config
A reusable object that allows the user to ensure they included needed parameters to connect to their database.

### Connection Pooling
Creates a connection pool to reduce the overhead of creating connections when running many queries sequentially.

If you have more than one connection in your pool, you could run many queries concurrently with your `NeilPool` object.

## Documentation

1. [Examples](./docs/examples.md)

## Name Inspiration
The name for this project comes from [Neil the Seal][Neil the Seal wiki].

## Attributions
The image for Neil comes from this [article][neil-the-seal-attr] from the New York Times.

<!-- References -->
[Neil the Seal wiki]: https://en.wikipedia.org/wiki/Neil_the_Seal
[Neil the Seal image]: ./static/neil-the-seal.png
[neil-the-seal-attr]: https://www.nytimes.com/2026/07/10/world/australia/neil-seal-australia-tasmania.html?smid=url-share
[mariadb-connector-c]: https://mariadb.com/docs/connectors/mariadb-connector-c/install-mariadb-connector-c
