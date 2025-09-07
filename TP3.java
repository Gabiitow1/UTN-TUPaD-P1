// CasoPráctico.java
public class CasoPractico {
    public static void main(String[] args) {
        // 1. Registro de Estudiantes
        System.out.println("===== 1. REGISTRO DE ESTUDIANTES =====");
        Estudiante estudiante = new Estudiante("Juan", "Pérez", "Programación I", 7);
        estudiante.mostrarInfo();
        estudiante.subirCalificacion(2);
        estudiante.bajarCalificacion(1);
        estudiante.mostrarInfo();

        // 2. Registro de Mascotas
        System.out.println("\n===== 2. REGISTRO DE MASCOTAS =====");
        Mascota mascota = new Mascota("Firulais", "Perro", 3);
        mascota.mostrarInfo();
        mascota.cumplirAnios();
        mascota.mostrarInfo();

        // 3. Encapsulamiento con Libro
        System.out.println("\n===== 3. LIBRO (ENCAPSULAMIENTO) =====");
        Libro libro = new Libro("El Quijote", "Miguel de Cervantes", 1605);
        libro.setAnioPublicacion(3000); // inválido
        libro.setAnioPublicacion(2005); // válido
        System.out.println("Título: " + libro.getTitulo() +
                ", Autor: " + libro.getAutor() +
                ", Año: " + libro.getAnioPublicacion());

        // 4. Gestión de Gallinas
        System.out.println("\n===== 4. GESTIÓN DE GALLINAS =====");
        Gallina g1 = new Gallina(1, 2, 10);
        Gallina g2 = new Gallina(2, 1, 5);
        g1.ponerHuevo();
        g1.envejecer();
        g2.envejecer();
        g2.ponerHuevo();
        g1.mostrarEstado();
        g2.mostrarEstado();

        // 5. Simulación Nave Espacial
        System.out.println("\n===== 5. NAVE ESPACIAL =====");
        NaveEspacial nave = new NaveEspacial("Apollo", 50, 100);
        nave.avanzar(20); // sin recargar
        nave.recargarCombustible(30);
        nave.avanzar(40);
        nave.mostrarEstado();
    }
}

// ===== 1. Clase Estudiante =====
class Estudiante {
    private String nombre;
    private String apellido;
    private String curso;
    private int calificacion;

    public Estudiante(String nombre, String apellido, String curso, int calificacion) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.curso = curso;
        this.calificacion = calificacion;
    }

    public void mostrarInfo() {
        System.out.println("Estudiante: " + nombre + " " + apellido +
                " | Curso: " + curso + " | Calificación: " + calificacion);
    }

    public void subirCalificacion(int puntos) {
        calificacion += puntos;
        System.out.println(nombre + " subió su calificación a: " + calificacion);
    }

    public void bajarCalificacion(int puntos) {
        calificacion -= puntos;
        if (calificacion < 0) calificacion = 0;
        System.out.println(nombre + " bajó su calificación a: " + calificacion);
    }
}

// ===== 2. Clase Mascota =====
class Mascota {
    private String nombre;
    private String especie;
    private int edad;

    public Mascota(String nombre, String especie, int edad) {
        this.nombre = nombre;
        this.especie = especie;
        this.edad = edad;
    }

    public void mostrarInfo() {
        System.out.println("Mascota: " + nombre + " | Especie: " + especie + " | Edad: " + edad);
    }

    public void cumplirAnios() {
        edad++;
        System.out.println(nombre + " ha cumplido años. Ahora tiene " + edad);
    }
}

// ===== 3. Clase Libro (Encapsulamiento) =====
class Libro {
    private String titulo;
    private String autor;
    private int anioPublicacion;

    public Libro(String titulo, String autor, int anioPublicacion) {
        this.titulo = titulo;
        this.autor = autor;
        setAnioPublicacion(anioPublicacion); // usa setter con validación
    }

    public String getTitulo() { return titulo; }
    public String getAutor() { return autor; }
    public int getAnioPublicacion() { return anioPublicacion; }

    public void setAnioPublicacion(int anio) {
        if (anio > 0 && anio <= 2025) {
            this.anioPublicacion = anio;
        } else {
            System.out.println("Año inválido: " + anio);
        }
    }
}

// ===== 4. Clase Gallina =====
class Gallina {
    private int idGallina;
    private int edad;
    private int huevosPuestos;

    public Gallina(int idGallina, int edad, int huevosPuestos) {
        this.idGallina = idGallina;
        this.edad = edad;
        this.huevosPuestos = huevosPuestos;
    }

    public void ponerHuevo() {
        huevosPuestos++;
        System.out.println("La gallina " + idGallina + " puso un huevo.");
    }

    public void envejecer() {
        edad++;
        System.out.println("La gallina " + idGallina + " ahora tiene " + edad + " años.");
    }

    public void mostrarEstado() {
        System.out.println("Gallina " + idGallina +
                " | Edad: " + edad +
                " | Huevos puestos: " + huevosPuestos);
    }
}

// ===== 5. Clase Nave Espacial =====
class NaveEspacial {
    private String nombre;
    private int combustible;
    private int capacidadMaxima;

    public NaveEspacial(String nombre, int combustible, int capacidadMaxima) {
        this.nombre = nombre;
        this.combustible = combustible;
        this.capacidadMaxima = capacidadMaxima;
    }

    public void despegar() {
        if (combustible >= 10) {
            combustible -= 10;
            System.out.println(nombre + " ha despegado.");
        } else {
            System.out.println(nombre + " no tiene suficiente combustible para despegar.");
        }
    }

    public void avanzar(int distancia) {
        int consumo = distancia / 2; // ejemplo: 1 unidad de combustible por cada 2 de distancia
        if (combustible >= consumo) {
            combustible -= consumo;
            System.out.println(nombre + " avanzó " + distancia + " km. Combustible restante: " + combustible);
        } else {
            System.out.println(nombre + " no tiene suficiente combustible para avanzar " + distancia + " km.");
        }
    }

    public void recargarCombustible(int cantidad) {
        if (combustible + cantidad <= capacidadMaxima) {
            combustible += cantidad;
            System.out.println(nombre + " recargó " + cantidad + " unidades. Combustible actual: " + combustible);
        } else {
            combustible = capacidadMaxima;
            System.out.println(nombre + " se recargó al máximo (" + capacidadMaxima + ").");
        }
    }

    public void mostrarEstado() {
        System.out.println("Nave: " + nombre + " | Combustible: " + combustible + "/" + capacidadMaxima);
    }
}
