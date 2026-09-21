<?php
session_start();
require_once 'utils.php';

$organizador = $_POST['organizador'] ?? '';
$agenda = intval($_POST['agenda']) ?? '';
$reserva = $_POST['reserva'] ?? '';
$etiqueta = $_POST['etiqueta'] ?? '';
$participantes = $_POST['participantes'] ?? '';


// Guardar datos para reusarlos
$_SESSION['form_data'] = $_POST;


try {
    $db = conectarBD();

    // Revisar que agenda ID es o no existente
    $stmt = $db->prepare("SELECT id FROM agenda a WHERE a.id = :agenda;");
    $stmt->bindParam(':agenda', $agenda);
    $stmt->execute();

    if ($stmt->fetch() === false && $agenda != 0) {
        $_SESSION['error'] = 'La agenda no existe: ' . $agenda;
        header('Location: crear_viaje.php');
        $is_agenda = false;
        exit();
    } elseif ($agenda == 0) {
        $is_agenda = false;

    } else {
        $is_agenda = true;
    }

    $query_a = "SELECT u.username FROM persona p
                JOIN usuario as u 
                ON p.correo = u.correo_usuario
                WHERE u.correo = :organizador;";

    $stmt_a = $db->prepare($query_a);
    $stmt_a->bindParam(':organizador', $organizador);
    $stmt_a->execute();
    $result_a = $stmt_a->fetch(PDO::FETCH_ASSOC);

    if ($result_a['username'] != $_SESSION['usuario']) {
        $_SESSION['error'] = 'Debe usar su correo';
        header('Location: crear_viaje.php');
        exit();
    }

    $db->beginTransaction();

    // Creando una nueva agenda si es que no existe previamente
    if ($is_agenda == false) {
        $stmt1 = $db->prepare("
            INSERT INTO agenda (correo_usuario, etiqueta) VALUES (:organizador, :etiqueta)
            RETURNING id;
        ");
        $stmt1->bindParam(':organizador', $organizador);
        $stmt1->bindParam(':etiqueta', $etiqueta);
        //$stmt1->bindParam(':id', $new_aid);
        $stmt1->execute();

        $agenda_id = $stmt1->fetchColumn();
    }

    // Guardamos el id de la agenda nueva para mostrarlo en la pantalla
    $stmt_aid = $db->prepare("
        SELECT id FROM agenda ORDER BY id DESC;
    ");
    $stmt_aid->execute();
    $resultado = $stmt_aid->fetch();
    $new_aid = $resultado['id'];



    // Actualizar valor agenda_id en las reservas correspondientes
    if ($is_agenda) {    
        // Si el usuario utiliza una agenda id existente
        $reservas = explode(",", $reserva);
        $stmt2 = $db->prepare("
            UPDATE reserva 
            SET agenda_id = :agenda
            WHERE id = :reserva;
        ");
        foreach ($reservas as $r){
            $r = intval($r);
            $stmt2->bindParam(':agenda', $agenda);
            $stmt2->bindParam(':reserva', $r);
            $stmt2->execute();
        }
    }else{
        // Si la agenda está siendo creada
            $reservas = explode(",", $reserva);

            $stmt4 = $db->prepare("
            UPDATE reserva 
            SET agenda_id = :id
            WHERE id = :reserva;
        ");
        foreach ($reservas as $r){
            $r = intval($r);
            $stmt4->bindParam(':id', $new_aid);
            $stmt4->bindParam(':reserva', $r);
            $stmt4->execute();
        }
    }

    if ($participantes != '') {
        $par = explode(';', $participantes);
        $n_participantes = count($par);

        foreach ($par as $p) {
            $pd = explode(',', $p);
            $panorama_id = intval($pd[0]);
            $nombre = $pd[1];
            $edad = $pd[2];

            $stmt_p = $db->prepare("SELECT * FROM panorama WHERE id = :panorama_id;");
            $stmt_p->bindParam(':panorama_id', $panorama_id);
            $stmt_p->execute();

            if ($stmt_p->fetch() === false) {
                $_SESSION['error'] = 'Este panorama no existe: ' . $panorama_id;
                header('Location: crear_viaje.php');
                exit();
            }else{

                $stmt3 = $db->prepare("
            INSERT INTO participante (panorama_id, nombre, edad) VALUES (:panorama_id, :nombre, :edad);
        ");

                $stmt3->bindParam(':panorama_id', $panorama_id);
                $stmt3->bindParam(':nombre', $nombre);
                $stmt3->bindParam(':edad', $edad);
                $stmt3->execute();
            }   
        }
    }
    
    $db->commit();

    //Calculamos el monto de cada reserva


    unset($_SESSION['form_data']);
    $_SESSION['success'] = 'Agenda creada correctamente, id: ' . $new_aid;
    header('Location: crear_viaje.php');
    exit();

} catch (Exception $e) { 
    if ($db->inTransaction()) $db->rollBack();
    $_SESSION['error'] = 'Viaje no creado';
    header('Location: crear_viaje.php');
    exit();
}
?>