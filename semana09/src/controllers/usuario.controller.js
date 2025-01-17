import {registrarUsuarioSerializer} from "./serializers/usuario.serializer.js"

export const  registrarUsuario = async (req,res) => {
    const data = req.body
    //valida si la data esta corresta
   
    const dataValidada = registrarUsuarioSerializer.parse(data);
    console.log(dataValidada);

    return  res.json({
        message:"Usuario registado exitosamente",
    })

};



