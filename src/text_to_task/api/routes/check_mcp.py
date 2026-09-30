from fastapi import APIRouter
from pydantic import BaseModel

from text_to_task.api.handler.check_mcp import check_mcp_handler

class CheckMCPRequest(BaseModel):
    text: str

router = APIRouter(prefix="/check-mcp")

@router.post("")
async def check_mcp(request: CheckMCPRequest):
    response = await check_mcp_handler(request.text)
    return {"message": response}