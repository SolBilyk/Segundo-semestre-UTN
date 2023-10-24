/*Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar si la fecha es correcta. Suponiendo que todos los meses son de 30 dias */

package Operaciones;

import java.util.Scanner;

public class Ejercicio9ConScanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese el dia: ");
        int dia = Integer.parseInt(entrada.nextLine());
        int mes = Integer.parseInt(entrada.nextLine());
        int anio = Integer.parseInt(entrada.nextLine());

        //usamos un if para cada variable
        if((dia != 0) && (dia <= 30)){
            if ((mes != 0)&&(mes <= 12)){
                if ((anio != 0) && (anio <= 2023)){
                    System.out.println("La fecha ingresada es: " + dia + "/" + mes + "/" + anio);
                }
                else {
                    System.out.println( "La fecha y el año son incorrectos");
                }
            }
            else {
                System.out.println("La fecha y el mes son incorrectos");
            }
        }
        else {
            System.out.println("Fecha y dia incorrecto");
            entrada.close(); 
        }
        } 
    
    }

