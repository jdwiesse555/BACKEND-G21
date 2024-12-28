const BACKEND_URL = "http://127.0.0.1:5000";
const contenedor = document.getElementById("contenedor");


const data_categorias = async (data) => {
    
    const resultado = await fetch(`${BACKEND_URL}/categorias`, {
      method: "GET",
       // Convertir nuestro json de javascript a un JSON que pueda recibir el backend,
      headers: {
      /*  "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNTI0NDAzMiwianRpIjoiYjVkYTlkMjYtYWFmYS00NmQ2LWFjY2MtYmI1MjQ4ODUxMTViIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3MzUyNDQwMzIsImNzcmYiOiI1ZmI1YjFjYi0yZGI5LTRlZjUtYmZmYi00MThmYjMyYTkyNTIiLCJleHAiOjE3MzUyNTUxNDJ9.5QW4AlWLP945M5jgMwWdcYgm0XG1VPo234S6XMhOkq0" ,*/
        "Content-Type": "application/json", // Indicar el tipo de informacion que estoy enviando en el body
      },
    });
    const respuesta = await resultado.json();
  
    return respuesta;
  };


  data_categorias("paso")
  .then((resultado) => {
     console.log((resultado));


     const div = document.createElement("div");
     HTML = ` <h1> Listado de Categorias </h1> <table class="table table-responsive table-hover" style="text-align: center;
        width: 98%;
        left: 0px;
        top: 5px; 
    background-color: #9b9bce;	
        border: medium double #9b9bce;
        border-width: 1px;
        bgcolor: #FFFFFF;
        background-repeat: no-repeat;
        background: #FFFFFF;
        padding: 10px 10px 10px 10px;
        margin: 10px 10px 10px 10px;" > <tr> <td >id </td> <td>nombre</td> <td>color </td><td>libros </td></tr>` 
     for (i=0;i<resultado.content.length;i++) {
      HTML = HTML +  ' <tbody> <tr class="clickable" data-toggle="collapse" data-target="#group-of-cau-'+i+'"> <td>' +  resultado.content[i].id +"</td> <td>"+ resultado.content[i].nombre +"</td> <td>"+resultado.content[i].color +'</td><td >'+resultado.content[i].librosDeLaCategoria.length+ "</td></tr> </tbody> "
      HTML = HTML + ' <tbody id="group-of-cau-'+i+'" class="collapse">' 
      for (j=0;j<resultado.content[i].librosDeLaCategoria.length;j++) {
        HTML = HTML + '  <tr><td>Libro:</td><td>'+resultado.content[i].librosDeLaCategoria[j].id+'</td> <td>'+resultado.content[i].librosDeLaCategoria[j].titulo+'</td> <td>'+resultado.content[i].librosDeLaCategoria[j].descripcion+'</td><td>'+resultado.content[i].librosDeLaCategoria[j].cantidad+' </td></tr>'

      } 
     HTML = HTML + ' </tbody>'
    }
      HTML = HTML + "</table>"

      div.innerHTML = HTML
     contenedor.appendChild(div);
});
