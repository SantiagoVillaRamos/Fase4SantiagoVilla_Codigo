# Documento de Requerimientos de Usuario
## Proyecto: Aplicación de Arquitectura de Estructuras Binarias
**Curso:** Estructuras de Datos — UNAD | Quinto Semestre  
**Fase:** 4 — Arquitectura de Estructuras Binarias  
**Autor:** Santiago Villa  
**Fecha:** Mayo 2026  
**Versión:** 1.0  
**Enfoque:** Historias de Usuario (Metodología Ágil)

---

## 1. Clasificación de Requerimientos

### 1.1 Requerimientos Primarios (Servicios Fundamentales)

Son las funcionalidades núcleo que el usuario desea ejecutar directamente y que sostienen el propósito educativo de la aplicación.

| ID | Historia de Usuario |
|----|---------------------|
| HU-P01 | Como estudiante, quiero **insertar un nodo** en el árbol binario ingresando un valor entero, para construir la estructura de forma interactiva. |
| HU-P02 | Como estudiante, quiero **eliminar un nodo** del árbol dado su valor, para practicar la reestructuración del ABB. |
| HU-P03 | Como estudiante, quiero **buscar un nodo** por su valor y verlo resaltado en la pantalla, para verificar su existencia y posición dentro del árbol. |
| HU-P04 | Como estudiante, quiero **ver el árbol dibujado gráficamente** con nodos y conexiones, para entender visualmente su estructura jerárquica. |
| HU-P05 | Como estudiante, quiero **ejecutar los recorridos Inorden, Preorden y Postorden**, para estudiar los distintos órdenes de visita de los nodos. |

### 1.2 Requerimientos Secundarios (Servicios de Soporte)

Son las acciones que soportan o complementan la realización de los requerimientos primarios.

| ID | Historia de Usuario |
|----|---------------------|
| HU-S01 | Como estudiante, quiero **limpiar/reiniciar el árbol** con un solo clic, para comenzar un nuevo ejercicio sin cerrar la aplicación. |
| HU-S02 | Como estudiante, quiero **ver estadísticas del árbol** (altura, número de nodos, si está balanceado), para analizar su estado estructural. |
| HU-S03 | Como estudiante, quiero **recibir mensajes de error claros** cuando ingrese un valor inválido (ej. letra en lugar de número), para corregir mi entrada sin confusiones. |
| HU-S04 | Como estudiante, quiero **ver el resultado de un recorrido en un panel de texto**, para copiar o verificar la secuencia de nodos visitados. |
| HU-S05 | Como estudiante, quiero que **la aplicación responda con una confirmación** cuando inserto o elimino un nodo exitosamente, para saber que la operación fue realizada. |

---

## 2. Detalle de Historias de Usuario

---

### HU-P01: Insertar Nodo

**Historia:**  
> *"Como estudiante, quiero insertar un nodo en el árbol binario ingresando un valor entero, para construir la estructura de forma interactiva."*

**Criterios de Aceptación:**

| # | Escenario | Resultado Esperado |
|---|-----------|-------------------|
| CA-01 | El usuario ingresa el número `45` y presiona "Insertar" | El nodo con valor 45 aparece dibujado en la posición correcta del ABB |
| CA-02 | El usuario intenta insertar un valor ya existente (ej. `45` de nuevo) | El sistema muestra el mensaje: *"El valor 45 ya existe en el árbol."* y no altera el árbol |
| CA-03 | El usuario deja el campo vacío y presiona "Insertar" | El sistema muestra el mensaje: *"Debe ingresar un valor entero."* |
| CA-04 | El usuario ingresa una cadena de texto (ej. `"abc"`) | El sistema muestra: *"Valor inválido. Solo se permiten números enteros."* |

---

### HU-P02: Eliminar Nodo

**Historia:**  
> *"Como estudiante, quiero eliminar un nodo del árbol dado su valor, para practicar la reestructuración del ABB."*

**Criterios de Aceptación:**

| # | Escenario | Resultado Esperado |
|---|-----------|-------------------|
| CA-01 | El usuario ingresa `45` y presiona "Eliminar"; el nodo existe | El nodo es eliminado, el árbol se reestructura y se redibuja automáticamente |
| CA-02 | El nodo a eliminar tiene dos hijos | El sistema reemplaza el nodo con su sucesor inorden y redibuja el árbol |
| CA-03 | El usuario intenta eliminar un valor que no existe (ej. `99`) | El sistema muestra: *"El valor 99 no se encuentra en el árbol."* |
| CA-04 | El usuario intenta eliminar del árbol vacío | El sistema muestra: *"El árbol está vacío. No hay nodos para eliminar."* |

---

### HU-P03: Buscar Nodo

**Historia:**  
> *"Como estudiante, quiero buscar un nodo por su valor y verlo resaltado en la pantalla, para verificar su existencia y posición."*

**Criterios de Aceptación:**

| # | Escenario | Resultado Esperado |
|---|-----------|-------------------|
| CA-01 | El usuario busca un valor existente (ej. `30`) | El nodo 30 se resalta con un color diferente (ej. amarillo/naranja) en el canvas |
| CA-02 | El usuario busca un valor inexistente (ej. `999`) | El sistema muestra: *"El valor 999 no se encuentra en el árbol."* |
| CA-03 | Se realiza una nueva búsqueda | El resaltado anterior desaparece y el nuevo nodo encontrado se resalta |

---

### HU-P04: Visualización Gráfica del Árbol

**Historia:**  
> *"Como estudiante, quiero ver el árbol dibujado gráficamente con nodos y conexiones, para entender visualmente su estructura jerárquica."*

**Criterios de Aceptación:**

| # | Escenario | Resultado Esperado |
|---|-----------|-------------------|
| CA-01 | El árbol tiene al menos un nodo | El canvas muestra los nodos como círculos con su valor en el centro |
| CA-02 | Los nodos tienen nodos hijo | Las aristas (líneas) conectan correctamente cada nodo con sus hijos izquierdo y derecho |
| CA-03 | Se inserta o elimina un nodo | El árbol se redibuja automáticamente sin que el usuario deba realizar ninguna acción adicional |
| CA-04 | El árbol está vacío | El canvas muestra el mensaje: *"El árbol está vacío."* |

---

### HU-P05: Recorridos del Árbol

**Historia:**  
> *"Como estudiante, quiero ejecutar los recorridos Inorden, Preorden y Postorden, para estudiar los distintos órdenes de visita de los nodos."*

**Criterios de Aceptación:**

| # | Escenario | Resultado Esperado |
|---|-----------|-------------------|
| CA-01 | El usuario presiona "Inorden" con árbol no vacío | El panel de texto muestra la secuencia de nodos en orden ascendente |
| CA-02 | El usuario presiona "Preorden" | El panel de texto muestra: raíz → izquierda → derecha |
| CA-03 | El usuario presiona "Postorden" | El panel de texto muestra: izquierda → derecha → raíz |
| CA-04 | El usuario ejecuta un recorrido sobre árbol vacío | El sistema muestra: *"El árbol está vacío. Inserte al menos un nodo."* |

---

### HU-S01: Limpiar/Reiniciar el Árbol

**Historia:**  
> *"Como estudiante, quiero limpiar/reiniciar el árbol con un solo clic, para comenzar un nuevo ejercicio."*

**Criterios de Aceptación:**

| # | Escenario | Resultado Esperado |
|---|-----------|-------------------|
| CA-01 | El usuario presiona "Limpiar" con árbol no vacío | Se muestra un diálogo de confirmación: *"¿Desea eliminar todos los nodos del árbol?"* |
| CA-02 | El usuario confirma la acción | El árbol queda vacío, el canvas se limpia y las estadísticas se resetean a cero |
| CA-03 | El usuario cancela la acción | El árbol permanece intacto |

---

### HU-S02: Estadísticas del Árbol

**Historia:**  
> *"Como estudiante, quiero ver estadísticas del árbol (altura, número de nodos, si está balanceado), para analizar su estado estructural."*

**Criterios de Aceptación:**

| # | Escenario | Resultado Esperado |
|---|-----------|-------------------|
| CA-01 | El árbol tiene nodos | El panel de estadísticas muestra: altura actual, cantidad de nodos, estado de balance |
| CA-02 | Se inserta o elimina un nodo | Las estadísticas se actualizan automáticamente sin acción adicional del usuario |
| CA-03 | El árbol está vacío | Las estadísticas muestran: Altura: 0, Nodos: 0, Balanceado: N/A |

---

## 3. Mapa de Requerimientos vs. Objetivos de Negocio

| Historia | OB-01 | OB-02 | OB-03 | OB-04 | OB-05 |
|----------|:-----:|:-----:|:-----:|:-----:|:-----:|
| HU-P01 (Insertar) | ✅ | ✅ | | ✅ | |
| HU-P02 (Eliminar) | ✅ | ✅ | | ✅ | |
| HU-P03 (Buscar) | ✅ | ✅ | | ✅ | |
| HU-P04 (Visualizar) | | ✅ | | ✅ | |
| HU-P05 (Recorridos) | ✅ | | ✅ | ✅ | |
| HU-S01 (Limpiar) | | | | ✅ | |
| HU-S02 (Estadísticas) | ✅ | | | ✅ | |
| HU-S03 (Errores) | | | | ✅ | |
| HU-S04 (Panel texto) | | | ✅ | ✅ | |
| HU-S05 (Confirmación) | | | | ✅ | ✅ |

---

*Documento generado para el proyecto académico Fase 4 — UNAD, Estructuras de Datos, Quinto Semestre.*
