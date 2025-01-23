import { conexion } from "../conexion.js";
//import { actulizartanqueSerializer,registrarTaqueSerializer } from "./serializers/tanques.serialize.js";
import {paginationSerializer} from "../util.js"
import { number } from "zod";
import { actulizarMedicionesSerializer,registrarMedicionesSerializer } from "./serializers/mediciones.serializer.js";

export const devolverMedicones = async (req,res) => {
    const Listasmediciones = await conexion.mediciones.findMany({include:{lmetrica_med:true,ltk_med:true}})
    
    return res.json({
        message:"Lista de medicones exitosamente",
        content : Listasmediciones,
    })
}

export const devolverMedicion = async (req,res) => {
       

    const medicionEncontrado = await conexion.mediciones.findFirstOrThrow({
        include:{lmetrica_med:true,ltk_med:true},
        where: { id:Number(req.body.id)},
    });
   
    return res.json({
        message:" Medicicon encontrado exitosamente",
        content : medicionEncontrado ,
         }
    )
}



export const actulizarMedicion = async (req,res) => {
    const data = req.body.data

    const dataValidada =actulizarMedicionesSerializer.parse(data)
    

    const medicionActualizado = await conexion.mediciones.update({
        data : dataValidada,
        
        where: {

            id:Number(req.body.id)
        },
    })
    return res.json({
        message:"Medicion actualizado exitosamente",
        content : medicionActualizado,
    })
}

export const registramedicion = async (req,res) => {
    const data = req.body.data
    
    data.fecha= new Date(data.fecha)
    console.log(data)
    const dataValidada =registrarMedicionesSerializer.parse(data)
    

    const medicioncreada = await conexion.mediciones.create({
        data : dataValidada,    })
    return res.json({
        message:"Medicion creada exitosamente",
        content : medicioncreada,
    })
}

export const borrarMedicon = async (req,res) => {
 
  
    const medicionaborrado = await conexion.mediciones.delete({
      
        select: {
            id :true,
            metrica:true,

        },
        where: {
            id:Number(req.body.id)
        },
    })
    
   
    return res.json({
        message:"Mediocion borrado exitosamente",
        content : medicionaborrado,
    })
}