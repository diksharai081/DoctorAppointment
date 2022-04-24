#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","doctorappointment")
cursor=db.cursor()

cursor.execute("select * from adddoctor")
data=cursor.fetchall()

print"""<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Doctor Appointment | All Doctor</title>
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<link href="css/font-awesome.min.css" rel="stylesheet">
		<link href="css/datepicker3.css" rel="stylesheet">
		<link href="css/bootstrap-table.css" rel="stylesheet">
		<link href="css/styles.css" rel="stylesheet">
		
		<style id="hide-theme">
			body{
				display:none;
			}
		</style>
		<script type="text/javascript">
			function setTheme(name){
				var theme = document.getElementById('theme-css');
				var style = 'css/theme-' + name + '.css';
				if(theme){
					theme.setAttribute('href', style);
				} else {
					var head = document.getElementsByTagName('head')[0];
					theme = document.createElement("link");
					theme.setAttribute('rel', 'stylesheet');
					theme.setAttribute('href', style);
					theme.setAttribute('id', 'theme-css');
					head.appendChild(theme);
				}
				window.localStorage.setItem('lumino-theme', name);
			}
			var selectedTheme = window.localStorage.getItem('lumino-theme');
			if(selectedTheme) {
				setTheme(selectedTheme);
			}
			window.setTimeout(function(){
					var el = document.getElementById('hide-theme');
					el.parentNode.removeChild(el);
				}, 5);
		</script>
		<link href="https://fonts.googleapis.com/css?family=Montserrat:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">
	
	</head>
	<body>
		<nav class="navbar navbar-custom navbar-fixed-top" role="navigation">
			<div class="container-fluid">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse"><span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span></button>
					<a class="navbar-brand" href="Dashboard.py"><span>Doctor Care &emsp;</span>Dashboard</a>
					
					
				</div>
			</div><!-- /.container-fluid -->
		</nav>
		<div id="sidebar-collapse" class="col-sm-3 col-lg-2 sidebar">
			
			<ul class="nav menu">
				<li class="active"><a href="Dashboard.py"><em class="fa fa-dashboard">&nbsp;</em> Dashboard</a></li>
				
				<li class="parent "><a data-toggle="collapse" href="#">
					<em class="fa fa-pencil">&nbsp;</em>Doctor Management<span data-toggle="collapse" href="#sub-item-1" class="icon pull-right"><i class="fa fa-plus"></i></span>
					</a>
					<ul class="children collapse" id="sub-item-1">
					    <li><a class="" href="AddDoctor.py">
							Add Doctor
						</a></li>
						<li><a class="" href="AllDoctor.py">
							All Doctor
						</a></li>
						
					</ul>
					
				</li>
				<li class="parent "><a  href="AllAppointment.py">
					<em class="fa fa-phone">&nbsp;</em>All Appointment<span  class="icon pull-right"></span>
					</a>
				</li>
				<li class="parent "><a  href="UserAppointment.py">
					<em class="fa fa-phone">&nbsp;</em>User All Appointment<span  class="icon pull-right"></span>
					</a>
				</li>
				<li class="parent "><a  href="AllContact.py">
					<em class="fa fa-phone">&nbsp;</em>All Contact<span  class="icon pull-right"></span>
					</a>
				</li>
				<li class="parent "><a  href="ChangePassword.py">
					<em class="fa fa-lock">&nbsp;</em>Change Password<span  class="icon pull-right"></span>
					</a>
				</li>
				<li class="parent "><a  href="../Manage.py?flg=10">
					<em class="fa fa-trash">&nbsp;</em>Logout<span  class="icon pull-right"></span>
					</a>
				</li>
			</ul>
		</div><!--/.sidebar-->
			
			
		<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">
			<div class="row">
				<ol class="breadcrumb">
					<li><a href="#">
						<em class="fa fa-home"></em>
					</a></li>
					<li class="active">All Doctor Data</li>
				</ol>
			</div><!--/.row-->
					
			
			<div class="row">
				
				<div class="col-lg-12">
					
					<div class="panel panel-default">
						
						<div class="panel-body btn-margins">
							<div class="col-md-12">
								<table class="table table-striped table-bordered">
									<thead>
										<tr>
											<th>Doctor ID</th>
											<th>Doctor Name</th>
											<th>Doctor Specilization</th>
											<th>Doctor Area</th>
											<th>Doctor Mobile</th>
											<th>Doctor Clinic Name</th>
											<th>Doctor Work Exp</th>
											<th>Address</th>
											<th>Date Time</th>
											<th>Action</th>
										</tr>
									</thead>
							
									<tbody>"""
for row in data:							
  print"""<tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
	<td><a href="../Manage.py?delid=%s&&flg=7"><i class="fa fa-trash text-danger" title="Data Delete"></i><a/></td>
  </tr>"""%(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[0])									
																				
									
print"""</tbody>
								</table>
							</div>
						</div>
					</div><!-- /.panel-->
				</div><!-- /.col-->
				
			</div>	
				
				
				
				
	<div class="col-sm-12">
				<p class="back-link"><b>Powered By :</b><a href="https://www.digicoders.in" target="_blank"><b> Diksha Rai(Kaushambi)</b></a></p>
			</div>
		</div><!-- /.row -->
		</div><!--/.main-->
		
		<script src="js/jquery-1.11.1.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="js/chart.min.js"></script>
		<script src="js/chart-data.js"></script>
		<script src="js/easypiechart.js"></script>
		<script src="js/easypiechart-data.js"></script>
		<script src="js/bootstrap-datepicker.js"></script>
		<script src="js/custom.js"></script>
		
		<script>
			window.onload = function () {
				var chart1 = document.getElementById("line-chart").getContext("2d");
				window.myLine = new Chart(chart1).Line(lineChartData, {
				responsive: true,
				scaleLineColor: "rgba(0,0,0,.2)",
				scaleGridLineColor: "rgba(0,0,0,.05)",
				scaleFontColor: "#c5c7cc"
				});
			};
		</script>
		
	</body>
</html>"""
