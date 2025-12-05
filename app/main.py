from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
# 子路由
from app.routers.employee import api_employee
from app.routers.position import api_position
from app.routers.project import api_project
from app.routers.role import api_role
# models
from app.models.database import check_and_rebuild_tables,create_db_and_tables

# 生命周期控制
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动前 event
    check_and_rebuild_tables()
    create_db_and_tables()          # 初始化数据库和表 
    yield      # yield for middle event
    # end event
    # maybe you can close connection with db

# 创建app，绑定生命周期活动和路由
app = FastAPI(lifespan=lifespan)
app.include_router(router=api_employee, prefix="/api/employee", tags=["员工管理接口"])
app.include_router(router=api_position, prefix="/api/position", tags=["岗位管理接口"])
app.include_router(router=api_project, prefix="/api/project", tags=["工作项目管理接口"])
app.include_router(router=api_role, prefix="/api/role", tags=["角色权限接口"])

@app.get('/')
async def root():
    return {"message": "hello fastapi user"}

@app.get('/login')
async def login():
    return {"message": "you access to the login Page"}

@app.get('/exit')
async def exit():
    return {"message": "you access to the exit Page"}

def main():
    """
    app 启动的py文件名
    host port 访问的ip端口
    reload .,.
    """
    uvicorn.run(app="app.main:app", host="127.0.0.1", port=8080, reload=True)

if __name__ == '__main__':
    main()