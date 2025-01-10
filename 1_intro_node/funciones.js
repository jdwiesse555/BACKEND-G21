// arrow funcion / funcion anonima

 const sumar = (numero1,numero2) => {
    const resultado = numero1 + numero2;
    return resultado;
}

// funcion tradicional

 function restar(numero1,numero2) {
    const resultado = numero1 - numero2;
    return resultado
    
}

//fubncion anomina de una solo linea

const multiplicar = (numero1,numero2) => numero1*numero2;

 // segun commonsJS para realizar una exportacion se realiza asi
module.exports = {
    sumar: sumar,
    // si tiene el mismo nombre se puede hacer asi
    restar,
    multiplicar,
 };
