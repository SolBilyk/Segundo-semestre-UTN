//Otra forma de hacerlo sin usar Scanner

import javax.swing.JOptionPane;

public class EjecicioCiclos1SinScanner {
    public static void main(String[] args) {

            int numero1, cuadrado1; //creo las variables.
            numero1 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero:")); //usando JOption podemos pedirle al usuario la informacion a traves de un cuadro de dialogo

            while(numero1 >= 0){ //le doy la condicion
                cuadrado1 = (int)Math.pow(numero1, 2); 
                System.out.println("El numero "+numero1+" elevado al cuadrado es: "+cuadrado1);
                numero1 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero:"));
            }

        System.out.println("El numero ingresado es negativo"); 
    }
}
