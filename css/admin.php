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
    p {font-size: 20px;}
    .margin {margin-bottom: 45px;}
    .bg-1 { 
        background-color: #132235; /* Header */
        color: #ffffff;
    }
    .bg-3 { 
        background-color: #ffffff; /* White */
        color: #555555;
    }
    .bg-4 { 
        background-color: #132235; /* Footer */
        color: #fff;
    }
    .container-fluid {
        padding-top: 70px;
        padding-bottom: 70px;
    }

    thead {
    color: black;
    }

    tbody {
    color: black;
    text-align: center;
    }

    .button {
    border: none;
    color: white;
    padding: 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    }

    .button1 {
    background-color: #4CAF50; /* Green */
    border-radius: 2px;}

    .button2 {
    background-color: #FF0000; /* Red */
    border-radius: 2px;}

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
            var t = setTimeout(startTime, 500);
          }
          function checkTime(i) {
            if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
            return i;
          }
    </script>

</head>
<body onload="startDate()">
<!-- First Container -->
<div class="container-fluid bg-1 text-center">
  <h1 class="margin">Admin</h1>
  <div class="col-md-12 center-block col-centered" style="padding: 5px;font-size: 80%" id="txt"></div>
</div>

<div class="container-fluid bg-3 text-center">
<div class="container">
  <h2>Admin Page</h2>
  <br>
  <br>            
  <table class="table table-striped">
    <thead>
      <tr>
        <th style="text-align:center"></th>
        <th style="text-align:center"></th>
        <th style="text-align:center"></th>
        <th style="text-align:center"></th>
        <th style="text-align:center"></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td></td>
        <td>Username</td>
        <td>Stock Ticker</td>
        <td>Quantity</td>
        <td>Price</td>
        <td>Clear/Reject</td>
      </tr>

      <tr>
        <td><input type="checkbox" id="vehicle3" name="vehicle3" value="Boat"></td>
        <td>Charlie</td>
        <td>MMM</td>
        <td>1</td>
        <td>$123.23</td>
        <td><button class="button button1">Clear</button>
        <button class="button button2">Reject</button></td>
      </tr>

    </tbody>
  </table>
</div>
</div>

    

<!-- Footer -->
<footer class="container-fluid bg-4 text-left">
  <p>© 2020 G8T8</p> 
</footer>

</body>    
</html>
