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


