const { Pool } = require('pg');
const express = require('express');
const cors = require('cors');

const app = express();
const port = 3000;

const pool = new Pool({
  connectionString: process.env.PG_CONNECTION_STRING,
});

async function main() {
  await pool.query(`
    CREATE TABLE IF NOT EXISTS users (
      id SERIAL PRIMARY KEY,
      name TEXT NOT NULL,
      email TEXT NOT NULL
    );
  `);

  await pool.query(`
    INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')
    ON CONFLICT DO NOTHING;
    `);

  await pool.query(`
    INSERT INTO users (name, email) VALUES ('Tom Smith', 'tom@example.com')
    ON CONFLICT DO NOTHING;
    `);
  
  await pool.query(`
    INSERT INTO users (name, email) VALUES ('Dick Taylor', 'dick@example.com')
    ON CONFLICT DO NOTHING;
    `);
  
  console.log('Prepared PostgreSQL');

  app.use(cors());

  app.get('/users', async (req, res) => {
    const result = await pool.query('SELECT * FROM users');
    res.send(result.rows);
  });

  app.listen(port, () => {
    console.log(`DevOps assignment app listening at http://localhost:${port}`);
  });
}

main()
  .then(() => console.log('server started'))
  .catch((err) => console.error(err));