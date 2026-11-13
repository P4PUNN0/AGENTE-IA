# 🛡️ AGENTE IA - Auditor de Seguridad para APIs

> Agente de inteligencia artificial para auditoría de seguridad de código estático y dinámico en aplicaciones Python.

## 📋 Descripción

**Joaquin - Rakesh Cibersecurity** es un agente de IA especializado en encontrar vulnerabilidades de código estático en aplicaciones Python. Fue diseñado como herramienta de apoyo para la materia de **Ciberseguridad en Tecmilenio**, proporcionando a los estudiantes una forma automatizada de generar reportes de auditoría profesionales.

## 🏗️ Estructura del Proyecto

```
AGENTE-IA/
├── README.md                          # Este archivo
├── AGENTS.md                          # Configuración y perfil del agente
├── generar_reporte_auditoria.py       # Script para generar reportes PDF
├── REPORTE_AUDITORIA_API_MVC.pdf      # Reporte de auditoría generado
└── revision-api/                      # Skill de auditoría de seguridad
    ├── SKILL.md                       # Instrucciones principales del skill
    ├── README.md                      # Documentación del skill
    ├── RECONNAISSANCE.md              # Fase 1: Reconocimiento
    ├── HUNTING.md                     # Fase 2: Caza de vulnerabilidades
    ├── ATTACK-CLASSES.md              # Clases de ataque soportadas
    ├── VALIDATION-AND-REPORTING.md    # Fase 3-6: Validación y reportes
    ├── WEB-PROTOCOL-AND-AUTH.md       # Auditoría de protocolos web y auth
    ├── AI-AND-LLM.md                 # Seguridad en IA y LLMs
    ├── CLIENT-SIDE.md                # Seguridad del lado del cliente
    ├── CLOUD-AND-DEPLOYMENT.md       # Seguridad en la nube
    ├── DATA-ISOLATION-AND-LIFECYCLE.md # Aislamiento de datos
    ├── DESKTOP-MOBILE-AND-LOCAL-IPC.md # Seguridad en desktop/mobile
    ├── MEMORY-SAFETY-AND-BINARY.md   # Seguridad de memoria
    ├── PROTOCOLS-RPC-AND-MESSAGING.md # Protocolos y mensajería
    ├── RESOURCE-EXHAUSTION-AND-AVAILABILITY.md # DoS y disponibilidad
    ├── SUPPLY-CHAIN-AND-RELEASE.md   # Cadena de suministro
    ├── report-schema.json            # Esquema JSON del reporte
    ├── validate-findings.cjs         # Validador de hallazgos
    ├── validate-findings.test.cjs    # Tests del validador
    ├── validate-coverage-ledger.cjs  # Validador de cobertura
    └── validate-coverage-ledger.test.cjs # Tests del validador de cobertura
```

## 🚀 ¿Cómo funciona?

### El Agente realiza una auditoría en 6 fases:

1. **🔍 Reconocimiento** — Mapea el código fuente, trust boundaries y rutas de build
2. **🎯 Caza de vulnerabilidades** — Búsqueda dirigida por cobertura usando clases de ataque
3. **✅ Validación de candidatos** — Consolida y verifica cada hallazgo con evidencia
4. **📊 Salida estructurada** — Genera `findings.json` validado contra el esquema
5. **🔎 Verificación independiente** — Agentes frescos verifican los hallazgos
6. **📄 Reporte final** — Genera el reporte PDF con hallazgos, evidencia y recomendaciones

### Tipos de análisis:
- **Análisis estático**: Revisión línea por línea del código fuente
- **Análisis dinámico**: Pruebas contra la API en ejecución (autenticación, inyección, headers, CORS, etc.)

## 📄 Último Reporte Generado

Se auditó una **API REST MVC** construida con `http.server` de Python. Resultados:

| Severidad | Cantidad | Hallazgos |
|-----------|----------|-----------|
| MEDIA     | 3        | Token hardcodeado, sin headers de seguridad, versión expuesta |
| BAJA      | 2        | Sin rate limiting, sin política CORS |
| INFO      | 2        | Logging deshabilitado, sin límite de body |

> ✅ No se encontraron vulnerabilidades **CRÍTICAS** ni **ALTAS**

## 🛠️ Generación de Reportes PDF

```bash
# Requisitos
pip install fpdf2

# Generar reporte
python generar_reporte_auditoria.py
```

El script genera un PDF profesional con:
- Portada con datos del proyecto
- Resumen ejecutivo con tabla de hallazgos
- Alcance y metodología de la auditoría
- Hallazgos detallados con evidencia y recomendaciones
- Resultados de pruebas dinámicas con tablas
- Matriz de riesgos
- Conclusiones y asuntos pendientes

## 👤 Perfil del Agente

- **Nombre**: Joaquin - Rakesh Cibersecurity
- **Objetivo**: Encontrar vulnerabilidades de código estático
- **Contexto**: Materia de Ciberseguridad - Tecmilenio
- **Herramientas**: Listar archivos, buscar texto, leer archivos
- **Permisos**: Lectura del código; escritura solo en la salida de auditoría

## 📚 Materia

**Ciberseguridad** — Tecmilenio

---

*Reporte generado automáticamente por el Agente de Auditoría de Seguridad IA*
