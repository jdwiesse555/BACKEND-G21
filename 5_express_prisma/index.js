import express from 'express';
// esta libreria se agrega cuando creamos los tipos de priema
// npx priema migrate generate
import Prisma from "@prisma/client";
import cors from "cors";

const conexion = new Prisma.PrismaClient();
const servidor = express();


servidor.use(cors());
servidor.use(express.json());
servidor.route("/loginuser/:password-:username")
.get(async (req,res) => {
  const username = (req.params.username)
  const password = (req.params.password)
try{
  const usuariologin = await conexion.usuario.findMany({
    where:{
      nombre:username,
      password:password,
    }
 });
 if (usuariologin.length>0){
  return res.json({
    message: "bienvenido",
    content : usuariologin,
  })
 } else {
  return res.json({
    message: "usuario o clave no existe",
    content : usuariologin,
  } )

  }

} catch (error) {
  return res.json({
    message: "usuario o clave no existe",
    content : usuariologin,
  });

}
})


servidor.route("/usuario")
.post(async (req,res) =>{
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
  })
  .get(async (req,res) => {
    const usuarios = await conexion.usuario.findMany(
  //    {
  //    select: {
  //      id: true,
  //      nombre: true,
  //    },}
    );

    return res.json(
        usuarios
    );
  });

  servidor.route("/notas")
  .post(async (req,res) =>{
    const data = req.body
    
    data.usuarioId = parseInt(data.usuarioId)
    try {
        const notaCreeada = await conexion.nota.create({data});

        return res.json({
            message:"Nota creada existosamente",
            notaCreeada,
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

    return res.json(
        notas
    );
  });

  servidor.route("/nota/:idnota")

  .delete(async (req,res) => {
    const data = req.body
    
    const notaId = parseInt(req.params.idnota)
    data.usuarioId = parseInt(data.usuarioId)
    console.log(data)
    try {
        const notaBorrada = await conexion.nota.delete({
          where:{
            id:notaId
          }
        });

        return res.json({
            message:"Nota borrada existosamente",
            notaBorrada,
        });
    } catch (error) {
        console.log(error)
        return res.json({
            message:"Error al borrar la nota",
            content:data,
        });
    }
  })
 
  .put(async (req,res) =>{
    const data = req.body
    
    const notaId = parseInt(req.params.idnota)
    data.usuarioId = parseInt(data.usuarioId)
    console.log(data)
    try {
        const notaCreeada = await conexion.nota.update({
          where:{
            id:notaId
          },data
        });

        return res.json({
            message:"Nota actualizada existosamente",
            notaCreeada,
        });
    } catch (error) {
        console.log(error)
        return res.json({
            message:"Error al actulizar la nota",
            content:data,
        });
    }
  })

  .get(async (req,res) => {
    const notaId = parseInt(req.params.idnota)
    const nota = await conexion.nota.findUniqueOrThrow({
      where:{
        id:notaId
      }
   });
    return res.json(nota);
  });


  servidor.listen(process.env.PORT, () => {
    console.log(`SERVIDOR CORRIENDIO EXITOSAMENTE EN PUERTO ${process.env.PORT}`)
  })
  