function click_sentiment_link(){
    $('#web_left_content').load("/Sentiment",null,function(response,status){
        if(status!="success"){
            console.log(status);
            $('#web_right_content').html(status);
        }
    });
}

function click_summary_link(){
    $('#web_left_content').load("/Summary",null,function(response,status){
        if(status!="success"){
            console.log(status);
            $('#web_right_content').html(status);
        }
    });
}

function click_aboutus_link(){
    $('#left_content').load("/AboutUs",null,function(response,status){
        if(status!="success"){
            console.log(status);
            $('#left_content').html(status);
        }
    });
}

function click_message_link(){
    $('#web_left_content').load("/message",null,function(response,status){
        if(status!="success"){
            console.log(status);
            $('#web_right_content').html(status);
        }
    });
}

function load_article(article_id){
    $('#left_content').load("/article/"+article_id,null,function(response,status){
        if(status!="success"){
            console.log(status);
            $('#left_content').html(status);
        }
    });
}

$('.login-register').click(function(){$(".theme-popover.login").fadeIn();});


var HtmlUtil = {
    /*1.用正则表达式实现html转码*/
    htmlEncodeByRegExp:function (str){
         var s = "";
         if(str.length == 0) return "";
         str= "\'"+str+"\'";
         console.log(str);
         s = str.replace(/&/g,"&amp;");
         s = s.replace(/</g,"&lt;");
         s = s.replace(/>/g,"&gt;");
         s = s.replace(/ /g,"&nbsp;");
         s = s.replace(/\'/g,"&#39;");
         s = s.replace(/\"/g,"&quot;");
         return s;
   },
   /*2.用正则表达式实现html解码*/
   htmlDecodeByRegExp:function (str){
         var s = "";
         if(str.length == 0) return "";
         str= "\'"+str+"\'";
         console.log(str);
         s = str.replace(/&amp;/g,"&");
         s = s.replace(/&lt;/g,"<");
         s = s.replace(/&gt;/g,">");
         s = s.replace(/&nbsp;/g," ");
         s = s.replace(/&#39;/g,"\'");
         s = s.replace(/&quot;/g,"\"");
         return s;
   }
};
