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
		<title>Doctor Care | User Profile</title>

		<link href="Admin/css/bootstrap.min.css" rel="stylesheet">
		<link href="Admin/css/font-awesome.min.css" rel="stylesheet">
		<link href="Admin/css/datepicker3.css" rel="stylesheet">
		<link href="Admin/css/styles.css" rel="stylesheet">

		<!--Theme Switcher-->
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
		
	<body>
		<nav class="navbar navbar-custom navbar-fixed-top" role="navigation">
			<div class="container-fluid">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse"><span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span></button>
					<a class="navbar-brand" href="Profile.py"><span>Doctor Care &emsp;</span>User Profile</a>
					
					
				</div>
			</div><!-- /.container-fluid -->
		</nav>
		<div id="sidebar-collapse" class="col-sm-3 col-lg-2 sidebar">
			
			<ul class="nav menu">
				<li class="active"><a href="Profile.py"><em class="fa fa-dashboard">&nbsp;</em> Profile</a></li>
			
				<li class="parent "><a  href="FeedBack.py">
					<em class="fa fa-phone">&nbsp;</em>FeedBack<span  class="icon pull-right"></span>
					</a>
				</li>
				<li class="parent "><a  href="ChangePassword.py">
					<em class="fa fa-lock">&nbsp;</em>Change Password<span  class="icon pull-right"></span>
					</a>
				</li>
				<li class="parent "><a  href="Manage.py?flg=13">
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
					<li class="active">See Your Profile | Book Your Appointment</li>
				</ol>
			</div><!--/.row-->
			
			
			<div class="panel panel-container">
				<div class="row">"""
				
for row in data:				
  print"""<div class="col-xs-6 col-md-3 col-lg-3 no-padding">
						<div class="panel panel-teal panel-widget border-right border-bottom">
							<div class="row no-padding">
							    <div class="large"><img src="images/dct.png" class="img-responsive" style="height:120px;width:120px;margin:0px auto;"/></div><br/>
								<div class="text-muted">%s</div><br/>
								<div class="text-muted">%s</div><br/>
								<div class="text-muted">%s</div><br/>
								<a href="UserAppointment.py?id=%s"><div class="text-muted btn btn-primary">Book Appointment</div></a>
							</div>
						</div>
					</div>"""%(row[1],row[2],row[3],row[0])
					
print"""</div><!--/.row-->
			</div>
			
		</div>	<!--/.main-->
		
		<div class="col-sm-12">
				<p class="back-link"><b>Powered By :</b><a href="https://www.digicoders.in" target="_blank"><b>DigiCoders Technologies Pvt Ltd</b></a></p>
		</div>
		</div><!-- /.row -->
		</div><!--/.main-->
		
		<script src="Admin/js/jquery-1.11.1.min.js"></script>
		<script src="Admin/js/bootstrap.min.js"></script>
		<script src="Admin/js/chart.min.js"></script>
		<script src="Admin/js/chart-data.js"></script>
		<script src="Admin/js/easypiechart.js"></script>
		<script src="Admin/js/easypiechart-data.js"></script>
		<script src="Admin/js/bootstrap-datepicker.js"></script>
		<script src="Admin/js/custom.js"></script>
		
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