window.onload = function (e) {
    liff.init(function (data) {
        initializeApp(data);
    });
};

function initializeApp(data) {
    liff.getProfile().then(profile => {
//        document.getElementById('useridfield').textContent = data.context.userId;
//        document.getElementById('displaynamefield').textContent = profile.displayName;
        $("#userid").val(data.context.userId);
        $("#disname").val(profile.displayName);
    });
    if(data.context.userId == ""){
        var button = document.getElementById('userForm');
        button.submit();
        window.alert("Submit");
    }
}
