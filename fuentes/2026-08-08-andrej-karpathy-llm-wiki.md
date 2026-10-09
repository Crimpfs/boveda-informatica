# LLM Wiki: Un patrón para construir bases de conocimiento personales usando LLMs
**Autor**: Andrej Karpathy  
**Fecha**: 2026-08-08  
**Tipo de Fuente**: Manifiesto de Arquitectura / Archivo de Ideas  
**Estado**: Fuente Cruda Inmutable  

---

## La Idea Central

La mayoría de las experiencias con LLMs y documentos se basan en RAG (Generación Aumentada por Recuperación): subes una colección de archivos, el LLM recupera fragmentos relevantes en el momento de la consulta y genera una respuesta. Esto funciona, pero el LLM está redescubriendo el conocimiento desde cero en cada pregunta. No hay acumulación. Si haces una pregunta sutil que requiere sintetizar cinco documentos, el LLM tiene que encontrar y unir los fragmentos relevantes cada vez. Nada se construye ni persiste. NotebookLM, las subidas de archivos en ChatGPT y la mayoría de los sistemas RAG operan así.

La idea aquí es diferente. En lugar de solo recuperar documentos crudos en el momento de la consulta, el LLM construye y mantiene de forma incremental una **wiki persistente**: una colección estructurada e interconectada de archivos Markdown que se sitúa entre tú y las fuentes originales. Cuando añades una nueva fuente, el LLM no solo la indexa para después; la lee, extrae la información clave y la integra en la wiki existente: actualiza páginas de entidades, revisa resúmenes de temas, señala dónde los datos nuevos contradicen afirmaciones antiguas y fortalece o cuestiona la síntesis en evolución. El conocimiento se compila una sola vez y se mantiene actualizado, en lugar de re-derivarse en cada consulta.

Esta es la diferencia fundamental: **la wiki es un artefacto persistente y acumulativo (compounding)**. Las referencias cruzadas ya están listas. Las contradicciones ya han sido señaladas. La síntesis ya refleja todo lo que has leído. La wiki se vuelve más rica con cada fuente que agregas y cada pregunta que haces.

Tú nunca (o casi nunca) escribes en la wiki: el LLM la redacta y mantiene por completo. Tú te encargas de seleccionar fuentes, explorar y hacer las preguntas correctas. El LLM hace todo el trabajo pesado: resumir, cruzar referencias, categorizar y organizar. En la práctica, tienes el agente LLM a un lado y Obsidian abierto al otro. El LLM realiza ediciones basadas en tu conversación y tú navegas los resultados en tiempo real: siguiendo enlaces, revisando la vista de grafo y leyendo las páginas actualizadas. **Obsidian es el IDE; el LLM es el programador; la wiki es la base de código.**

## Arquitectura

Consta de tres capas:
1. **Fuentes crudas (`fuentes/`)**: tu colección seleccionada de documentos de origen (artículos, papers, imágenes, datos). Son inmutables: el LLM solo lee de ellas, nunca las modifica. Es tu fuente de verdad.
2. **La wiki (`wiki/`)**: un directorio de archivos Markdown generados por el LLM (resúmenes, entidades, conceptos, comparativas, síntesis). El LLM es dueño absoluto de esta capa. Tú la lees; el LLM la escribe.
3. **El esquema (`CLAUDE.md` / `AGENTS.md`)**: el documento que le enseña al LLM cómo está estructurada la wiki, qué convenciones seguir y qué flujos aplicar al procesar fuentes o responder preguntas.

## Operaciones

- **Ingestión (Ingest)**: Colocas una fuente en `fuentes/` y el LLM la procesa: la lee, crea un resumen, actualiza el índice, actualiza 10-15 páginas de conceptos/entidades vinculadas y añade una entrada al registro (`log.md`).
- **Consulta (Query)**: Haces preguntas sobre la wiki. El LLM busca páginas relevantes, sintetiza respuestas con citas y las respuestas valiosas se pueden guardar nuevamente en la wiki como nuevas páginas.
- **Auditoría (Lint)**: El LLM revisa periódicamente la salud de la wiki: detecta páginas huérfanas, contradicciones, menciones sin enlazar y sugiere qué temas investigar.
