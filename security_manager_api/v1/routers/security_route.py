from b2wexceptions.models import responses
from b2worm.schema import get_session_local
from fastapi import APIRouter, Body, HTTPException
from fastapi.params import Header
from ..utils.constants import Constants
from ..models.exceptions import UpdateSecurityException
from keycloak.exceptions import KeycloakGetError
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from ..logger import get_logger
from ..service import security_service as service


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
    "/security",
    response_model_exclude_unset=True,
    responses={**responses},
)
def test(
    access_token: str = Header(None, alias=Constants.AUTHORIZATION_HEADER_NAME),
):
    try:
        response = service.get_security_info(access_token)
        return response
    except (UpdateSecurityException, KeycloakGetError) as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.post("/security", response_model_exclude_unset=True, responses={**responses})
def update_policies(
    access_token: str = Header(None, alias=Constants.AUTHORIZATION_HEADER_NAME),
    policies: dict = Body(...),
):
    try:
        response = service.update_policies(token=access_token, policies=policies)
        return JSONResponse(content=jsonable_encoder(response))
    except (UpdateSecurityException, KeycloakGetError) as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
