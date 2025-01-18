import express from "express";
import { usuarioEnrutador } from "../routes/usuario.routes.js";
import { ZodError } from "zod";
import { Prisma } from "@prisma/client";
import cors from "cors";
import { equipoEnrutador } from "../routes/equipo.routes.js";
import AWS from "aws-sdk"

new AWS.S3({ credentials : {
    accessKeyId:process.env.ACCESS_KEY,
    secretAccessKey:process.env.SECRET_ACCESS_KEY,
     }
});

const servidor = express();
// cros para poder permitir peticiones en mi backend
servidor.use(cors());
servidor.use(express.json());

//agregar rutas
servidor.use(usuarioEnrutador);
servidor.use(equipoEnrutador);
//Para capturar el error local debe estar antes de las rutas
servidor.use((error,req,res,next) => {
    if(error instanceof ZodError){
        return res.status(400).json({
            message:"Error al recibir la informacion",
            content:error.errors,
        })
    }
    if (error instanceof Prisma.PrismaClientKnownRequestError){
        return res.status(404).json({
            message:`El ${error.meta.modelName } no existe`,
        })
    }

    console.log(error)
    return res.status(400).json({
        message:"Error al hacer la peticion"
    })
});


servidor.listen(process.env.PORT,() => {
    console.log(`serviodr corriendo exitosamente en el puerto ${process.env.PORT} `)
})