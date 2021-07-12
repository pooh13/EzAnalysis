///////////////////////////////////////
// INITIALIZATION
///////////////////////////////////////

window.onload = function(){
    emojiSelect(e_id);
}

// 選取心情
var e_id;
function emojiSelect(e_id) {
    var arr = document.getElementsByName('emoji_btn');
    for(var i=0; i<arr.length; i++){
        arr[i].onclick = function(){
            //this是当前激活的按钮，在这里可以写对应的操作
            if(this.className == 'btn1'){
                this.className = 'btn2';
                e_id = this.id;
                document.getElementById('mood').value = this.value;
                var btn = document.getElementsByClassName('btn2');
                for(var j=0;j<btn.length;j++){
                    if(btn[j].id!=e_id){
                    btn[j].className = 'btn1';
                    }
                }
            }
        }
    }
}

// 設定時間
function ShowTime(){
    today = new Date();
    var year = today.getFullYear();
    var month = today.getMonth()+1;
    var day = today.getDate();
    var monthString = ( month < 10)? ('0'+ month) : ('' + month);
    var dayString = ( day < 10)? ('0'+ day) : ('' + day);
    var hour = today.getHours();
    var minute = today.getMinutes();
    var second = today.getSeconds();
    var hourString = ( hour < 10)? ('0'+ hour) : ('' + hour);
    var minString = ( minute < 10)? ('0'+ minute) : ('' + minute);
    var secString = ( second < 10)? ('0'+ second) : ('' + second);
    var date = year + '/' + monthString + '/' + dayString;
    var time = hourString + ':' + minString;
    document.getElementById('date').innerText = date;
　	document.getElementById('time').innerText = time;
　	document.getElementById('diary_date').value = date + ' ' + time;
}
window.setInterval('ShowTime()',1000);

// 上傳照片 & 預覽照片
function readURL() {
    var preview = document.getElementById('image');
    var file    = document.querySelector('input[type=file]').files[0];
    var reader  = new FileReader();

    reader.addEventListener("load", function () {
        preview.src = reader.result;
    }, false);

    if (file) {
        reader.readAsDataURL(file);
    }
}

// 是否都填寫完成
function check(){
    var form = document.getElementById('diaryForm');
    var mood = document.getElementById('mood').value;
    if(mood == ''){
        swal("請選擇表情", "", "error");
    }else{
        form.submit();
    }
}
