import os
import uvicorn
from fastapi import FastAPI

from security_manager_api.v1.main import app as v1_app

security_manager = FastAPI()
security_manager.mount("/v1", v1_app)

PORT = int(os.getenv("B2W_SECURITYMANAGER_PORT", 80))

if __name__ == "__main__":
    uvicorn.run(
        "main:security_manager",
        port=PORT,
        reload=True,
        host="0.0.0.0",
        root_path="/api/security-manager",
    )
