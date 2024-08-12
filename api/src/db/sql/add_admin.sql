INSERT INTO users
VALUES (
        1,
        DEFAULT,
        DEFAULT,
        'admin',
        'admin',
        'admin'
    ) ON CONFLICT DO NOTHING;
