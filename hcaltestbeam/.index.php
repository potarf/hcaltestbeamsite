<!doctype html>
<html>

<head>
  <meta charset="UTF-8">
  <title>Directory Contents</title>
  <script src=".sorttable.js"></script>

  <?php readfile(".src/loadflatui_d0.html"); ?>
  <link rel="stylesheet" href=".src/style.css">
</head>

<body>
    <div id="container">
        <h1>Hcal testbeam 2017 (site under construction)</h1>

        <div class="row">
            <div class="col-md-3">Run Number <small>(detail)</small></div>
            <div class="col-md-3">Analysis</div>
            <div class="col-md-3">Status</div>
            <div class="col-md-3">Date Taken</div>
        </div>

        <?php
        //format of inputs file:
        //[Runnumber] [Analysis link] [Status] [Date of run]
        $runnum="002529";
        $analysisref=".";
        $status="Good";
        $datetaken="2017-02-29";

        for($index=0; $index < 5; $index++){
            print("        <div class="row">
                        <div class="col-md-3">$runnum<small>(detail)</small></div>
                        <div class="col-md-3">$analysisref</div>
                        <div class="col-md-3">$status</div>
                        <div class="col-md-3">$datetaken</div>
                    </div>");
        }


        ?>


    </div>

</body>

</html>
