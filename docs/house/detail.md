
### 房屋详情

#### request 请求

	GET /house/detail/[id]/

#### param 参数

	id int 房屋id

#### response 响应

	{
	  "booking": 0, 
	  "facility_list": [
	    {
	      "css": "parkingspace-ico", 
	      "id": 20, 
	      "name": "\u505c\u8f66\u4f4d"
	    }, 
	    {
	      "css": "tv-ico", 
	      "id": 22, 
	      "name": "\u7535\u89c6"
	    }
	  ], 
	  "house": {
	    "acreage": 30, 
	    "address": "\u9752\u7f8a\u533a\u5929\u5e9c\u5927\u9053", 
	    "beds": "\u5355\u4eba\u5e8a1.5x1.2", 
	    "capacity": 2, 
	    "deposit": 300, 
	    "facilities": [
	      {
	        "css": "parkingspace-ico", 
	        "id": 20, 
	        "name": "\u505c\u8f66\u4f4d"
	      }, 
	      {
	        "css": "tv-ico", 
	        "id": 22, 
	        "name": "\u7535\u89c6"
	      }
	    ], 
	    "id": 6, 
	    "images": [
	      "/static/upload/house\\orm.png", 
	      "/static/upload/house\\mvt.png"
	    ], 
	    "max_days": 30, 
	    "min_days": 3, 
	    "order_count": 0, 
	    "price": 166, 
	    "room_count": 10, 
	    "title": "\u5355\u8eab\u516c\u5bd33", 
	    "unit": "\u4e00\u5ba4\u4e00\u5385", 
	    "user_avatar": "/static/upload\\mvc.png", 
	    "user_name": "12"
	  }
	}


响应参数：
	
facility_list： 配套设置的信息
	
	id int ID
	css str 样式
	name str 名称

house：房屋的信息

	acreage int 房屋面积
	address str 面积
	beds str 房屋床铺的配置
	deposit	int 房屋押金
    facilities str 配套设施
	id int ID
	image str 房屋图片
	min_days int 最少入住天数
    max_days int 最多入住天数，0表示不限制
    order_count int 预订完成的该房屋的订单数
    price str 价格
	user_avatar str 用户头像
	user_name str 用户名称

