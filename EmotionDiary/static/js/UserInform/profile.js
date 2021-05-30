window.onload = function(){
    liff.init({ liffId: '1655966851-ekR0DQNG' })
    liff.ready.then(() => {
        // do something you want when liff.init finishes
        if(!liff.isLoggedIn()){
            liff.login();
        }
        liff.getProfile().then(profile => {
          const user = profile.userId;
          $('#userid').val(profile.userId);
          $('#disname').val(profile.displayName);
          location.replace('https://34cef46bea8d.ngrok.io/AI_analyze/editUser/' + profile.userId)
        })
//        const accessToken = liff.getAccessToken();
//        console.log(accessToken)
    })
}
