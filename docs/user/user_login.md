
### 登录接口


#### request请求

 	POST /user/login/

##### params参数：

	mobile str 电话号码

	password  str  密码


#### response响应

##### 失败响应1：


	{
	    "code": 1001,
	    "msg": "参数错误"
	}

##### 失败响应2：

	{
	    "code": 1002,
	    "msg": "电话号码错误"
	}

##### 失败响应3：

	{
	    "code": 1003,
	    "msg": "密码错误"
	}

##### 失败响应4：

	{
	    "code": 1004,
	    "msg": "用户不存在"
	}

##### 成功响应：

	{
	    "code": 200,
	    "msg": "请求成功"
	}