
### 修改预约单的状态

#### request 请求

	PUT /order/[id]/

#### param 参数

	id int 订单的id

	comment str 可选提交，用户对预约单的评论

#### response 响应

响应失败：

	{
        'code': 401,
        'msg': '数据库错误'
	}

响应成功：

    {
        'code': 200
    }


