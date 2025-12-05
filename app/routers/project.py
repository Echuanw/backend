from fastapi import APIRouter
api_project = APIRouter()

# 工作项目管理

# 1. 创建项目
# HTTP 方法: POST
# 路径: /project/
# 请求参数:
# project_name: 项目名称
# description: 项目描述
# start_date: 项目开始日期
# end_date: 项目结束日期
# 描述: 创建一个新的项目
@api_project.post('/') 
async def add_project():
    """
    POST /project/    创建一个新的项目
    """
    return {"method":"创建一个新的项目"}

# 2. 删除项目
# HTTP 方法: DELETE
# 路径: /project/{project_id}
# 描述: 删除指定的项目

# 3. 更新项目
# HTTP 方法: PUT
# 路径: /project/{project_id}
# 请求参数:
# project_name: 项目名称
# description: 项目描述
# start_date: 项目开始日期
# end_date: 项目结束日期
# 描述: 更新指定项目的信息

# 4. 获取某个项目的所有task
# HTTP 方法:get
# 路径: /project/{project_id}/task/
# 描述: 返回项目所有task的列表
@api_project.get('/{project_id}/task/') 
async def get_all_task():
    """
    GET /project/{project_id}/task/    返回项目所有task的列表
    """
    return {"method":"返回项目所有task的列表"}

# 5. 创建任务（Task）
# HTTP 方法: POST
# 路径: /project/{project_id}/task
# 请求参数:
# task_name: 任务名称
# description: 任务描述
# assigned_to: 指派给的员工 ID
# due_date: 任务截止日期
# 描述: 在指定项目下创建一个新的任务
@api_project.post('/{project_id}/task') 
async def add_task():
    """
    POST /project/    在指定项目下创建一个新的任务
    """
    return {"method":"在指定项目下创建一个新的任务"}

# 6. 获取某个项目的指定task
# HTTP 方法:GET
# 路径: /project/{project_id}/task/{task_id}
# 描述: 获取某个项目的指定task
@api_project.get('{project_id}/task/{task_id}') 
async def get_task():
    """
    GET /project/{project_id}/task/    返回项目所有task的列表
    """
    return {"method":"返回项目所有task的列表"}

# 7. 删除任务（Task）
# HTTP 方法: DELETE
# 路径: /project/{project_id}/task/{task_id}
# 描述: 删除指定项目下的任务
@api_project.delete('/{project_id}/task/{task_id}') 
async def del_project():
    """
    GET /project/{project_id}/task/{task_id}    删除指定项目下的任务
    """
    return {"method":"删除指定项目下的任务"}


# 8. 更新任务（Task）
# HTTP 方法: PUT
# 路径: /project/{project_id}/task/{task_id}
# 请求参数:
# task_name: 任务名称
# description: 任务描述
# assigned_to: 指派给的员工 ID
# due_date: 任务截止日期
# 描述: 更新指定项目下的任务信息
@api_project.put('/{project_id}/task/{task_id}') 
async def update_task():
    """
    GET /project/{project_id}/task/{task_id}    更新指定项目下的任务信息
    """
    return {"method":"更新指定项目下的任务信息"}

# 9. 获取某个task的所有Comment
# HTTP 方法:get
# 路径: /project/{project_id}/task/{task_id}/comment
@api_project.get('/{project_id}/task/{task_id}/comment') 
async def get_all_comment():
    """
    GET /project/{project_id}/task/    
    """
    return {"method":"获取某个task的所有Comment"}

# 10. 创建评论（Comment）
# HTTP 方法: POST
# 路径: /project/{project_id}/task/{task_id}/comment
# 请求参数:
# comment: 评论内容
# 描述: 在指定任务下创建一个新的评论
@api_project.post('/{project_id}/task/{task_id}/comment') 
async def add_comment():
    """
    GET /project/{project_id}/task/{task_id}/comment    在指定任务下创建一个新的评论
    """
    return {"method":"在指定任务下创建一个新的评论"}

# 11. 删除评论（Comment）
# HTTP 方法: DELETE
# 路径: /project/{project_id}/task/{task_id}/comment/{comment_id}
# 描述: 删除指定任务下的评论
@api_project.delete('/{project_id}/task/{task_id}/comment/{comment_id}') 
async def del_comment():
    """
    GET /project/{project_id}/task/{task_id}/comment/{comment_id}    删除指定任务下的评论
    """
    return {"method":"删除指定任务下的评论"}

# # 12. 更新评论（Comment）
# # HTTP 方法: PUT
# # 路径: /project/{project_id}/task/{task_id}/comment/{comment_id}
# # 请求参数:
# # comment: 评论内容
# # 描述: 更新指定任务下的评论内容
# @api_project.put('/{project_id}') 
# async def update_project():
#     """
#     GET /project/{project_id}    更新员工信息
#     """
#     return {"method":"更新员工信息"}

# 13. 导出项目的工作日志
# HTTP 方法: GET
# 路径: /project/{project_id}/task/export
# 请求参数:
# format: 导出格式（例如，csv、xlsx）
# start_date: 开始日期（可选）
# end_date: 结束日期（可选）
# 描述: 导出指定项目的工作日志，可以选择导出格式和时间范围
@api_project.get('/{project_id}/task/{task_id}/export') 
async def export_all_comment():
    """
    GET /project/{project_id}/task/export
    """
    return {"method":"导出指定项目的工作日志，可以选择导出格式和时间范围"}