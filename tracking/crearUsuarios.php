<?php 
    ini_set('display_errors', 0);
    error_reporting(E_ALL);

    require 'conexion.php';

    session_start();

    if (!isset($_SESSION['id'])) {
        header("location: index.php");
    }

    $nombre = $_SESSION['nombre'];
    $tipo_usuario = $_SESSION['tipo_usuario'];
?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Dashboard | Transportes JR</title>
	<link rel="stylesheet" type="text/css" href="css/dashboard.css">
</head>
<body>
	<div class="container">
		<div class="navigation">
			<ul>
				<li>
					<a href="#">
						<span class="icon"><ion-icon name="car-outline"></ion-icon></span>
						<span class="title">TRANSPORTES JR</span>
					</a>
				</li>
				<li>
					<a href="principal.php">
						<span class="icon"><ion-icon name="home-outline"></ion-icon></span>
						<span class="title">Inicio</span>
					</a>
				</li>
				<?php if ($tipo_usuario == 1) {?>
					<li>
						<a href="controlUsuarios.php">
							<span class="icon"><ion-icon name="people-outline"></ion-icon></span>
							<span class="title">Control Usuarios</span>
						</a>
					</li>
					<li>
						<a href="crearUsuarios.php">
							<span class="icon"><ion-icon name="person-add-outline"></ion-icon></span>
							<span class="title">Crear Usuarios</span>
						</a>
					</li>
				<?php } ?>
				<li>
					<a href="logout.php">
						<span class="icon"><ion-icon name="log-out-outline"></ion-icon></span>
						<span class="title">Cerrar Sesión</span>
					</a>
				</li>
			</ul>
		</div>
		<!-- Main -->
		<div class="main">
			<div class="topbar">
				<div class="toggle">
					<ion-icon name="menu-outline"></ion-icon>
				</div>
				<!-- search -->
				<div class="search">
					<label>
						<input type="text" placeholder="Search here">
						<ion-icon name="search-outline"></ion-icon>
					</label>
				</div>
				<!-- userImg -->
				<div class="user">
					<span><?php echo htmlspecialchars($nombre); ?></span><ion-icon name="person-circle-outline"></ion-icon>
				</div>
			</div>
			<div class="details">
				<div class="recentOrders">
					<div class="cardHeader">
						<h2>Crear Usuario</h2>
					</div>
					<div class="formBx">
						<form method="POST" class="form" action="guarda.php">
							<div class="inputBx">
								<label>Usuario:</label><br>
								<input type="text" name="usuario">
							</div>
							<div class="inputBx">
								<label>Contraseña del usuario:</label><br>
								<input type="text" name="password">
							</div>
							<div class="inputBx">
								<label>Nombre del usuario:</label><br>
								<input type="text" name="nombre">
							</div>
							<label>Rol del usuario:</label>
							<div class="select">
								<select name="tipo_usuario">
									<option>----SELECCION EL ROL----</option>
									<option value="2">Usuario Estándar</option>
									<option value="1">Administrador</option>
								</select>
							</div>
							<div class="inputBx">
								<a href="principal.php" class="btn">Regresar</a>
								<input type="submit" name="submit" class="btn" value="Crear">
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</div>
	<script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
	<script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
	<script>
		//MenuToggle
		let toggle = document.querySelector('.toggle');
		let navigation = document.querySelector('.navigation');
		let main = document.querySelector('.main');

		toggle.onclick = function(){
			navigation.classList.toggle('active');
			main.classList.toggle('active');
		}
		//add hovered class in selected list item
		let list = document.querySelectorAll('.navigation li');
		function activeLink() {
			list.forEach((item)=>{
				item.classList.remove('hovered');
			});
			this.classList.add('hovered');
		}
		list.forEach((item)=>{
			item.addEventListener('mouseover', activeLink)
		})
	</script>
</body>
</html>