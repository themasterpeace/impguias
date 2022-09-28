<?php 
    ini_set('display_errors', 1);
    error_reporting(E_ALL);

    require 'conexion.php';

    session_start();

    if (!isset($_SESSION['id'])) {
        header("location: index.php");
    }

    $nombre = $_SESSION['nombre'];
    $tipo_usuario = $_SESSION['tipo_usuario'];

    $sql = "SELECT id, usuario, nombre, tipo_usuario FROM usuarios";
    $sentencia = $mysqli->prepare($sql);
    $sentencia->execute();

    $resultadoSet = $sentencia->get_result();
   
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
					<span><?php echo htmlspecialchars($nombre); ?> </span><ion-icon name="person-circle-outline"></ion-icon>
				</div>
			</div>
			<div class="details">
				<div class="recentOrders">
					<div class="cardHeader">
						<h2>Control Usuarios</h2>
					</div>
					<table>
						<thead>
							<tr>
								<td>#</td>
								<td>Usuario</td>
								<td>Nombre</td>
								<td>Tipo Usuario</td>
								<td></td>
								<td></td>
							</tr>
						</thead>
							<tbody>
								<?php while ($resultado = $resultadoSet->fetch_array()) { ?>
									<tr>
										<td><?php echo htmlspecialchars($resultado['id']);?></td>
										<td><?php echo htmlspecialchars($resultado['usuario']);?></td>
										<td><?php echo htmlspecialchars($resultado['nombre']);?></td>
										<td>
											<?php 
												if ($resultado['tipo_usuario'] == 1) {
													echo 'Administrador';
												}elseif ($resultado['tipo_usuario'] == 2) {
													echo "Usuario Estándar";
												}
											?>
										</td>
										<td><a href="editar.php?id=<?php echo htmlspecialchars($resultado['id']); ?>" class="btnEditar">Editar</a></td>
										<td><a href="eliminar.php?id=<?php echo htmlspecialchars($resultado['id']); ?>" class="btnEliminar">Eliminar</a></td>
									</tr>
								<?php } ?>
							</tbody>
					</table>
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