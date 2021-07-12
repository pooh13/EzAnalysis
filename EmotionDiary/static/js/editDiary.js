///////////////////////////////////////
// INITIALIZATION
///////////////////////////////////////

window.onload = function(){
    ShowEmoji();
}

function ShowEmoji() {
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
            title: "test",
            ImageUrl: "/static/images/moods/ID051-joy.png",
            ImageSize: "30x30",
        });
    }
}
