package Caja;

public class pruebaCaja {
    public static void main(String args[]){
        // variables locales
        int mAncho = 3;
        int mAlto = 2; // valores ingresados
        int mProf = 6;

        Caja caja1 = new Caja();
        caja1.ancho = mAncho;
        caja1.alto = mAlto;
        caja1.profundidad = mProf;
        int resultado = caja1.volumen();
        System.out.println("resultado de volumen de caja 1 es: " + resultado);

        Caja caja2 = new Caja(2, 4, 6); // llamamos al constructor 2 con nuevos argumentos
        // llamamos con el nuevo objeto al metodo para un nuevo calculo
        System.out.println("resultado volumen de caja2: " + caja2.volumen());

    }
}

