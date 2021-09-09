DROP VIEW IF EXISTS person_read;
CREATE VIEW person_read AS
    SELECT
          first_name || ' ' || last_name as name
        , age
    FROM person;