
package domain;

public class Persona {

    
    //cargamos los atributos
    private int idPersona;
    private static int contadorPersona;
    private String nombre;
    
    //constructor
    public Persona(String nombre){
        //no usamos el constructor vacio, le ponemos un parametro que se llama nombre
        //Incrementar el contador por cada objeto nuevo
        this.nombre = nombre;
        Persona.contadorPersona++; 
//no utilizar el operador this, la referencia debe ser a traves de la clase
   //vamos a asignar nuevos valores a la variable idPersona
        this.idPersona = Persona.contadorPersona;
        
    }
    
    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        contadorPersona = aContadorPersona;
    }

    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
//esto se pone con insert code
    //sobre escribimos la clase object
    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
}
