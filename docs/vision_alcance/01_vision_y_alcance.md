# Documento de Visión y Alcance
## Proyecto: Aplicación de Arquitectura de Estructuras Binarias
**Curso:** Estructuras de Datos — UNAD | Quinto Semestre  
**Fase:** 4 — Arquitectura de Estructuras Binarias  
**Autor:** Santiago Villa  
**Fecha:** Mayo 2026  
**Versión:** 1.0

---

## 1. Requerimientos de Negocio

### 1.1 Antecedentes

La Universidad Nacional Abierta y a Distancia (UNAD) imparte el curso de **Estructuras de Datos** como parte del programa de Ingeniería de Sistemas. En las fases anteriores (Fases 1, 2 y 3), los estudiantes han trabajado con estructuras lineales como pilas, colas y listas enlazadas. La Fase 4 representa la transición hacia **estructuras jerárquicas no lineales**, específicamente los **árboles binarios**, considerados fundamentales en la ciencia de la computación para la organización y búsqueda eficiente de información.

Hasta la fecha, el aprendizaje de estas estructuras se ha realizado de forma teórica-textual, lo que dificulta la comprensión visual del comportamiento dinámico de un árbol binario durante operaciones de inserción, eliminación y recorrido.

### 1.2 Oportunidad de Negocio (Educativa)

Existe una brecha clara entre la comprensión teórica de los árboles binarios y su aplicación práctica en software real. Desarrollar una **aplicación gráfica interactiva** que permita visualizar y operar una estructura de árbol binario en tiempo real representa:

- Una oportunidad de reforzar el aprendizaje activo (learning by doing).
- Una herramienta de demostración reutilizable para futuros estudiantes del curso.
- Un ejercicio de integración de conceptos de POO (Programación Orientada a Objetos) con estructuras de datos jerárquicas.

### 1.3 Objetivos de Negocio y Criterios de Éxito

| # | Objetivo | Criterio de Éxito |
|---|----------|-------------------|
| OB-01 | Aplicar la teoría de árboles binarios en una solución de software funcional | La aplicación permite insertar, eliminar y buscar nodos correctamente |
| OB-02 | Diseñar una interfaz gráfica que represente visualmente el árbol | El árbol se renderiza de forma jerárquica con nodos y conexiones visibles |
| OB-03 | Implementar los tres recorridos estándar (inorden, preorden, postorden) | Los recorridos producen salidas correctas y verificables |
| OB-04 | Aplicar principios de POO en la arquitectura del código | El código posee clases diferenciadas: Nodo, ArbolBinario, Controlador e Interfaz |
| OB-05 | Entregar el producto académico dentro del plazo establecido | El documento final y el código se entregan en las fechas de la agenda del curso |

### 1.4 Necesidades del Cliente (Contexto Educativo)

- **Estudiante (Santiago Villa):** Necesita demostrar comprensión aplicada de los árboles binarios mediante una solución funcional codificada en un lenguaje OOP.
- **Docente/Tutor UNAD:** Necesita evidencia observable y evaluable del logro del RAC 3.
- **Comunidad académica:** Se beneficia de una herramienta de referencia abierta y documentada.

### 1.5 Riesgos de Negocio

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|----|--------|-------------|---------|------------|
| RN-01 | Complejidad en el renderizado gráfico del árbol | Media | Alto | Usar librerías de canvas/gráficos bien documentadas (tkinter) |
| RN-02 | Desbordamiento de pila en árboles no balanceados muy profundos | Baja | Medio | Implementar límite de profundidad y manejo de excepciones |
| RN-03 | No entrega dentro del plazo académico | Media | Alto | Planificación por sprints cortos siguiendo las fechas de la agenda |
| RN-04 | Código sin documentación suficiente para su evaluación | Baja | Alto | Docstrings obligatorios en cada clase y método |

---

## 2. Visión de la Solución

### 2.1 Enunciado de Visión

> **Para** los estudiantes de Estructuras de Datos de la UNAD, **que necesitan** comprender y aplicar los árboles binarios de forma práctica, **el sistema** es una **aplicación de escritorio con interfaz gráfica** que permite insertar, eliminar, buscar y recorrer nodos de un árbol binario de búsqueda (ABB) en tiempo real. **A diferencia de** los ejemplos teóricos en texto plano, **nuestra solución** proporciona una representación visual dinámica e interactiva del árbol, codificada bajo los principios de la Programación Orientada a Objetos.

### 2.2 Características Principales

| ID | Característica | Descripción |
|----|---------------|-------------|
| CP-01 | Inserción de nodos | El usuario puede ingresar un valor numérico entero y el sistema lo inserta en la posición correcta del ABB |
| CP-02 | Eliminación de nodos | El usuario puede eliminar un nodo por su valor, manteniendo la integridad del árbol |
| CP-03 | Búsqueda de nodos | El sistema localiza un nodo dado un valor y lo resalta visualmente |
| CP-04 | Recorridos del árbol | El sistema ejecuta y muestra los recorridos Inorden, Preorden y Postorden |
| CP-05 | Visualización gráfica | El árbol se dibuja jerárquicamente con nodos circulares y aristas conectoras |
| CP-06 | Limpieza/Reinicio | El usuario puede resetear el árbol para comenzar desde cero |
| CP-07 | Información estadística | El sistema muestra altura del árbol, número de nodos y si está balanceado |

### 2.3 Suposiciones y Dependencias

| ID | Tipo | Descripción |
|----|------|-------------|
| SUP-01 | Suposición | El lenguaje de programación principal es **Python 3.10+** |
| SUP-02 | Suposición | La librería gráfica principal es **Tkinter** (incluida en la distribución estándar de Python) |
| SUP-03 | Suposición | El sistema operativo de desarrollo y pruebas es **Linux (Ubuntu/Debian)** |
| SUP-04 | Dependencia | Se requiere Python 3.10 o superior instalado en el sistema |
| SUP-05 | Dependencia | La librería tkinter debe estar disponible (python3-tk) |
| DEP-01 | Dependencia académica | El diseño debe seguir el Anexo 4 — Planteamiento del Problema Fase 4 (UNAD) |

---

## 3. Alcance y Limitaciones

### 3.1 Alcance de la Versión Inicial (v1.0)

La versión 1.0 incluirá obligatoriamente:

- Árbol Binario de Búsqueda (ABB) con valores enteros
- Operaciones CRUD: Insertar, Eliminar, Buscar
- Tres recorridos: Inorden, Preorden, Postorden (salida textual)
- Visualización gráfica del árbol en canvas Tkinter
- Interfaz de usuario con panel de controles y área de dibujo
- Arquitectura OOP: clases `Nodo`, `ArbolBinario`, `Controlador`, `VentanaPrincipal`
- Documentación de código (docstrings en inglés)
- Documento académico con estructura APA: portada, introducción, objetivos, enlace al código, conclusiones y referencias

### 3.2 Alcance de Versiones Subsecuentes (v2.0+)

Funcionalidades propuestas para futuras versiones:

- Soporte para **Árbol AVL** (auto-balanceo con rotaciones visuales)
- Animaciones paso a paso de inserciones y eliminaciones
- Exportación del árbol como imagen (PNG/SVG)
- Soporte para valores de tipo cadena (string)
- Modo de árbol Rojo-Negro
- Persistencia de datos (guardar/cargar árbol desde archivo JSON)

### 3.3 Limitaciones y Exclusiones

| ID | Limitación / Exclusión |
|----|------------------------|
| LIM-01 | No se implementará autenticación de usuarios |
| LIM-02 | No se usará base de datos; la estructura vive únicamente en memoria RAM durante la sesión |
| LIM-03 | No se desarrollará versión web ni móvil; la aplicación es exclusivamente de escritorio |
| LIM-04 | No se implementará balanceo automático en la v1.0 (sin AVL ni Rojo-Negro) |
| LIM-05 | El árbol solo admite valores **enteros** en la versión inicial |
| LIM-06 | No se contempla deshacer operaciones (sin historial/undo) |

---

## 4. Contexto de Negocio

### 4.1 Perfiles de los Interesados en el Sistema

| Interesado | Rol | Interés / Expectativa |
|------------|-----|----------------------|
| **Santiago Villa** | Desarrollador y usuario principal | Aprobar la fase con la implementación correcta del RAC 3 |
| **Tutor UNAD** | Evaluador | Verificar que la aplicación cumpla con los criterios de la rúbrica: POO, árboles binarios, interfaz gráfica |
| **Compañeros del curso** | Usuarios secundarios | Referencia y retroalimentación en el foro colaborativo |
| **UNAD** | Patrocinador académico | Garantizar el logro de los resultados de aprendizaje del curso |

### 4.2 Prioridades del Proyecto

Las restricciones se ordenan de mayor a menor peso:

1. **Tiempo:** El plazo de entrega definido en la agenda del curso es inamovible.
2. **Funcionalidad:** El sistema debe cumplir el 100% del alcance de la v1.0 antes de cualquier mejora estética.
3. **Calidad de código:** El código debe seguir principios OOP y estar documentado (requerido por la rúbrica).
4. **Usabilidad:** La interfaz debe ser clara e intuitiva, pero no requiere diseño UX profesional.
5. **Rendimiento:** No es una prioridad crítica dado el tamaño esperado de los árboles (máx. ~100 nodos en entorno académico).

### 4.3 Ambiente de Operación

| Aspecto | Descripción |
|---------|-------------|
| **Plataforma** | Escritorio Linux (Ubuntu 22.04+) / Windows 10+ / macOS 12+ |
| **Lenguaje** | Python 3.10+ |
| **Interfaz gráfica** | Tkinter (librería estándar de Python) |
| **Entorno de desarrollo** | VS Code / cualquier IDE con soporte Python |
| **Uso esperado** | Sesiones individuales de estudio; un usuario a la vez |
| **Conectividad** | No requiere conexión a internet en tiempo de ejecución |
| **Resolución mínima** | 1024 x 768 píxeles |

---

*Documento generado para el proyecto académico Fase 4 — UNAD, Estructuras de Datos, Quinto Semestre.*
