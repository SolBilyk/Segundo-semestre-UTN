public class Aritmetica {
    // Atributos de clase

    int a; // se asigna 0 por defecto
    int b;

    // Sobrecarga de constructores
    // el constructor es un metodo especial
    public Aritmetica() {
        System.out.println("Se esta ejecutando este constructor numero 1");
    }

    public Aritmetica(int a, int b) {
        this.a = a;
        this.b = b;
        System.out.println("Se ejecuta el constructor 2");
    }

    // Creamos metodos
    public void sumarNumeros() {
        int res = a + b;
        System.out.println("Resultado= " + res);
    }

    public int sumarConRetorno() {
        int resultado = a + b;
        return resultado;
    }

    public int sumarConArgumentos(int a, int b) {
        // a=arg1;
        this.a = a;
        // b=arg2;
        this.b = b;
        // return a+b;
        // return sumarConRetorno();
        return this.sumarConRetorno();
    }
}