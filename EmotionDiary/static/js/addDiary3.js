///////////////////////////////////////
// INITIALIZATION
///////////////////////////////////////

window.onload = function(){
//    thingSelect(t_id);
}

var t_id;
//function thingSelect(t_id){
//    // msg_block
//    var block = document.getElementById('list');
//    var b_child = block.children;
//    for(var n=0; n<b_child.length; n++){
//        console.log(n);
//        console.log(b_child[n]);
//        for(var i=0; i<b_child[0].children[1].children.length; i++){
//            console.log(b_child[n].children[1].children[i]);
//            b_child[n].children[1].children[i].onclick = function(){
//            // this是当前激活的按钮，在这里可以写对应的操作
//                if(this.className == 'btn1'){
//                    this.className = 'btn2';
//                    t_id = this.id;
////                    b_child[n].children[0].children[1].value = this.id;
//                    var btn = document.getElementsByClassName('btn2');
//                    for(var j=0; j<btn.length; j++){
//                        if(btn[j].id!=t_id){
//                            btn[j].className = 'btn1';
//                        }
//                    }
//                }
//            }
//        }
//    }
//}
//    for(var i=0; i<g_child.length; i++){
//        g_child[i].onclick = function(){
//            // this是当前激活的按钮，在这里可以写对应的操作
//            if(this.className == 'btn1'){
//                this.className = 'btn2';
//                t_id = this.id;
//                document.getElementById('test').value = this.id;
//                var btn = document.getElementsByClassName('btn2');
//                for(var j=0; j<btn.length; j++){
//                    if(btn[j].id!=t_id){
//                        btn[j].className = 'btn1';
//                    }
//                }
//            }
//        }
//    }

function thingSelect(t_id){
    var parent = t_id.parentNode;
    var block = parent.parentNode;
    // 判斷t_id是for中的哪區塊
    for(var i=0; i<parent.children.length; i++){
        for(var j=0; j<parent.children.length; j++){
            if(parent.children[j].id!=t_id){
                parent.children[j].className = 'btn1';
            }
        }
    }
    // t_id.class
    if(t_id.className == 'btn1'){
        t_id.className = 'btn2';
    }
    // 印出所選取的t_id
    block.children[0].children['test'].value = t_id.id;
}

function check(){
    var form = document.getElementById('addDiaryForm');
    var button = document.getElementById('finish_button');
    swal("儲存成功", "", "success", {button:"OK"})
        .then(() => {
            form.submit();
        });
    }
