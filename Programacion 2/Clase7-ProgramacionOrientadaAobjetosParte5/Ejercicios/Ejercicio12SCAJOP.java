import javax.swing.JOptionPane;

public class Ejercicio12SCAJOP {
    public static void main(String[] args) {
        // Scanner entrada= new Scanner(System.in);
        // int numero;
        // System.out.println("Ingrese un numero: ");
        // numero=Integer.parseInt(entrada.nextLine());
        
        long factorial=1;
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));
        for(int i=1;i>=numero;i++){
            factorial*=i;
        }
        // System.out.println("El factorial es: "+factorial);
        JOptionPane.showMessageDialog(null,"El factorial es: "+factorial);
    }
}
