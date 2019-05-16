/**
 * 
 */
$(function() {	//通知栏样式
	toastr.options = {
			  "closeButton": true,
			  "debug": false,
			  "newestOnTop": true,
			  "progressBar": true,
			  "positionClass": "toast-top-center",
			  "preventDuplicates": true,
			  "onclick": null,
			  "showDuration": "300",
			  "hideDuration": "1000",
			  "timeOut": "5000",
			  "extendedTimeOut": "1000",
			  "showEasing": "swing",
			  "hideEasing": "linear",
			  "showMethod": "fadeIn",
			  "hideMethod": "fadeOut"
			}
})

function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var dataJson = { "username": username, "password": password };
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "login", false);
    xmlhttp.setRequestHeader("Content-type", "application/json");
    xmlhttp.send(JSON.stringify(dataJson));
    var resultJson = JSON.parse(xmlhttp.responseText);
    if (resultJson.code == 0) {
        toastr.info(resultJson['msg']);
        window.location.href = resultJson['redirect'];
    } else {
        toastr.error(resultJson['msg']);
    }
}