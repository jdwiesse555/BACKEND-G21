const email = document.getElementById("email");
const password = document.getElementById("password");
const resetPasswordBtn = document.getElementById("inicio-sesion-btn");
const BACKEND_URL = "http://127.0.0.1:5000";
const BACKEND_URL1 = "http://127.0.0.1:5500";

resetPasswordBtn.addEventListener("click", (e) => {
  e.preventDefault();
  const correo = email.value;
  const clave = password.value;
  console.log(clave);

  // Con esto desactivamos el boton para evitar hacer clicks repetitivos
  resetPasswordBtn.disabled = true;

  inicioSession(correo,clave)
    .then((resultado) => {
      console.log(resultado.message);
      if (resultado.message  == 'Cresdenciales incorrectas') {
      Swal.fire({
        title: "LOGIN ",
        text: "Cresdenciales incorrectas",
        icon: "error",
        confirmButtonText: "Entendido",
      }).then(() => {
        // Cambiamos el endpoint de nuestra pagina y le ponemos el login
        window.location.pathname = "/frontend/login";
      });}
      else  {

          Swal.fire({
        title: "Bienvenido ",
        text: "Cresdenciales correctas",
        icon: "success",
        confirmButtonText: "Entendido",
      }).then(() => {
        // Cambiamos el endpoint de nuestra pagina y le ponemos el login
        console.log(resultado)
        sessionStorage.setItem("token",resultado.token)
        window.location.pathname = "/frontend/aplicativo";
      });}
    

      

    })
    .catch((e) => {
      console.error(e);
    });
});

const inicioSession = async (correo,clave) => {
  const body = { correo: correo,password: clave};
  const resultado = await fetch(`${BACKEND_URL}/login`, {
    method: "POST",
    body: JSON.stringify(body), // Convertir nuestro json de javascript a un JSON que pueda recibir el backend,
    headers: {
      "Content-Type": "application/json", // Indicar el tipo de informacion que estoy enviando en el body
    },
  });
  const respuesta = await resultado.json();
 
  return respuesta;
};