//获取用户信息，判断是否进行过实名认证
$.get('/house/auth_myhouse/',function (data) {
    if(data.code== '200'){
        //已经完成实名认证
        $('#houses-list').show();
        var html=template('house_list',{hlist:data.hlist});
        $('#houses-list').append(html);
    }else{
        //未实名认证
        $('#auth-warn').show();
    }
});
