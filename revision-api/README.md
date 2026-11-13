# Security Audit Skill

Skill de auditoría de seguridad y análisis estático de código basado en [`cloudflare/security-audit-skill`](https://github.com/cloudflare/security-audit-skill).

Orquesta agentes para realizar revisiones de seguridad sistemáticas y estructuradas a través de 6 fases defensivas:
1. **Reconnaissance (Reconocimiento)**: Mapeo de arquitectura, límites de confianza, superficies de entrada y creación del registro de cobertura (`architecture.md` y `coverage-ledger.json`).
2. **Coverage-led hunting (Búsqueda guiada)**: Asignación de inspectores aislados según las unidades del registro, utilizando guías especializadas de clases de ataque.
3. **Candidate validation (Validación de candidatos)**: Validación independiente para intentar desmentir o confirmar cada vulnerabilidad candidata.
4. **Structured output (Salida estructurada)**: Registro determinista de hallazgos en formato JSON (`findings.json`) validado mediante esquema.
5. **Independent record verification (Verificación independiente)**: Revisión cruzada de hallazgos contra el código fuente para eliminar falsos positivos.
6. **Target-neutral reporting (Reporte de resultados)**: Generación de reportes estandarizados (`REPORT.md`, `FINDINGS-DETAIL.md`, `NEEDS-VALIDATION.md`).

---

## Estructura de Archivos

- **`SKILL.md`**: Punto de entrada con la definición del skill, modos de operación (`guidance` vs `full audit`) y reglas de aislamiento de escritura.
- **Guías de clases de ataque (`*.md`)**:
  - `ATTACK-CLASSES.md`: Índice de vectores y clases principales.
  - `WEB-PROTOCOL-AND-AUTH.md`: Autenticación, sesiones y protocolos web.
  - `DATA-ISOLATION-AND-LIFECYCLE.md`: Aislamiento de datos, multi-tenancy e IDOR.
  - `AI-AND-LLM.md`: Seguridad de modelos de lenguaje y aplicaciones con IA.
  - `CLIENT-SIDE.md`: Vulnerabilidades de navegador y cliente.
  - `CLOUD-AND-DEPLOYMENT.md`: Configuración en la nube, contenedores y serverless.
  - `RESOURCE-EXHAUSTION-AND-AVAILABILITY.md`: Agotamiento de recursos y DoS.
  - `SUPPLY-CHAIN-AND-RELEASE.md`: Dependencias y cadena de suministro.
  - `MEMORY-SAFETY-AND-BINARY.md`: Seguridad de memoria y binarios.
  - `PROTOCOLS-RPC-AND-MESSAGING.md`: gRPC, GraphQL, brokers de mensajería y colas.
  - `DESKTOP-MOBILE-AND-LOCAL-IPC.md`: IPC local y entornos de escritorio/móvil.
- **Validadores Node.js (`*.cjs`)**:
  - `validate-findings.cjs` / `validate-findings.test.cjs`: Valida `findings.json` contra `report-schema.json`.
  - `validate-coverage-ledger.cjs` / `validate-coverage-ledger.test.cjs`: Valida la integridad del registro de cobertura.

---

## Requisitos

- **Node.js** (v18 o superior) para ejecutar los scripts de validación (`node validate-findings.test.cjs`).
- Entorno de ejecución seguro (sandbox) para pruebas locales aisladas.
