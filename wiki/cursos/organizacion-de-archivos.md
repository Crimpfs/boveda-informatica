---
title: "Organización de Archivos (UNT - Ciclo IV)"
type: curso
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/curso
  - ciclo/iv
  - domain/bases-datos-archivos
aliases:
  - "Estructuras de Almacenamiento"
  - "ODA"
docentes:
  - "Dr. Celestino Medardo Quispe Varón (cmquispe@unitru.edu.pe)"
  - "Ms. Martín Gustavo Salcedo Quiñones (msalcedo@unitru.edu.pe)"
creditos: 3
codigo: 13636
prerequisito: "Estructura de Datos"
---

# 🗄️ Organización de Archivos

> **Facultad de Ciencias Físicas y Matemáticas — Departamento de Informática (UNT)**  
> **Ciclo:** IV | **Créditos:** 3 | **Código:** 13636 | **Régimen:** Obligatorio  
> **Tutoría:** Martes 08:00 - 09:00 (Cubil) / Viernes 14:00 - 16:00 (Sala Profesores)

---

## 📊 Sistema de Evaluación y Fórmulas de Calificación

- **Nota mínima aprobatoria:** 14 (El medio punto 0.5 favorece al estudiante).
- **Fórmulas por Unidad:**
  - $PU_1 = (PL \cdot 0.50) + (DA \cdot 0.20) + (EU \cdot 0.30)$
  - $PU_2 = (PL \cdot 0.50) + (DA \cdot 0.20) + (EU \cdot 0.30)$
  - $PU_3 = (PL \cdot 0.50) + (TF \cdot 0.30) + (EU \cdot 0.20)$
- **Promedio Promocional ($PP$):**
  $$PP = \frac{PU_1 + PU_2 + PU_3}{3}$$

*(Donde: $PL$ = Prácticas de Laboratorio 50%, $DA$ = Desarrollo de Actividades / Tareas, $TF$ = Trabajo Final de Aplicación, $EU$ = Examen de Unidad).*

---

## 🗺️ Hoja de Ruta Semana a Semana

### 🟡 Unidad I: Fundamentos de Dispositivos de Almacenamiento
- [ ] **Semana 1:** Almacenamiento primario vs secundario. Tipos de organización de archivos.
- [ ] **Semana 2:** Tiempos de transmisión y rendimiento de discos (Tiempo de acceso, tiempo de búsqueda/seek, latencia rotacional, tasa de transferencia).
- [ ] **Semana 3:** Tipos de archivos, registros y campos. Organización con Registros de Longitud Fija (RLF).
- [ ] **Semana 4:** Organización con Registros de Longitud Variable (RLV). Uso de delimitadores, indicadores de longitud y cabeceras.
- [ ] **Semana 5:** 📝 **Examen de Unidad I**.

### 🔵 Unidad II: Organización Básica de Archivos
- [ ] **Semana 6:** Organización de archivos mediante Listas Enlazadas en disco.
- [ ] **Semana 7:** Mantenimiento de archivos en disco. Técnicas de compactación.
- [ ] **Semana 8:** Eliminación lógica (flags de borrado) vs Eliminación física (reubicación y recolección de basura).
- [ ] **Semana 9:** Organización **Secuencial Indexada (ISAM)**. Índices densos y no densos.
- [ ] **Semana 10:** 📝 **Examen de Unidad II**.

### 🟢 Unidad III: Organización Híbrida, Hashing y Árboles en Disco
- [ ] **Semana 11:** Dispersión (Hashing). Funciones hash y resolución de colisiones (Open addressing, encadenamiento).
- [ ] **Semana 12:** Estructuras de Árboles Binarios en memoria secundaria.
- [ ] **Semana 13:** Operaciones de inserción y eliminación en Árboles en disco.
- [ ] **Semana 14:** **Árboles Balanceados AVL y Árboles B / B+** para indexación en bases de datos y sistemas de archivos. Técnicas de compresión.
- [ ] **Semana 15:** 📝 **Examen de Unidad III** y Sustentación del Trabajo Final.
- [ ] **Semana 16:** Examen Sustitutorio y Aplazados.

---

## 📚 Bibliografía Oficial
- **Pal, D. (2018)**: *Data Structure and Algorithm with C* (Alpha Science).
- **Singh, J. (2018)**: *Data Structure Simplified: Implementation using C++*.
- **Malhotra, D. & Malhotra, N. (2019)**: *Data Structures and Program Design using C++*.
- **Folk, Zoellick & Riccardi**: *File Structures: An Object-Oriented Approach with C++*.
