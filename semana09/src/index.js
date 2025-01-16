import express from "express";

const servidor = express();

servidor.listen(process.env.PORT,() => {
    console.log(`serviodr corriendo exitosamente en el puerto ${process.env.PORT} `)
})