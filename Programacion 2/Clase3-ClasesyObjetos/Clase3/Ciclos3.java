/* Ejercicio 3: Leer número hasta que se introduzca un cero. Para cada uno indicar si es par o impar. Primero lo hacemos con la clase Scanner
Luego con la clase JOptionPane */

 package Clase3; 

import java.util.Scanner;

public class Ciclos3 {

    public static void main(String[] args) {
        try (Scanner entrada = new Scanner(System.in)) {
            int numero;
            System.out.println("Ingrese un número: ");
            numero = Integer.parseInt(entrada.nextLine());
            while(numero != 0) {
                if (numero % 2 == 0) {
                    System.out.println("El numero ingresado "+numero+" es PAR");
                    
                }
                else{
                    System.out.println("El número ingresado "+numero+" es IMPAR");
                }
                System.out.println("Ingrese otro número: ");
                numero = Integer.parseInt(entrada.nextLine());
            }
            System.out.println("El número ingresado es "+numero+" finaliza el programa.");
        
        }
    }
}