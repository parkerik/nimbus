INSERT INTO albums
VALUES (
        1,
        DEFAULT,
        DEFAULT,
        'public'
    ) ON CONFLICT DO NOTHING;
