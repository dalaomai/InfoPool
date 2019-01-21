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