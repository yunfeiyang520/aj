
### 房东查看预约订单

#### request 请求

	GET /order/fd/


#### response 响应

	{
        "olist": [{
                "amount": 251,
                "begin_date": "2018-05-22",
                "comment": null,
                "create_date": "2018-05-22",
                "days": 1,
                "end_date": "2018-05-22",
                "house_title": "情侣公寓",
                "image": "/static/upload/house\\mvc.png",
                "order_id": 6,
                "status": "WAIT_ACCEPT"
            },
            {
                "amount": 502,
                "begin_date": "2018-05-22",
                "comment": "不安逸",
                "create_date": "2018-05-22",
                "days": 2,
                "end_date": "2018-05-23",
                "house_title": "爱情公寓",
                "image": "/static/upload/house\\home01.jpg",
                "order_id": 5,
                "status": "REJECTED"
            }
        ]
    }


响应参数：

amount int 总价格

begin_date str 入住时间

comment str 评论

create_date date 创建时间

days int 住多少天

end_date str 离店时间

house_title str 房屋标题

image str 房屋的首图

order_id int 订单的id

status str 订单的状态
