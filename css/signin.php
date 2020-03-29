<?php 
  ob_start();
  session_start(); ?>

<!DOCTYPE html>
<!-- saved from url=(0040)https://www.discoverci.com/users/sign_in -->
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <script type="text/javascript" src="./signin_files/a3c762919b"></script>
    <script src="./signin_files/nr-1167.min.js.download"></script>
    <script async="" src="./signin_files/analytics.js.download"></script>
    <script>window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","errorBeacon":"bam.nr-data.net","licenseKey":"a3c762919b","applicationID":"535784320","transactionName":"JVlWR0FeXF9UShgHVBBfS1YcQlVAQlFYDUJJWF1E","queueTime":3,"applicationTime":15,"agent":""}</script>

    <title>Sign In | G8T8</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Sign In to access the best, most comprehensive stock data and analysis tools on the web. We aggregate all available stock information so you can spend less time looking for data and more time analyzing data.">
    <link href="https://www.discoverci.com/users/sign_in" rel="canonical">    <meta name="csrf-param" content="authenticity_token">
    <meta name="csrf-token" content="+KDrxmz7YD5SInSxknV8T8EBscDlK4FY0jkrzAWXu2zIVHMwMO5gwfnO+Xf1K8eNE2oQ24DfwlpCyKeAjEUTkg==">

    <link rel="stylesheet" media="all" href="./signin_files/application-f856fa345de0ec2f4fe1dd4f4bf20d11398b4c689a39df184edb3529b69ca4b2.css">
    <script src="./signin_files/application-68273e5f3d04ef1145a286e7de748f4bc42a857705e7de5274c9a62680a53942.js.download"></script>
    <style type="text/css">/* Chart.js */
@-webkit-keyframes chartjs-render-animation{from{opacity:0.99}to{opacity:1}}@keyframes chartjs-render-animation{from{opacity:0.99}to{opacity:1}}.chartjs-render-monitor{-webkit-animation:chartjs-render-animation 0.001s;animation:chartjs-render-animation 0.001s;}</style><style type="text/css"></style>
    <script src="./signin_files/saved_resource"></script>
    <link rel="icon" type="image/png" href="./resources/g8t8.png">
    <meta name="stripe-key" content="pk_live_TeRP9zBRkmBOmKsPmL0lB4Wj">
  </head>

<body class="gray-bg  pace-done">

  <div class="row">
  <div class="col-xs-12">
    <div class="center-brand-container">
      <a href="./home.html"><img height="250" width="250" src="./resources/g8t8.png" alt="Logo"></a>
    </div>
  </div>
  <div class="col-xs-12">
    <div class="loginColumns animated fadeInDown">
      <div class="row">
        <div class="col-md-6 center-block col-centered">
          <div class="ibox-content center-carousel">
            <h3>Sign In</h3>
            <form class="simple_form new_user" method="post" action="">
            
              <div class="form-group">
                <div class="form-group email required user_email">
                  <input class="form-control string email required" autofocus="autofocus" required="required" aria-required="true" placeholder="Username" type="text" name="username" id="username">
                </div>
              </div>
              <div class="form-group">
                <div class="form-group password required user_password">
                  <input class="form-control password required" required="required" aria-required="true" placeholder="Password" type="text" name="password" id="password">
                </div>
              </div>
              <div class="row">
                <div class="col-sm-6">
                  <div class="form-group">
                  <div class="form-group boolean optional user_remember_me"><div class="checkbox"><input value="0" type="hidden" name="user[remember_me]"><label class="boolean optional" for="user_remember_me"><input class="boolean optional" type="checkbox" value="1" name="user[remember_me]" id="user_remember_me">Remember me</label></div></div>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="form-group">
                    <div class="checkbox text-right">
                      <a class="float-right" href="https://www.discoverci.com/users/password/new">Forgot password?</a>
                    </div>
                  </div>
                </div>
              </div>
              <input type="submit" id="signin" value="Sign in" class="btn btn-default btn-primary block full-width m-b font-bold signup-btn" data-disable-with="Sign in">
            </form>          
              
            <?php

              $message="";

              if(count($_POST)>0) {
                $conn = mysqli_connect("localhost","root","","g8t8");
                $result = mysqli_query($conn,"SELECT * FROM users WHERE username='" . $_POST["username"] . "' and password = '". $_POST["password"]."'");
                $count  = mysqli_num_rows($result);
                if($count==0) {
                  $message = "Invalid Username or Password.";
                } else {
                  $_SESSION['username'] = $_POST["username"];
                  header("Location:account.php");
                  ob_end_flush();
                  $message = "Successfully authenticated.";
                }
              }
            ?>
          
          <?php echo "<p align = 'center'>".$message."</p>"; ?>
          
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

</body>
</html>
