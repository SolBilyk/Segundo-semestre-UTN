
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        System.out.println("persona1 su nombre es: " + persona1.getNombre());
        //modificamos a traves de los metodos 
        persona1.setNombre("Juan Ignacio");
        System.out.println("persona1 con su nombre modificado: " + persona1.getNombre());
        
        System.out.println("persona1 el resultado para el sueldo es: " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: " + persona1.isEliminado());
        
        System.out.println("persona1: " + persona1.toString()); //esta es la sintaxis correcta para mostrar el toString cuando ya esta definido y creado, pero no hace falta llamarlo
        System.out.println("persona1 = " + persona1 ); //de esta forma se lo llama automaticamente
                
    }
    
}
