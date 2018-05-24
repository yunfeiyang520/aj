
### 用户信息接口

#### request请求

 	PUT /user/user/

#### params参数

    avatar file 头像

    name str 用户名


#### response响应

##### 响应成功

上传头像图片：
	{
      "code": "200",
      "url": "/static/upload\\landlord01.jpg"
    }

修改用户名：
    {
        code: 200,
        msg: "请求成功"
    }

修改用户名重复：
    {
        code: 1008,
        msg: "用户名已经存在"
    }