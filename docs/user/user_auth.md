
### 实名认证接口

### 1. 获取登录实名认证的信息

#### request请求

 	GET /user/auths/

#### response响应

    {
        id_card:"123456789012345678"
        id_name:"王飞"
    }

### 2. 修改实名认证的信息

#### request请求

 	PUT /user/auths/

#### params参数

    id_name str 实名认证的用户名信息

    id_card str 实名认证的身份证信息


#### response响应

成功响应：

    {
	    "code": 200,
	    "msg": "请求成功"
	}

失败响应：

    {
	    "code": 401,
	    "msg": "数据库错误"
	}