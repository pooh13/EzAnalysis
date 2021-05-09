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
}
function myMsg(){
    alert("儲存成功!"+ g_id);
}

//window.onload = function (data) {
//    liff.getProfile().then(profile => {
//        document.getElementById('useridfield').textContent = data.context.userId;
//        document.getElementById('displaynamefield').textContent = profile.displayName;
//        $("#disname").val(profile.displayName);
//    });
//}
