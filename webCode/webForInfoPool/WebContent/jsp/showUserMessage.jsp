<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="user" type="com.infoPool.bean.User" scope="session"></jsp:useBean>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title></title>
    <script type="text/javascript">
        function isInclude(name){
            var js= /js$/i.test(name);
            var es=document.getElementsByTagName(js?'script':'link');
            for(var i=0;i<es.length;i++) 
            if(es[i][js?'src':'href'].indexOf(name)!=-1)return true;
            return false;
        }
        if (!isInclude("bootstrap.min.css")) {
            var fileref = document.createElement('link');
            fileref.setAttribute("rel", "stylesheet");
            fileref.setAttribute("type","text/css");
            fileref.setAttribute("href","https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css");
            document.getElementsByTagName("head")[0].appendChild(fileref);
        }
    </script>
    <link rel="stylesheet" type="text/css" href="css/showUserMsg.css" />
</head>
<body>
    <div class="form">
        <div class="input-group">
            <span class="input-group-addon">name</span>
            <input type="text" class="form-control" value="${user.userName}" />
        </div>
        <br />
        <br />
        <div class="input-group">
            <span class="input-group-addon">password</span>
            <input type="password" class="form-control" placeholder="Password" />
        </div>
        <br />
        <br />
        <div class="input-group">
            <span class="input-group-addon">wechatId</span>
            <input type="text" class="form-control" value="${user.wechatId}" />
        </div>
        <br />
        <br />
        <div class="input-group">
            <span class="input-group-addon">wechatName</span>
            <input type="text" class="form-control" value="${user.wechatName}" />
        </div>
        <br />
        <br />
        <div class="input-group">
            <span class="input-group-addon">phoneNumber</span>
            <input type="text" class="form-control" value="${user.phoneNumber}" />
        </div>
        <br />
        <br />
        <div class="input-group">
            <span class="input-group-addon">emailAddress</span>
            <input type="text" class="form-control" value="${user.emailAddress}" />
        </div>
        <br /><br />
        <div class="submit">
            <button type="button" class="btn btn-primary">submit</button>
        </div>
    </div>
</body>
</html>
