import os

from b2wcache import Cache
from .settings import CACHE_PARAMS

cache = Cache(**CACHE_PARAMS)


os.environ["b2w_dbi_location"] = f"{__package__}.db"
os.environ["b2w_dbi_varname"] = "db_instance"
