function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$('#form-avatar').submit(function () {
    $('.error_msg').hide();
    $(this).ajaxSubmit({
        url: "/user/user/",
        type: "put",
        dataType: "json",
        success: function (data) {
            if (data.code == '200') {
                $('#user-avatar').attr('src',data.url);
            } else {
                $('#error_msg1').show();
            }
        }
    });
    return false;
});

$('#form-name').submit(function () {
    $('.error_msg2').hide();
    $.ajax({
        url:'/user/user/',
        type:'put',
        data:{'name':$('#user-name').val()},
        success:function (data) {
            if(data.code== '200'){
                //
            }else{
                $('.error_msg2').html('<i class="fa fa-exclamation-circle"></i>' +data.msg);
                $('.error_msg2').show();

            }
        }
    });
    return false;
});