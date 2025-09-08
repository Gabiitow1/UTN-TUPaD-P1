// ========================================
// EJERCICIO 1: Pasaporte - Foto - Titular
// Composición y Asociación bidireccional
// ========================================
class Foto {
    private String imagen;
    private String formato;

    public Foto(String imagen, String formato) {
        this.imagen = imagen;
        this.formato = formato;
    }

    public String getImagen() { return imagen; }
    public String getFormato() { return formato; }
}

class Titular {
    private String nombre;
    private String dni;
    private Pasaporte pasaporte; // Asociación bidireccional

    public Titular(String nombre, String dni) {
        this.nombre = nombre;
        this.dni = dni;
    }

    public void setPasaporte(Pasaporte pasaporte) {
        this.pasaporte = pasaporte;
    }

    public Pasaporte getPasaporte() { return pasaporte; }
}

class Pasaporte {
    private String numero;
    private String fechaEmision;
    private Foto foto;  // Composición
    private Titular titular;  // Asociación bidireccional

    public Pasaporte(String numero, String fechaEmision, Foto foto) {
        this.numero = numero;
        this.fechaEmision = fechaEmision;
        this.foto = foto;
    }

    public void setTitular(Titular titular) {
        this.titular = titular;
        titular.setPasaporte(this);
    }

    public String getNumero() { return numero; }
    public String getFechaEmision() { return fechaEmision; }
    public Foto getFoto() { return foto; }
    public Titular getTitular() { return titular; }
}

// ========================================
// EJERCICIO 2: Celular - Batería - Usuario
// Agregación y Asociación bidireccional
// ========================================
class Bateria {
    private String modelo;
    private int capacidad;

    public Bateria(String modelo, int capacidad) {
        this.modelo = modelo;
        this.capacidad = capacidad;
    }

    public String getModelo() { return modelo; }
    public int getCapacidad() { return capacidad; }
}

class UsuarioCelular {
    private String nombre;
    private String dni;
    private Celular celular; // Asociación bidireccional

    public UsuarioCelular(String nombre, String dni) {
        this.nombre = nombre;
        this.dni = dni;
    }

    public void setCelular(Celular celular) {
        this.celular = celular;
    }

    public Celular getCelular() { return celular; }
}

class Celular {
    private String imei;
    private String marca;
    private String modelo;
    private Bateria bateria; // Agregación
    private UsuarioCelular usuario; // Asociación bidireccional

    public Celular(String imei, String marca, String modelo, Bateria bateria) {
        this.imei = imei;
        this.marca = marca;
        this.modelo = modelo;
        this.bateria = bateria;
    }

    public void setUsuario(UsuarioCelular usuario) {
        this.usuario = usuario;
        usuario.setCelular(this);
    }
}

// ========================================
// EJERCICIO 3: Libro - Autor - Editorial
// Asociación unidireccional y Agregación
// ========================================
class Autor {
    private String nombre;
    private String nacionalidad;

    public Autor(String nombre, String nacionalidad) {
        this.nombre = nombre;
        this.nacionalidad = nacionalidad;
    }
}

class Editorial {
    private String nombre;
    private String direccion;

    public Editorial(String nombre, String direccion) {
        this.nombre = nombre;
        this.direccion = direccion;
    }
}

class Libro {
    private String titulo;
    private String isbn;
    private Autor autor; // Asociación unidireccional
    private Editorial editorial; // Agregación

    public Libro(String titulo, String isbn, Autor autor, Editorial editorial) {
        this.titulo = titulo;
        this.isbn = isbn;
        this.autor = autor;
        this.editorial = editorial;
    }
}

// ========================================
// EJERCICIO 4: TarjetaDeCredito - Cliente - Banco
// Asociación bidireccional y Agregación
// ========================================
class Banco {
    private String nombre;
    private String cuit;

    public Banco(String nombre, String cuit) {
        this.nombre = nombre;
        this.cuit = cuit;
    }
}

class Cliente {
    private String nombre;
    private String dni;
    private TarjetaDeCredito tarjeta; // Asociación bidireccional

    public Cliente(String nombre, String dni) {
        this.nombre = nombre;
        this.dni = dni;
    }

    public void setTarjeta(TarjetaDeCredito tarjeta) {
        this.tarjeta = tarjeta;
    }

    public TarjetaDeCredito getTarjeta() { return tarjeta; }
}

class TarjetaDeCredito {
    private String numero;
    private String fechaVencimiento;
    private Cliente cliente; // Asociación bidireccional
    private Banco banco; // Agregación

    public TarjetaDeCredito(String numero, String fechaVencimiento, Banco banco) {
        this.numero = numero;
        this.fechaVencimiento = fechaVencimiento;
        this.banco = banco;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
        cliente.setTarjeta(this);
    }
}

// ========================================
// EJERCICIO 5: Computadora - PlacaMadre - Propietario
// Composición y Asociación bidireccional
// ========================================
class PlacaMadre {
    private String modelo;
    private String chipset;

    public PlacaMadre(String modelo, String chipset) {
        this.modelo = modelo;
        this.chipset = chipset;
    }
}

class Propietario {
    private String nombre;
    private String dni;
    private Computadora computadora; // Asociación bidireccional

    public Propietario(String nombre, String dni) {
        this.nombre = nombre;
        this.dni = dni;
    }

    public void setComputadora(Computadora computadora) {
        this.computadora = computadora;
    }
}

class Computadora {
    private String marca;
    private String numeroSerie;
    private PlacaMadre placa; // Composición
    private Propietario propietario; // Asociación bidireccional

    public Computadora(String marca, String numeroSerie, PlacaMadre placa) {
        this.marca = marca;
        this.numeroSerie = numeroSerie;
        this.placa = placa;
    }

    public void setPropietario(Propietario propietario) {
        this.propietario = propietario;
        propietario.setComputadora(this);
    }
}

// ========================================
// EJERCICIO 6: Reserva - Cliente - Mesa
// Asociación unidireccional y Agregación
// ========================================
class ClienteReserva {
    private String nombre;
    private String telefono;

    public ClienteReserva(String nombre, String telefono) {
        this.nombre = nombre;
        this.telefono = telefono;
    }
}

class Mesa {
    private int numero;
    private int capacidad;

    public Mesa(int numero, int capacidad) {
        this.numero = numero;
        this.capacidad = capacidad;
    }
}

class Reserva {
    private String fecha;
    private String hora;
    private ClienteReserva cliente; // Asociación unidireccional
    private Mesa mesa; // Agregación

    public Reserva(String fecha, String hora, ClienteReserva cliente, Mesa mesa) {
        this.fecha = fecha;
        this.hora = hora;
        this.cliente = cliente;
        this.mesa = mesa;
    }
}

// ========================================
// EJERCICIO 7: Vehículo - Motor - Conductor
// Agregación y Asociación bidireccional
// ========================================
class Motor {
    private String tipo;
    private String numeroSerie;

    public Motor(String tipo, String numeroSerie) {
        this.tipo = tipo;
        this.numeroSerie = numeroSerie;
    }
}

class Conductor {
    private String nombre;
    private String licencia;
    private Vehiculo vehiculo; // Asociación bidireccional

    public Conductor(String nombre, String licencia) {
        this.nombre = nombre;
        this.licencia = licencia;
    }

    public void setVehiculo(Vehiculo vehiculo) {
        this.vehiculo = vehiculo;
    }
}

class Vehiculo {
    private String patente;
    private String modelo;
    private Motor motor; // Agregación
    private Conductor conductor; // Asociación bidireccional

    public Vehiculo(String patente, String modelo, Motor motor) {
        this.patente = patente;
        this.modelo = modelo;
        this.motor = motor;
    }

    public void setConductor(Conductor conductor) {
        this.conductor = conductor;
        conductor.setVehiculo(this);
    }
}

// ========================================
// EJERCICIO 8: Documento - FirmaDigital - Usuario
// Composición y Agregación
// ========================================
class FirmaDigital {
    private String codigoHash;
    private String fecha;

    public FirmaDigital(String codigoHash, String fecha) {
        this.codigoHash = codigoHash;
        this.fecha = fecha;
    }
}

class UsuarioFirma {
    private String nombre;
    private String email;

    public UsuarioFirma(String nombre, String email) {
        this.nombre = nombre;
        this.email = email;
    }
}

class Documento {
    private String titulo;
    private String contenido;
    private FirmaDigital firma; // Composición

    public Documento(String titulo, String contenido, FirmaDigital firma) {
        this.titulo = titulo;
        this.contenido = contenido;
        this.firma = firma;
    }
}

// ========================================
// EJERCICIO 9: CitaMédica - Paciente - Profesional
// Asociación unidireccional
// ========================================
class Paciente {
    private String nombre;
    private String obraSocial;

    public Paciente(String nombre, String obraSocial) {
        this.nombre = nombre;
        this.obraSocial = obraSocial;
    }
}

class Profesional {
    private String nombre;
    private String especialidad;

    public Profesional(String nombre, String especialidad) {
        this.nombre = nombre;
        this.especialidad = especialidad;
    }
}

class CitaMedica {
    private String fecha;
    private String hora;
    private Paciente paciente; // Asociación unidireccional
    private Profesional profesional; // Asociación unidireccional

    public CitaMedica(String fecha, String hora, Paciente paciente, Profesional profesional) {
        this.fecha = fecha;
        this.hora = hora;
        this.paciente = paciente;
        this.profesional = profesional;
    }
}

// ========================================
// EJERCICIO 10: CuentaBancaria - ClaveSeguridad - Titular
// Composición y Asociación bidireccional
// ========================================
class ClaveSeguridad {
    private String codigo;
    private String ultimaModificacion;

    public ClaveSeguridad(String codigo, String ultimaModificacion) {
        this.codigo = codigo;
        this.ultimaModificacion = ultimaModificacion;
    }
}

class TitularCuenta {
    private String nombre;
    private String dni;
    private CuentaBancaria cuenta; // Asociación bidireccional

    public TitularCuenta(String nombre, String dni) {
        this.nombre = nombre;
        this.dni = dni;
    }

    public void setCuenta(CuentaBancaria cuenta) {
        this.cuenta = cuenta;
    }
}

class CuentaBancaria {
    private String cbu;
    private double saldo;
    private ClaveSeguridad clave; // Composición
    private TitularCuenta titular; // Asociación bidireccional

    public CuentaBancaria(String cbu, double saldo, ClaveSeguridad clave) {
        this.cbu = cbu;
        this.saldo = saldo;
        this.clave = clave;
    }

    public void setTitular(TitularCuenta titular) {
        this.titular = titular;
        titular.setCuenta(this);
    }
}

// ========================================
// EJERCICIO 11: Reproductor - Canción - Artista
// Asociación unidireccional y Dependencia de uso
// ========================================
class ArtistaMusical {
    private String nombre;
    private String genero;

    public ArtistaMusical(String nombre, String genero) {
        this.nombre = nombre;
        this.genero = genero;
    }
}

class CancionMusical {
    private String titulo;
    private ArtistaMusical artista;

    public CancionMusical(String titulo, ArtistaMusical artista) {
        this.titulo = titulo;
        this.artista = artista;
    }
}

class ReproductorMusical {
    public void reproducir(CancionMusical cancion) { // Dependencia de uso
        System.out.println("Reproduciendo: " + cancion.titulo);
    }
}

// ========================================
// EJERCICIO 12: Impuesto - Contribuyente - Calculadora
// Asociación unidireccional y Dependencia de uso
// ========================================
class Contribuyente {
    private String nombre;
    private String cuil;

    public Contribuyente(String nombre, String cuil) {
        this.nombre = nombre;
        this.cuil = cuil;
    }
}

class Impuesto {
    private double monto;

    public Impuesto(double monto) {
        this.monto = monto;
    }
}

class Calculadora {
    public void calcular(Impuesto impuesto) { // Dependencia de uso
        System.out.println("Calculando impuesto de: " + impuesto.monto);
    }
}

// ========================================
// EJERCICIO 13: GeneradorQR - Usuario - CódigoQR
// Asociación unidireccional y Dependencia de creación
// ========================================
class UsuarioQR {
    private String nombre;
    private String email;

    public UsuarioQR(String nombre, String email) {
        this.nombre = nombre;
        this.email = email;
    }
}

class CodigoQR {
    private String valor;
    private UsuarioQR usuario;

    public CodigoQR(String valor, UsuarioQR usuario) {
        this.valor = valor;
        this.usuario = usuario;
    }
}

class GeneradorQR {
    public void generar(String valor, UsuarioQR usuario) { // Dependencia de creación
        CodigoQR qr = new CodigoQR(valor, usuario);
        System.out.println("Generado QR: " + valor + " para usuario " + usuario.nombre);
    }
}

// ========================================
// EJERCICIO 14: EditorVideo - Proyecto - Render
// Asociación unidireccional y Dependencia de creación
// ========================================
class Proyecto {
    private String nombre;
    private int duracionMin;

    public Proyecto(String nombre, int duracionMin) {
        this.nombre = nombre;
        this.duracionMin = duracionMin;
    }
}

class Render {
    private String formato;
    private Proyecto proyecto;

    public Render(String formato, Proyecto proyecto) {
        this.formato = formato;
        this.proyecto = proyecto;
    }
}

class EditorVideo {
    public void exportar(String formato, Proyecto proyecto) { // Dependencia de creación
        Render render = new Render(formato, proyecto);
        System.out.println("Exportando proyecto " + proyecto.nombre + " en formato " + formato);
    }
}
