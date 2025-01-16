 npx prisma init --> inicializar mi proyecto con prisma
 npx prisma migrate dev -> crea el archivo de migracion y las tablas en la base datos

 cambio en el modelo sin ejecutar en la base datos
 npx prisma migrate dev --create-only

 se revisa y despues se ejecuta
 npx prisma migrate deploy

 para actualiar
 npx prisma generate