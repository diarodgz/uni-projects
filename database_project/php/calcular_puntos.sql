
--query to get the price per person of each reserva:
--SELECT r.id, r.agenda_id, t.precio_asiento, p.precio_persona, h.precio_noche FROM reserva as r LEFT OUTER JOIN transporte as t ON
--r.id = t.id LEFT OUTER JOIN panorama as p ON p.id = r.id LEFT OUTER JOIN hospedaje as h ON h.id = r.id;


--query to get price of panorama per participant:
--SELECT COUNT(pn.id) as n_part, COUNT(pn.id)*t.precio_asiento as total_trans, COUNT(pn.id)*p.precio_persona as total_pan, COUNT(pn.id)*h.precio_noche as total_hosp, r.id, r.agenda_id, t.precio_asiento, p.precio_persona, h.precio_noche FROM reserva as
--r LEFT OER JOIN transporte as t ON r.id = t.id LEFT OUTER JOIN panorama as p ON p.id = r.id LEFT OUTER JOIN hospedaje as h ON h.id =
--r.id RIGHT OUTER JOIN participante as pn ON pn.panorama_id = r.id GROUP BY r.id, t.precio_asiento, p.precio_persona, h.precio_noche;

CREATE OR REPLACE FUNCTION calcular_puntos(agenda_id, n_part, correo)
RETURNS void AS $$
DECLARE
agenda_id ALIAS FOR $1;
n_part ALIAS FOR $2;
puntos int;
BEGIN
    SELECT SUM(COALESCE(t.precio_asiento  * n_part, 0) + COALESCE(p.precio_persona * n_part,0) + COALESCE(h.precio_
noche * n_part, 0)) as total INTO int;
    FROM reserva as r 
    LEFT OUTER JOIN transporte as t ON
    r.id = t.id 
    LEFT OUTER JOIN panorama as p 
    ON p.id = r.id 
    LEFT OUTER JOIN hospedaje as h 
    ON h.id = r.id;
    WHERE r.agenda_id = agenda_id;

    INSERT INTO usuario (correo, puntos) VALUES (correo, )
END;
$$ LANGUAGE plpgsql