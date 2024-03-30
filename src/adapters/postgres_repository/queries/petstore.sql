-- name: GetPet :one
SELECT
  *
FROM
  pets
WHERE id = sqlc.arg('pet_id')::int
;

