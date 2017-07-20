<!doctype html>
<html>

<head>
  <meta charset="UTF-8">
  <title>Directory Contents</title>
  <script src=".sorttable.js"></script>

  <?php readfile("../.src/loadflatui_d0.html"); ?>
  <link rel="stylesheet" href=".src/style.css">
</head>

<body>
    <div id="container">
        <h1>Hcal testbeam 2017</h1>
        <h2>(site under construction)</h2>
Beam file	Trigger	Energy	Run key	Number of events	Eta	Table eta	Phi	Table phi	Start time	End time
        <div class="row">
            <div class="col-md-6"><h3>[Run Number]</h3></div>
            <div class="col-md-3">Status</div>
            <div class="col-md-3">Date Taken</div>
        </div>
        <div class="row">
            <div class="col-md-4">Path to raw data</div>
            <div class="col-md-4">Path to processed data file</div>
            <div class="col-md-4">Analysis</div>
        </div>
        <div class="row">
            <div class="col-md-2">Beam file</div>
            <div class="col-md-1">Trigger Energy</div>
            <div class="col-md-2">Run key</div>
            <div class="col-md-1">Number of events</div>
            <div class="col-md-1">Eta</div>
            <div class="col-md-1">Table eta</div>
            <div class="col-md-1">Phi</div>
            <div class="col-md-1">Table phi</div>
            <div class="col-md-1">Start time</div>
            <div class="col-md-1">End time</div>
        </div>


        <?php
        //format of inputs file:
        //[Runnumber] [Analysis link] [Status] [Date of run]
        $runnum="002529"; //from data file
        $analysisref="."; //from whether analysis files exist
        $status="Good"; //input by the shifter
        $datetaken="2017-02-29"; //from data file last modified


        $files = array_diff(scandir('./rawdata'), array('.', '..'));
        for($index=0; $index < 5; $index++) {
            print("
            <div class=\"row\">
                <div class=\"col-md-3\">$runnum<small>(detail)</small></div>
                <div class=\"col-md-3\">$analysisref</div>
                <div class=\"col-md-3\">$status</div>
                <div class=\"col-md-3\">$datetaken</div>
            </div>");
        }


        ?>


    </div>

</body>

</html>
