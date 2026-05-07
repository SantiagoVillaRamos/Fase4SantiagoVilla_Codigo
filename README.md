# Fase 4 — Arquitectura de Estructuras Binarias
**Autor:** Santiago Villa | **Curso:** Estructuras de Datos — UNAD | **Semestre:** Quinto | **Año:** 2026

---

## Descripción del Proyecto

Aplicación de escritorio desarrollada en **Python 3.10+** con interfaz gráfica **Tkinter** que implementa un **Árbol Binario de Búsqueda (ABB)** interactivo. El sistema permite insertar, eliminar, buscar y recorrer nodos con representación visual dinámica, aplicando principios de **Programación Orientada a Objetos**.

**RAC 3:** *Aplicar los fundamentos de la teoría general de árboles binarios como estructuras jerárquicas de datos, a través del diseño de interfaces gráficas de árboles binarios codificados en un lenguaje de programación orientado a objetos, para la solución de problemas de aplicación.*

---

## Estructura del Proyecto

```
arquitectura_de_estructuras_binarias/
│
├── docs/                                   # Documentación de planificación
│   ├── vision_alcance/
│   │   └── 01_vision_y_alcance.md          # Documento de Visión y Alcance (Wiegers 2013)
│   ├── requerimientos_usuario/
│   │   └── 02_requerimientos_usuario.md    # Historias de Usuario con criterios de aceptación
│   └── especificacion_requerimientos/
│       └── 03_especificacion_requerimientos.md  # SRS: RF detallados, QA, restricciones, interfaces
│
├── src/                                    # Código fuente de la aplicación
│   ├── models/
│   │   ├── nodo.py                         # Clase Nodo (valor, izquierdo, derecho)
│   │   └── arbol_binario.py               # Clase ArbolBinarioBusqueda (lógica del ABB)
│   ├── views/
│   │   ├── ventana_principal.py            # Clase VentanaPrincipal (layout Tkinter)
│   │   └── canvas_arbol.py                # Clase CanvasArbol (renderizado gráfico)
│   ├── controllers/
│   │   └── controlador.py                 # Clase Controlador (mediador Vista-Modelo)
│   └── main.py                            # Punto de entrada de la aplicación
│
├── tests/                                  # Pruebas unitarias
│   └── test_arbol_binario.py              # Tests de inserción, eliminación, recorridos
│
└── README.md                              # Este archivo
```

---

## Documentos de Planificación

| # | Documento | Descripción |
|---|-----------|-------------|
| 1 | [Visión y Alcance](docs/vision_alcance/01_vision_y_alcance.md) | Requerimientos de negocio, visión de la solución, alcance y contexto |
| 2 | [Requerimientos de Usuario](docs/requerimientos_usuario/02_requerimientos_usuario.md) | Historias de usuario (primarias y secundarias) con criterios de aceptación |
| 3 | [Especificación de Requerimientos (SRS)](docs/especificacion_requerimientos/03_especificacion_requerimientos.md) | RF detallados, atributos de calidad (escenarios), restricciones, interfaces externas |

---

## Requisitos del Sistema

- Python 3.10 o superior
- Tkinter (incluido en Python estándar; en Linux instalar con `sudo apt install python3-tk`)
- Sin dependencias externas adicionales

---

## Cómo Ejecutar

```bash
# 1. Clonar o descomprimir el proyecto
# 2. Verificar Python y Tkinter
python3 --version
python3 -c "import tkinter; print('Tkinter OK')"

# 3. Ejecutar la aplicación
cd src
python3 main.py
```

---

## Entrega Académica

El documento de entrega se llama **`Fase4SantiagoVilla`** y contiene:

| Página | Contenido | Idioma |
|--------|-----------|--------|
| 1 | Portada con normas APA | Español |
| 2 | Introducción | **Inglés** |
| 3 | Objetivos | **Inglés** |
| 4 | Enlace al archivo .zip con el código completo (público) | — |
| 5 | Conclusiones | **Inglés** |
| 6 | Referencias bibliográficas | APA |

---

*Proyecto académico — UNAD, Estructuras de Datos, Quinto Semestre, 2026.*
