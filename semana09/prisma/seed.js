import prisma from '@prisma/client'

const conexion = new prisma.PrismaClient()

async function poblarBD() {
    const equipos = [
        {
            nombre: "Melgar",
            estadio: "UNSA",
            imagenId: null,
          },
          {
            nombre: "Universitario de Deportes",
            estadio: "Monumental",
            imagenId: null,
          },
          {
            nombre: "Alianza Lima",
            estadio: "Alejandro Villanueva - Matute",
            imagenId: null,
          },
          {
            nombre: "Sport Boys",
            estadio: "Estadio del Callao",
            imagenId: null,
          },
          {
            nombre: "Sporting Cristal",
            estadio: "Alberto Gallardo",
            imagenId: null,
          },
          {
            nombre: "Cienciano",
            estadio: "Estadio de Cuzco",
            imagenId: null,
          },
          {
            nombre: "Chankas F.C.",
            estadio: "Estadio de Madre Dios",
            imagenId: null,
          },
    ]

  for (const equipo of equipos) {
    await conexion.equipo.upsert({
        create :equipo,
        update: equipo,
        where : {
            nombre:equipo.nombre,
        }
    })
  }  
}

poblarBD().then(() => {
    console.log("el proceso fue realizado con exito");
})
.catch((e) => {
    console.error("error")
    console.error(e)

})