function tableCreate() {
  var body = document.getElementsByTagName('body')[0];
  var tbl = document.createElement('table');
  tbl.setAttribute('class', "appGrid");
  var tbdy = document.createElement('tbody');
  for (var i = 0; i < 15; i++) {
    var tr = document.createElement('tr');
    for (var j = 0; j < 15; j++) {
        var td = document.createElement('td');
		
		var tmpimg = document.createElement("img"); tmpimg.src = "https://cdn.discordapp.com/emojis/515873857526300685.png";
        td.appendChild(tmpimg)
        tr.appendChild(td)
    }
    tbdy.appendChild(tr);
  }
  tbl.appendChild(tbdy);
  document.getElementById("centerdiv").appendChild(tbl)
}
tableCreate();