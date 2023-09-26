package Clase4;

public class CreacionDeUnObjeto {
   
    /*Una clase es un nuevo tipo definido en java, por esto no solo la vamos a poder utilizar dentro de nuestros proyectos sino que podemos compartirla a otros proyectos.
     * Dentro de la clase (Accion) podemos poner el metodo main para ejecutar, porque el main esta para ejecutar hacia la consola nuestros programas, se pueden poner dentro tambien dentro de la clase pero se recomienda hacerlo fuera, creando otra clase.
     * Entonces vamos al paquete de clases, new java class, le ponemos de nombre: prueba persona. Se crea otra clase, otro archivo
     */
    public static void main(String[] args) { /*esto se hace para ejecutar el programa */
        /*ponemos el nombre del otro archivos: Persona
         * Entonces comenzamos con la creacion de un objeto pero lo hacemos llamando a la clase persona, ponemos el tipo:
         * Persona (y le ponemos un nombre al objeto)
         * Persona persona1; (no le asignamos nada todavia
         * ahora si llamamos al constructor que tenemos de la clase persona)
         * entonces ponemos: 
         * persona1 = new Persona() [al ponerle los parentesis estamos llamando directamente al constructor desde el objeto (variable), la variable pasa a ser un objeto]
         * este constructor es el que nos permite asignar valores al objeto desde que lo creamos.
         * una variable se almacena en una parte diferente que los objetos en lo que es la memoria, por eso java los administra de manera distinta.
         * hemos creado un objeto de tipo : persona.
         * el constructor es un metodo especial donde reserva memoria para poder crear objetos, al crearla, el constructor le regresa la referencia donde se creo el objeto y se lo asigna a la variable una vez hecha la conexion, de esta forma se puede acceder a los atributos y metodos de la clase persona en este caso.
         * Ya tenemos una persona creada, ahora usamos el objeto y ponemos:
         * persona1 (ponemos un punto y esto nos da acceso al constructor hacia la clase persona a los atributos donde esta apellido y nombre) entonces se ve escrito asi: //llamamos al constructor
         * persona1.nombre = "Ariel"
         * persona1.apellido = "Betancud"
         * llamamos al objeto: donde dice obtener informacion.
         * persona1.obtenerInformacion();
         */
        
    }
}
