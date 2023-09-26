var nombre = "Sol";  //tipo string
console.log(typeof nombre);

nombre = 6;
console.log(typeof nombre);

nombre = 10.2;
console.log(typeof nombre);

var numero = 2500;  //tipo numerico
console.log(typeof numero);

var objeto = {     //tipo objeto, va con llaves y dos puntos
    nombre : "Maria Sol",
    apellido : "Bilyk",
    telefono : "262583654349"
}
console.log(typeof objeto);

//Tipos de datos booleanos

var bandera = true;
console.log(bandera);

//FUNCIONES: permiten realizar una tarea especifica, se pueden usar las veces necesarias, para eso debemos llamarlas.

function miFuncion(){}
console.log(typeof miFuncion);

//tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo)

//tipo de dato clases: tambien son funciones
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
//La palabra this hace referencia a los atributos de nuestra clase.
console.log(Persona);