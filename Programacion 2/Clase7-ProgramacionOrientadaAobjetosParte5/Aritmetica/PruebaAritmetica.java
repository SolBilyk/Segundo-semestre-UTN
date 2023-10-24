public class PruebaAritmetica {
    public static void main(String[] args) {  /*Creamos un objeto de la clase aritmetica */
        //var a=10;   //variables locales
       // int b=7;    //memoria stack
        miMetodo(); //llamamos al metodo nuevo

        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();

        //para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " + resultado);

        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);

        Aritmetica aritmetica2=new Aritmetica(5,8);
        System.out.println("aritmetica 2= "+aritmetica2.a);
        System.out.println("aritmetica 2= "+aritmetica2.b);
        // aritmetica1=null; lo utilizamos para limpiar el valor del objeto pero no hace falta
        // System.gc(); otro metodo para limpiar pero tampoco hace falta
        Persona persona = new Persona("Ariel", "Betancud");
        System.out.println("persona ="+persona);
        System.out.println("Persona nombre "+persona.nombre);
        System.out.println("Persona nombre "+persona.apellido);

    }
    public static void miMetodo(){
        // int a=10;
        System.out.println("Aqui hay otro metodo");
    }

}

class Persona{
    //solo puede haber una clase tipo public y se asigna default o package a las nuevas classes
    String nombre;
    String apellido;

    Persona(String nombre, String apellido){ //constructor
        // super(); //llamada al constructor de clase padre
        new Imprimir().imprimir(this);
        this.nombre=nombre;
        this.apellido=apellido;
        System.out.println("Objeto persona usando this "+this.nombre);
    }
}

class Imprimir{
    public Imprimir(){
        super();
    }
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresion del objetoi actial (this): "+this );
    }
}
