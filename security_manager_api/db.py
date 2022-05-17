import sys

from b2worm.db import B2WOrm

from .settings import DATABASES

if "pytest" in sys.modules:
    db_instance = B2WOrm(
        test=True,
        engine={"connect_args": {"check_same_thread": False}},
        **DATABASES["test"]
    )
else:
    db_instance = B2WOrm(**DATABASES["postgres"])
