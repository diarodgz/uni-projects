<?php
session_start();
require_once 'utils.php';

$correo = htmlspecialchars($_POST['correo']) ?? '';

// Guardar datos para reusarlos
$_SESSION['form_data'] = $_POST;

try {
    $db = conectarBD();
    $stmt_e = $db->prepare("SELECT correo FROM empleado e WHERE e.correo = :correo;");
    $stmt_e->bindParam(':correo', $correo);
    $stmt_e->execute();

    if ($stmt_e->fetch() === false) {
        $_SESSION['error'] = 'El empleado no está registrado';
        header('Location: borrar_empleado.php');
        exit();
    }

    $db->beginTransaction();

    $stmt = $db->prepare("
        DELETE FROM transporte
        WHERE correo_empleado = :correo;
    ");
    $stmt->bindParam(':correo', $correo);
    $stmt->execute();

    $stmt2 = $db->prepare("
        DELETE FROM empleado
        WHERE correo = :correo;
    ");
    $stmt2->bindParam(':correo', $correo);
    $stmt2->execute();

    $stmt3 = $db->prepare("
        DELETE FROM persona
        WHERE correo = :correo;
    ");
    $stmt3->bindParam(':correo', $correo);
    $stmt3->execute();

    $db->commit();

    unset($_SESSION['form_data']);
    $_SESSION['success'] = 'Empleado borrado correctamente';
    header('Location: borrar_empleado.php');
    exit();

} catch (Exception $e) {
    if ($db->inTransaction()) $db->rollBack();
    $_SESSION['error'] = 'Empleado no se pudo borrar' . $e;
    header('Location: borrar_empleado.php');
    exit();
}
?>
