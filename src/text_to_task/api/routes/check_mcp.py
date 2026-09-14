from fastapi import APIRouter

router = APIRouter(prefix="/check-mcp")

@router.post("")
def check_mcp():
    return {"message": "Check MCP"}