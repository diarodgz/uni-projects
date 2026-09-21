<?php
session_start();
require_once 'utils.php';

$reserva = htmlspecialchars($_POST['reserva_re']) ?? '';
$correo = htmlspecialchars($_POST['correo_emp']) ?? '';

// Guardar datos para reusarlos
$_SESSION['form_data'] = $_POST;

try {
    $db = conectarBD();

    $stmt_r = $db->prepare("SELECT id FROM transporte t WHERE t.id = :reserva;");
    $stmt_r->bindParam(':reserva', $reserva);
    $stmt_r->execute();

    $stmt_e = $db->prepare("SELECT correo FROM empleado e WHERE e.correo = :correo;");
    $stmt_e->bindParam(':correo', $correo);
    $stmt_e->execute();

    if ($stmt_r->fetch() === false) {
        $_SESSION['error'] = 'La reserva no existe';
        header('Location: reasignar_empleado.php');
        exit();
    } elseif ($stmt_e->fetch() === false) {
        $_SESSION['error'] = 'El empleado no está registrado';
        header('Location: reasignar_empleado.php');
        exit();
    }

    $db->beginTransaction();

    $stmt = $db->prepare("
        UPDATE transporte
        SET correo_empleado = :correo
        WHERE id = :reserva;
    ");
    $stmt->bindParam(':reserva', $reserva);
    $stmt->bindParam(':correo', $correo);
    $stmt->execute();

    $db->commit();

    unset($_SESSION['form_data']);
    $_SESSION['success'] = 'Empleado reasignado correctamente';
    header('Location: reasignar_empleado.php');
    exit();

} catch (Exception $e) {
    if ($db->inTransaction()) $db->rollBack();
    $_SESSION['error'] = 'Empleado no se pudo reasignar';
    header('Location: reasignar_empleado.php');
    exit();
}
?>
