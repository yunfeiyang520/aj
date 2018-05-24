
### 注册接口


#### request请求

 	POST /user/register/

##### params参数：

	moblie str 电话号码

	password  str  密码

	password2 str 确认密码



#### response响应

##### 失败响应1：


	{
	    "code": 1000,
	    "msg": "注册信息参数错误"
	}

##### 失败响应2：

	{
	    "code": 1002,
	    "msg": "手机号码已注册"
	}

##### 失败响应3：

	{
	    "code": 1003,
	    "msg": "注册密码两次不一致"
	}

##### 成功响应：

	{
	    "code": 200,
	    "msg": "请求成功"
	}