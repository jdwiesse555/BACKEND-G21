
const nombreProducto = document.getElementById('nombreProducto')
const descripcionProducto = document.getElementById('descripcionProducto')
const btmDelProducto = document.getElementById('btmDelProducto')



btmDelProducto.addEventListener('click',(e)=> {

    let text = "Press a button!\nEither OK or Cancel.";
    if (confirm(text) == true) {
      text = "You pressed OK!";
    } else {
        e.preventDefault();
    }
})