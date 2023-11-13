--Design the schema for a medical center.
    --A medical center employs several doctors
    --A doctor can see several patients
    --A patient can see several doctors
    --During a visit, a patient may be diagnosed to have one or more diseases

CREATE TABLE medcenters(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT,
)

CREATE TABLE providers(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    medcenter_id INTEGER REFERENCES medcenters,
)

CREATE TABLE patients(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    provider_id INTEGER REFERENCES providers,
    diagnoses_id INTEGER REFERENCES diagnoses,
)

CREATE TABLE diagnoses(
    id SERIAL PRIMARY KEY,
    diagnosis TEXT NOT NULL,
)