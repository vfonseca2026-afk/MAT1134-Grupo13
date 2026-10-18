# MAT1134 - Cálculo Intermedio (Grupo 13)
## Proyecto Manim: El infinito en la definición de integral

Repositorio oficial del proyecto grupal para la asignatura **MAT1134** de la Universidad Católica de Temuco.

### Integrantes del Grupo 13
* Carlos Meléndez
* Danna Ramirez
* Vicente Fonseca

---

### Descripción del Proyecto
Este proyecto audiovisual, desarrollado utilizando **Manim Community**, aborda el análisis conceptual y gráfico de las sumas de Riemann para responder a la pregunta central:
> *¿Qué significa realmente hacer que $n \to \infty$ en una suma de Riemann, y por qué el infinito es una tendencia y no un número que se pueda sustituir directamente?*

### Tecnologías y Entorno
* **Lenguaje:** Python
* **Motor de Animación:** Manim Community
* **Gestión de Dependencias:** `uv`
* **Compilación LaTeX:** MiKTeX

### Instrucciones de Ejecución
Para clonar el repositorio y renderizar el video localmente:

1. Clona el repositorio y entra al directorio.
2. Instala las dependencias y ejecuta el script en baja calidad para vista previa (`-pql`) o alta calidad (`-pqh`):
   ```powershell
   uv run manim -pql eid_grupo13.py VideoExplicativoGrupo13