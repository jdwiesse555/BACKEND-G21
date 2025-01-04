const btmCrearProducto = document.getElementById('btmCrearProducto')
const nombreProducto = document.getElementById('nombreProducto')
const descripcionProducto = document.getElementById('descripcionProducto')
const btmDelProducto = document.getElementById('btmDelProducto')

btmCrearProducto.addEventListener('click',(e)=> {
    if(nombreProducto.value == ''){
        alert('El nombre es requerido')
        e.preventDefault()
    }
   
})

btmDelProducto.addEventListener('click',(e)=> {

    if(nombreProducto.value == 'lapiz'){
        alert('El nombre es requerido')
        e.preventDefault()
    }
})