from sqlalchemy import Table
from b2worm import db_instance
from ..utils.enums import TableEnums


def get_catalog_structure_table() -> Table:
    return db_instance.Base.classes[TableEnums.CATALOG_STRUCTURE_TABLE]


def get_catalog_table() -> Table:
    return db_instance.Base.classes[TableEnums.CATALOG_TABLE]


def get_sales_configuration_tags_table() -> Table:
    return db_instance.Base.classes[TableEnums.SALES_CONFIGURATION_TABLE]


def get_families_table() -> Table:
    return db_instance.Base.classes[TableEnums.FAMILIES_TABLE]


def get_families_attributes_table() -> Table:
    return db_instance.Base.classes[TableEnums.FAMILIES_ATTRIBUTES_TABLE]


def get_attributes_table() -> Table:
    return db_instance.Base.classes[TableEnums.ATTRIBUTES_TABLE]


def get_domains_table() -> Table:
    return db_instance.Base.classes[TableEnums.DOMAINS_TABLE]


def get_products_families_table() -> Table:
    return db_instance.Base.classes[TableEnums.PRODUCT_FAMILIES_TABLE]


def get_price_model_parameters_table() -> Table:
    return db_instance.Base.classes[TableEnums.PRICE_MODEL_PARAMETERS_TABLE]
