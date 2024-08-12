SELECT images.filepath
FROM images
    INNER JOIN albums ON albums.id = images.album_id
WHERE albums.name = :album
ORDER BY images.created_at DESC
LIMIT :num_images OFFSET :offset
