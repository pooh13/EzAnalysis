///////////////////////////////////////
// INITIALIZATION
///////////////////////////////////////

window.onload = function(){
    ShowEmoji();
}

function ShowEmoji(){
    var mood = document.getElementById('mood_btn').value;
    var img = document.getElementById('mood_img');
    if(mood == '4'){
        img.src = '/static/images/Diary/moods/ID051-happy.png';
    }
}
