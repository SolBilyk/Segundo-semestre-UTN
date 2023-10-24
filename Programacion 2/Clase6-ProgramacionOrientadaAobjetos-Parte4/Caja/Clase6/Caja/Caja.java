package Caja;

public class Caja {
    // atributos
    int alto;
    int ancho;
    int profundidad;

    // metodos constructores (acciones)
    public Caja() { // constructor 1 vacio

    }

    // contructor2 con parametros
    public Caja(int ancho, int alto, int profundidad) {
        this.alto = alto;
        this.ancho = ancho;
        this.profundidad = profundidad;
    }

    public int volumen() {
        return ancho * alto * profundidad;
    }

}