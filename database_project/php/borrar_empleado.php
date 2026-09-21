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

?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Eliminar Empleado</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div class="container">
        <h1>Borrar Empleado</h1>
            <form action="procesar_borrar_empleado.php" method="POST" class="formulario">

                <label for="correo">Correo Empleado:</label>
                <input type="text" id="correo" name="correo" value="<?= htmlspecialchars($form_data['correo'] ?? '') ?>"
                placeholder="e.g. nombre@viajes.cl">

                <button type="submit">Borrar Empleado</button>
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