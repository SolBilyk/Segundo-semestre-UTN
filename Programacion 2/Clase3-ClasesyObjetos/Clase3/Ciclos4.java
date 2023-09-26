/*Ejercicio 4: Pedir números hasta que se teclee un numero negativo y mostrar 
cuantos numeros se han introducido.
Con Scanner*/

package Clase3;

import java.util.Scanner;

public class Ciclos4 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
       
        int numero,conteo = 0;
       
        System.out.println("Ingrese un numero: ");
       
        numero = Integer.parseInt(entrada.nextLine());
       
        while(numero >= 0){
            System.out.println("El numero "+numero+ " es positivo");
            conteo++;
            System.out.println("Ingrese otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Se ingresaron: "+conteo+" numeros positivos");
        entrada.close();
    }
}
