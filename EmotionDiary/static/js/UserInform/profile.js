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
          window.location.replace('https://cdf0d3b0252f.ngrok.io/AI_analyze/editUser/' + profile.userId)
        })
    })
}
