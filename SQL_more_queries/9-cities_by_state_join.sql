-- comments
SELECT c.id, c.name, s.name FROM states s JOIN cities c on s.id = c.state_id ORDER BY c.id ASC;