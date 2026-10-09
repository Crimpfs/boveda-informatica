---
title: "Conocimiento Acumulativo (Compounding Knowledge)"
type: concept
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/concepto
  - domain/gestion-conocimiento
  - domain/segundo-cerebro
aliases:
  - "Conocimiento Compuesto"
  - "Efecto Compuesto de la Memoria"
sources:
  - "[[fuentes/2026-08-08-andrej-karpathy-llm-wiki.md]]"
---

# Conocimiento Acumulativo (Compounding)

> [!NOTE] Definición
> El **Conocimiento Acumulativo** es la propiedad de un sistema de información donde el procesamiento de cada nuevo documento incrementa el valor y coherencia de todas las notas existentes mediante enlaces proactivos, síntesis continua y resolución de discrepancias.

---

## 📈 La Curva Acumulativa vs. La Carga de Mantenimiento

```
Valor / Tiempo
    ^
    |                   / [Wiki Acumulativa Gestionada por LLM]
    |                  /
    |                 /
    |     _ _ _ _ _ _/ _ _ _ [Umbral de Abandono Humano Tradicional]
    |    /          /
    |   /          /
    |  /__________/__________> Complejidad / Número de Fuentes
```

En las bases de conocimiento personales tradicionales (Zettelkasten, Notion, wikis manuales):
- A medida que crece el número de notas, el esfuerzo humano requerido para vincular, actualizar y conciliar notas crece exponencialmente ($O(n^2)$ conexiones).
- Los humanos inevitablemente alcanzan un **muro de mantenimiento** y terminan abandonando el sistema.

En un **Segundo Cerebro gestionado por LLM**:
- El costo marginal de mantenimiento por cada documento nuevo desciende casi a cero.
- El LLM puede revisar y editar 10 a 20 archivos vinculados en una sola pasada, asegurando que la red de notas permanezca siempre viva y actualizada.

---

## 🔗 Páginas Relacionadas

- **Marco Principal**: [[wiki/conceptos/llm-wiki-pattern|Patrón LLM Wiki]]
- **Síntesis**: [[wiki/sintesis/rag-vs-llm-wiki|Comparativa: RAG vs. Arquitectura LLM Wiki]]
- **Fuentes**: [[wiki/resumenes/source-karpathy-llm-wiki|Resumen de Fuente: Karpathy LLM Wiki]]
