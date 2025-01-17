import express from "express";
import { usuarioEnrutador } from "../routes/usuario.routes.js";
import { ZodError } from "zod";
const servidor = express();
servidor.use(express.json());

//agregar rutas
servidor.use(usuarioEnrutador);
//Para capturar el error local debe estar antes de las rutas
servidor.use((error,req,res,next) => {
    if(error instanceof ZodError){
        return res.status(400).json({
            message:"Error al recibir la informacion",
            content:error.errors,
        })
    }
    return res.status(400).json({
        message:"Error al hacer la peticion"
    })
});


servidor.listen(process.env.PORT,() => {
    console.log(`serviodr corriendo exitosamente en el puerto ${process.env.PORT} `)
})