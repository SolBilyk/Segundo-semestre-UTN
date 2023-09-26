/*Ejercicio 5: Realizar un juego para adivinar un numero, para ello generar un numero aleatorio entre 0-100, y luego ir pidiendo numero indicando "es mayor" o "es menor" segun sea mayor o menor con respecto a N. El proceso termina cuando el usuario acierta y mostramos el numero de intentos hechos. */
package Clase3;

import java.util.Scanner;

public class Ciclos5 {
    /**
     * @param args
     */
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio= (int)(Math.random()*100); //esto genera un numero aleatorio.
        do {
            System.out.println("Ingrese un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            if (numero < aleatorio){
                System.out.println("Ingrese un numero mayor: ");}
            else if (numero > aleatorio){
                System.out.println("Ingrese un numero menor: ");}
            else{  //aca adivina el numero que ingreso el usuario
                System.out.println("FELICIDADES!! Has adivinado el numero!!");
            }
            conteo++;
        } 
        while(numero != aleatorio);
        System.out.println("Adivinaste el numero en "+conteo+" intentos."); 
        entrada.close();
    }
}
