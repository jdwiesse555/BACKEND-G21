import express from 'express';
// esta libreria se agrega cuando creamos los tipos de priema
// npx priema migrate generate
import Prisma from "@prisma/client";

const conexion = new Prisma.PrismaClient();
const servidor = express();
servidor.use(express.json());
servidor.post("/registro", async (req, res) => {
    try {
        const  data = req.body  // {nombre:'',email:'',nickname:''}
      // resultado > seria la ejecucion correcta de la funcion
      const resultado = await conexion.usuario.create({
        data,
      });
      // ACA PONES TU MENSAJE
      return res.json({
        message: "Usuario creado exitosamente",
        content : resultado
      });
    } catch (error) {
      // obtenemos el error de la ejecucion del proceso asincrono
      if (error instanceof Prisma.Prisma.PrismaClientValidationError) {
        return res.json({
          message: "error al hacer la peticion a la bd",
        });
      }
      return res.json({
        mesage: "Error al crear el usuario",
      });
    }
  });

  servidor.route("/notas")
  .post(async (req,res) =>{
    const data = req.body
    console.log(data)
    try {
        const notaCreeada = await conexion.nota.create({data});

        return res.json({
            message:"Nota creada existosamente",
            content:notaCreeada,
        });
    } catch (error) {
        console.log(error)
        return res.json({
            message:"Error al crear la nota",
            content:data,
        });
    }
  })

  .get(async (req,res) => {
    const notas = await conexion.nota.findMany();

    return res.json({
        content:notas,
    });
  });
  
  servidor.listen(process.env.PORT, () => {
    console.log(`SERVIDOR CORRIENDIO EXITOSAMENTE EN PUERTO ${process.env.PORT}`)
  })