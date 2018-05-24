
### 搜索

#### request 请求

	GET /house/searchall/?aid=[id]

#### param 参数

	id int 区域id

#### response 响应

	{
    "areas": [
        {
            "id": 1,
            "name": "锦江区"
        },
        {
            "id": 2,
            "name": "金牛区"
        },
        {
            "id": 3,
            "name": "青羊区"
        },
        {
            "id": 4,
            "name": "高新区"
        },
        {
            "id": 5,
            "name": "武侯区"
        },
        {
            "id": 6,
            "name": "天府新区"
        },
        {
            "id": 7,
            "name": "双流县"
        },
        {
            "id": 8,
            "name": "成华区"
        },
        {
            "id": 9,
            "name": "青白江区"
        },
        {
            "id": 10,
            "name": "新都区"
        },
        {
            "id": 11,
            "name": "温江区"
        },
        {
            "id": 12,
            "name": "温江区"
        },
        {
            "id": 13,
            "name": "郫县"
        },
        {
            "id": 14,
            "name": "蒲江县"
        },
        {
            "id": 15,
            "name": "大邑县"
        },
        {
            "id": 16,
            "name": "新津县"
        }
    ],
    "code": 200,
    "houses": [
        {
            "address": "天府大道",
            "area": "青羊区",
            "create_time": "2018-05-20 15:35:04",
            "id": 6,
            "image": "\\static\\upload\\house\\orm.png",
            "order_count": 0,
            "price": 166,
            "room": 10,
            "title": "单身公寓3"
        }
    ]
}


响应参数：
	
areas： 省份信息
	
	id int ID
	name str 名称

houses：房屋的信息

	acreage int 房屋面积
	address str 面积
	id int ID
	image str 房屋图片
	create_time str 创建时间
    order_count int 预订完成的该房屋的订单数


