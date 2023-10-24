public class PruebaP{
    public static void main(String[] args) {
        Persona persona1; //variable local
        persona1 = new Persona(); //llamamos al constructor
        persona1.nombre="Juan";
        persona1.apellido="Belich";
        persona1.obtenerInformacion();

        Persona persona2=new Persona();
        System.out.println("persona2 = "+persona2);//imprimimos el espacio de memoria
        System.out.println("persona1 = "+persona1);

        persona2.obtenerInformacion(); //null porque no se le cargo ningun valor

        persona2.nombre="Osbaldo";
        persona2.apellido="giordanini";
        persona2.obtenerInformacion();
        
    }
}