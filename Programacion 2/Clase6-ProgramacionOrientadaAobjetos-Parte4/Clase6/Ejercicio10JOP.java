import javax.swing.JOptionPane;

public class Ejercicio10JOP {
    public static void main(String[] args) {
        int numero, suma = 0;
        for (int i = 1; i <= 10; i++) {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
            suma += numero;
        }
        JOptionPane.showMessageDialog(null, "\n La suma de todos los numeros es: " + suma);

    }
}