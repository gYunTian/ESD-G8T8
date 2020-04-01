<!DOCTYPE html>
<!-- saved from url=(0041)https://www.discoverci.com/company-search -->
<html>
  <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <title>Company Search Results | G8T8</title>
      <link rel="icon" type="image/png" href="./resources/g8t8.png">
      <link rel="stylesheet" media="all" href="./search_files/application-f856fa345de0ec2f4fe1dd4f4bf20d11398b4c689a39df184edb3529b69ca4b2.css">  
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
      <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
      <style>
        
          body {background:grey; font-family:helvetica;font-size:72px;}
          @keyframes blink {
              0% {
                opacity: .2;
              }
              20% {
                opacity: 1;
              }
              100% {
                opacity: .2;
              }
          }

          .saving span {
              animation-name: blink;
              animation-duration: 1.4s;
              animation-iteration-count: infinite;
              animation-fill-mode: both;
          }

          .saving span:nth-child(2) {
              animation-delay: .2s;
          }

          .saving span:nth-child(3) {
              animation-delay: .4s;
          }
          
          .visual {
            border:2px solid;
            font-weight:400;
            font-size: 150%;
            text-align: center;
            border-color:#132235
          }

          .visual2 {
            font-weight:400;
            font-size: 150%;
            text-align: center;
          }

          .color::-webkit-input-placeholder {
              color: #F23535
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
            var t = setTimeout(startTime, 500);
          }
          function checkTime(i) {
            if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
            return i;
          }
          </script>
  </head>

  <body class="gray-bg landing-page body-small  pace-done" onload="startDate()">
    <div class="navbar-wrapper blue-section">
      <nav class="navbar contentNavigation">
          <div class="container-fluid"><div class="navbar-header"><a href="./home.html"><img height="120" width="120" alt="G8T8 Logo" class="img-responsive logo-img" src="./resources/g8t8.png"></a></div>
          </div>
      </nav>
    </div>

    <section class="blue-section">
        <div class="heroContent"><div class="container">
          <div class="row">
            <h1><strong><div class="col-md-12 center-block col-centered" style="padding: 5px" id='company'>Company Name<br></div></strong></h1>
            <div class="col-md-12 center-block col-centered" style="padding: 10px" id="action-bar">           
                <input placeholder="Quantity " id='amt_box' class="form-control input-lg topnavbar-search input-shadow b-r-md" type="number" style="width: 15% !important; display: inline-block !important; margin-right: 1em !important; margin-top: 3px !important;font-size: 20px !important; vertical-align: top !important; height: 43.5px !important;" pattern="[1-9]{3}" min="1" onkeydown="return event.keyCode !== 69 && event.keyCode !== 189">

              <button class="btn btn-outline-visualize nav-btn action" id='buy' name='buy' style="margin-right: 1em; margin-top: 3px; width: 15%; font-size: 20px; color: #71D980; vertical-align: top !important;">Buy</button>

              <button class="btn btn-outline-visualize nav-btn action" id='sell' name='sell' style="margin-right: 1em; margin-top: 3px; width: 15%; font-size: 20px; color: #F23535; vertical-align: top !important;" >Sell</button>

            </div>
            
            </div>
            <p style="font-size:130%;" id='change'><div class="col-md-12 center-block col-centered" style="padding: 5px" id="txt"></div></p>
          </div>
        </div></div>
    </section>

    <div class="container-fluid">
      <div class="col-md-6 visual" id='stock_price' data-toggle="tooltip" title="The price is computed using Dicounted Cash Flow method. This value is based on historical data." style="background-color:#e5e6e6; padding: 80px">Stock</div>

      <div class="col-md-6 visual" id='vix' data-toggle="tooltip" title="The volatility index measures the market volatility. A value above 31 suggest high volatilty. " style="background-color:#e5e6e6; padding: 80px">Volatility Index</div>

      <div class="col-md-6 visual" id='general' data-toggle="tooltip" title="This value measures the general market sentiment. " style="background-color:#e5e6e6; padding: 80px">General Sentiment</div>
      <div class="col-md-6 visual" id='stock_sentiment' data-toggle="tooltip" title="This value measures the specific stock news sentiment." style="background-color:#e5e6e6; padding: 80px">Stock Sentiment</div>
      <div class="col-md-12 visual">
        <div class="col-md-8 visual2" id='indicator' data-toggle="tooltip" title="This graph visualizes the historical price and simple moving average." style="background-color:white; padding: 100px">Chart</div>
        <div class="col-md-4 visual2" id='indicator2' data-toggle="tooltip" title="These indicators measures the price movement." style="background-color:white; padding: 100px">Indicators</div>
      </div>
    </div>
    <!-- <div class="grid-container1" id='top'>
      <div class="grid-item grid-special visual" id='indicator' data-toggle="tooltip" title="This graph visualizes the historical price and simple moving average.">Chart<br><br><br></div>
      <div class="grid-item visual  " id='indicator2' data-toggle="tooltip" title="These indicators measures the price movement.">Indicators<br><br><br></div>
    </div>   -->

    <section class="blue-section contact">
      <div class="container">
        <div class="row"><p class="m-l-sm"><strong>© 2020 G8T8</strong></p>
        </div>
      </div>
    </section>
    
    <script type="text/javascript" src="./scripts/control.js"></script>
  
  </body>
</html>