<?php
session_start();

if (!isset($_SESSION['usuario'])) {
    header('Location: index.php?error=Debes iniciar sesión');
    exit();
}

$mensaje_error = $_SESSION['error'] ?? null;
$_SESSION['form_data'] = $_POST;
unset($_SESSION['error'], $_SESSION['success'], $_SESSION['form_data']);
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Detalles del Viaje</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div class="container">
        <div class="container">
            <form method="post" action="desplegar_viaje.php" class="formulario">
                <h1>Detalles del Viaje</h1>
                <label for="agenda">Agenda ID:</label>
                <input type="text" id="agenda" name="agenda" placeholder='e.g. 10000' required>
                <button type="submit">Ver</button>
            </form>
            <a href="main.php">Volver al inicio</a>

            <?php if ($mensaje_error): ?>
            <p class="error"><?= htmlspecialchars($mensaje_error) ?></p>
            <?php elseif ($mensaje_success): ?>
                <p class="success"><?= htmlspecialchars($mensaje_success) ?></p>
            <?php endif; ?>
        </div>
            <!-- Aquí se mostrarán los detalles del viaje -->
            <!-- La idea es que rellenen con lo solicitado en la sección 2.3 del enunciado -->
            <!-- Apoyate con los estilos css para que se vea bonito :) -->

        <div>
            <?php
                if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['agenda'])) {
                    require_once 'utils.php';

                    $db = conectarBD();
                    $agenda = htmlspecialchars($_POST['agenda']) ?? '';

                    // Revisar si agenda pertenece a usuario
                    $query_a = "SELECT a.id, p.username FROM agenda a 
                                JOIN persona as p 
                                ON p.correo = a.correo_usuario
                                WHERE a.id = :agenda;";

                    $stmt_a = $db->prepare($query_a);
                    $stmt_a->bindParam(':agenda', $agenda);
                    $stmt_a->execute();
                    $result_a = $stmt_a->fetch(PDO::FETCH_ASSOC);

                    if ($result_a['username'] != $_SESSION['usuario']) {
                        $_SESSION['error'] = 'No tiene acceso a este viaje';
                        header('Location: desplegar_viaje.php');
                        exit();
                    }


                    $query = "SELECT * FROM agenda a WHERE a.id = :agenda;";

                    $stmt = $db->prepare($query);
                    $stmt->bindParam(':agenda', $agenda);
                    $stmt->execute();
                    $result = $stmt->fetch(PDO::FETCH_ASSOC);

                    

                    if ($result) {
                        $_SESSION['success'] = 'Viaje desplegado';
                        // Consulta adicional para obtener referencias cruzadas
                        $query_transport = "SELECT * FROM reserva as r JOIN transporte as t ON r.id = t.id WHERE r.agenda_id = :agenda;";
                        $stmt_transport = $db->prepare($query_transport);
                        $stmt_transport->bindParam(':agenda', $agenda);
                        $stmt_transport->execute();
                        $transport = $stmt_transport->fetchAll(PDO::FETCH_ASSOC);

                        $query_panorama = "SELECT * FROM reserva as r JOIN panorama as p ON r.id = p.id WHERE r.agenda_id = :agenda;";
                        $stmt_panorama = $db->prepare($query_panorama);
                        $stmt_panorama->bindParam(':agenda', $agenda);
                        $stmt_panorama->execute();
                        $panorama = $stmt_panorama->fetchAll(PDO::FETCH_ASSOC);

                        $query_hospedaje = "SELECT * FROM reserva as r JOIN hospedaje as h ON r.id = h.id WHERE r.agenda_id = :agenda;";
                        $stmt_hospedaje = $db->prepare($query_hospedaje);
                        $stmt_hospedaje->bindParam(':agenda', $agenda);
                        $stmt_hospedaje->execute();
                        $hospedaje = $stmt_hospedaje->fetchAll(PDO::FETCH_ASSOC);

                        $query_participante = "SELECT * FROM reserva as r JOIN participante as p ON r.id = p.panorama_id WHERE r.agenda_id = :agenda;";
                        $stmt_participante = $db->prepare($query_participante);
                        $stmt_participante->bindParam(':agenda', $agenda);
                        $stmt_participante->execute();
                        $participante = $stmt_participante->fetchAll(PDO::FETCH_ASSOC);
                        
                        echo "<div>";
                        echo "<table style class='tabla-estandar'>";
                        echo "<tr>";
                        echo "<th>Agenda ID</th>";
                        echo "<th>Organizador</th>";
                        echo "<th>Etiqueta</th>";
                        echo "</tr>";
                        echo "<tr>";
                        echo "<td>". $result['id'] . "</td>";
                        echo "<td>". $result['correo_usuario'] ."</td>";
                        echo "<td>". $result['etiqueta'] . "</td>";
                        echo "</tr>";
                        echo "<tr>";
                        echo "</tr>";
                        echo "</table>";
                        echo "</div>";

                        echo "<div>";
                        echo "<table style class='tabla-estandar'>";
                        echo "<p>Participantes</p>";
                        echo "<tr>";
                        echo "<th>ID</th>";
                        echo "<th>Panorama ID</th>";
                        echo "<th>Nombre</th>";
                        echo "<th>Edad</th>";
                        echo "</tr>";
                        foreach ($participante as $p) {
                            echo "<tr>";
                            echo "<td>". $p['id'] . "</td>";
                            echo "<td>". $p['panorama_id'] ."</td>";
                            echo "<td>". $p['nombre'] . "</td>";
                            echo "<td>". $p['edad'] . "</td>";
                            echo "</tr>";
                        }
                        echo "<tr>";
                        echo "</tr>";
                        echo "</table>";
                        echo "</div>";
                        
                        echo "<div>";
                        echo "<table style class='tabla-estandar'>";
                        echo "<p>Transporte</p>";
                        echo "<tr>";
                        echo "<th>ID</th>";
                        echo "<th>Fecha</th>";
                        echo "<th>Monto</th>";
                        echo "<th>Cantidad Personas</th>";
                        echo "<th>Estado Disponibilidad</th>";
                        echo "<th>Puntos</th>";
                        echo "<th>Correo Empleado</th>";
                        echo "<th>Lugar Origen</th>";
                        echo "<th>Lugar Llegada</th>";
                        echo "<th>Capacidad</th>";
                        echo "<th>Tiempo Estimado</th>";
                        echo "<th>Precio Asiento</th>";
                        echo "<th>Empresa</th>";
                        echo "<th>Fecha Salida</th>";
                        echo "<th>Fecha Llegada</th>";
                        echo "</tr>";
                        foreach ($transport as $t) {
                            echo "<tr>";
                            echo "<td>". $t['id'] . "</td>";
                            echo "<td>". $t['fecha'] ."</td>";
                            echo "<td>". $t['monto'] . "</td>";
                            echo "<td>". $t['cantidad_personas'] . "</td>";
                            echo "<td>". $t['estado_disponibilidad'] . "</td>";
                            echo "<td>". $t['puntos'] . "</td>";
                            echo "<td>". $t['correo_empleado'] . "</td>";
                            echo "<td>". $t['lugar_origen'] . "</td>";
                            echo "<td>". $t['lugar_llegada'] . "</td>";
                            echo "<td>". $t['capacidad'] . "</td>";
                            echo "<td>". $t['tiempo_estimado'] . "</td>";
                            echo "<td>". $t['precio_asiento'] . "</td>";
                            echo "<td>". $t['empresa'] . "</td>";
                            echo "<td>". $t['fecha_salida'] . "</td>";
                            echo "<td>". $t['fecha_llegada'] . "</td>";
                            echo "</tr>";
                        }
                        echo "<tr>";
                        echo "</tr>";
                        echo "</table>";
                        echo "</div>";

                        echo "<div>";
                        echo "<table style class='tabla-estandar'>";
                        echo "<p>Panormas</p>";
                        echo "<tr>";
                        echo "<th>ID</th>";
                        echo "<th>Fecha</th>";
                        echo "<th>Monto</th>";
                        echo "<th>Cantidad Personas</th>";
                        echo "<th>Estado Disponibilidad</th>";
                        echo "<th>Puntos</th>";
                        echo "<th>Empresa</th>";
                        echo "<th>Nombre</th>";
                        echo "<th>Descripción</th>";
                        echo "<th>Capacidad</th>";
                        echo "<th>Ubicación</th>";
                        echo "<th>Duración</th>";
                        echo "<th>Precio Persona</th>";
                        echo "<th>Capacidad</th>";
                        echo "<th>Restricciones</th>";
                        echo "<th>Fecha Panorama</th>";
                        echo "</tr>";
                        foreach ($panorama as $p) {
                            echo "<tr>";
                            echo "<td>". $p['id'] . "</td>";
                            echo "<td>". $p['fecha'] ."</td>";
                            echo "<td>". $p['monto'] . "</td>";
                            echo "<td>". $p['cantidad_personas'] . "</td>";
                            echo "<td>". $p['estado_disponibilidad'] . "</td>";
                            echo "<td>". $p['puntos'] . "</td>";
                            echo "<td>". $p['empresa'] . "</td>";
                            echo "<td>". $p['nombre'] . "</td>";
                            echo "<td>". $p['descripcion'] . "</td>";
                            echo "<td>". $p['capacidad'] . "</td>";
                            echo "<td>". $p['ubicacion'] . "</td>";
                            echo "<td>". $p['duracion'] . "</td>";
                            echo "<td>". $p['precio_persona'] . "</td>";
                            echo "<td>". $p['capacidad'] . "</td>";
                            echo "<td>". $p['restricciones'] . "</td>";
                            echo "<td>". $p['fecha_panorama'] . "</td>";
                            echo "</tr>";
                        }
                        echo "<tr>";
                        echo "</tr>";
                        echo "</table>";
                        echo "</div>";

                        echo "<div>";
                        echo "<table style class='tabla-estandar'>";
                        echo "<p>Hospedajes</p>";
                        echo "<tr>";
                        echo "<th>ID</th>";
                        echo "<th>Fecha</th>";
                        echo "<th>Monto</th>";
                        echo "<th>Cantidad Personas</th>";
                        echo "<th>Estado Disponibilidad</th>";
                        echo "<th>Puntos</th>";
                        echo "<th>Nombre</th>";
                        echo "<th>Ubicación</th>";
                        echo "<th>Precio Noche</th>";
                        echo "<th>Estrellas</th>";
                        echo "<th>Comodidades</th>";
                        echo "<th>Fecha Checkin</th>";
                        echo "<th>Fecha Checkout</th>";
                        echo "<th>Restricciones</th>";
                        echo "</tr>";
                        foreach ($hospedaje as $h) {
                            echo "<tr>";
                            echo "<td>". $h['id'] . "</td>";
                            echo "<td>". $h['fecha'] ."</td>";
                            echo "<td>". $h['monto'] . "</td>";
                            echo "<td>". $h['cantidad_personas'] . "</td>";
                            echo "<td>". $h['estado_disponibilidad'] . "</td>";
                            echo "<td>". $h['puntos'] . "</td>";
                            echo "<td>". $h['nombre_hospedaje'] . "</td>";
                            echo "<td>". $h['ubicacion'] . "</td>";
                            echo "<td>". $h['precio_noche'] . "</td>";
                            echo "<td>". $h['fecha_checkin'] . "</td>";
                            echo "<td>". $h['fecha_checkout'] . "</td>";
                            echo "</tr>";
                        }
                        echo "<tr>";
                        echo "</tr>";
                        echo "</table>";
                        echo "</div>";
                    }else{
                        $_SESSION['error'] = 'La agenda no existe';
                        header('Location: desplegar_viaje.php');
                        exit();
                    }
                }else{
                    echo "<label> </label>";
                }
            ?>
        </div>
    </div>
</body>
</html>
