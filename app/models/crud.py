import pytz
import uuid
import app.models.models as models
import app.models.schemas as schemas
from sqlmodel import select
from .database import SessionDep
from datetime import datetime
from fastapi.encoders import jsonable_encoder

# 获取时间信息的工具方法
def get_time_now():
    return datetime.now(pytz.timezone("Asia/Shanghai"))
def get_time_str():
    return get_time_now().strftime("%Y-%m-%d %H:%M:%S")
def get_date_str():
    return get_time_now().strftime("%Y-%m-%d")
# 更新记录的 id 和 创建更新时间
def update_id_time(db_record: models.ModelBase, type: str):
    time_now = get_time_now()
    db_record.id = type + '_' + str(uuid.uuid4())
    db_record.create_at, db_record.update_at = time_now, time_now

# Position

def get_position_by_name(db: SessionDep, position_name: str):
    return db.exec(select(models.Position).where(models.Position.position_name == position_name)).first()

def get_position_by_id(db: SessionDep, position_id: str):
    return db.exec(select(models.Position).where(models.Position.id == position_id)).first()

def create_position(db: SessionDep, record_in: schemas.PositionIn):
    """新增 Position, 需要检查是不是有同名的"""
    existing_record = get_position_by_name(db, record_in.position_name)
    if existing_record:
        return None  # 返回 None 以表明岗位已存在
    db_record = models.Position.model_validate(record_in)
    update_id_time(db_record, "position")
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_position(db: SessionDep, offset: int, limit : int):
    """查询所有 Position"""
    return list(db.exec(select(models.Position).offset(offset).limit(limit)).all())

def update_position(db: SessionDep, position_id:str, record_in: schemas.PositionIn):
    """更新 Position,"""
    existing_record = get_position_by_id(db, position_id)                          # 获取原数据
    if existing_record:
        db_record = record_in.model_dump(exclude_unset=True)                         # 新数据转成 Position 并去除未设置的字段
        for key, value in db_record.items():                                         # 依次更新字段
            setattr(existing_record, key, value)
        existing_record.update_at = get_time_now()                                # 设置新数据的更新时间
        db.commit()                           # 提交到暂存区
        db.refresh(existing_record)           # 最后才能更新
        return existing_record
    return None

def delete_position(db: SessionDep, position_id:str):
    """更新 Position,"""
    existing_record = get_position_by_id(db, position_id)                          # 获取原数据
    if existing_record:
        db.delete(existing_record) 
        db.commit()                     
        return existing_record
    return None

# User user 是伴随着Employee一起创建的

# def get_user_by_name(db: SessionDep, user_name: str):
#     return db.exec(select(models.Position).where(models.Position.position_name == user_name)).first()

# def get_user_by_id(db: SessionDep, user_id: str):
#     return db.exec(select(models.Position).where(models.Position.id == position_id)).first()

# def create_user(db: SessionDep, record_in: schemas.PositionIn):
#     """新增 Position, 需要检查是不是有同名的"""
#     existing_record = get_position_by_name(db, record_in.position_name)
#     if existing_record:
#         return None  # 返回 None 以表明岗位已存在
#     db_record = models.Position.model_validate(record_in)
#     update_id_time(db_record, "position")
#     db.add(db_record)
#     db.commit()
#     db.refresh(db_record)
#     return db_record

# def get_user(db: SessionDep, offset: int, limit : int):
#     """查询所有 Position"""
#     return list(db.exec(select(models.Position).offset(offset).limit(limit)).all())

# def update_user(db: SessionDep, user_id:str, record_in: schemas.PositionIn):
#     """更新 Position,"""
#     existing_record = get_position_by_id(db, position_id)                          # 获取原数据
#     if existing_record:
#         db_record = record_in.model_dump(exclude_unset=True)                         # 新数据转成 Position 并去除未设置的字段
#         for key, value in db_record.items():                                         # 依次更新字段
#             print(key, value)
#         existing_record.update_at = get_time_now()                                # 设置新数据的更新时间
#         db.commit()                           # 提交到暂存区
#         db.refresh(existing_record)         # 最后才能更新
#         return existing_record
#     return None

# def delete_user(db: SessionDep, user_id:str):
#     """更新 Position,"""
#     existing_record = get_position_by_id(db, position_id)                          # 获取原数据
#     if existing_record:
#         db.delete(existing_record) 
#         db.commit()                     
#         return existing_record
#     return None

# User

# Employee

def get_employee_by_username(db: SessionDep, username: str):
    return db.exec(select(models.Employee).where(models.Employee.username == username)).first()

def get_employee_by_id(db: SessionDep, employee_id: str):
    return db.exec(select(models.Employee).where(models.Employee.id == employee_id)).first()

def create_employee(db: SessionDep, record_in: schemas.EmployeeIn):
    """新增 employee, 需要检查是不是有同用户名的， 岗位是否正确"""
    existing_record = get_employee_by_username(db, record_in.username)
    if existing_record:
        print("以表明这个用户名已经被占用")
        return None  # 返回 None 以表明这个用户名已经被占用
    existing_position = get_position_by_id(db, record_in.position_id)
    if existing_position is None:
        print("以表明这个输入的这个岗位不存在")
        return None  # 返回 None 以表明这个输入的这个岗位不存在
    db_record = models.Employee.model_validate(record_in)
    update_id_time(db_record, "employee")
    db_record.email = db_record.username + "@company.com"        # 邮箱需要username + 公司邮箱
    user_record = models.User(               # 创建新的员工后，为他创建一个公司账号
        id = 'user_' + str(uuid.uuid4()),
        username = db_record.username,
        password = db_record.username,
        type = '普通用户',
        employee_id = db_record.id,
        email = db_record.email,
        status = '启用',
        create_at=db_record.create_at,
        update_at=db_record.create_at
    ) 
    db.add(user_record)
    db.commit()
    db.refresh(user_record)                 
    db_record.user_id = user_record.id       # 账号创建好user后，填充user_id
    db.add(db_record)
    db.commit()
    db.refresh(db_record)                    # 然后创建employee记录
    return db_record

def get_employee(db: SessionDep, offset: int, limit : int):
    """查询所有 Employee"""
    return list(db.exec(select(models.Employee).offset(offset).limit(limit)).all())

def update_employee(db: SessionDep, employee_id:str, record_in: schemas.EmployeeIn):
    """更新 Position,"""
    existing_record = get_employee_by_id(db, employee_id)                          # 获取原数据
    if existing_record:
        db_record = record_in.model_dump(exclude_unset=True)                         # 新数据转成 Employee 并去除未设置的字段
        for key, value in db_record.items():                                         # 依次更新字段
            if key in ('id', 'username', 'email', 'create_date'): continue           # 跳过指定字段的更新
            setattr(existing_record, key, value)
        existing_position = get_position_by_id(db, existing_record.position_id)
        if existing_position is None:
            print("以表明这个输入的这个岗位不存在")
            return None  # 返回 None 以表明这个输入的这个岗位不存在
        existing_record.update_at = get_time_now()                                # 设置新数据的更新时间
        db.commit()                           # 提交到暂存区
        db.refresh(existing_record)         # 最后才能更新
        return existing_record
    return None

def delete_employee(db: SessionDep, employee_id:str):
    """更新 Position,"""
    existing_record = get_employee_by_id(db, employee_id)                          # 获取原数据
    if existing_record:
        db.delete(existing_record) 
        db.commit()                     
        return existing_record
    return None


# UserRole
def get_userrole_by_roleid(db: SessionDep, role_id: str, offset: int, limit : int):
    return list(db.exec(select(models.UserRole).where(models.UserRole.role_id == role_id).offset(offset).limit(10)).all())

# Role
def generate_composite_key(key1: str, key2:str):
    """获取复合主键id"""
    _key_list = []
    _key_list.append(key1)
    _key_list.append(key2)
    return '|'.join(sorted(_key_list))

def get_role_by_name(db: SessionDep, role_name: str):
    return db.exec(select(models.Role).where(models.Role.role_name == role_name)).first()

def get_role_by_id(db: SessionDep, role_id: str):
    return db.exec(select(models.Role).where(models.Role.id == role_id)).first()

def create_role(db: SessionDep, record_in: schemas.RoleIn):
    """新增 Role, 需要检查是不是有同名的"""
    existing_record = get_role_by_name(db, record_in.role_name)
    if existing_record:
        return None  # 返回 None 以表明岗位已存在
    db_record = models.Role.model_validate(record_in)
    update_id_time(db_record, "role")
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_role(db: SessionDep, offset: int, limit : int):
    """查询所有 Role"""
    return list(db.exec(select(models.Role).offset(offset).limit(limit)).all())

def update_role(db: SessionDep, role_id:str, record_in: schemas.RoleIn):
    """更新 Role,"""
    existing_record = get_position_by_id(db, role_id)                          # 获取原数据
    if existing_record:
        db_record = record_in.model_dump(exclude_unset=True)                         # 新数据转成 Position 并去除未设置的字段
        for key, value in db_record.items():                                         # 依次更新字段
            setattr(existing_record, key, value)
        existing_record.update_at = get_time_now()                                # 设置新数据的更新时间
        db.commit()                           # 提交到暂存区
        db.refresh(existing_record)           # 最后才能更新
        return existing_record
    return None

def delete_role(db: SessionDep, role_id:str):
    """更新 Position,"""
    get_userrole_by_roleid(db, )
    existing_record = get_role_by_id(db, role_id)                          # 获取原数据
    if existing_record:
        db.delete(existing_record) 
        db.commit()                     
        return existing_record
    return None
