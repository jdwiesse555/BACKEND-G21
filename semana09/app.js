import  express  from "express";
import pg from "pg";




const app = express();

app.use(express.json());

const conexion = new pg.Pool({connectionString: process.env.DATABASE_URL});



app
  .route("/productos")
  .get(async (req,res) => {
    const result = await conexion.query("select *  from productos");
    const registros =  result.rows;
    return res.json({
      comntent : registros,
    });
  })
  .post(async (req,res) => {
    const data = req.body
    const nuevoProducto = await conexion.query(
      "INSERT INTO productos (nombre, precio) VALUES ($1,$2) RETURNING *",
      [data.nombre,data.precio]
  );
    const resultado = nuevoProducto.rows;
    return res.json({
      message:"producto creado existosamente",
      comntent : resultado,
    });

  });

app.listen(process.env.PORT,  () => {
  console.log(`Server running on ${process.env.PORT}`);
});
Promise.all([
  conexion.query(
    "CREATE TABLE IF NOT EXISTS productos (id SERIAL PRIMARY KEY, nombre TEXT, precio FLOAT)"
  ),
]).then(() => {
  console.log("Las tablas fueron creadas exitosamente");
});