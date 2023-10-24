import java.util.Scanner;

public class Ejercicio10SCA {
    public static void main(String[] args) {
        Scanner entrada= new Scanner(System.in);
        int numero, suma=0;
        for(int i=1;i<=10;i++){
            System.out.println("Engrese un numero: ");
            numero= Integer.parseInt(entrada.nextLine());
            suma+=numero;
        }
        System.out.println("\n La suma de todos los numeros es: "+suma);
        entrada.close();
    }
}
