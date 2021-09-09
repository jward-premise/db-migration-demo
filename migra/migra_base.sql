SET SEARCH_PATH TO migra;

CREATE TABLE person
(
    first_name TEXT NOT NULL,
    last_name  TEXT NOT NULL,
    age        INT  NOT NULL
);

CREATE TABLE address
(
    street_number INT  NOT NULL,
    street_name   TEXT NOT NULL,
    apt_num       TEXT,
    city          TEXT NOT NULL,
    state         TEXT NOT NULL
);

CREATE OR REPLACE VIEW person_read AS (
    SELECT
          first_name || ' ' || last_name as name
        , age
      FROM person
);