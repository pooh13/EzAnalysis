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
          $('#userid').val(profile.userId);
          $('#disname').val(profile.displayName);
          window.location.replace('https://f1a089c5d606.ngrok.io/AI_analyze/editUser/' + profile.userId)
        })
    })
}
