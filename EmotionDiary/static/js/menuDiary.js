///////////////////////////////////////
// INITIALIZATION
///////////////////////////////////////

// 是否填寫過日記 -> 新增日記
function addDiary(){
    var userid = document.getElementById('userid').innerText;
    var message = document.getElementById('message').innerText;
    if(message){
        swal("您今天已填寫日記了呦～");
    }else{
        window.location.href='../addDiary1/'+ userid;
    }
}

// 修改日記
function editDiary(){
    var userid = document.getElementById('userid').innerText;
    var message = document.getElementById('message').innerText;
    if(message == ''){
        swal("您今天還沒填寫日記了呦～");
    }else{
        window.location.href='../editDiary/'+ userid;
    }
}
