<?php
	ini_set('display_errors', 1);
	error_reporting(E_ALL);

	require 'conexion.php';

	$usuario = $_POST['usuario'];
	$nombre = $_POST['nombre'];
	$password = password_hash($_POST['password'], PASSWORD_DEFAULT);
	$tipo_usuario = 2;
	$correcto = false;

	if ($usuario == "" or $nombre == "" or $password == "") {
		echo "Todos los campos son requeridos. Vuelve a intentarlo.";
		die();
	}

	$sql = "INSERT INTO usuarios (id, usuario, nombre, password, tipo_usuario) VALUES (NULL, ?, ?, ?, ?)";

	$sentencia = $mysqli->prepare($sql);
	$sentencia->bind_param("sssi", $usuario, $nombre, $password, $tipo_usuario);
	$exec = $sentencia->execute();

	if ($exec) {
		$correcto = true;
		header("Location: index.php");
		die();
	}
?>