from sqlmodel import Field, SQLModel
from .models import *

# Position
class PositionIn(SQLModel):
    position_name: str | None = Field(default=None)                #	VARCHAR	岗位名称
    description: str | None = Field(default=None)                  #	TEXT	岗位描述
    department: str | None = Field(default=None)                   #	VARCHAR	岗位所属的部门
    pass

class PositionOut(SQLModel):                                       # 指定输出顺序
    id: str | None = Field(default=None)            
    position_name: str | None = Field(default=None)                # 岗位名称
    department: str | None = Field(default=None)                   # 岗位所属的部门
    description: str | None = Field(default=None)                  # 岗位描述
    create_at: datetime | None = Field(default=None)               # 创建时间
    update_at: datetime | None = Field(default=None)               # 更新时间
    pass

# User
class UserIn(SQLModel):
    __tablename__ = "user"
    username: str | None                         #		VARCHAR	用户名或组名
    password: str | None                         #		VARCHAR	登录密码
    type: str | None = Field(default='普通用户')  #		VARCHAR	用户类型（如 "普通用户"、 "功能用户"、"用户组"等）
    employee_id: str | None                      #	    VARCHAR 外键，绑定的员工id，可选，可以不绑定
    email: str | None                            #		VARCHAR	用户电子邮件地址
    status: str | None = Field(default='启用')    #		VARCHAR	用户状态（如 "启用"、"禁用"）
    pass

class UserOut(SQLModel):                                       # 指定输出顺序
    id: str | None = Field(default=None)            
    position_name: str | None = Field(default=None)                # 岗位名称
    department: str | None = Field(default=None)                   # 岗位所属的部门
    description: str | None = Field(default=None)                  # 岗位描述
    create_at: datetime | None = Field(default=None)               # 创建时间
    update_at: datetime | None = Field(default=None)               # 更新时间
    pass


# Employee
class EmployeeIn(SQLModel):
    name: str | None                                                      #	VARCHAR	员工的姓名
    username: str | None                                                  #	VARCHAR	员工的用户名，这个创建后就不可以更新的
    gender: str | None  = Field(default='M')                              #	VARCHAR	员工的性别
    date_of_birth: str | None = Field(default='1970-01-01')               #	VARCHAR	员工的出生日期
    hire_date: str | None                                                 #	VARCHAR	员工的入职日期
    phone: str | None = Field(default='1xxxxxx1234')                      #	VARCHAR	员工的联系电话
    email: str | None = Field(default=None)                               #	VARCHAR	员工的电子邮件地址（字符串，需唯一），这个创建后就不可以更新的
    address: str | None                                                   #	VARCHAR	员工的居住地址
    position_id: str | None                                               #	VARCHAR	外键，指向岗位表的 ID。
    status: str | None = "在职"                                            # VARCHAR 员工的状态（字符串，例如 "在职"、"离职" 等）
    pass

class EmployeeOut(SQLModel):
    id: str | None = Field(default=None)
    name: str | None                                                      #	VARCHAR	员工的姓名
    username: str | None                                                  #	VARCHAR	员工的用户名
    gender: str | None  = Field(default='M')                              #	VARCHAR	员工的性别
    date_of_birth: str | None = Field(default='1970-01-01')               #	VARCHAR	员工的出生日期
    hire_date: str | None                                                 #	VARCHAR	员工的入职日期
    phone: str | None = Field(default='1xxxxxx1234')                      #	VARCHAR	员工的联系电话
    email: str | None                                                     #	VARCHAR	员工的电子邮件地址（字符串，需唯一）
    address: str | None                                                   #	VARCHAR	员工的居住地址
    position_id: str | None                                               #	VARCHAR	外键，指向岗位表的 ID。
    status: str | None = "在职"                                            # VARCHAR 员工的状态（字符串，例如 "在职"、"离职" 等）
    create_at: datetime | None = Field(default=None)                      # 创建时间
    update_at: datetime | None = Field(default=None)                      # 更新时间
    pass

class EmployeeUpdate(SQLModel):
    id: str | None = Field(default=None)
    name: str | None                                                      #	VARCHAR	员工的姓名
    username: str | None                                                  #	VARCHAR	员工的用户名
    gender: str | None  = Field(default='M')                              #	VARCHAR	员工的性别
    date_of_birth: str | None = Field(default='1970-01-01')               #	VARCHAR	员工的出生日期
    hire_date: str | None                                                 #	VARCHAR	员工的入职日期
    phone: str | None = Field(default='1xxxxxx1234')                      #	VARCHAR	员工的联系电话
    email: str | None                                                     #	VARCHAR	员工的电子邮件地址（字符串，需唯一）
    address: str | None                                                   #	VARCHAR	员工的居住地址
    position_id: str | None                                               #	VARCHAR	外键，指向岗位表的 ID。
    status: str | None = "在职"                                            # VARCHAR 员工的状态（字符串，例如 "在职"、"离职" 等）
    create_at: datetime | None = Field(default=None)                      # 创建时间
    update_at: datetime | None = Field(default=None)                      # 更新时间
    pass


class UserCreate(User):
    pass
