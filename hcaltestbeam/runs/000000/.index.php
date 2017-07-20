<!doctype html>
<html>

<head>
  <meta charset="UTF-8">
  <title>Directory Contents</title>
  <script src=".sorttable.js"></script>

  <?php readfile("../../.src/loadflatui_d2.html"); ?>
  <link rel="stylesheet" href="../../.src/style.css">
</head>

<body>
    <div id="container">
        <div class="row">
            <div class="col-md-6"><h3>Run #[Run Number]</h3></div>
    	    <div class="col-md-3"><br><br><h5>Status: [status]</h5></div>
            <div class="col-md-3"><br><br><h5>Date Taken: [date]</h5></div>
        </div>
        <div class="row">
            <div class="col-md-4">Path to raw data: [data file path]</div>
            <div class="col-md-4">Path to processed data file: [processed data file path]</div>
            <div class="col-md-4"><a href="[link to analysis]">Analysis</a></div>
        </div>
	<br>
        <div class="row">
            <div class="col-md-2">Beam file: [beamfile]</div>
            <div class="col-md-2">Trigger: [trigger]</div>
	    <div class="col-md-2">Energy: [energy]</div>
            <div class="col-md-2">Run key: [runkey]</div>
            <div class="col-md-2">Number of events: [numevents]</div>
            <div class="col-md-1">Eta: [eta]</div>
            <div class="col-md-2">Table eta: [tableeta]</div>
            <div class="col-md-1">Phi: [phi]</div>
            <div class="col-md-2">Table phi: [tablephi]</div>
            <div class="col-md-2">Start time: [starttime]</div>
            <div class="col-md-2">End time: [endtime]</div>
        </div>

    </div>

</body>

</html>
