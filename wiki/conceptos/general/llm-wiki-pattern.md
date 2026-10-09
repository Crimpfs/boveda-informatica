---
title: "Patrón LLM Wiki"
type: concept
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/concepto
  - domain/sistemas-ia
  - domain/grafos-conocimiento
aliases:
  - "Patrón Wiki Compilada"
  - "Wiki Agéntica"
sources:
  - "[[fuentes/2026-08-08-andrej-karpathy-llm-wiki.md]]"
---

# Patrón LLM Wiki

> [!NOTE] Definición
> El **Patrón LLM Wiki** es una arquitectura para la gestión del conocimiento donde un agente de IA actúa como curador y compilador persistente, traduciendo de forma incremental fuentes crudas e inmutables a un grafo interconectado de documentos Markdown.

---

## 🏗️ Modelo Arquitectónico

El patrón organiza la información en tres niveles complementarios:

```
[ Fuentes Crudas (Inmutables) ] 
            ↓ (Ingestión y Compilación por el LLM)
    [ La Wiki (Grafo de Markdown) ]  ⟵  Gobernado por [ Esquema (CLAUDE.md) ]
            ↓ (Consulta y Síntesis por el LLM)
    [ Conocimiento Acumulado y Respuestas ]
```

### Diferencias Clave

| Dimensión | RAG Estándar | Patrón LLM Wiki |
| :--- | :--- | :--- |
| **Estado del Conocimiento** | Efímero, recalculado en cada consulta | Grafo Markdown persistente e interconectado |
| **Referencias Cruzadas** | Realizadas sobre fragmentos de vectores crudos | Precompiladas en enlaces bidireccionales (`[[wikilinks]]`) |
| **Resolución de Contradicciones** | Queda a merced del contexto del prompt | Explícitamente señalada y registrada en las notas |
| **Rol del Humano** | Curador y generador de prompts | Curador, explorador y formulador de preguntas |
| **Rol del Agente** | Herramienta momentánea de búsqueda y resumen | Mantenimiento continuo del segundo cerebro |

---

## 🔄 Operaciones Centrales

1. **Ingestión**: Procesar una fuente actualiza múltiples nodos de conceptos y entidades simultáneamente.
2. **Consulta**: Las respuestas se sintetizan a partir de la wiki pre-enlazada; las conclusiones valiosas se guardan como páginas de síntesis.
3. **Auditoría (Lint)**: Revisiones periódicas detectan notas huérfanas, enlaces rotos, menciones sin vincular y vacíos de información.

---

## 🔗 Páginas Relacionadas

- **Entidades**: [[wiki/entidades/andrej-karpathy|Andrej Karpathy]]
- **Conceptos**: [[wiki/conceptos/compounding-knowledge|Conocimiento Acumulativo]]
- **Síntesis**: [[wiki/sintesis/rag-vs-llm-wiki|Comparativa: RAG vs. Arquitectura LLM Wiki]]
- **Fuentes**: [[wiki/resumenes/source-karpathy-llm-wiki|Resumen de Fuente: Karpathy LLM Wiki]]
