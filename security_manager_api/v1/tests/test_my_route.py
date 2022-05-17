# from requests import Response
# from starlette import status
from starlette.testclient import TestClient

from ..main import app

client = TestClient(app)
global INSERTED_UUID


# def test_example() -> None:
#     """
#     Example api unit test
#     """
#     response: Response = client.get("/example")
#     assert response.status_code == status.HTTP_200_OK
