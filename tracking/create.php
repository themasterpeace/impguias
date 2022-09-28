<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="css/index.css">
	<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
	<title>Registro | Transportes JR</title>
</head>
<body>
	<section>
		<div class="box">
			<div class="form">
				<h2>Registro</h2>
				<form action="registrarUser.php" method="POST">
					<div class="inputBx">
						<input type="text" name="usuario" placeholder="Usuario" autocomplete="off">
						<ion-icon name="person-circle-outline"></ion-icon>
					</div>
					<div class="inputBx">
						<input type="text" name="nombre" placeholder="Nombre de Usuario" autocomplete="off">
						<ion-icon name="person-outline"></ion-icon>
					</div>
					<div class="inputBx">
						<input type="password" name="password" placeholder="Contraseña" autocomplete="off">
						<ion-icon name="lock-closed-outline"></ion-icon>
					</div>
					<div class="inputBx">
						<input type="submit" value="Registrar">
					</div>
				</form>
				<p>Ya tienes una <a href="index.php">cuenta</a>.</p>
			</div>
		</div>
	</section>
	<script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
</body>
</html>