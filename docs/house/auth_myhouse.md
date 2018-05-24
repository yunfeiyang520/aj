
### 房屋详情

#### request 请求

	GET /house/auth_myhouse/

#### response 响应

正常响应：

	{
        "code": "200",
        "hlist": [{
                "address": "xxx100号",
                "area": "锦江区",
                "create_time": "2018-05-21 08:59:08",
                "id": 7,
                "image": "/static/upload/house\\mvc.png",
                "order_count": 0,
                "price": 251,
                "room": 10,
                "title": "情侣公寓"
            },
            {
                "address": "天府大道",
                "area": "锦江区",
                "create_time": "2018-05-20 15:24:19",
                "id": 2,
                "image": "\\static\%upload\\house\\orm.png",
                "order_count": 0,
                "price": 166,
                "room": 10,
                "title": "单身公寓"
            }
        ]
    }

失败响应：

    {
        'code': 1010,
        'msg': '用户没有实名认证'
    }


响应参数：

id int ID

address str 地址

area str 区域名称

create_time str 创建时间

image file 房间图片

order_count int 住过几次

room int 可出租房间个数

title str 房屋标题