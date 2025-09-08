public class Empleado {

    // Atributos privados (encapsulamiento)
    private int id;
    private String nombre;
    private String puesto;
    private double salario;

    // Atributo estático para contar total de empleados
    private static int totalEmpleados = 0;
    private static int idAutomatico = 1; // para generar id automáticamente

    // Constructor con todos los atributos
    public Empleado(int id, String nombre, String puesto, double salario) {
        this.id = id;
        this.nombre = nombre;
        this.puesto = puesto;
        this.salario = salario;
        totalEmpleados++;
    }

    // Constructor con solo nombre y puesto
    public Empleado(String nombre, String puesto) {
        this.id = idAutomatico++;
        this.nombre = nombre;
        this.puesto = puesto;
        this.salario = 30000; // salario por defecto
        totalEmpleados++;
    }

    // Getters y Setters
    public int getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getPuesto() {
        return puesto;
    }

    public void setPuesto(String puesto) {
        this.puesto = puesto;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    // Métodos sobrecargados actualizarSalario
    // Aumento por porcentaje
    public void actualizarSalario(double porcentaje) {
        this.salario += this.salario * (porcentaje / 100);
    }

    // Aumento por cantidad fija
    public void actualizarSalario(double cantidad, boolean fijo) {
        this.salario += cantidad;
    }

    // Método toString
    @Override
    public String toString() {
        return "Empleado [ID=" + id + ", Nombre=" + nombre + ", Puesto=" + puesto + ", Salario=" + salario + "]";
    }

    // Método estático para mostrar total de empleados
    public static int mostrarTotalEmpleados() {
        return totalEmpleados;
    }
}

Clase Main de prueba

public class Main {
    public static void main(String[] args) {

        // Crear empleados con ambos constructores
        Empleado e1 = new Empleado("Ana Pérez", "Analista");
        Empleado e2 = new Empleado("Luis Gómez", "Programador");
        Empleado e3 = new Empleado(100, "María López", "Gerente", 60000);

        // Aplicar aumentos
        e1.actualizarSalario(10); // 10% de aumento
        e2.actualizarSalario(5000, true); // aumento fijo de 5000
        e3.actualizarSalario(5); // 5% de aumento

        // Mostrar información de cada empleado
        System.out.println(e1);
        System.out.println(e2);
        System.out.println(e3);

        // Mostrar total de empleados creados
        System.out.println("Total de empleados: " + Empleado.mostrarTotalEmpleados());
    }
}
