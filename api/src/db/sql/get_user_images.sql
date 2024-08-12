SELECT images.filepath
FROM images
    INNER JOIN users ON users.id = images.user_id
WHERE users.username = :username
