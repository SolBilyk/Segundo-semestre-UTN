/*Ejercicio 4: Pedir números hasta que se teclee un numero negativo y mostrar 
cuantos numeros se han introducido.
Con JOptionPane*/

package Clase3;

import javax.swing.JOptionPane;

public class Ciclos4ConJOption {
    public static void main(String[] args) {
        int numero,conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        while(numero >= 0){
            JOptionPane.showMessageDialog(null,"El numero "+numero+ " es positivo");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero: "));
        }
        JOptionPane.showMessageDialog(null,"Se ingresaron: "+conteo+" numeros positivos");
    }
}
