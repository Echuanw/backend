from fastapi import APIRouter, Query, Body, status, HTTPException
from typing import Annotated
from app.models.database import SessionDep
import app.models.schemas as schemas
import app.models.crud as crud
api_position = APIRouter()

# 1. 获取所有岗位信息
@api_position.get('/', response_model=list[schemas.PositionOut]) 
async def get_position(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    """
    获取所有岗位信息
    """
    return crud.get_position(session, offset, limit)

# 2. 创建一个岗位
@api_position.post(
    '/', 
    response_model=schemas.PositionIn, 
    status_code=status.HTTP_200_OK,
    summary="Create an position", 
	description="Create an position with all info, it will failure when position_name already exists"
) 
async def create_position(
    session: SessionDep,
    position: Annotated[schemas.PositionIn, Body(
            examples = [{
                "position_name": "Project Manager",
                "description": "研发部 - 产品经理",
                "department": "Research and Development",
            }]
        )]
):
    """
    POST /position/    创建一个新的岗位
    """
    db_record = crud.create_position(session, position)
    if db_record is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Position already exists.")
    return db_record


# 3. 更新一个岗位
@api_position.put('/{position_id}') 
async def update_position(
    session: SessionDep,
    position_id: str,     
    position: Annotated[schemas.PositionIn, Body(
            examples = [{
                "position_name": "Project Manager",
                "description": "研发部 - 产品经理",
                "department": "Research and Development",
            }]
        )]):
    """
    PUT /position/{position_id}    更新指定岗位的信息
    """
    print(position_id)
    print(position)
    db_record = crud.update_position(session, position_id, position)
    if db_record is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Position not exists.")
    return db_record

# 4. 删除一个岗位
@api_position.delete('/{position_id}') 
async def del_position(
    session: SessionDep,
    position_id: str     
):
    """
    DELETE /position/{position_id}    删除指定的岗位
    """
    db_record = crud.delete_position(session, position_id)
    if db_record is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Position not exists.")
    return db_record