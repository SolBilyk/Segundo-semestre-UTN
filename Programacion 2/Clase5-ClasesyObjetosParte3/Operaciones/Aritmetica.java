package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;

    //Metodo
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("Resultado =" + resultado);
    }

    public int sumarConRetorno(){ //nos regresa un dato entero
        int resultado = a + b; //podemos poner una variable o una expresion
        return resultado;

    }

    public int sumarConArgumentos(int arg1, int arg2) {
        this.a = arg1; //llamamos al nuevo metodo y proporcionamos 2 metodos enteros, recibe y devuelve tipos enteros
        this.b = arg2;
        //return a + b; //hacemos un regreso de la suma
        return this.sumarConRetorno(); //dentro de un metodo pedimos que se retorne otro metodo, esto se hace solo dentro de una misma clase
    //cambio en las variables de arriba donde decia a = arg1 pongo el this
    //la variable this se crea mientras se crea automaticamente, apunta al objeto en ejecucion, al espacio de memoria donde esta el objeto para hacer modificacione
    //el uso del this hace referencia a un atributo y no una variable, su uso es opcional, hace que sea mas legile el codigo y que se diferencien los atributos de los argumentos aunque tengan el mismo nombre
    }
}
