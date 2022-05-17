from typing import Dict, List


class Constants:
    AUTHORIZATION_HEADER_NAME = "X-Auth-Request-Access-Token"
    GENERIC_EXCEPTION_FORMAT: str = "Exception: {e}"
    CLONED_SUFFIX: str = "_Cloned_"
    PRODUCT_MAPPING_NAME: str = "product_mapping"
    EXCLUDED_COLUMN_PRODUCT: List[str] = [
        "guid",
        "created_date",
        "updated_date",
        "system_record",
        "code",
    ]

    """
    = - displays only rows with data that is the same as the filter
    != - displays rows with a value that is not equal to the filter value
    < - displays rows with a value less than the filter value
    <= - displays rows with a value less than or qual to the filter value
    > - displays rows with a value greater than the filter value
    >= - displays rows with a value greater than or qual to the filter value
    like - displays any rows with data that contains the specified string anywhere in the specified field. (case insensitive)
    in - displays any rows with a value in the filter value array passed to the filter
    """
    FILTER_OPERATORS: Dict[str, str] = {
        "=": "__eq__",
        "!=": "__ne__",
        "<": "__lt__",
        "<=": "__le__",
        ">": "__gt__",
        ">=": "__ge__",
        "like": "like",
        "in": "in_",
    }
    ASC_SORTER: str = "asc"
    DESC_SORTER: str = "desc"
    VALID_SORTERS: List[str] = [ASC_SORTER, DESC_SORTER]
    REGEX_EXPR_INPUT: str = "^[a-zA-Z0-9_-]*$"
    REGEX_EXPR_PATTERN: str = "^[a-zA-Z0-9.*_@#-]*$"

    def __init__(self, _: str, description: str):
        self.description = description
