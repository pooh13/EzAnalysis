window.onload = function(){
    liff.init({
        liffId: '1655976131-1Qa8zKvQ'
    })
    .then(() => {
        // do something you want when liff.init finishes
        if(!liff.isLoggedIn()){
            liff.login();
        }
        liff.getProfile().then(profile => {
          window.location.replace('https://f1a089c5d606.ngrok.io/AI_analyze/editUser/' + profile.userId)
        })
    })
}
