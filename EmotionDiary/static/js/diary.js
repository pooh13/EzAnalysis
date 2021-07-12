window.onload = function(){
    liff.init({
        liffId: '1655966851-vA7AZYl9'
    })
    .then(() => {
        // do something you want when liff.init finishes
        if(!liff.isLoggedIn()){
            liff.login();
        }
        liff.getProfile().then(profile => {
            window.location.replace('https://d3f74f7f848c.ngrok.io/AI_analyze/menuDiary/' + profile.userId);
        })
    })
}
