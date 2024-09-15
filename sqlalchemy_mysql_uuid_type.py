from uuid import UUID

from sqlalchemy.types import BINARY, TypeDecorator


class UUIDColumn(TypeDecorator):
    """
    Custom SQLAlchemy column type for storing UUIDs.

    This type stores UUIDs as binary data (16 bytes) in the database and
    converts them to/from Python `UUID` objects when binding parameters or
    processing results. The representation of the UUID when retrieved can be
    controlled using the `as_string` parameter.

    :param length: The length of the binary data in bytes (default is 16).
    :type length: int
    :param as_string: Whether to return the UUID as a string when processing
                      results (default is `False`). If `False`, returns the UUID
                      as a `UUID` object.
    :type as_string: bool
    """
    impl = BINARY

    cache_ok = True

    def __init__(self, length=16, as_string=True, *args, **kwargs):
        """
        Initialize a UUIDColumn with a specific binary length and string representation option.

        :param length: The length of the binary column (default is 16).
        :type length: int
        :param as_string: Whether to return the UUID as a string when processing
                          results (default is `False`). If `False`, returns the UUID
                          as a `UUID` object.
        :type as_string: bool
        """
        self.length = length
        self.as_string = as_string

        super().__init__(length, *args, **kwargs)

    def process_bind_param(self, value, dialect):
        """
        Convert the Python UUID value to binary for storage in the database.

        :param value: The value to be bound to the database column. This can
                      be a `UUID` object, a string representation of a UUID,
                      or `None`.
        :type value: UUID or str or None
        :param dialect: The dialect in use (not used in this implementation).
        :type dialect: Dialect
        :return: The binary representation of the UUID or `None` if the value is `None`.
        :rtype: bytes or None
        :raises ValueError: If the value is neither a UUID nor a string representation of a UUID.
        """
        if isinstance(value, UUID):
            return value.bytes
        elif isinstance(value, str):
            return UUID(value).bytes
        elif value is None:
            return None
        else:
            raise ValueError(f"Invalid UUID value: {value}")

    def process_result_value(self, value, dialect):
        """
        Convert the binary data retrieved from the database to a Python UUID (string or object).

        :param value: The binary value from the database or `None`.
        :type value: bytes or None
        :param dialect: The dialect in use (not used in this implementation).
        :type dialect: Dialect
        :return: The UUID object as a string or `UUID` object based on `as_string` or `None` if the value is `None`.
        :rtype: str or UUID or None
        """
        if value is not None:
            uuid_obj = UUID(bytes=value)

            if self.as_string:
                return str(uuid_obj)

            return uuid_obj

        return None

    def copy(self, *args, **kwargs):
        """
        Create a copy of this UUIDColumn with the same parameters.

        :param kwargs: Additional keyword arguments to update (not used in this implementation).
        :return: A new instance of UUIDColumn with the same length and `as_string` setting.
        :rtype: UUIDColumn
        """
        return UUIDColumn(
            length=self.length, as_string=self.as_string, *args, **kwargs
        )
