
### 区域和设施接口

#### request 请求

	GET /house/area_facility/

#### response 响应

	{
	"area": [{
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
	"facility": [{
			"css": "wirelessnetwork-ico",
			"id": 1,
			"name": "无线网络"
		},
		{
			"css": "shower-ico",
			"id": 2,
			"name": "热水淋浴"
		},
		{
			"css": "aircondition-ico",
			"id": 3,
			"name": "空调"
		},
		{
			"css": "heater-ico",
			"id": 4,
			"name": "暖气"
		},
		{
			"css": "smoke-ico",
			"id": 5,
			"name": "允许吸烟"
		},
		{
			"css": "drinking-ico",
			"id": 6,
			"name": "饮水设备"
		},
		{
			"css": "brush-ico",
			"id": 7,
			"name": "牙具"
		},
		{
			"css": "soap-ico",
			"id": 8,
			"name": "香皂"
		},
		{
			"css": "slippers-ico",
			"id": 9,
			"name": "拖鞋"
		},
		{
			"css": "toiletpaper-ico",
			"id": 10,
			"name": "手纸"
		},
		{
			"css": "towel-ico",
			"id": 11,
			"name": "毛巾"
		},
		{
			"css": "toiletries-ico",
			"id": 12,
			"name": "沐浴露、洗发露"
		},
		{
			"css": "icebox-ico",
			"id": 13,
			"name": "冰箱"
		},
		{
			"css": "washer-ico",
			"id": 14,
			"name": "洗衣机"
		},
		{
			"css": "elevator-ico",
			"id": 15,
			"name": "电梯"
		},
		{
			"css": "iscook-ico",
			"id": 16,
			"name": "允许做饭"
		},
		{
			"css": "pet-ico",
			"id": 17,
			"name": "允许带宠物"
		},
		{
			"css": "meet-ico",
			"id": 18,
			"name": "允许聚会"
		},
		{
			"css": "accesssys-ico",
			"id": 19,
			"name": "门禁系统"
		},
		{
			"css": "parkingspace-ico",
			"id": 20,
			"name": "停车位"
		},
		{
			"css": "wirednetwork-ico",
			"id": 21,
			"name": "有线网络"
		},
		{
			"css": "tv-ico",
			"id": 22,
			"name": "电视"
		},
		{
			"css": "jinzhi-ico",
			"id": 23,
			"name": "浴缸"
		}
	]
}


响应参数：

facility参数：

    id int 设施ID

    name str 名称

    css str 样式

area参数：

    id int 区域ID

    name str 区域名称
