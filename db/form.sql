CREATE TABLE {} (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    xform_data_id INT NOT NULL,
    xform_id INT NOT NULL,
    data JSON NOT NULL,
    edited VARCHAR(255),
    status VARCHAR(255),
    version VARCHAR(255),
    duration DECIMAL,
    media_count INT,
    total_media INT,
    submitted_by VARCHAR(255),
    submission_time DATETIME
);