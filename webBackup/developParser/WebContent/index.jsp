<%@ page contentType = "text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>

<head>
    <title>规则开发</title>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <script type="text/javascript" src="developParser.js"></script>
</head>

    <body>
        <div id="source" style="float:left">
            网址：
            <input type="text" id="url" oninput="urlChange()" />
            网页名
            <input type="text" id="webname" />
            <button type="button" onclick="selectText()">选择</button>
            <br />
            网页源码：<br />
            <textarea id="textR" cols="80" rows="40" style:"overflow-y"></textarea>
        </div>

        <div id="ruleResult" style="float:right">
            <div id="rule">
                <div>
                    type:<input type="text" id="type" value="regular" size="5" />
                    <button type="button" onclick="replaceText()">替换</button>
                    <select id="replace">
                        <option value="0">无用</option>
                        <option value="1">子式</option>
                        <option value="2">时间</option>
                    </select>
                    <h4 aling="center">pattern</h4><br /><textarea id="pattern" oninput="patternChange()" cols="120" rows="4"></textarea>
                </div>
                        <br />
                        <div align="center">
                            <p align="center">position</p>
                            title:<input type="text" name="position" id="title" value="" />
                            href:<input type="text" name="position" id="href" value="" />
                            time:<input type="text" name="position" id="time" value="" />
                        </div>
            </div>

            <div id="result">
                <div style="float:left">
                    info_node<br /><textarea cols="60" rows="30" style="overflow-y" id="info_node"></textarea>
                </div>
                <div style="float:right">
                    info_list<br /><textarea cols="60" rows="30" style="overflow-y" id="info_list"></textarea>
                </div>
            </div>
        </div>

    </body>
</html>