import express from 'express';

const servidor = express();
//configurar lo que podemos recibir por metodo body
// express json() > indicamos que el contenido que podemos reciir por el boay
servidor.use(express.json())
//para recibir por body formato x-www-url-encoded
servidor.use(express.urlencoded());
//para recibir texto
servidor.use(express.text());

servidor.get("/",(req,res) => {
    res.json({
        mwssage:"Bienvenido a mi API",
    })
});
servidor.post("/crear-usuario",(req,res) => {
        //req body es todo cuerpo que me envia el clinete
        console.log(req.body)
        res.json({
            message:"Usuario creado exitosamente",
        })
    });

servidor.listen(3000,() => {
    console.log("Servidor corriendo exitosamente");
});