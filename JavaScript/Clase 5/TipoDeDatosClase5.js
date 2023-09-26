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

//CLASE 5

//Tipo de dato undefined
var x;
console.log(x); //no le asignamos ningun valor, entonces lo coloca como indefinido pero al poner typeof nos dice eso
//podemos asignarle nosotros mismos que es indefinida
x = undefined;
console.log(typeof x);

// null: significa la ausencia del valor, vacia, ningun tipo de dato
var y = null; //null no es un tipo de dato pero su origen es considerado como un objeto
console.log(typeof y); //es de tipo objeto

//tipo de dato array y empty string
//son del tipo object (Esto lo diferencia de otros lenguajes como java)
//usamos corchetes, puede tener cualquier tipo de dato
var autos = ["citroen, audi, BMW, ford"];
console.log(autos);
console.log(typeof autos);

//Valores vacios, sino especificamos el valor se entiende por undefined entonces aca SI le asignamos un valor de una cadena vacia.
//le ponemos comillas vacias
var z = "";
console.log(z);








