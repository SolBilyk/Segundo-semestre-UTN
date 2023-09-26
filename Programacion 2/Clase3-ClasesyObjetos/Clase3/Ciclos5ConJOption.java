package Clase3;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ciclos5ConJOption {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio= (int)(Math.random()*100); //esto genera un numero aleatorio.
        do {
            System.out.println("Ingrese un numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
            if (numero < aleatorio){
                JOptionPane.showMessageDialog(null, "Ingrese un numero MAYOR");}
            else if (numero > aleatorio){
               JOptionPane.showMessageDialog(null, "Ingrese un numero MENOR");}
            else{  //aca adivina el numero que ingreso el usuario
                JOptionPane.showMessageDialog(null,"FELICITACIONES!! Has adivinado el numero!!");
            }
            conteo++;
        } 
        while(numero != aleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el numero en "+conteo+" intentos.");
        entrada.close();
    }
}
