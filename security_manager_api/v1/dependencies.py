# Dependency
from b2worm.schema import get_session_local


def get_db():
    db = get_session_local()
    try:
        yield db
    finally:
        db.close()
