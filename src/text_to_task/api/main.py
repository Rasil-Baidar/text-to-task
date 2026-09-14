from fastapi import APIRouter
from text_to_task.api.routes import check_mcp


api_router = APIRouter(prefix="/api/v1")
api_router.include_router(check_mcp.router)