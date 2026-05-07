# Fase 4 — Arquitectura de Estructuras Binarias

**Autor:** Santiago Villa
**Curso:** Estructuras de Datos — UNAD
**Semestre:** Quinto
**Año:** 2026

---

## 📌 Descripción del Proyecto

Esta es una aplicación de escritorio desarrollada en **Python 3.10+** con interfaz gráfica **Tkinter** que implementa un **Árbol Binario de Búsqueda (ABB)** de forma interactiva y visual. El sistema permite al usuario insertar, buscar y eliminar nodos (números enteros), mientras el árbol se dibuja dinámicamente en pantalla, soportando hasta un máximo de 4 niveles de profundidad.

Adicionalmente, el proyecto ejecuta y grafica en tiempo real los recorridos estándar de árboles binarios:
*   **Preorden** (Raíz → Izquierda → Derecha)
*   **Inorden** (Izquierda → Raíz → Derecha)
*   **Posorden** (Izquierda → Derecha → Raíz)

Este proyecto da cumplimiento al resultado de aprendizaje de aplicar los fundamentos de la teoría general de árboles binarios mediante interfaces gráficas y Programación Orientada a Objetos.

---

## 🏗 Arquitectura del Sistema

La aplicación está diseñada siguiendo estrictamente el paradigma de **Programación Orientada a Objetos (POO)** y un patrón arquitectónico derivado de **MVC (Modelo-Vista-Controlador)** para asegurar una alta cohesión y bajo acoplamiento:

*   **Modelo (`src/models/`):**
    *   `nodo.py`: Define la estructura básica de datos (el nodo) con un valor numérico y punteros a sus hijos izquierdo y derecho.
    *   `arbol_binario.py`: Contiene toda la lógica de negocio y reglas del Árbol Binario de Búsqueda (validaciones de nivel máximo, inserción recursiva, algoritmos de recorrido, y prevención de duplicados).
*   **Vista (`src/views/`):**
    *   `login_window.py`: Gestiona la interfaz de acceso inicial, validando la contraseña genérica.
    *   `main_window.py`: Contiene la interfaz gráfica principal utilizando lienzos (`Canvas`) de Tkinter para dibujar la representación del árbol y sus secuencias de recorrido.
*   **Controlador (`src/controllers/`):**
    *   `controlador.py`: Actúa como intermediario. Recibe los inputs del usuario desde la vista, maneja las excepciones, delega las acciones al modelo y devuelve respuestas formateadas para que la vista actualice la pantalla.

**Estructura de Directorios:**
```text
arquitectura_de_estructuras_binarias/
├── src/
│   ├── main.py
│   ├── controllers/
│   │   └── controlador.py
│   ├── models/
│   │   ├── arbol_binario.py
│   │   └── nodo.py
│   └── views/
│       ├── login_window.py
│       └── main_window.py
└── README.md
```

---

## 🚀 Requisitos del Sistema

- **Lenguaje:** Python 3.10 o superior.
- **Librería gráfica:** Tkinter (Incluida por defecto en la instalación estándar de Python en Windows/macOS. En distribuciones Linux basadas en Debian/Ubuntu puede requerir ejecutar `sudo apt install python3-tk`).
- No requiere dependencias externas vía `pip`.

---

## 💻 Cómo Ejecutar la Aplicación

Sigue estos pasos para iniciar la aplicación localmente:

1.  **Clona este repositorio** o descarga y descomprime el archivo `.zip`.
2.  Abre una terminal y **navega hasta el directorio del proyecto**:
    ```bash
    cd ruta/hasta/arquitectura_de_estructuras_binarias
    ```
3.  **Ingresa a la carpeta del código fuente:**
    ```bash
    cd src
    ```
4.  **Ejecuta el archivo principal:**
    ```bash
    python3 main.py
    ```
    *(Nota: Dependiendo de tu sistema operativo, el comando puede ser simplemente `python main.py`)*
5.  **Credenciales de acceso:** Al abrirse la ventana inicial, ingresa la contraseña genérica para acceder a la aplicación:
    *   **Contraseña:** `ARBOL`

---
*Proyecto académico — UNAD, Ingeniería de Sistemas.*
