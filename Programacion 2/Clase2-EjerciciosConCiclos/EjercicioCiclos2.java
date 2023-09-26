/* Ejercicio 2: Leer un numero e indicar si es positivo o negativo. El proceso se repetira hasta que se introduzca un 0.  */

import java.util.Scanner;

public class EjercicioCiclos2 {
    public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in); 
    
    System.out.println("Ingrese un numero: ");
    var numero = Integer.parseInt(entrada.nextLine());

    while(numero != 0){
        if (numero > 0){
            System.out.println("El numero "+numero+" es positivo!!!");
        }
        else {
            System.out.println("El numero "+numero+" es negativo!!!");
        }
        }
    System.out.println("El numero "+numero+ " termina el programa");
    entrada.close();
    }
}


