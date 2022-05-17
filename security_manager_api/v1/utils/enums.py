# COMMON ENUMS
# COMMON ENUMS


class TableEnums:
    PRODUCT_MANAGER_TABLE = "product_manager"
    CATALOG_STRUCTURE_TABLE = "catalog_structure"
    CATALOG_TABLE = "catalogs"
    SALES_CONFIGURATION_TABLE = "sales_configuration_tags"
    FAMILIES_TABLE = "families"
    FAMILIES_ATTRIBUTES_TABLE = "families_attributes"
    DOMAINS_TABLE = "domains"
    ATTRIBUTES_TABLE = "attributes"
    PRODUCT_FAMILIES_TABLE = "products_families"
    PRICE_MODEL_PARAMETERS_TABLE = "price_model_parameters"

    def __init__(self, _: str, description: str):
        self.description = description
