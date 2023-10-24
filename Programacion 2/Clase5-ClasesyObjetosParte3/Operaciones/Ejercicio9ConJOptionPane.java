package Operaciones;

import javax.swing.JOptionPane;

public class Ejercicio9ConJOptionPane {
    public static void main(String[] args) {

    int dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el dia: "));
    int mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes: "));
    int anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año: "));

        //usamos un if para cada variable
        if((dia != 0) && (dia <= 30)){
            if ((mes != 0)&&(mes <= 12)){
                if ((anio != 0) && (anio <= 2023)){
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: " + dia + "/" + mes + "/" + anio);
                }
                else {
                    JOptionPane.showMessageDialog(null, "La fecha y el año son incorrectos");
                }
            }
            else {
                JOptionPane.showMessageDialog(null, "La fecha y el mes son incorrectos");
                
            }
        }
        else {
            JOptionPane.showMessageDialog(null, "Fecha y dia incorrecto");
        }
    
    }
}

