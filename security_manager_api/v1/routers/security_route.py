from b2wexceptions.models import responses
from b2worm.schema import get_session_local
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session


from ..logger import get_logger


router = APIRouter()
logger = get_logger(__name__)


# Dependency
def get_db():
    db = get_session_local()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/test",
    response_model_exclude_unset=True,
    responses={**responses},
)
def test(session: Session = Depends(get_db)):
    return "OK"
