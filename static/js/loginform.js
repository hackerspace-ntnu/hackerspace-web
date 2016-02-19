$(function() {
    var showLogin = false;
    $('#loginform').addClass('loginStill');
    $('#status').click(function() {
        showLogin = !showLogin;
        $('#loginform').removeClass('loginStill');
        if (showLogin) {
            $('#loginform').removeClass('loginOut');
            $('#loginform').addClass('loginIn');
            $('#loginform').css('display', 'inline');
        } else {
            $('#loginform').removeClass('loginIn');
            $('#loginform').addClass('loginOut');
            setTimeout(function () {
              $('#loginform').css('display', 'none');
            }, 500);
        }
    });
});
