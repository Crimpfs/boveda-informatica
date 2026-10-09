---
title: "Comparativa: RAG vs. Arquitectura LLM Wiki"
type: synthesis
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/sintesis
  - domain/arquitectura-ia
  - domain/segundo-cerebro
aliases:
  - "Síntesis Comparativa RAG"
sources:
  - "[[fuentes/2026-08-08-andrej-karpathy-llm-wiki.md]]"
---

# Síntesis Comparativa: RAG Tradicional vs. Wiki LLM Compilada

---

## 🎯 Resumen Ejecutivo

La transición desde la **Generación Aumentada por Recuperación (RAG)** hacia una **Wiki Mantenida por LLM** refleja el paso de un modelo interpretado sobre la marcha a una indexación compilada persistente. Mientras que los sistemas RAG sobresalen en búsquedas puntuales sobre documentos desestructurados, carecen de memoria acumulativa y evolución semántica. El patrón LLM Wiki resuelve este cuello de botella utilizando el grafo de Markdown en Obsidian como representación intermedia persistente.

---

## 📊 Matriz Comparativa Completa

| Atributo | RAG Tradicional (NotebookLM, Vector DBs) | Wiki LLM Compilada (Obsidian + Agente LLM) |
| :--- | :--- | :--- |
| **Procesamiento de Datos** | Fragmentación (chunking) y embeddings al consultar | Extracción semántica y enlaces bidireccionales en el grafo |
| **Costo de Síntesis** | Se paga en cada pregunta individual ($O(Consultas)$) | Se paga una vez al ingerir y se mantiene continuamente |
| **Seguimiento de Contradicciones** | Sin resolver; fragmentos opuestos chocan en el prompt | Resueltas o señaladas explícitamente mediante Alertas |
| **Interfaz Humana** | Ventana de chat temporal / resultados efímeros | Vista de Grafo de Obsidian, Canvas, archivos Markdown locales |
| **Sinergia con Herramientas** | Silos cerrados en la nube | Control de versiones con Git, plugins (Dataview, Marp), almacenamiento local |

---

## 🔗 Páginas Relacionadas

- **Marco Principal**: [[wiki/conceptos/llm-wiki-pattern|Patrón LLM Wiki]]
- **Mecanismo**: [[wiki/conceptos/compounding-knowledge|Conocimiento Acumulativo]]
- **Autor/Creador**: [[wiki/entidades/andrej-karpathy|Andrej Karpathy]]
- **Fuente Principal**: [[wiki/resumenes/source-karpathy-llm-wiki|Resumen de Fuente: Karpathy LLM Wiki]]
