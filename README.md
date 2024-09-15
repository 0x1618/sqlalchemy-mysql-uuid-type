# SQLAlchemy UUIDColumn

`UUIDColumn` is a custom column type for SQLAlchemy designed to simplify the storage and retrieval of UUIDs. It stores UUIDs efficiently as binary data and allows for flexible representation when reading from the database.

## Features

-   **Efficient Storage**: UUIDs are stored as binary data (16 bytes) in the database.
-   **Flexible Representation**: Option to retrieve UUIDs as either strings or `UUID` objects.
-   **Seamless Integration**: Easily integrates with SQLAlchemy models for straightforward usage.

## Installation

Ensure you have SQLAlchemy or Flask-SQLAlchemy installed. You can install them using pip:

```bash
pip install sqlalchemy
```

or

```bash
pip install flask-sqlalchemy
```

Include the `UUIDColumn` class in your project. If it's in a separate file (e.g., `sqlalchemy_mysql_uuid_type.py`), adjust the import statement in your code accordingly.

## Usage

### Define a Model with UUIDColumn

In your SQLAlchemy models, use `UUIDColumn` for UUID fields:

```python
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_mysql_uuid_type import UUIDColumn
from uuid import uuid4

db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = 'items'

    uuid = db.Column(UUIDColumn(), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
```

## `UUIDColumn` Class

The `UUIDColumn` class provides a custom SQLAlchemy column type for UUIDs with the following features:

-   **Parameters**:

    -   `length`: The length of the binary column (default is 16 bytes).
    -   `as_string`: Whether to return the UUID as a string when processing results (default is `False`).

-   **Methods**:
    -   `process_bind_param(value, dialect)`: Converts a Python `UUID` object or string to binary for storage.
    -   `process_result_value(value, dialect)`: Converts binary data from the database to a Python `UUID` object or string.
    -   `copy(**kwargs)`: Creates a copy of the `UUIDColumn` instance.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
