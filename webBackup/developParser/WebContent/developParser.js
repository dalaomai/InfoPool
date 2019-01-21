function get(url, cfunc) {
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = cfunc;
    xmlhttp.open("GET", url, true);
    xmlhttp.send(null);

}

function post(url, cfunc, data) {
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = cfunc;
    xmlhttp.open("POST", url, true);
    xmlhttp.send(data);

}

function urlChange() {
	var url = 'getResource?url='+document.getElementById("url").value;
    get(url, function () {
        if (xmlhttp.readyState == 4) {
            document.getElementById("textR").value = xmlhttp.responseText;
        } else {
            document.getElementById("textR").value = "error";
        }
    });
}

function patternChange(){
    var url = 'pattern';
    var data = {
        "url": document.getElementById("url").value,
        "webname": document.getElementById("webname").value,
        "type": document.getElementById("type").value,
        "pattern": document.getElementById("pattern").value,
        "title": document.getElementById("title").value,
        "href": document.getElementById("href").value,
        "time": document.getElementById("time").value,
        "textR": document.getElementById("textR").value
    };
    data = JSON.stringify(data);
    //data = JSON.parse(data);

    post(url,function(){
        if (xmlhttp.readyState == 4) {
            var data = JSON.parse(xmlhttp.responseText);
            var value = null;
            document.getElementById("info_list").value =JSON.stringify( data["info_list"][0]);
            value = "";
            for (var i = 0; i < data["info_node"].length; i++) {
                value = value + "\n\n\n" + data["info_node"][i];
            }
            document.getElementById("info_node").value = value;
        } else {
            document.getElementById("info_node").value = "error";
        }
    },data);
}

function selectText() {
    var selection = window.getSelection();
    document.getElementById('pattern').value = selection.toString();
}

function replaceText() {
    var selection = window.getSelection();
    switch (document.getElementById('replace').value) {
        case '0':
            document.getElementById('pattern').value = document.getElementById('pattern').value.replace(selection.toString(), '[\\s\\S]*?');
            break;
        case '1':
            document.getElementById('pattern').value = document.getElementById('pattern').value.replace(selection.toString(), '([\\s\\S]*?)');
            break;
        case '2':
            document.getElementById('pattern').value = document.getElementById('pattern').value.replace(selection.toString(), '([0-9]{4}-[0-9]{2}-[0-9]{2})');
            break;
    }
    
}

window.onload = function () {
    document.getElementById("url").value = "http://www.fskw.gov.cn/tzgg/";
    document.getElementById("webname").value = "佛山市科学技术局";
    document.getElementById("pattern").value = "<li><span>[\\s\\S]*?([0-9]{4}-[0-9]{2}-[0-9]{2})[\\s\\S]*?href=\"([\\s\\S]*?)\"[\\s\\S]*?title=\"([\\s\\S]*?)\">[\\s\\S]*?</li>";
    document.getElementById("title").value = "2";
    document.getElementById("href").value = "1";
    document.getElementById("time").value = "0";
    patternChange();
    urlChange();
}