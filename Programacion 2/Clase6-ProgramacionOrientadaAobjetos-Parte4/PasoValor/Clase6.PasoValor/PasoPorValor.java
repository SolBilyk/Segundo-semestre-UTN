public class PasoPorValor{
    public static void main(String[] args) {
        var x=20;
        System.out.println("ValorX ="+x);
        cambioValor(x);//solo le envviamos una copia
        System.out.println("ValorX ="+ x);
    }

    public static void cambioValor(int arg1){
        System.out.println("arg1 = "+arg1);
        arg1=15;
    }
}