package Clase4;

public class Metodos {

    /*Atributos de la clase (Caracteristicas) */
    String nombre;
    String apellido;

    /*Metodos de la clase (Acciones) 
     * Lo categorizamos como que estas son las acciones, ya definimos los atributos arriba que son de tipo string.
     * Un metodo es una parte de codigo que vamos a poder reutilizar. Se lo puede llamar las veces que sean necesarias.
     * Los metodos pueden recibir valores, estos se conocen como argumentos.
     * Tambien pueden regresar valores, a esto se lo llama valor de retorno que tambien puede regresar a nuestro metodo.
     * Entonces para definir un metodo comenzamos poniendo:
     * Public: indica que el metodo se puede usar fuera de esta clase.
     * Void: indica que no regresa ningun tipo de informacion.
     * En el nombre del metodo usamos la nomenclatura cammel case, ponemos por ej: ObtenerInformacion(), los parentesis indican que podemos recibir informacion que puede recibir un metodo, esto que recibe se conoce como argumentos, puede recibir o no un metodo.
    */
    public void ObtenerInformacion() {
        System.out.println("Nombre: "+nombre); /*Escribimos Nombre y concatenamos el atributo nombre. nombre aqui, no es simplemente una variable, es un atributo de la clase, y no importa que no se defina dentro del metodo, porque al ser un atributo se puede usar dentro de cualquier metodo definido dentro de la clase.
        el metodo que creamos esta dentro de la clase. 
        Imprimimos los atributos de la clase.*/
    }

}