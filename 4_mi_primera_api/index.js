import express from 'express';

const servidor = express();

servidor.get("/",(req,res) => {
    res.json({
        mwssage:"Bienvenido a mi API",
    })
});

servidor.listen(3000,() => {
    console.log("Servidor corriendo exitosamente");
});