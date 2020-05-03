$(function () {
        $(".navbar-nav li").click(function () {
                //获取点击的元素给其添加样式，讲其兄弟元素的样式移除
                //$(this).addClass("active").siblings().removeClass("active");
                //获取选中元素的下标
                var index = $(this).index();

                if (index == 0) {
                        $.ajax({url:"/home",async:false,success:function(result){
                                str = result;
                        }});
                        $("#home").append(str);
                } else {
                        $.ajax({url:"/us",async:false,success:function(result){
                                str = result;

                        }});
                         $("#menu1").append(str);
                }
                setTimeout(null,3000)
                console.log("icomin")
                console.log(str);
        });
});