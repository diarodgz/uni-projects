<?php
function conectarBD() {
    $host = 'bdd1.ing.puc.cl'; // Cambiar al servidor bdd1.ing.puc.cl si se quiere usar el servidor remoto
    $dbname = 'cgrodriguez1.e3'; // Nombre de usuario
    $usuario = 'cgrodriguez1.e3'; // Nombre de usuario
    $clave = '21205868'; // Número de alumno

    try {
        $db = new PDO("pgsql:host=$host;dbname=$dbname", $usuario, $clave);
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $db;
    } catch (PDOException $e) {
        echo "Error de conexión: " . $e->getMessage();
        exit();
    }
}
?>
