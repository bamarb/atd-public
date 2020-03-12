<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Arista ATD Lab">
    <meta name="author" content="Alex Feigenson (alexf@arista.com)">

    <title>Arista ATD</title>

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/simple-sidebar.css" rel="stylesheet">

</head>

<body>
    <?php $realIP = file_get_contents("http://ipecho.net/plain"); ?>
    <div id="wrapper" class="toggled">

        <!-- Sidebar -->
        <div id="sidebar-wrapper">
            <ul class="sidebar-nav">
                <br>
                <img src="images/logotransparent.png" class="arista-logo">
                <hr class="hr">
                <li>
                    <a href="/labguides/" target="_blank">Lab Guides</a> <a href="/labguides/ATD.pdf" target="_blank">(PDF)</a>
                </li>
                <li>
                    <a href="/guacamole" target="_blank">Lab Frontend</a>
                </li>
                <li>
                    <a href="https://<?php echo $realIP; ?>" target="_blank">CVP</a>
                </li>
                <li>
                    <a href="https://<?php echo $realIP; ?>/telemetry/" target="_blank">CVP Telemetry</a>
                </li>
                <li>
                    <a href="/jenkins" target="_blank">Jenkins</a>
                </li>
            </ul>
        </div>
        <!-- /#sidebar-wrapper -->

        <!-- Page Content -->
        <div id="page-content-wrapper">
            <div class="container-fluid">
                <h1>Arista Test Drive Lab</h1>
                Welcome to the Arista Test Drive Lab! Please use the links on the left to navigate through the lab.
                <br><br>
                <!-- <h2>Usernames and Passwords</h2>
                Use the following usernames and passwords to access the ATD:
                <br>
                <br>
                <table class="table table-striped">
                  <thead> <tr> <th>Device</th> <th>Username</th> <th>Password</th> </tr> </thead>
                  <tbody> <tr>
                    <td>Lab Frontend</td> <td>arista</td> <td>@rista123</td> </tr> <tr>
                    <td>CVP</td> <td>arista</td> <td>arista</td> </tr> <tr>
                    <td>Lab VM SSH</td> <td>arista</td> <td>arista1234</td> </tr>
                    <td>VEOS Instances</td> <td>arista</td> <td>arista</td> </tr>
                  </tbody> </table> -->

                <br>
            </div>
        </div>
        <!-- /#page-content-wrapper -->

    </div>
    <!-- /#wrapper -->

    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/popper/popper.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>

    </script>

</body>

</html>
