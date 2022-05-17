from logging import Logger
from typing import Dict, List

from sqlalchemy.sql.elements import and_, or_

# use get_filter_payload like payload_filter=get_filter_payload(filters,table), query.filter(*payload_filters)
# table must be db_instance.Base.classes["products_structure"]

FILTER_OPERATORS: Dict[str, str] = {
    "=": "__eq__",
    "!=": "__ne__",
    "<": "__lt__",
    "<=": "__le__",
    ">": "__gt__",
    ">=": "__ge__",
    "like": "like",
    "notLike": "notlike",
    "in": "in_",
    "notIn": "notin_",
    "between_and": "between",
    "ilike": "ilike",
    "notilike": "notilike",
}
INTRA_FILTER_OPERATORS = {
    "=": "or",
    "!=": "and",
    "<": "or",
    "<=": "or",
    ">": "or",
    ">=": "or",
    "like": "or",
    "notLike": "and",
    "in": "or",
    "notIn": "and",
    "between_and": "or",
    "ilike": "or",
    "notilike": "and",
}


def is_valid_sql(sql_text: any) -> bool:
    """
    Check if is valid SQL statement
    :param sql_text: str (Part of SQL statement)
    :return: bool (True if it is valid, False Otherwise)
    """
    SQL_NOT_ALLOWED_STATEMENTS = [
        "select",
        "from",
        "join",
        "set",
        "on",
        ";",
        "drop",
        "where",
        "*",
    ]

    if isinstance(sql_text, list):
        for sql in sql_text:
            if isinstance(sql, list):
                for entry in sql:
                    entry = entry.lower()
                    if any(x in sql for x in SQL_NOT_ALLOWED_STATEMENTS):
                        return False
            else:
                if isinstance(sql, str):
                    sql = sql.lower()
                if sql in SQL_NOT_ALLOWED_STATEMENTS:
                    return False
    elif isinstance(sql_text, str):
        sql_text = sql_text.lower()
        if any(x in sql_text for x in SQL_NOT_ALLOWED_STATEMENTS):
            return False

    return True


def get_filter_payload(filters, table):
    condition: List = []
    if filters is not None:
        for current_filter in filters:
            filter_field = current_filter.key
            filter_op = current_filter.operator
            filter_value = current_filter.value.lower()
            if hasattr(table, filter_field) and filter_op in FILTER_OPERATORS.keys():
                if is_valid_sql(filter_value):
                    eligibility_criteria_items_column = getattr(table, filter_field)
                    filter_function = getattr(
                        eligibility_criteria_items_column,
                        FILTER_OPERATORS[filter_op],
                    )
                    if (
                        hasattr(eligibility_criteria_items_column.type, "enums")
                        and FILTER_OPERATORS[filter_op] == FILTER_OPERATORS["="]
                    ):
                        possible_values = eligibility_criteria_items_column.type.enums
                        if filter_value not in possible_values:
                            Logger.warning(
                                "value `{value}` for field '{filter_field}' is not a valid enum, available values {possible_values}".format(
                                    value=filter_value,
                                    filter_field=filter_field,
                                    possible_values=possible_values,
                                )
                            )
                            raise ValueError(
                                "value `{value}` for field '{filter_field}' is not a valid enum, available values {possible_values}".format(
                                    value=filter_value,
                                    filter_field=filter_field,
                                    possible_values=possible_values,
                                )
                            )
                    if (
                        FILTER_OPERATORS[filter_op] == FILTER_OPERATORS["in"]
                        or FILTER_OPERATORS[filter_op] == FILTER_OPERATORS["notIn"]
                    ):
                        if not isinstance(filter_value, list):
                            filter_value = [filter_value]
                        condition.append(filter_function(filter_value))
                    else:
                        if isinstance(filter_value, list):
                            sub_condition: List = []
                            for value in filter_value:
                                if (
                                    FILTER_OPERATORS[filter_op]
                                    == FILTER_OPERATORS["like"]
                                    or FILTER_OPERATORS[filter_op]
                                    == FILTER_OPERATORS["notLike"]
                                    or FILTER_OPERATORS[filter_op]
                                    == FILTER_OPERATORS["ilike"]
                                    or FILTER_OPERATORS[filter_op]
                                    == FILTER_OPERATORS["notilike"]
                                ):
                                    value = "%" + value + "%"
                                if FILTER_OPERATORS[filter_op] == FILTER_OPERATORS[
                                    "between_and"
                                ] and isinstance(value, list):
                                    sub_condition.append(filter_function(*value))
                                else:
                                    sub_condition.append(filter_function(value))
                            if len(sub_condition) == 1:
                                condition.append(*sub_condition)
                            elif INTRA_FILTER_OPERATORS[filter_op] == "and":
                                condition.append(and_(*sub_condition))
                            elif INTRA_FILTER_OPERATORS[filter_op] == "or":
                                condition.append(or_(*sub_condition))
                        else:
                            if (
                                FILTER_OPERATORS[filter_op] == FILTER_OPERATORS["like"]
                                or FILTER_OPERATORS[filter_op]
                                == FILTER_OPERATORS["notLike"]
                                or FILTER_OPERATORS[filter_op]
                                == FILTER_OPERATORS["ilike"]
                                or FILTER_OPERATORS[filter_op]
                                == FILTER_OPERATORS["notilike"]
                            ):
                                filter_value = "%" + filter_value + "%"
                            condition.append(filter_function(filter_value))
                else:
                    raise ValueError(
                        # ERROR_LABELS["SQL_INJECTION_FIELD"].format(field="value")
                    )
            else:
                raise ValueError(
                    # ERROR_LABELS["TABLE_DO_NOT_HAVE_COLUMN"].format(
                    #    table=TableEnums.COUPON_TABLE, column=filter_field
                    # )
                )
    return condition
