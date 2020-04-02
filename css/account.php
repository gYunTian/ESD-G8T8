<?php
  session_start();
?>

<html>
    <head>
    <title>Account | G8T8</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <style>
    body {
        font: 20px Montserrat, sans-serif;
        line-height: 1.8;
        color: #f5f6f7;
    }

    p {
      font-size: 20px;
    }

    .margin {margin-bottom: 45px;}

    .bg-1 { 
        background-color: #132235; /* Header */
        color: #ffffff;
        padding: 20px;
    }
    .bg-3 { 
        background-color: #ffffff; /* White */
        color: #555555;
        margin: 50px;
    }
    .bg-4 { 
        background-color: #132235; /* Footer */
        color: #fff;
    }
    .container-fluid {
        padding-top: 50px;
        padding-bottom: 50px;
    }

    thead {
    color: black;
    }

    tbody {
    color: black;
    text-align: center;
    }

    #left {
      align-self: center;
    }

    </style>

    <script>
          function startDate() {
            var today = new Date();
            var dd = String(today.getDate()).padStart(2, '0');
            var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0
            var yyyy = today.getFullYear();
            var h = today.getHours();
            var m = today.getMinutes();
            var s = today.getSeconds();
            m = checkTime(m);
            s = checkTime(s);
            document.getElementById('txt').innerHTML =
            dd + "/" + mm + "/" + yyyy + "  " + h + ":" + m + ":" + s;
            //var t = setTimeout(startTime, 500);
          }
          function checkTime(i) {
            if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
            return i;
          }
    </script>

</head>
<body onload="startDate()">

<div class="container-fluid bg-1 text-center" style="padding: 0px !important;">
  <a href="./home.php"><img height="150" width="150" alt="G8T8 Logo" class="img-responsive logo-img" src="./resources/g8t8.png"></a>
  <div id="report-search">
  <div class="col-md-4"></div>
    <div class="col-md-3" style="padding:0px; margin=0px">
      <div class="easy-autocomplete eac-description" style="width: 553px;">
        <input placeholder="Search Stock Ticker" id='search_input' class="form-control input-lg topnavbar-search input-shadow b-r-md" id="report-search" type="text" name="term" autocomplete="off">
          <div class="easy-autocomplete-container" id="eac-container-report-search"></div>
      </div>
    </div>
    <div class="col-md-1"><button type="submit" id='search_ticker' class="btn btn-primary input-lg btn-primary-shadow subscribe-button">Search</button></div>
  </div>
  <span id='error' style="font-size: large; display: none; margin-top: 5px; color: rgb(223, 62, 94);">Ticker not found!</span>
</div>






<!-- First Container -->
<div class="container-fluid bg-1 text-center" style="padding: 0px !important;">
  <h1 class="margin">Hello, <?php 
    if (isset($_SESSION['username'])) { 
      echo ucfirst($_SESSION['username']);
    } 
    else {
      echo '<a href="./signin.php">Not Logged in</a>';
    }
    ?></h1>
  <div class="col-md-12 center-block col-centered" style="padding: 5px;font-size: 80%" id="txt"></div>
</div>

<div class="container-fluid bg-3 text-center" style="padding: 10px !important;">
<div class="container">
  <h2> Transaction Stocks </h2> </br>  
  <table class="table table-striped">
    <thead>
      <tr>
        <th style="text-align:center">Bought/Sold</th>
        <th style="text-align:center">Stock Ticker</th>
        <th style="text-align:center">Qty</th>
        <th style="text-align:center">Price</th>
        <th style="text-align:center">Current Price</th>
      </tr>
    </thead>
    <tbody>
      <!-- <tr>
        <td>Bought</td>
        <td>MMM</td>
        <td>1</td>
        <td>$132.34</td>
        <td>$123.34</td>
      </tr>
      <tr>
        <td>Bought</td>
        <td>MMM</td>
        <td>1</td>
        <td>$132.34</td>
        <td>$123.34</td>
      </tr>
      <tr>
        <td>Bought</td>
        <td>MMM</td>
        <td>1</td>
        <td>$132.34</td>
        <td>$123.34</td>
      </tr> -->
    </tbody>
  </table>
</div>
</div>

    

<!-- Footer -->
<footer class="container-fluid bg-4 text-left">
  <p>© 2020 G8T8</p> 
</footer>

</body> 

<script type="text/javascript" src="./scripts/check.js"></script>
<script type="text/javascript" src="./scripts/account.js"></script>
</html>


