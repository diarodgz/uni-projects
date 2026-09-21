<?php
session_start();

if (!isset($_SESSION['usuario'])) {
    header('Location: index.php?error=Debes iniciar sesión');
    exit();
}
$mensaje = $_GET['mensaje'] ?? null;
$mensaje_error = $_SESSION['error'] ?? null;
$mensaje_success = $_SESSION['success'] ?? null;
$form_data = $_SESSION['form_data'] ?? [];

unset($_SESSION['error'], $_SESSION['success'], $_SESSION['form_data']);
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Crear Viaje</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div class="container">
        <h1>Crear nuevo viaje</h1>
        <form action="procesar_crear_viaje.php" method="POST" class="formulario">
            
            <label for="organizador">Organizador (correo):</label>
            <input type="text" id="organizador" name="organizador" required
            value="<?= htmlspecialchars($form_data['organizador'] ?? '') ?>">

            <label for="etiqueta">Etiqueta:</label>
            <input type="text" id="etiqueta" name="etiqueta" required
            value="<?= htmlspecialchars($form_data['etiqueta'] ?? '') ?>">

            <label for="agenda">Agenda ID:</label>
            <input type="text" id="agenda" name="agenda" value="<?= htmlspecialchars($form_data['agenda'] ?? '') ?>"
            placeholder="0 si no existe">

            <label for="reserva">Reserva ID:</label>
            <input type="text" name="reserva" id="reserva" value="<?= htmlspecialchars($form_data['reserva'] ?? '') ?>"
            placeholder="e.g. 10000,10001,10002">

            <p><a href="buscador_reservas.php">Buscador de Reservas</a></p>

            <label for="participantes">Participantes:</label>
            <textarea id="participantes" name="participantes" rows="4"
            value="<?= htmlspecialchars($form_data['participantes'] ?? '') ?>" placeholder='e.g. PanoramaID,Nombre1,edad1;PanoramaID,Nombre2,edad2;...'></textarea>

        <!-- Cuando se crea el viaje, se debe calcular el precio total y puntaje obtenido por este y luego sumarle ese puntaje al usuario  -->

            <button type="submit" name="accion" value="crear">Crear viaje</button>
        </form>
            

        <?php if ($mensaje_error): ?>
            <p class="error"><?= htmlspecialchars($mensaje_error) ?></p>
        <?php elseif ($mensaje_success): ?>
            <p class="success"><?= htmlspecialchars($mensaje_success) ?></p>
        <?php endif; ?>

        <p><a href="main.php">Volver al inicio</a></p>
    </div>
</body>
</html>
