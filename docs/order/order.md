
### 预约详情

#### request 请求

	GET /house/getbookingbyid/[id]/

#### param 参数

	id int 房屋id

#### response 响应

	{
    "house": {
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