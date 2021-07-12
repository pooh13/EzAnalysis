///////////////////////////////////////
// INITIALIZATION
///////////////////////////////////////

window.onload = function(){
    genderSelect(g_id);
    jobSelect(j_id);
}

function check(){
    var form = document.getElementById('userForm');
    var username = document.getElementById('disname').value;

    if(username == 0){
        swal("請填寫名字", "", "error");
    }
    else{
        swal("儲存成功", "", "success", {button:"OK"})
            .then(() => {
                form.submit();
            });
    }

}

// 選取性別
var g_id;
function genderSelect(g_id) {
    var arr = document.getElementsByName('gender_btn');
    var user_gen = document.getElementById('gender').value;

    if(user_gen == 'M'){
        document.getElementsByTagName('button').G1.className='btn2';
    }else if(user_gen == 'F'){
        document.getElementsByTagName('button').G2.className='btn2';
    }

    for(var i = 0;i<arr.length;i++){
        arr[i].onclick = function(){
            //this是当前激活的按钮，在这里可以写对应的操作
            if(this.className == 'btn1'){
                this.className = 'btn2';
                g_id = this.id;
                document.getElementById('gender').value = this.value;
                var btn = document.getElementsByClassName('btn2');
                for(var j=0;j<btn.length;j++){
                    if(btn[j].id!=g_id){
                    btn[j].className = 'btn1';
                    }
                }
            }
        }
    }

}

// 選取職業
var j_id;
function jobSelect(j_id){
    var arr = document.getElementsByName('job_btn');
    var user_job = document.getElementById('job').value;

    if(user_job == 'C001'){
        document.getElementsByTagName('button').C001.className='btn4';
    }else if(user_job == 'C002'){
        document.getElementsByTagName('button').C002.className='btn4';
    }else if(user_job == 'C003'){
        document.getElementsByTagName('button').C003.className='btn4';
    }else if(user_job == 'C004'){
        document.getElementsByTagName('button').C004.className='btn4';
    }else if(user_job == 'C005'){
        document.getElementsByTagName('button').C005.className='btn4';
    }else if(user_job == 'C006'){
        document.getElementsByTagName('button').C006.className='btn4';
    }else if(user_job == 'C007'){
        document.getElementsByTagName('button').C007.className='btn4';
    }else if(user_job == 'C008'){
        document.getElementsByTagName('button').C008.className='btn4';
    }else if(user_job == 'C009'){
        document.getElementsByTagName('button').C009.className='btn4';
    }

    for(var i = 0;i<arr.length;i++){
        arr[i].onclick = function(){
            //this是当前激活的按钮，在这里可以写对应的操作
            if(this.className == 'btn3'){
                this.className = 'btn4';
                j_id = this.id;
                document.getElementById('job').value = this.value;
                var btn = document.getElementsByClassName('btn4');
                for(var j=0;j<btn.length;j++){
                    if(btn[j].id!=j_id){
                    btn[j].className = 'btn3';
                    }
                }
            }
        }
    }
}
