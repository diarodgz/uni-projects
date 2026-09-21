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
    <title>Reasignar Empleadoe</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div class="container">
        <h1>Reasignar Conductor</h1>
            <form action="procesar_reasignar_empleado.php" method="POST" class="formulario">
                <p>Reasignar Empleado de Transporte</p>

                <label for="reserva_re">Reserva ID Reasignado:</label>
                <input type="text" id="reserva_re" name="reserva_re" value="<?= htmlspecialchars($form_data['reserva_re'] ?? '') ?>"
                placeholder="e.g. 10000">

                <label for="correo_emp">Correo Empleado:</label>
                <input type="text" name="correo_emp" id="correo_emp" value="<?= htmlspecialchars($form_data['correo_emp'] ?? '') ?>"
                placeholder="e.g. nombre@viajes.cl">

                <button type="submit">Reasignar Empleado</button>
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