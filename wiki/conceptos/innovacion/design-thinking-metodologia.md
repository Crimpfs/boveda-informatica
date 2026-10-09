---
title: "Metodología Design Thinking: Innovación Centrada en las Personas"
type: concept
created: 2026-10-09
updated: 2026-10-09
tags:
  - wiki/concepto
  - domain/innovacion-emprendimiento
  - curso/innovacion-y-emprendimiento
aliases:
  - "Design Thinking"
  - "Doble Diamante"
  - "Human-Centered Design"
---

# 🎨 Metodología Design Thinking: Innovación Centrada en las Personas

El **Design Thinking** (popularizado por IDEO y la d.school de Stanford University) es una metodología de resolución de problemas complejos enfocada en entender profundamente las necesidades de los usuarios para crear soluciones tecnológicas deseables, factibles y viables.

```mermaid
flowchart LR
    E["1. 👁️ Empatizar<br/>(Comprender al usuario)"] --> D["2. 🎯 Definir<br/>(Enfocar el problema clave - POV)"]
    D --> I["3. 💡 Idear<br/>(Generar lluvia de soluciones)"]
    I --> P["4. 🛠️ Prototipar<br/>(Materializar la idea en baja fidelidad)"]
    P --> T["5. 🧪 Testear<br/>(Validar con usuarios reales)"]
    
    T -.->|Retroalimentación| E
    T -.->|Ajustar solución| I
    P -.->|Detectar dudas| D
```

---

## 1. El Modelo del Doble Diamante (Divergencia y Convergencia)

El proceso de diseño no es lineal, sino una alternancia constante entre **abrir la mente a múltiples opciones** (Divergir) y **seleccionar la mejor opción** (Converger):

```mermaid
flowchart LR
    subgraph Diamante1 ["DIAMANTE 1: EL ESPACIO DEL PROBLEMA"]
        direction LR
        D1A["DIVERGENCIA<br/>Empatizar<br/>(Entrevistar, observar muchas realidades)"] --> D1B["CONVERGENCIA<br/>Definir<br/>(Sintetizar hallazgos, crear el POV único)"]
    end
    subgraph Diamante2 ["DIAMANTE 2: EL ESPACIO DE LA SOLUCIÓN"]
        direction LR
        D2A["DIVERGENCIA<br/>Idear<br/>(Generar decenas de posibles soluciones)"] --> D2B["CONVERGENCIA<br/>Prototipar & Testear<br/>(Construir el MVP y validar con métricas)"]
    end
    Diamante1 --> Diamante2
```

1. **Diamante del Problema:** ¿Estamos resolviendo el problema correcto? (Construir la cosa correcta).
2. **Diamante de la Solución:** ¿Estamos diseñando la solución correcta? (Construir la cosa correctamente).

---

## 2. Las 5 Fases del Proceso Explicadas

| Fase | Objetivo Principal | Herramientas Clave | Salida / Artefacto |
| :---: | :--- | :--- | :--- |
| **1. Empatizar** | Ponerse en los zapatos del usuario y entender sus frustraciones sin juzgar. | Entrevistas en profundidad, Observación directa (Shadowing). | Transcripciones, citas textuales, historias de vida. |
| **2. Definir** | Transformar el caos de datos recopilados en un foco de diseño accionable. | Mapa de Empatía, Arquetipo/Buyer Persona, Matriz de Hallazgos. | **Point of View (POV)** y Pregunta disparadora **HMW**. |
| **3. Idear** | Generar la mayor cantidad de ideas posibles sin censura previa. | Brainstorming, SCAMPER, Crazy Eights, Co-diseño. | Lista priorizada de funcionalidades y conceptos de solución. |
| **4. Prototipar** | Hacer tangibles las ideas para que el usuario pueda interactuar con ellas. | Wireframes en papel, maquetas en Figma, mockups interactivos sin backend. | Prototipo de baja / media fidelidad (Clickable Prototype). |
| **5. Testear** | Poner el prototipo frente a usuarios reales y escuchar sus reacciones. | Malla receptora de información, pruebas de usabilidad, métricas de éxito. | Decisiones de iteración: Mejorar, Perseverar o Pivotar. |

---

## 3. ¿Por qué es Vital para Ingenieros Informáticos?

Los programadores suelen cometer el error de empezar abriendo el editor de código (**VS Code**) antes de entender qué necesita el cliente:

```mermaid
graph TD
    A["❌ Enfoque Tradicional Fallido: Construir a ciegas"] --> B["3 meses programando backend y frontend"]
    B --> C["Lanzamiento al mercado"]
    C --> D["Nadie lo descarga: Fracaso total de la Startup"]

    E["✅ Enfoque Design Thinking: Validar antes de codificar"] --> F["1 semana empatizando y definiendo"]
    F --> G["Prototipo de Figma probado en 2 días"]
    G --> H["Solo se programa el software cuando la solución está validada"]
```

---

> [!NOTE] Unidad II del Curso UNT
> En la Universidad Nacional de Trujillo, las semanas 6 a 10 están dedicadas a recorrer rigurosamente este ciclo sobre un proyecto real enfocado en el ecosistema regional (empresas locales, salud o educación).

---
**Fuentes y Referencias:**
* 📄 UNT: *1. TALLER 2 - DESIGN THINKING Y LEAN CANVAS (1).pdf*.
* 📄 UNT: *3. GUÍA DESIGN THINKING V 1.2 JMV_compressed.pdf*.
* 📚 Brown, Tim — *Change by Design: How Design Thinking Transforms Organizations* (IDEO).
* 🔗 Relacionado con: [[fase-empatizar-y-mapa-de-empatia|Fase 1: Empatizar]] | [[fase-definir-pov-y-hmw|Fase 2: Definir]] | [[scrum-para-startups|Scrum para Startups]]
