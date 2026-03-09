## Gestor de Tareas CLI en Python

🌐 **Languages**

[![English](https://img.shields.io/badge/English-blue?style=for-the-badge)](/README.md)
[![Português](https://img.shields.io/badge/Português-green?style=for-the-badge)](README_PT.md)
[![한국어](https://img.shields.io/badge/한국어-purple?style=for-the-badge)](README_KO.md)

Un gestor de tareas simple en línea de comandos hecho con Python. Este proyecto permite a los usuarios gestionar sus tareas diarias directamente desde el terminal de forma rápida y práctica.

### Funcionalidades

* Añadir nuevas tareas
* Listar todas las tareas
* Marcar tareas como completadas
* Eliminar tareas
* Almacenamiento persistente de datos usando archivos JSON
* Interfaz de línea de comandos simple e intuitiva

### Cómo funciona

Las tareas se almacenan en un archivo local `tasks.json`. Cada tarea contiene:

* **ID** – identificador único
* **Descripción de la tarea**
* **Estado** – "En progreso" o "Completado"

El programa carga el archivo JSON cuando se inicia y lo actualiza cada vez que se crea, completa o elimina una tarea.

### Tecnologías Utilizadas

* **Python 3**
* **JSON** para la persistencia de datos
* **Módulo OS** para utilidades del terminal

### Cómo usar

1. Clonar el repositorio:

```
git clone https://github.com/Hallow303/cli-task-manager.git
```

2. Navegar a la carpeta del proyecto:

```
cd cli-task-manager
```

3. Ejecutar el programa:

```
python main.py
```

4. Usar el menú del terminal para gestionar las tareas:

* Añadir una tarea
* Ver tareas
* Marcar una tarea como completada
* Eliminar una tarea

### Propósito

Este proyecto fue creado como un ejercicio de aprendizaje para practicar:

* Manejo de archivos en Python
* Trabajo con datos en JSON
* Construcción de aplicaciones simples en CLI
* Organización del código usando funciones
