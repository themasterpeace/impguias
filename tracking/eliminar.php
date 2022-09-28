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

	$id = $_GET['id'];
	$sql = "DELETE FROM usuarios WHERE id = ?";

	$sentencia = $mysqli->prepare($sql);
	$sentencia->bind_param("i", $id);
	$exec = $sentencia->execute();

	if ($exec) {
		header ("Location: controlUsuarios.php");
		die();
	}else{
		echo "ERROR AL ELIMINAR USUARIO";
	}
?>