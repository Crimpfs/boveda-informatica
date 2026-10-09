---
title: "Resumen de Fuente: Patrón LLM Wiki (Andrej Karpathy)"
type: summary
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/resumen
  - domain/gestion-conocimiento
  - domain/segundo-cerebro
aliases:
  - "Manifiesto Karpathy LLM Wiki"
sources:
  - "[[fuentes/2026-08-08-andrej-karpathy-llm-wiki.md]]"
---

# Resumen de Fuente: Patrón LLM Wiki
*Destilado de la fuente original por [[wiki/entidades/andrej-karpathy|Andrej Karpathy]]*

> [!ABSTRACT] Idea Central (Elevator Pitch)
> Un nuevo paradigma para la gestión del conocimiento personal que pasa de la recuperación pasiva y efímera (RAG) a una wiki en Markdown compilada, persistente y mantenida de forma autónoma por un agente LLM dentro de Obsidian.

---

## 📌 Puntos Clave Extraídos

1. **RAG vs. Wiki LLM**: Los sistemas RAG tradicionales redescubren el conocimiento desde cero en cada consulta sin acumular aprendizaje. El [[wiki/conceptos/llm-wiki-pattern|Patrón LLM Wiki]] compila los datos entrantes en un grafo estructurado una sola vez y lo mantiene siempre al día.
2. **La Analogía Desarrollador / IDE**: Obsidian funciona como el IDE; el agente LLM actúa como el programador/compilador; la wiki en Markdown es la base de código acumulativa.
3. **El Sistema de 3 Capas**:
   - **Capa 1 (Fuentes Crudas / `fuentes/`)**: Documentos originales inmutables (fuente de verdad).
   - **Capa 2 (La Wiki / `wiki/`)**: Notas en Markdown redactadas y actualizadas por el LLM (`conceptos`, `entidades`, `resúmenes`, `síntesis`).
   - **Capa 3 (El Esquema / `CLAUDE.md`)**: El manual de reglas que controla el formato, enlaces, indexación y flujos de trabajo.
4. **Automatización del Mantenimiento**: Los humanos suelen abandonar las wikis personales porque el esfuerzo de mantener referencias cruzadas y actualizar notas crece exponencialmente. El LLM elimina por completo esta carga de trabajo.

---

## 🔗 Conexiones en la Wiki

- **Conceptos**: [[wiki/conceptos/llm-wiki-pattern|Patrón LLM Wiki]], [[wiki/conceptos/compounding-knowledge|Conocimiento Acumulativo (Compounding)]]
- **Entidades**: [[wiki/entidades/andrej-karpathy|Andrej Karpathy]]
- **Síntesis**: [[wiki/sintesis/rag-vs-llm-wiki|Comparativa: RAG vs. Arquitectura LLM Wiki]]
