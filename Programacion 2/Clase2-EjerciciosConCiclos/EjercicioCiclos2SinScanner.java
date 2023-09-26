import javax.swing.JOptionPane;

public class EjercicioCiclos2SinScanner {
    public static void main(String[] args) {
       int numero;
       numero = Integer.parseInt(JOptionPane.showInputDialog("Señor usuario ingrese un numero: "));
    while(numero != 0){
        if (numero > 0){
            System.out.println("El numero "+numero+" es positivo!!!");
        }
        else {
            System.out.println("El numero "+numero+" es negativo!!!");
        }
    numero = Integer.parseInt(JOptionPane.showInputDialog("Señor usuario ingrese otro un numero: "));
    }

    JOptionPane.showMessageDialog(null,"El numero "+numero+" finaliza el programa" );
}
}
