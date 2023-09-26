/*Ejercicio1: Leer un numero y mostrar su cuadrado, repetir el proceso hasta que se introduzca un numero negativo. */

import java.util.Scanner;

public class EjercicioCiclos1 {
    
    public static void main(String[] args) {
        try (Scanner entrada = new Scanner(System.in)) {
            int numero, cuadrado; //creo las variables.
            System.out.println("Ingrese un numero:");
            numero = Integer.parseInt(entrada.nextLine());

            while(numero >= 0){ //le doy la condicion
                cuadrado = (int)Math.pow(numero, 2); //usando math.pow me pide dos datos, la variable donde se guardan los nros que ingrese el usuario y el nro que ingrese para elevar el dato anterior. En este caso elevado al cuadrado.
                System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado);
                System.out.println("Ingrese otro numero");
                numero = Integer.parseInt(entrada.nextLine());
            }
            System.out.println("El numero ingresado es negativo");
    }
}}