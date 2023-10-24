
package test;

import domain.Persona;

public class PersonaPrueba {
    private int contador;
    
    public static void main(String[] args) {
        Persona persona1 = new Persona("Ariel");
        System.out.println("persona1 = " + persona1); //nos muestra los valores que tienen los atributos
        Persona persona2 = new Persona("Naty");
        System.out.println("persona2= " + persona2);
        imprimir(persona1); //si ponemos esto nos da error entonces tenemos que escribir static abajito en el public void
        imprimir(persona2); 
        PersonaPrueba personaP1 = new PersonaPrueba();
        System.out.println(personaP1.getContador());
    }
    //esto no es estatico, trabaja de forma dinamica
    public static void imprimir(Persona persona){
        System.out.println("persona = " + persona);
    }
    public int getContador(){
        imprimir(new Persona("Liliana"));
        return this.contador;
    }
}
