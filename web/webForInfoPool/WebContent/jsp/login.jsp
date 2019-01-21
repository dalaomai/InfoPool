<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>MP-Login</title>
	<link rel="icon" href="../img/favicon.ico" type="image/x-icon"/>
	<br id="preload-01">
	<br id="preload-02">
	<br id="preload-03">
    <script src="https://cdn.bootcss.com/jquery/2.2.4/jquery.min.js"></script>
    <link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.bootcss.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/css/toastr.min.css" rel="stylesheet">
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/js/toastr.min.js"></script>
    <link rel="stylesheet" href="css/Login.css">
    <script src="js/login.js"></script>
</head>
<body>
    <div class="container">
        <div class="form row">
            <div class="form-horizontal col-md-offset-3" id="login_form">
                <h3 class="form-title">LOGIN</h3>
                <form method="post">	<!-- 登陆表格 -->
					<div class="col-md-9">
                    <div class="form-group">	<!-- 用户名 -->
                        <i class="fa fa-user fa-lg"></i>
                        <input class="form-control required" type="text" placeholder="Username" id="username" name="username" autofocus="autofocus" maxlength="20"/>
                    </div>
                    <div class="form-group">	<!-- 密码 -->
                            <i class="fa fa-lock fa-lg"></i>
                            <input class="form-control required" type="password" placeholder="Password" id="password" name="password" maxlength="8"/>
                    </div>
                    <div class="form-group">	<!-- 是否记住 -->
                        <label class="checkbox">
                            <input type="checkbox" name="remember" value="1"/>Remember Me
                        </label>
                    </div>
                    <div class="form-group col-md-offset-9">	<!-- 提交按钮 -->
                        <button type="submit" class="btn btn-success pull-right" name="submit">Login</button>
                    </div>
				</form>
                </div>
            </div>
        </div>
    </div>
</body>
</html>