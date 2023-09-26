package Clase3;

import javax.swing.JOptionPane;

public class Ciclos3ConJOption {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        
        while(numero != 0) {
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null, "El número ingresado " + numero + " es PAR");
            } else {
                JOptionPane.showMessageDialog(null, "El número ingresado " + numero + " es IMPAR");
            }
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número: "));
        }
        
        JOptionPane.showMessageDialog(null, "El número ingresado es " + numero + ". Finaliza el programa.");
    }
}
