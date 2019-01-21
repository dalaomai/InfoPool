<%@ page contentType = "text/html; charset=UTF-8" pageEncoding="UTF-8" import="java.util.*" %>
<jsp:useBean id="info" type="com.beans.InfoBean" scope="session"/>

<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    

    <title>showInfo</title>
</head>

<body>

    <table class="table table-striped" id="showInfo_table">
        <thead>
            <tr>
                <th scope="col">title</th>
                <th scope="col">time</th>
                <th scope="col">source</th>
            </tr>
        </thead>
        <tbody>
            <%
            int infoSize = info.getTitle().length;
            for(int i=0; i<infoSize;i++){%>
                <tr>
                    <td scope="row"><a href=<%= info.getHref()[i] %>><%= info.getTitle()[i] %></a></td>
                    <td><%= info.getTime()[i] %></td>
                    <td><a href=<%= info.getUrl()[i] %>><%= info.getWebName()[i] %></a></td>
                </tr>
            <%
            }
            %>
		</tbody>
    </table>
    <nav aria-label="Page navigation">
        <ul class="pagination">
        	<% int nowPage = (int)session.getAttribute("page"); %>
            <li>
                <a href="?page=<%= nowPage-1 %>" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                </a>
            </li>
            <li><a href="?page=0">1</a></li>
            <li><a href="?page=1">2</a></li>
            <li><a href="?page=2">3</a></li>
            <li><a href="?page=3">4</a></li>
            <li><a href="?page=4">5</a></li>
            <li>
                <a href="?page=<%= nowPage+1 %>" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                </a>
            </li>
        </ul>
    </nav>
    <div>
        <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
        <script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"></script>
        <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js"></script>
        <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    </div>
</body>
</html>