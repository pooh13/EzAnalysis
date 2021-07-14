///////////////////////////////////////
// INITIALIZATION
///////////////////////////////////////

window.onload = function(){
    showEmoji();
    emojiSelect(e_id);
    showThing();
}

// 選擇心情 Mood
function showEmoji() {
    var btn = document.getElementById('mood_btn');
    var mood = document.getElementById('mood_btn').value;
    var img = document.getElementById('mood_img');
    if(mood == '5'){
        img.src = '/static/images/moods/ID051-joy.png';
    }else if(mood == '4'){
        img.src = '/static/images/moods/ID051-happy.png';
    }else if(mood == '3'){
        img.src = '/static/images/moods/ID051-neutral.png';
    }else if(mood == '2'){
        img.src = '/static/images/moods/ID051-sad.png';
    }else {
        img.src = '/static/images/moods/ID051-cry.png';
    }

    btn.onclick = function() {
        swal({
     		title: '今天心情如何呢？',
     		html: '<button id="joy_btn" name="emoji_btn" type="button" class="btn1" value="5"><img class="emoji_img" src="/static/images/moods/ID051-joy.png"></button><button id="happy_btn" name="emoji_btn" type="button" class="btn1" value="4"><img class="emoji_img" src="/static/images/moods/ID051-happy.png"></button><button id="neutral_btn" name="emoji_btn" type="button" class="btn1" value="3"><img class="emoji_img" src="/static/images/moods/ID051-neutral.png"></button><button id="sad_btn" name="emoji_btn" type="button" class="btn1" value="2"><img class="emoji_img" src="/static/images/moods/ID051-sad.png"></button><button id="cry_btn" name="emoji_btn" type="button" class="btn1" value="1"><img class="emoji_img" src="/static/images/moods/ID051-cry.png"></button>',
     	});
    }
}

var e_id;
function emojiSelect(e_id) {
    var arr = document.getElementsByName('emoji_btn');
    for(var i=0; i<arr.length; i++){
        arr[i].onclick = function(){
            //this是当前激活的按钮，在这里可以写对应的操作
            if(this.className == 'btn1'){
                this.className = 'btn2';
                e_id = this.id;
//                document.getElementById('mood').value = this.value;
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

// 做了什麼 Thing
function showThing() {
    var btn = document.getElementById('thing_btn');
    btn.onclick = function() {
        swal({
     		title: '那今天做了什麼呢？',
     		html: '<div id="shopping" class="things"><button id="shopping_btn" type="button" name="thing_btn" class="btn3" value="T001"><img class="thing_img" src="/static/images/things/shopping-bag.png"></button><div class="thing_text">購物</div></div><div id="eat" class="things"><button id="eat_btn" type="button" name="thing_btn" class="btn3" value="T002"><img class="thing_img" src="/static/images/things/fast-food.png"></button><div class="thing_text">美食</div></div><div id="friend" class="things"><button id="friend_btn" type="button" name="thing_btn" class="btn3" value="T003"><img class="thing_img" src="/static/images/things/friends.png"></button><div class="thing_text">朋友</div></div><div id="game" class="things"><button id="game_btn" type="button" name="thing_btn" class="btn3" value="T004"><img class="thing_img" src="/static/images/things/joystick.png"></button><div class="thing_text">玩遊戲</div></div><div id="sport" class="things"><button id="sport_btn" type="button" name="thing_btn" class="btn3" value="T005"><img class="thing_img" src="/static/images/things/sport.png"></button><div class="thing_text">運動</div></div><div id="favourite" class="things"><button id="favourite_btn" type="button" name="thing_btn" class="btn3" value="T006"><img class="thing_img" src="/static/images/things/favourite.png"></button><div class="thing_text">約會</div></div><div id="clean" class="things"><button id="clean_btn" type="button" name="thing_btn" class="btn3" value="T007"><img class="thing_img" src="/static/images/things/broom.png"></button><div class="thing_text">清潔</div></div><div id="travel" class="things"><button id="travel_btn" type="button" name="thing_btn" class="btn3" value="T008"><img class="thing_img" src="/static/images/things/luggage.png"></button><div class="thing_text">旅行</div></div><div id="work" class="things"><button id="work_btn" type="button" name="thing_btn" class="btn3" value="T009"><img class="thing_img" src="/static/images/things/briefcase.png"></button><div class="thing_text">工作</div></div><div id="relax" class="things"><button id="relax_btn" type="button" name="thing_btn" class="btn3" value="T010"><img class="thing_img" src="/static/images/things/relaxing.png"></button><div class="thing_text">放鬆</div></div><div id="party" class="things"><button id="party_btn" type="button" name="thing_btn" class="btn3" value="T011"><img class="thing_img" src="/static/images/things/confetti.png"></button><div class="thing_text">派對</div></div><div id="reading" class="things"><button id="reading_btn" type="button" name="thing_btn" class="btn3" value="T012"><img class="thing_img" src="/static/images/things/open-book.png"></button><div class="thing_text">閱讀</div></div><div id="movie" class="things"><button id="movie_btn" type="button" name="thing_btn" class="btn3" value="T013"><img class="thing_img" src="/static/images/things/video-player.png"></button><div class="thing_text">看電影</div></div><div id="other" class="things"><button id="other_btn" type="button" name="thing_btn" class="btn3" value="T014"><img class="thing_img" src="/static/images/things/add.png"></button><div class="thing_text">其他</div></div>',
     	});
    }
}
