# ScheduleControl – Backend

ScheduleControl es un sistema de gestión de turnos y citas orientado a pequeños negocios, como barberías, consultorios, salones de belleza u otros servicios que trabajan bajo programación previa.

Este proyecto hace parte de la etapa productiva del programa **Análisis y Desarrollo de Software (ADSO)** del **SENA**.

---

## 🚀 Objetivo del proyecto

Desarrollar una aplicación web que permita a los negocios gestionar de manera organizada sus citas, clientes y servicios, reduciendo errores comunes como:

- Pérdida de citas
- Duplicación de horarios
- Falta de control sobre la agenda
- Uso de métodos manuales como cuadernos o archivos dispersos
- En esta etapa, el proyecto se enfoca en el desarrollo del backend, implementando la lógica de negocio y una API REST funcional.

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Flask** (Framework web)
- **Flask-SQLAlchemy**
- **SQLite**
- **Git & GitHub**
- **HTML / CSS** (frontend futuro)

---

## 📂 Estructura del proyecto

schedulecontrol/
├── app/
│   ├── models/
│   │   ├── negocio.py
│   │   ├── cliente.py
│   │   ├── servicio.py
│   │   ├── cita.py
│   │   └── usuarios.py
│   ├── routes/
│   │   ├── negocios.py
│   │   ├── clientes.py
│   │   ├── servicios.py
│   │   └── citas.py
│   └── __init__.py
├── instance/
│   └── schedulecontrol.db
├── create_db.py
├── run.py
├── requirements.txt
├── README.md
└── .gitignore

## 🔄 Funcionalidades implementadas (CRUD)

### Negocios
- Crear negocio con horario de atención

### Clientes
- Crear, listar, actualizar y eliminar clientes

### Servicios
- Crear, listar, actualizar y eliminar servicios

### Citas
- Crear, listar, actualizar estado y eliminar citas

## ⚠️ Reglas de negocio implementadas

- ❌ No se permiten citas cruzadas en el mismo negocio
- ❌ No se permiten citas fuera del horario de atención
- ✅ Validación de existencia de negocio, cliente y servicio
- 📩 Respuestas claras con códigos HTTP

## 📌 Estado del proyecto

✅ Backend completamente funcional  
🟡 Frontend pendiente  
🟡 Despliegue en la nube pendiente  

### 📁 Descripción de carpetas y archivos

- **app/**: Contiene la lógica principal del backend desarrollado con Flask.
  
- **app/models/**: Define los modelos de la base de datos mediante SQLAlchemy (Negocio, Cliente, Servicio, Cita y Usuario).

- **app/routes/**: Contiene los endpoints de la API REST organizados por módulo, implementando operaciones CRUD para cada entidad.

- **app/__init__.py**: Inicializa la aplicación Flask, configura la base de datos y registra los Blueprints.

- **instance/**: Almacena la base de datos SQLite utilizada durante el desarrollo.

- **create_db.py**: Script encargado de crear e inicializar la base de datos.

- **run.py**: Punto de entrada para ejecutar la aplicación Flask.

- **venv/**: Entorno virtual que contiene las dependencias del proyecto.

- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.

- **README.md**: Documentación general del proyecto.