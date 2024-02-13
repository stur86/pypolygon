"""Utility functions for the pypolygon package."""


def snake_to_camel(s: str) -> str:
    """Convert a snake_case string to a camelCase string.

    Args:
        s (str): The snake_case string.

    Returns:
        str: The camelCase string.
    """

    tokens = s.split("_")
    return tokens[0] + "".join(token.title() for token in tokens[1:])


def camel_to_snake(s: str) -> str:
    """Convert a camelCase string to a snake_case string.

    Args:
        s (str): The camelCase string.

    Returns:
        str: The snake_case string.
    """

    return "".join(["_" + c.lower() if c.isupper() else c for c in s]).lstrip("_")


def arg_to_urlparam(s: str) -> str:
    """Convert an input argument name to a URL parameter name.
    This changes range_from to from and range_to to to, since
    from is a reserved keywords in Python.

    Args:
        s (str): The input argument name.

    Returns:
        str: The URL parameter name.
    """

    # Special exception for keywords "from" and "to" since
    # "from" is a reserved keyword in Python
    if s == "range_from":
        return "from"
    if s == "range_to":
        return "to"
    return snake_to_camel(s)


def urlparam_to_arg(s: str) -> str:
    """Convert a URL parameter name to an input argument name.
    This changes from to range_from and to to range_to, since
    from is a reserved keywords in Python.

    Args:
        s (str): The URL parameter name.

    Returns:
        str: The input argument name.
    """

    # Special exception for keywords "from" and "to" since
    # "from" is a reserved keyword in Python
    s = camel_to_snake(s)
    if s == "from":
        return "range_from"
    if s == "to":
        return "range_to"
    return s
