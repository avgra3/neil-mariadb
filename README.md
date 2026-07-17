# Neil
![neil-the-seal][neil the seal image]
A simple tool to handle MariaDB queries and reduce friction when interacting with query results.

## NOTE

This project is in its early stages and likely has bugs or issues.

## Features
### Errors
Errors are handled with a `NeilError` object which contains essentially the MariaDB errors which normally come as a tuple, as a usable object broken into the error message, SQL state, and error number which corresponds to what the MariaDB database would return to the user.

### Results
Result objects that gives back the sql statement ran, updated rows, returned data (if any), metadata, warnings, and errors.

### Config
A reusable object that allows the user to ensure they included needed parameters to connect to their database.

### Connection Pooling
Creates a connection pool to reduce the overhead of creating connections when running many queries sequentially.

If you have more than one connection in your pool, you could run many queries concurrently with your `NeilPool` object.

## Name Inspiration
The name for this project comes from [Neil the Seal][Neil the Seal wiki].

## Attributions
The image for Neil comes from this [article][neil-the-seal-attr] from the New York Times.

<!-- References -->
[Neil the Seal wiki]: https://en.wikipedia.org/wiki/Neil_the_Seal
[Neil the Seal image]: ./static/neil-the-seal.png
[neil-the-seal-attr]: https://www.nytimes.com/2026/07/10/world/australia/neil-seal-australia-tasmania.html?smid=url-share
