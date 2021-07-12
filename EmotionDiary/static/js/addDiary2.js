///////////////////////////////////////
// INITIALIZATION
///////////////////////////////////////

window.onload = function(){
    thingSelect(t_id);
}

var t_id=[];
function thingSelect(t_id) {
    var arr = document.getElementsByName('thing_btn');
    for(var i=0; i<arr.length; i++){
        arr[i].onclick = function(){
            //this是当前激活的按钮，在这里可以写对应的操作
            if(this.className == 'btn1'){
                this.className = 'btn2';
            }else {
                this.className = 'btn1';
            }

            // 列出所選取事情的id
            var choose=[];
            var btn = document.getElementsByClassName('btn2');
            for (var i=0; i<btn.length; i++) {
                choose.push(btn[i].value);
                document.getElementById('chooseThing').value = choose;
            }
            if(choose == ''){
                document.getElementById('chooseThing').value = '';
            }
        }
    }
}

function check(){
    var form = document.getElementById('diaryForm2');
    form.submit();
}
