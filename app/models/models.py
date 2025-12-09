# 定义员工、岗位、菜单、角色和工作日志的模型
from datetime import datetime
from sqlmodel import Field, SQLModel

class ModelBase(SQLModel):
    """
    ModelBase
    """
    id: str | None = Field(default=None, primary_key=True)            # id 直到插入到数据库中才会有值，所以这里可以为None
    create_at: datetime | None = Field(default=None)                                       # 创建时间
    update_at: datetime | None = Field(default=None)                                       # 更新时间

class Employee(ModelBase, table=True):
    """
    Employee
    """
    __tablename__ = "employee"
    name: str | None                                                      #	VARCHAR	员工的姓名
    user_id: str | None = Field(default=None)                             #	VARCHAR	员工的用户id，一开始没有，user创建好才有
    username: str | None                                                  #	VARCHAR	员工的用户名
    gender: str | None                                                    #	VARCHAR	员工的性别
    date_of_birth: str | None = Field(default='1970-01-01')               #	VARCHAR	员工的出生日期
    hire_date: str | None                                                 #	VARCHAR	员工的入职日期
    phone: str | None                                                     #	VARCHAR	员工的联系电话
    email: str | None = Field(default=None)                               #	VARCHAR	员工的电子邮件地址（字符串，需唯一）
    address: str | None                                                   #	VARCHAR	员工的居住地址
    position_id: str | None                                               #	VARCHAR	外键，指向岗位表的 ID（整数）。
    status: str | None                                                    #	VARCHAR	员工的状态（字符串，例如 "在职"、"离职" 等）
    
class Position(ModelBase, table=True):
    """
    Position
    """
    __tablename__ = "position"
    position_name: str | None                #	VARCHAR	岗位名称
    description: str | None                  #	TEXT	岗位描述
    department: str | None                   #	VARCHAR	岗位所属的部门
    
class Project(ModelBase, table=True):
    """
    Project
    """
    __tablename__ = "project"
    project_name: str | None                 # VARCHAR	项目名称
    description: str | None                  # TEXT	    项目描述
    start_date: str | None                   # VARCHAR	项目开始日期
    end_date: str | None                     # VARCHAR	项目结束日期（可选）
    status: str | None                       # VARCHAR	项目状态（如 "进行中"、"已完成"、"已取消"）
    
class Task(ModelBase, table=True):
    """
    Task
    """
    __tablename__ = "task"
    project_id: str | None                   # 	VARCHAR	外键，项目id
    create_emp_id: str | None                # 	VARCHAR	外键，指向创建这个工作的员工 ID
    employee_id: str | None                  # 	VARCHAR	外键，指向执行的员工表的 ID
    work_date: str | None                    # 	VARCHAR	工作日期
    start_time: datetime | None              # 	TIME	工作开始时间
    end_time: datetime | None                # 	TIME	工作结束时间
    duration: int | None                     # 	INTERVAL	工作时长（可选，计算得出）
    description: str | None                  # 	TEXT	工作内容描述
    
class Comment(ModelBase, table=True):
    """
    Comment
    """
    __tablename__ = "comment"
    task_id: str | None                      #	VARCHAR	外键，指向工作日志表的 ID
    comment: str | None                      #	TEXT	评论内容
    
class User(ModelBase, table=True):
    """
    User
    """
    __tablename__ = "user"
    username: str | None                     #		VARCHAR	用户名或组名
    password: str | None                     #		VARCHAR	登录密码
    type: str | None                         #		VARCHAR	用户类型（如 "普通用户"、 "功能用户"、"用户组"等）
    employee_id: str | None                  #	    VARCHAR 外键，绑定的员工id，可选，可以不绑定
    email: str | None                        #		VARCHAR	用户电子邮件地址
    status: str | None                       #		VARCHAR	用户状态（如 "启用"、"禁用"）
    
class Role(ModelBase, table=True):
    """
    Role
    """
    __tablename__ = "role"
    role_name: str | None                    #	VARCHAR	角色名称
    description: str | None                  #	TEXT	角色描述
    
class Permission(ModelBase, table=True):
    """
    Permission
    """
    __tablename__ = "permission"
    permission_name: str | None              #	VARCHAR	权限名称
    resource_id: str | None                  #	VARCHAR	外键，指向资源表的 ID
    action: str | None                       #	VARCHAR	权限操作（"ALL", "创建"、"读取"、"更新"、"删除"）
    description: str | None                  #	TEXT	权限描述
    
class Resource(ModelBase, table=True):
    """
    Resource
    """
    __tablename__ = "resource"
    resource_type: str | None                #	VARCHAR	资源类型（例如，"页面"、"API"、"功能"等）
    resource_name: str | None                #	VARCHAR	资源名称（例如，API 路径、页面名称等）
    description: str | None                  #	TEXT	资源描述

    
class UserRole(ModelBase, table=True):
    """
    UserRole
    """
    __tablename__ = "user_role"
    user_id: str | None = Field(default=None, primary_key=True)         # 主键，指向用户表的 ID
    role_id: str | None = Field(default=None, primary_key=True)         # 主键，指向角色表的 ID


    
class RolePermission(SQLModel, table=True):
    """
    RolePermission
    """
    __tablename__ = "role_permission"
    # 角色权限关联表（RolePermission Table）
    role_id: str | None = Field(default=None, primary_key=True)         # 主键，指向角色表的 ID
    permission_id: str | None = Field(default=None, primary_key=True)   # 主键，指向权限表的 ID