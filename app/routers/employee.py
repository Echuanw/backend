from fastapi import APIRouter, Query, Body, status, HTTPException
from typing import Annotated
from app.models.database import SessionDep
import app.models.schemas as schemas
import app.models.crud as crud
api_employee = APIRouter()

# 员工管理

# 1. 创建员工
@api_employee.post(
    '/', 
    response_model=schemas.EmployeeIn, 
    status_code=status.HTTP_200_OK,
) 
async def create_employee(
    session: SessionDep,
    employee: Annotated[schemas.EmployeeIn, Body(
        examples = [{
            "name" : "张三",
            "username" : "zhangsan",
            "gender" : "M",
            "date_of_birth" : "1994-11-29",
            "hire_date" : "2014-11-29",
            "phone" : "1xxxxxx1234",
            "address" : "804 Aspen Dr, Tehachapi, CA 93561",
            "position_id" : "",
            "status" : "在职"
        }]
    )]
):
    """
    Create an employee, need username not already exists and correct position_id
    """
    db_record = crud.create_employee(session, employee)
    if db_record is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="用户名已经被占用或岗位不存在.")
    return db_record

# 2. 获取所有员工
@api_employee.get('/', response_model=list[schemas.EmployeeOut]) 
async def get_all_employee(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    """
    返回所有员工的列表
    """
    return crud.get_employee(session, offset, limit)

# 3. 获取单个员工
@api_employee.get('/{employee_id}', response_model=schemas.EmployeeOut) 
async def get_employee(
    session: SessionDep,
    employee_id: str
):
    """
    根据员工 ID 获取员工详细信息
    """
    return crud.get_employee_by_id(session, employee_id)

# 4. 更新员工信息
@api_employee.put('/{employee_id}') 
async def update_employee(
    session: SessionDep,
    employee_id: str,
    employee: Annotated[schemas.EmployeeIn, Body(
        examples = [{
            "name": "张三",
            "username": "zhangsan",
            "gender": "M",
            "date_of_birth": "1994-11-29",
            "hire_date": "2014-11-29",
            "phone": "1xxxxxx1234",
            "email": "zhangsan@company.com",
            "address": "804 Aspen Dr, Tehachapi, CA 93561",
            "position_id": "position_fb52292d-6299-42d6-8d4b-247bc42ae06c",
            "status": "在职",
        }]
    )]
):
    """
    GET /employee/{employee_id}    更新员工信息
    """
    db_record = crud.update_employee(session, employee_id, employee)
    if db_record is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="岗位不存在.")
    return db_record

# 5. 删除员工
@api_employee.delete('/{employee_id}') 
async def del_employee(
    session: SessionDep,
    employee_id: str     
):
    """
    GET /employee/    获取所有岗位信息
    """
    db_record = crud.delete_employee(session, employee_id)
    if db_record is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="employee not exists.")
    return db_record
