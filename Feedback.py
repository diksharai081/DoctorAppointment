#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

print"""<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Doctor Care | FeedBack</title>

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
	</head>
	<body>
		<nav class="navbar navbar-custom navbar-fixed-top" role="navigation">
			<div class="container-fluid">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse"><span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span></button>
					<a class="navbar-brand" href="Profile.py"><span>Doctor Care &emsp;</span>User FeedBack</a>
					
					
				</div>
			</div><!-- /.container-fluid -->
		</nav>
		<div id="sidebar-collapse" class="col-sm-3 col-lg-2 sidebar">
			
			<ul class="nav menu">
				<li class="active"><a href="Profile.py"><em class="fa fa-dashboard">&nbsp;</em> FeedBack</a></li>
				
				<li class="parent "><a  href="Feedback.py">
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
						<em class="fa fa-pencil"></em>
					</a></li>
					<li class="active">FeedBack Forms</li>
				</ol>
			</div><!--/.row-->
			
			
			<div class="row">
				<div class="col-md-12">
					<div class="panel panel-default">
						
						<div class="panel-body">
							<form class="form-horizontal row-border" action="Manage.py?flg=12" method="post" enctype="multipart/form-data">
								<div class="form-group">
									<label class="col-md-2 control-label">Name</label>
									<div class="col-md-10">
										<input type="text" name="name" class="form-control" placeholder="Enter name...">
									</div>
								</div>
								<div class="form-group">
									<label class="col-md-2 control-label">Mobile</label>
									<div class="col-md-10">
										<input class="form-control" type="text" name="npass" placeholder="Enter Mobile">
									</div>
								</div>
								<div class="form-group">
									<label class="col-md-2 control-label">Message</label>
									<div class="col-md-10">
										<input class="form-control" type="text" name="msg" placeholder="Message">
									</div>
								</div>
								<div class="form-group">
									<label class="col-md-2 control-label"></label>
									<div class="col-md-4">
										<button class="btn btn-primary btn-block btn-lg">Submit FeedBack</button>
									</div>
								</div>
								
							</form>
						</div>
					</div>
				</div>
			</div><!--/.row-->
			
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