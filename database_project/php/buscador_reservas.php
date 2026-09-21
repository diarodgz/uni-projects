<?php
session_start();

if (!isset($_SESSION['usuario'])) {
    header('Location: index.php?error=Debes iniciar sesión');
    exit();
}

$_SESSION['form_data'] = $_POST;
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
            <form method="post" action="buscador_reservas.php" class="formulario">
                <h1>Buscador de Reservas</h1>
                <label for="fecha_inicio">Fecha de inicio:</label>
                <input type="date" id="fecha_inicio" name="fecha_inicio"
                value="<?= htmlspecialchars($form_data['fecha_inicio'] ?? '') ?>">

                <label for="fecha_fin">Fecha de término:</label>
                <input type="date" id="fecha_fin" name="fecha_fin"
                value="<?= htmlspecialchars($form_data['fecha_fin'] ?? '') ?>">

                <label for="ciudad">Ciudad destino:</label>
                <input type="text" id="ciudad" name="ciudad"
                value="<?= htmlspecialchars($form_data['ciudad'] ?? '') ?>">

                <label for="tipo">Tipo:</label>
                <input type="text" id="tipo" name="tipo" placeholder='e.g. Transporte' required
                value="<?= htmlspecialchars($form_data['tipo'] ?? '') ?>">


                <button type="submit">Ver</button>
            </form>
            <a href="main.php">Volver al inicio</a>
            <a href="crear_viaje.php">Volver a Crear Viaje</a>
        </div>

        <div>
            <?php
                if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['tipo'])) {
                    require_once 'utils.php';

                    $db = conectarBD();

                    $tipo = htmlspecialchars($_POST['tipo']) ?? '';
                    $fecha_inicio = htmlspecialchars($_POST['fecha_inicio']) ?? '';
                    $fecha_fin = htmlspecialchars($_POST['fecha_fin']) ?? '';
                    $ciudad = htmlspecialchars($_POST['ciudad']) ?? '';

                    if ($tipo == 'Transporte') {
                        
                        $query_transport = "SELECT * 
                                            FROM reserva as r 
                                            JOIN transporte as t 
                                            ON r.id = t.id 
                                            WHERE r.estado_disponibilidad = 'Disponible'
                                            AND t.fecha_salida >= :fecha_inicio AND t.fecha_llegada <= :fecha_fin;";
                        $stmt_transport = $db->prepare($query_transport);
                        $stmt_transport->bindParam(':fecha_inicio', $fecha_inicio);
                        $stmt_transport->bindParam(':fecha_fin', $fecha_fin);
                        $stmt_transport->execute();
                        $transport = $stmt_transport->fetchAll(PDO::FETCH_ASSOC);

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

                    }elseif ($tipo == 'Panorama') {
                        $query_panorama = "SELECT * FROM reserva as r 
                                            JOIN panorama as p 
                                            ON r.id = p.id 
                                            WHERE r.estado_disponibilidad = 'Disponible'
                                            AND p.ubicacion = ";
                        $stmt_panorama = $db->prepare($query_panorama);
                        $stmt_panorama->execute();
                        $panorama = $stmt_panorama->fetchAll(PDO::FETCH_ASSOC);
                        
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
                    }elseif ($tipo == 'Hospedaje'){
                        $query_hospedaje = "SELECT * FROM reserva as r JOIN hospedaje as h ON r.id = h.id WHERE r.estado_disponibilidad = 'Disponible'";
                        $stmt_hospedaje = $db->prepare($query_hospedaje);
                        $stmt_hospedaje->execute();
                        $hospedaje = $stmt_hospedaje->fetchAll(PDO::FETCH_ASSOC);

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
                    }
                }else{
                    echo "<p>No se encontraron resultados.</p>";
                    //$_SESSION['error'] = 'No se encontraron resultados';
                    //header('Location: buscador_reservas.php');
                    //exit();
                }
            ?>
        </div>
    </div>
</body>
</html>
