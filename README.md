# 📅 ScheduleControl

Sistema de gestión de turnos y citas para negocios pequeños como barberías, consultorios o centros de servicios.

---

## 🚀 Descripción

ScheduleControl permite administrar de forma organizada:

- Clientes  
- Servicios  
- Citas  

El sistema evita conflictos de horarios y asegura que las citas se asignen dentro del horario de atención del negocio.

---

## 🧠 Funcionalidades principales

✅ Registro y gestión de clientes  
✅ Creación y administración de servicios  
✅ Agendamiento de citas  
✅ Validación de citas cruzadas (sin solapamientos)  
✅ Validación de horario del negocio  
✅ Edición y eliminación de registros  
✅ Interfaz web (frontend con Flask templates)  

---

## 🛠️ Tecnologías utilizadas

- Python 🐍  
- Flask  
- Flask-SQLAlchemy  
- SQLite  
- HTML + CSS  
- Jinja2  

---

## 📁 Estructura del proyecto

schedulecontrol/
│
├── app/
│ ├── models/
│ ├── routes/
│ ├── templates/
│ ├── static/
│ └── extensions.py
│
├── instance/
│ └── schedulecontrol.db
│
├── run.py
├── requirements.txt
└── README.md


---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/FredyBernal02/schedulecontrol.git
cd schedulecontrol

Crear entorno virtual:

python3 -m venv venv
source venv/bin/activate

Instalar dependencias:

pip install -r requirements.txt

Ejecutar la aplicación:

python run.py

Abrir en navegador:

http://127.0.0.1:5000

📸 Capturas del sistema

Panel principal
Gestión de clientes
Gestión de servicios
Gestión de citas

📌 Estado del proyecto

🟢 Backend completo
🟢 Frontend funcional
🟡 Mejoras visuales en progreso
🔜 Vista para clientes (agendamiento público)

👨‍💻 Autor

Fredy Bernal

GitHub: https://github.com/FredyBernal02
LinkedIn: https://www.linkedin.com/in/fredybernaltech

📘 Proyecto académico

Desarrollado como parte del programa ADSO - SENA
Ficha: 2721519

