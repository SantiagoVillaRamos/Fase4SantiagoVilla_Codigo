# Documento de Especificación de Requerimientos de Software (SRS)
## Proyecto: Aplicación de Arquitectura de Estructuras Binarias
**Curso:** Estructuras de Datos — UNAD | Quinto Semestre  
**Fase:** 4 — Arquitectura de Estructuras Binarias  
**Autor:** Santiago Villa  
**Fecha:** Mayo 2026  
**Versión:** 1.0  
**Basado en:** IEEE 830 / Wiegers 2013

---

## 1. Requerimientos Funcionales Detallados

Esta sección desciende a nivel de decisiones de interfaz y diseño de implementación física.

### RF-01: Campo de Entrada de Valor

- El campo de entrada de datos debe ser un widget `Entry` de Tkinter de ancho máximo **10 caracteres**.
- Solo se aceptarán **dígitos numéricos enteros** (positivos y negativos). El sistema aplicará validación en el evento `<FocusOut>` y en el clic del botón de acción.
- El campo debe limpiarse automáticamente tras cada operación exitosa de inserción o eliminación.
- El campo debe tener el foco (cursor activo) al iniciar la aplicación y tras completar cada operación.

### RF-02: Botones de Operación Principal

- Los botones de acción disponibles son: **Insertar**, **Eliminar**, **Buscar**, **Limpiar**.
- Los botones deben tener un estado **deshabilitado** (`DISABLED`) cuando la operación no aplique (ej. "Eliminar" y "Buscar" deshabilitados si el árbol está vacío).
- Los botones deben responder a la tecla `<Enter>` del teclado cuando el campo de entrada tiene el foco, siendo la acción por defecto "Insertar".

### RF-03: Botones de Recorrido

- Los botones de recorrido son tres: **Inorden**, **Preorden**, **Postorden**.
- Al presionar cualquiera de ellos, el resultado se muestra en un widget `Text` de solo lectura ubicado en el panel inferior de la interfaz.
- El panel de texto debe mostrar el **nombre del recorrido** seguido de los valores separados por ` → ` (ej. `Inorden: 10 → 20 → 30 → 45`).
- Los botones de recorrido deben estar **deshabilitados** cuando el árbol esté vacío.

### RF-04: Canvas de Visualización del Árbol

- El árbol se dibuja en un widget `Canvas` de Tkinter con dimensiones mínimas de **800 × 500 píxeles**, con soporte de scroll horizontal y vertical.
- Cada nodo se representa como un **círculo** (óvalo) de radio 22 píxeles.
- El **color de fondo del nodo** es `#2E86AB` (azul acero) y el texto del valor es blanco (`#FFFFFF`) en fuente `Helvetica 10 bold`.
- Las **aristas** (líneas de conexión) son de color `#A8DADC` con grosor de 2 píxeles.
- El nodo raíz se posiciona en el **centro horizontal superior** del canvas con un margen superior de 40 píxeles.
- El espaciado horizontal entre nodos en el mismo nivel se calcula como `canvas_width / (2 ^ profundidad)` para evitar solapamientos.
- El nodo resaltado por una búsqueda exitosa usa el color `#F4A261` (naranja) hasta que se realice otra operación.

### RF-05: Panel de Estadísticas

- El panel de estadísticas debe mostrar tres métricas en tiempo real:
  - **Nodos:** cantidad total de nodos en el árbol.
  - **Altura:** nivel máximo del árbol (la raíz tiene altura 1).
  - **Balanceado:** "Sí" si la diferencia de altura entre subárboles izquierdo y derecho en cada nodo es ≤ 1; "No" en caso contrario.
- Las estadísticas se actualizan **automáticamente** tras cada operación (insertar, eliminar, limpiar).

### RF-06: Mensajes al Usuario

- Todos los mensajes de error se muestran mediante `messagebox.showerror()` de Tkinter.
- Los mensajes de confirmación se muestran mediante `messagebox.showinfo()`.
- El diálogo de confirmación para "Limpiar" usa `messagebox.askyesno()`.

### RF-07: Algoritmo de Eliminación

- La eliminación de un nodo con **dos hijos** debe usar el algoritmo del **sucesor inorden** (nodo mínimo del subárbol derecho).
- La eliminación de un nodo con **un hijo** debe reemplazar el nodo por su único hijo.
- La eliminación de un nodo **hoja** (sin hijos) elimina directamente el nodo.

### RF-08: Arquitectura de Clases (POO)

El código debe organizarse en las siguientes clases:

| Clase | Archivo | Responsabilidad |
|-------|---------|----------------|
| `Nodo` | `models/nodo.py` | Representa un nodo del árbol con atributos: `valor`, `izquierdo`, `derecho` |
| `ArbolBinarioBusqueda` | `models/arbol_binario.py` | Lógica del ABB: insertar, eliminar, buscar, recorridos, altura, balance |
| `Controlador` | `controllers/controlador.py` | Intermediario entre la vista y el modelo; valida entradas y ejecuta operaciones |
| `VentanaPrincipal` | `views/ventana_principal.py` | Define y organiza todos los widgets de la interfaz Tkinter |
| `CanvasArbol` | `views/canvas_arbol.py` | Maneja el renderizado gráfico del árbol en el canvas |
| `main` | `main.py` | Punto de entrada; instancia la aplicación |

---

## 2. Atributos de Calidad

Los atributos de calidad se documentan mediante **escenarios** con seis elementos: Fuente, Estímulo, Contexto, Artefacto, Respuesta, Medida.

---

### AQ-01: Desempeño — Velocidad de Renderizado

| Elemento | Descripción |
|----------|-------------|
| **Fuente del estímulo** | El estudiante presiona el botón "Insertar" |
| **Estímulo** | Inserción de un nodo en el árbol |
| **Contexto de operación** | El árbol contiene entre 1 y 50 nodos; sistema ejecutándose en hardware estándar (≥4 GB RAM, CPU dual-core) |
| **Artefacto** | Módulo `CanvasArbol` (renderizado gráfico) |
| **Respuesta** | El sistema inserta el nodo y redibuja el árbol completo en el canvas |
| **Medida de respuesta** | El árbol actualizado debe ser visible en pantalla en **menos de 300 milisegundos** desde el clic |

---

### AQ-02: Usabilidad — Claridad de Mensajes de Error

| Elemento | Descripción |
|----------|-------------|
| **Fuente del estímulo** | Un estudiante sin experiencia previa en la aplicación |
| **Estímulo** | El usuario ingresa un valor no numérico en el campo de entrada (ej. `"abc"`) y presiona "Insertar" |
| **Contexto de operación** | Primera sesión de uso de la aplicación |
| **Artefacto** | Módulo de validación en `Controlador` |
| **Respuesta** | El sistema muestra un mensaje de error descriptivo indicando la causa y la acción correctiva |
| **Medida de respuesta** | El mensaje debe ser comprensible sin consultar documentación adicional; en pruebas de usuario, al menos el **90% de los participantes** debe comprender el error y corregirlo en el primer intento |

---

### AQ-03: Confiabilidad — Integridad del Árbol tras Eliminación

| Elemento | Descripción |
|----------|-------------|
| **Fuente del estímulo** | El estudiante ejecuta 20 operaciones consecutivas de inserción y eliminación aleatoria |
| **Estímulo** | Secuencia de eliminaciones incluyendo nodos hoja, nodos con un hijo y nodos con dos hijos |
| **Contexto de operación** | El árbol tiene entre 10 y 50 nodos; las eliminaciones incluyen la raíz |
| **Artefacto** | Método `eliminar()` de la clase `ArbolBinarioBusqueda` |
| **Respuesta** | El árbol mantiene la propiedad ABB (todo nodo izquierdo < raíz < todo nodo derecho) tras cada eliminación |
| **Medida de respuesta** | La validación de la propiedad ABB mediante un recorrido Inorden debe producir siempre una secuencia **estrictamente ascendente** en el **100% de los casos** |

---

### AQ-04: Mantenibilidad — Separación de Responsabilidades

| Elemento | Descripción |
|----------|-------------|
| **Fuente del estímulo** | Un desarrollador (o el tutor evaluando el código) necesita modificar el algoritmo de eliminación |
| **Estímulo** | Solicitud de cambio en la lógica de eliminación (ej. usar predecesor inorden en lugar de sucesor) |
| **Contexto de operación** | Entorno de desarrollo en VS Code; código fuente disponible |
| **Artefacto** | Clase `ArbolBinarioBusqueda` en `models/arbol_binario.py` |
| **Respuesta** | El cambio se realiza únicamente en el método `eliminar()` sin tocar la vista ni el controlador |
| **Medida de respuesta** | El cambio debe requerir modificaciones en **máximo 1 archivo** del proyecto |

---

### AQ-05: Portabilidad — Ejecución Multiplataforma

| Elemento | Descripción |
|----------|-------------|
| **Fuente del estímulo** | El tutor descarga el .zip del proyecto para evaluarlo |
| **Estímulo** | El tutor ejecuta `python main.py` en su sistema operativo (Windows o macOS) |
| **Contexto de operación** | Sistema con Python 3.10+ y Tkinter instalado; sin configuración adicional |
| **Artefacto** | Aplicación completa (todos los módulos) |
| **Respuesta** | La aplicación inicia correctamente y presenta la interfaz gráfica sin errores de dependencia |
| **Medida de respuesta** | La aplicación debe ejecutarse sin modificaciones en **Linux, Windows y macOS** |

---

## 3. Restricciones

Las siguientes restricciones son **inamovibles** y operan como drivers arquitectónicos con prioridad absoluta:

| ID | Tipo | Restricción |
|----|------|-------------|
| REST-01 | Técnica | El código debe estar escrito en **Python 3.10+** como lenguaje principal (requerimiento del curso) |
| REST-02 | Técnica | La interfaz gráfica debe implementarse con **Tkinter** (librería estándar; no se permiten dependencias externas de pago) |
| REST-03 | Técnica | La arquitectura del código debe seguir el paradigma de **Programación Orientada a Objetos** con mínimo 4 clases diferenciadas |
| REST-04 | Académica | El documento de entrega debe llamarse exactamente **`Fase4SantiagoVilla`** y seguir la estructura definida en la guía de actividades (APA) |
| REST-05 | Académica | El código completo debe entregarse en un archivo **`.zip`** con enlace público (ej. GitHub, Google Drive) |
| REST-06 | Temporal | El desarrollo completo debe finalizarse dentro de las **fechas establecidas en la agenda del curso UNAD** |
| REST-07 | Económica | No se puede adquirir ninguna librería, herramienta o servicio de pago; solo se permiten recursos **gratuitos y open source** |
| REST-08 | Técnica | El sistema debe funcionar **completamente offline**; no requiere conexión a internet en tiempo de ejecución |

---

## 4. Interfaces Externas

### 4.1 Interfaces de Software

| ID | Interfaz | Descripción |
|----|----------|-------------|
| IE-01 | **Python Standard Library** | La aplicación usa exclusivamente módulos de la librería estándar de Python (`tkinter`, `tkinter.messagebox`, `tkinter.ttk`). No requiere instalación de paquetes externos via `pip`. |
| IE-02 | **Sistema Operativo (OS)** | La aplicación interactúa con el SO únicamente para: (a) renderizar la ventana gráfica mediante el sistema de ventanas nativo (X11 en Linux, Win32 en Windows, Quartz en macOS), y (b) gestionar el foco del teclado. |

### 4.2 Interfaces de Hardware

| ID | Interfaz | Descripción |
|----|----------|-------------|
| IH-01 | **Teclado** | El sistema acepta entrada del usuario a través del teclado para ingresar valores numéricos. Se vinculan los eventos `<Return>` (Enter) para activar la operación de inserción por defecto. |
| IH-02 | **Ratón/Mouse** | Los botones de operación, los botones de recorrido y el canvas responden a eventos de clic (`<Button-1>`). El canvas soporta scroll con la rueda del ratón para árboles con muchos nodos. |
| IH-03 | **Pantalla** | La aplicación requiere una pantalla con resolución mínima de **1024 × 768 píxeles** para mostrar correctamente el canvas y todos los paneles de control. |

### 4.3 Interfaces de Comunicación

| ID | Interfaz | Descripción |
|----|----------|-------------|
| IC-01 | **No aplica** | La versión 1.0 es una aplicación de escritorio **monousuario y offline**. No implementa ningún protocolo de red (HTTP, TCP/IP, WebSocket, etc.) ni se conecta a servicios externos, APIs de terceros o bases de datos remotas. |

---

## 5. Reglas de Negocio / Invariantes del Sistema

Estas reglas deben mantenerse en **todo momento** durante la ejecución:

| ID | Regla |
|----|-------|
| RN-01 | La propiedad ABB debe preservarse: para todo nodo N, todos los valores en el subárbol izquierdo son **estrictamente menores** que N, y todos los valores en el subárbol derecho son **estrictamente mayores** que N |
| RN-02 | No se permiten valores **duplicados** en el árbol |
| RN-03 | El árbol solo acepta valores de tipo **entero** (int) en la versión 1.0 |
| RN-04 | El canvas siempre muestra el estado **actualizado** del árbol; nunca puede estar desincronizado con el modelo de datos |
| RN-05 | El panel de estadísticas refleja siempre el estado **actual** del árbol tras cualquier operación |

---

*Documento generado para el proyecto académico Fase 4 — UNAD, Estructuras de Datos, Quinto Semestre.*
