 <?php
session_start();
require_once 'utils.php';

$usuario = $_POST['usuario'] ?? '';
$contrasena = $_POST['contrasena'] ?? '';

$db = conectarBD();

$query = "SELECT u.username, u.contrasena
            FROM persona p
            JOIN usuario u ON p.correo = u.correo
            WHERE p.username = :usuario
            AND p.contrasena = :contrasena;";
$stmt = $db->prepare($query);
$stmt->bindParam(':usuario', $usuario);
$stmt->bindParam(':contrasena', $contrasena);
$stmt->execute();

$resultado = $stmt->fetch();

if ($resultado) {
    $_SESSION['usuario'] = $usuario;
    header('Location: main.php');
    exit();
} else {
    header('Location: index.php?error=Usuario no existe o contrasena errónea');
    exit();
}
?>
