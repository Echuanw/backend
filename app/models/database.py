import os
from sqlalchemy import inspect
from sqlmodel import SQLModel, create_engine, Session, Field, text
from fastapi import Depends
from typing import Annotated
from app.models.models import *

sqlite_url = f"sqlite:///db_local/crm_project.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def check_and_rebuild_tables():
    # 字段有差异时，重新建表
    print("start check_and_rebuild_tables")
    inspector = inspect(engine)                                         # 检查数据库中的表结构
    for table_name, cls in SQLModel.metadata.tables.items():            # 检查pydantic中的定义表结构
        db_status = str(sorted({column['name'] for column in inspector.get_columns(table_name)}))
        pydantic_status = str(sorted({column.name for column in cls.columns}))
        if db_status != pydantic_status:
            print("db_status : " + db_status + "\r\npydantic_status : " + pydantic_status)
            with engine.connect() as conn:
                # 使用 text() 函数将 SQL 字符串转换为可执行对象
                conn.execute(text(f"DROP TABLE IF EXISTS {table_name};"))  # 删除表
                SQLModel.metadata.create_all(engine)                # 重新创建表
                print(f"Table " + table_name + " has been recreated. \r\n")

def create_db_and_tables():
    print("start create_db_and_tables")
    SQLModel.metadata.create_all(engine)              # 为所有定义好的table model创建表

# 4 session函数
def get_session():
    # 会把 engine 对象存在内存中
    with Session(engine) as session:
        yield session
SessionDep = Annotated[Session, Depends(get_session)]