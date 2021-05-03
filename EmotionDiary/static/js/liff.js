function initializeApp(data) {
        $("#userid").val(data.context.userId);
      }

      $(function() {
        liff.init(function(data) {
          initializeApp(data);
        });

        $("#ButtonGetProfile").click(function() {
          liff.getProfile().then(profile => {
            $("#UserInfo").val(profile.displayName);
            alert("done");
          });
        });

        $("#ButtonSendMsg").click(function() {
          liff
            .sendMessages([
              {
                type: "text",
                text: $("#msg").val()
              }
            ])
            .then(() => {
              alert("done");
              liff.closeWindow(); // 關掉頁面
            });
        });
      });
