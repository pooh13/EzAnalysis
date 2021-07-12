window.onload = function(){
    liff.init({
        liffId: '1655966851-ekR0DQNG'
    })
    .then(() => {
        // do something you want when liff.init finishes
        if(!liff.isLoggedIn()){
            liff.login();
        }
        liff.getProfile().then(profile => {
            window.location.replace('https://d3f74f7f848c.ngrok.io/AI_analyze/editUser/' + profile.userId);
        })
    })
}
