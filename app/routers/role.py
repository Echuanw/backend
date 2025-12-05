from fastapi import APIRouter
api_role = APIRouter()

# 员工管理

# 1. 获取所有角色信息
# HTTP 方法:GET
# 路径:/role/
# 描述: 获取所有角色的列表
@api_role.get('/') 
async def get_all_role():
    """
    GET /role/    获取所有角色的列表
    """
    return {"method": "获取所有角色的列表"}

# 2. 获取某个角色绑定的所有人员
# HTTP 方法:GET
# 路径:/role/{role_id}/user
# 描述: 获取指定角色绑定的所有人员
@api_role.get('/{role_id}/user') 
async def get_all_user_by_role():
    """
    GET /role/{role_id}/user    获取指定角色绑定的所有人员
    """
    return {"method": "获取指定角色绑定的所有人员"}

# 3. 获取某个角色绑定的所有权限
# HTTP 方法:GET
# 路径:/role/{role_id}/permission
# 描述: 获取指定角色绑定的所有权限
@api_role.get('/{role_id}/permission') 
async def get_all_permission_by_role():
    """
    GET /role/{role_id}/permission    获取指定角色绑定的所有权限
    """
    return {"method": "获取指定角色绑定的所有权限"}

# 4. 创建一个角色
# HTTP 方法:POST
# 路径:/role/
# 请求参数:
# role_name: 角色名称
# description: 角色描述
# 描述: 创建一个新的角色
@api_role.post('/') 
async def add_role():
    """
    GET /role/    创建一个角色
    """
    return {"method": "创建一个角色"}

# 5. 删除一个角色
# HTTP 方法:DELETE
# 路径:/role/{role_id}
# 描述: 删除指定的角色
@api_role.delete('/{role_id}') 
async def del_role():
    """
    GET /role/{role_id}    删除指定的角色
    """
    return {"method": "删除指定的角色"}


# 6. 为一个角色绑定权限
# HTTP 方法:POST
# 路径:/role/{role_id}/permission
# 请求参数:
# permission_ids: 权限 ID 列表
# 描述: 为指定角色绑定权限
@api_role.post('/{role_id}/permission') 
async def add_role():
    """
    POST /role/{role_id}/permission    为一个角色绑定权限
    """
    return {"method": "为一个角色绑定权限"}


# 7. 为一个角色解绑权限
# HTTP 方法:DELETE
# 路径:/role/{role_id}/permission
# 请求参数:
# permission_ids: 权限 ID 列表
# 描述: 为指定角色解绑权限
@api_role.delete('/{role_id}/permission') 
async def del_role():
    """
    DELETE /role/{role_id}/permission    为指定角色解绑权限
    """
    return {"method": "为指定角色解绑权限"}

# 8. 为一个角色绑定人员
# HTTP 方法:POST
# 路径:/role/{role_id}/user
# 请求参数:
# user_ids: 用户 ID 列表
# 描述: 为指定角色绑定人员
@api_role.post('/{role_id}/user') 
async def add_role():
    """
    POST /role/{role_id}/user    为指定角色绑定人员
    """
    return {"method": "为指定角色绑定人员"}

# 9. 为一个角色解绑人员
# HTTP 方法:DELETE
# 路径:/role/{role_id}/user
# 请求参数:
# user_ids: 用户 ID 列表
# 描述: 为指定角色解绑人员
@api_role.delete('/{role_id}/user') 
async def del_role():
    """
    DELETE /role/{role_id}/user    为一个角色解绑人员
    """
    return {"method": "为一个角色解绑人员"}