Created db from squirell and then ran these commands
DROP SCHEMA IF EXISTS ea CASCADE;
create schema ea
CREATE TABLE ea.user (
    id SERIAL unique,
    email VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255),
    is_admin BOOLEAN DEFAULT FALSE,
    is_product_admin BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT FALSE,
    name VARCHAR(100),
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP USER IF EXISTS eauser;

CREATE USER eauser WITH SUPERUSER PASSWORD 'eauser';

GRANT ALL PRIVILEGES ON DATABASE autogen TO eauser;

ALTER DATABASE autogen OWNER TO eauser;
