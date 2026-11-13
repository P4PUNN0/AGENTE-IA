#!/usr/bin/env python3
"""Reporte de Auditoria de Seguridad - API MVC"""
import sys
sys.path.insert(0, "/home/rodrigo/Escritorio/CIBERSEGURIDAD/API/api_mvc/.venv/lib/python3.14/site-packages")

from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(100, 100, 100)
        self.cell(95, 8, "Reporte de Auditoria de Seguridad - API MVC", align="L")
        self.cell(95, 8, "Fecha: " + datetime.now().strftime('%d/%m/%Y'), align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(41, 128, 185)
        self.set_line_width(0.4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, "Pagina " + str(self.page_no()) + "/{nb}", align="C")

    def seccion(self, texto):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(41, 128, 185)
        self.ln(4)
        self.cell(0, 9, texto, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(41, 128, 185)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def sub(self, texto):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(44, 62, 80)
        self.ln(2)
        self.cell(0, 7, texto, new_x="LMARGIN", new_y="NEXT")

    def txt(self, texto):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 5.5, texto)
        self.ln(1)

    def bullet(self, texto):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(50, 50, 50)
        self.set_x(10)
        self.multi_cell(190, 5.5, "  > " + texto)

    def hallazgo(self, id_h, titulo, sev, desc, evidencia, rec):
        colors = {"MEDIA": (243,156,18), "BAJA": (46,204,113), "INFO": (52,152,219)}
        c = colors.get(sev, (100,100,100))
        self.ln(3)
        self.set_fill_color(*c)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 10)
        self.cell(22, 7, " " + sev, fill=True)
        self.set_text_color(44, 62, 80)
        self.cell(0, 7, "  " + id_h + " - " + titulo, new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(80, 80, 80)
        self.cell(0, 6, "Descripcion:", new_x="LMARGIN", new_y="NEXT")
        self.txt(desc)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(80, 80, 80)
        self.cell(0, 6, "Evidencia:", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Courier", "", 8)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 4.5, evidencia)
        self.ln(1)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(80, 80, 80)
        self.cell(0, 6, "Recomendacion:", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 10)
        self.set_text_color(39, 174, 96)
        self.multi_cell(0, 5.5, rec)
        self.ln(2)
        self.set_draw_color(200, 200, 200)
        self.line(15, self.get_y(), 195, self.get_y())


pdf = PDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)

# === PORTADA ===
pdf.add_page()
pdf.ln(35)
pdf.set_font("Helvetica", "B", 28)
pdf.set_text_color(41, 128, 185)
pdf.cell(0, 15, "REPORTE DE AUDITORIA", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 15, "DE SEGURIDAD", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)
pdf.set_font("Helvetica", "", 15)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 10, "API MVC - Analisis de Codigo Estatico y Dinamico", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(15)
pdf.set_draw_color(41, 128, 185)
pdf.set_line_width(1)
pdf.line(60, pdf.get_y(), 150, pdf.get_y())
pdf.ln(15)
pdf.set_font("Helvetica", "", 12)
pdf.set_text_color(80, 80, 80)
info = [
    "Materia: Ciberseguridad - Tecmilenio",
    "Agente Auditor: Joaquin - Rakesh Cibersecurity",
    "Fecha: " + datetime.now().strftime('%d de noviembre de %Y, %H:%M hrs'),
    "Clasificacion: USO ACADEMICO",
]
for line in info:
    pdf.cell(0, 8, line, align="C", new_x="LMARGIN", new_y="NEXT")

# === RESUMEN EJECUTIVO ===
pdf.add_page()
pdf.seccion("1. RESUMEN EJECUTIVO")
pdf.txt(
    "Se realizo una auditoria de seguridad sobre la API MVC ubicada en "
    "/home/rodrigo/Escritorio/CIBERSEGURIDAD/API/api_mvc/. "
    "La API esta construida con el modulo estandar http.server de Python 3.14, "
    "implementa el patron MVC (Modelo-Vista-Controlador) y expone tres endpoints REST: "
    "/api/salud, /api/productos y /api/privado (este ultimo protegido por Bearer token)."
)
pdf.txt(
    "La auditoria combino analisis de codigo estatico (revision manual de cada archivo fuente) "
    "con pruebas dinamicas contra la API en ejecucion (http://127.0.0.1:5000). "
    "Se identificaron 7 hallazgos clasificados por severidad."
)

pdf.sub("Resumen de hallazgos")
pdf.set_fill_color(41, 128, 185)
pdf.set_text_color(255, 255, 255)
pdf.set_font("Helvetica", "B", 10)
pdf.cell(40, 8, "Severidad", border=1, fill=True, align="C")
pdf.cell(30, 8, "Cantidad", border=1, fill=True, align="C")
pdf.cell(120, 8, "Estado", border=1, fill=True, align="C", new_x="LMARGIN", new_y="NEXT")
filas = [("MEDIA","3","Confirmados"),("BAJA","2","Confirmados"),("INFO","2","Observaciones")]
pdf.set_text_color(50, 50, 50)
pdf.set_font("Helvetica", "", 10)
for s,c,e in filas:
    pdf.cell(40,7,s,border=1,align="C")
    pdf.cell(30,7,c,border=1,align="C")
    pdf.cell(120,7,e,border=1,align="C",new_x="LMARGIN",new_y="NEXT")
pdf.ln(3)
pdf.txt(
    "No se encontraron vulnerabilidades de severidad CRITICA ni ALTA. "
    "La API, al ser un ejercicio academico con datos ficticios y token fijo, "
    "presenta un nivel de riesgo aceptable para su proposito educativo."
)

# === ALCANCE ===
pdf.seccion("2. ALCANCE DE LA AUDITORIA")
pdf.sub("2.1 Objetivo auditado")
pdf.txt("API REST MVC construida con http.server de Python (sin framework externo).")
pdf.bullet("Ruta: /home/rodrigo/Escritorio/CIBERSEGURIDAD/API/api_mvc/")
pdf.bullet("Servidor: ThreadingHTTPServer en 127.0.0.1:5000")
pdf.bullet("Lenguaje: Python 3.14.10")
pdf.bullet("Entorno virtual: .venv/ (activado para ejecucion)")

pdf.sub("2.2 Archivos analizados")
pdf.bullet("app.py - Punto de entrada, servidor HTTP")
pdf.bullet("controllers/api_controller.py - Enrutamiento y logica de dispatch")
pdf.bullet("models/producto.py - Modelo de datos (productos ficticios)")
pdf.bullet("views/json_view.py - Serializacion JSON")
pdf.bullet("security/token_auth.py - Autenticacion por Bearer token")

pdf.sub("2.3 Endpoints probados")
pdf.bullet("GET /api/salud - Health check (publico)")
pdf.bullet("GET /api/productos - Lista de productos (publico)")
pdf.bullet("GET /api/privado - Recurso protegido (requiere Bearer token)")

pdf.sub("2.4 Metodologia")
pdf.bullet("Analisis estatico: revision linea por linea del codigo fuente")
pdf.bullet("Analisis dinamico: pruebas con curl contra la API en ejecucion")
pdf.bullet("Pruebas de autenticacion: token valido, invalido, ausente, malformado")
pdf.bullet("Pruebas de rutas: path traversal, rutas inexistentes, metodos no permitidos")
pdf.bullet("Pruebas de inyeccion: SQL injection via query string, header injection")
pdf.bullet("Pruebas de headers: verificacion de cabeceras de seguridad")
pdf.bullet("Pruebas de CORS: verificacion de politica de origen cruzado")

# === HALLAZGOS ===
pdf.add_page()
pdf.seccion("3. HALLAZGOS DETALLADOS")

pdf.hallazgo("VUL-001","Token de autenticacion hardcodeado en codigo fuente","MEDIA",
    "El archivo security/token_auth.py contiene el token de autenticacion "
    "como constante en texto plano: TOKEN_DEMO = 'clase13-token-demo'. "
    "Cualquier persona con acceso al codigo fuente puede autenticarse. "
    "En un entorno real, esto constituiria una exposicion de credenciales (CWE-798).",
    'TOKEN_DEMO = "clase13-token-demo"  # Linea 3 de token_auth.py\n'
    "Archivo: security/token_auth.py",
    "Usar variables de entorno (os.environ['API_TOKEN']) o un gestor de secretos. "
    "Nunca incluir credenciales en el codigo fuente.")

pdf.hallazgo("VUL-002","Ausencia de headers de seguridad HTTP","MEDIA",
    "Las respuestas de la API no incluyen headers de seguridad estandar: "
    "X-Content-Type-Options, X-Frame-Options, Strict-Transport-Security, "
    "Content-Security-Policy, ni X-XSS-Protection. Esto podria facilitar ataques "
    "de tipo MIME sniffing, clickjacking o XSS en integraciones con frontend (CWE-16).",
    "HTTP/1.0 200 OK\n"
    "Server: BaseHTTP/0.6 Python/3.14.10\n"
    "Content-Type: application/json; charset=utf-8\n"
    "Cache-Control: no-store\n"
    "# Faltan: X-Content-Type-Options, X-Frame-Options, etc.",
    "Agregar headers de seguridad en el metodo responder() de app.py:\n"
    "self.send_header('X-Content-Type-Options', 'nosniff')\n"
    "self.send_header('X-Frame-Options', 'DENY')")

pdf.hallazgo("VUL-003","Exposicion de version del servidor en headers","MEDIA",
    "El header 'Server: BaseHTTP/0.6 Python/3.14.10' revela la tecnologia, "
    "el framework y la version exacta de Python. Esto facilita el reconocimiento "
    "a un atacante que busque vulnerabilidades especificas (CWE-200).",
    "Server: BaseHTTP/0.6 Python/3.14.10\n"
    "# Presente en TODAS las respuestas HTTP",
    "Sobrescribir server_version y sys_version en la clase ApiHandler:\n"
    "server_version = 'API/1.0'\n"
    "sys_version = ''")

pdf.add_page()

pdf.hallazgo("VUL-004","Ausencia de limitacion de tasa (Rate Limiting)","BAJA",
    "La API no implementa ningun mecanismo de rate limiting. Un atacante podria "
    "enviar un gran volumen de peticiones para intentar fuerza bruta contra el "
    "endpoint /api/privado o causar denegacion de servicio (CWE-770). "
    "ThreadingHTTPServer crea un hilo por cada peticion sin limite.",
    "# No se encontro ningun mecanismo de rate limiting\n"
    "# en app.py ni en api_controller.py\n"
    "# ThreadingHTTPServer no tiene limite de hilos",
    "Implementar un rate limiter basado en IP con un diccionario de contadores "
    "y timestamps, o usar un reverse proxy (nginx) con limit_req_zone.")

pdf.hallazgo("VUL-005","Sin politica CORS definida","BAJA",
    "La API no define headers Access-Control-Allow-Origin. Los navegadores "
    "bloquearan peticiones cross-origin por defecto (comportamiento seguro). "
    "Sin embargo, la ausencia de una politica CORS explicita puede causar problemas "
    "si se integra con un frontend en otro dominio. OPTIONS retorna 405 (CWE-942).",
    "OPTIONS /api/salud -> 405 Method Not Allowed\n"
    "# No se observa Access-Control-Allow-Origin",
    "Si se necesita acceso cross-origin, implementar manejo explicito de OPTIONS "
    "con headers CORS restrictivos. Si no, documentar como solo same-origin.")

pdf.hallazgo("VUL-006","Logging deshabilitado completamente","INFO",
    "El metodo log_message() en app.py esta sobreescrito con 'pass', eliminando "
    "todo registro de peticiones. La ausencia total de logs impide detectar ataques, "
    "accesos no autorizados o fallos del sistema (CWE-778).",
    'def log_message(self, format, *args):\n'
    '    pass  # No registrar credenciales\n'
    "# Archivo: app.py, lineas 30-31",
    "Implementar logging selectivo que registre metodo, ruta y codigo de respuesta "
    "sin incluir headers de autorizacion ni datos sensibles.")

pdf.hallazgo("VUL-007","Ausencia de validacion del cuerpo de la peticion","INFO",
    "Aunque la API solo acepta GET, el servidor no limita el tamano del body en "
    "metodos POST/PUT. Un atacante podria enviar peticiones con payloads muy grandes "
    "que consumirian memoria del servidor antes del rechazo (CWE-400).",
    "POST /api/salud con body de 100,000 bytes -> 405\n"
    "# El body se lee completo en memoria antes del rechazo",
    "Implementar un limite de Content-Length en el handler. "
    "Rechazar con 413 Payload Too Large si supera 1 KB.")

# === ASPECTOS POSITIVOS ===
pdf.add_page()
pdf.seccion("4. ASPECTOS POSITIVOS IDENTIFICADOS")
pdf.txt("La auditoria tambien identifico buenas practicas de seguridad implementadas:")
pdf.ln(2)
pdf.bullet("Uso de compare_digest() para comparacion de tokens: previene ataques de timing side-channel.")
pdf.bullet("Validacion correcta del formato Bearer: requiere 2 partes y verifica el prefijo (case-insensitive).")
pdf.bullet("Binding a 127.0.0.1: la API solo escucha en loopback, no es accesible desde la red externa.")
pdf.bullet("Whitelist de rutas: solo acepta las 3 rutas definidas; cualquier otra retorna 404.")
pdf.bullet("Whitelist de metodos HTTP: solo acepta GET; otros metodos retornan 405 con header Allow.")
pdf.bullet("Header Cache-Control: no-store: previene almacenamiento en cache de respuestas sensibles.")
pdf.bullet("Content-Type explicito: application/json con charset utf-8 en todas las respuestas.")
pdf.bullet("Datos ficticios sin base de datos: elimina vectores de SQL injection u ORM injection.")
pdf.bullet("Serializacion segura con json.dumps(): sin uso de eval(), pickle o deserializacion insegura.")
pdf.bullet("Separacion clara MVC: la logica de seguridad, datos y presentacion estan bien aisladas.")

# === PRUEBAS DINAMICAS ===
pdf.add_page()
pdf.seccion("5. RESULTADOS DE PRUEBAS DINAMICAS")

def tabla_pruebas(pdf, titulo, data):
    pdf.sub(titulo)
    pdf.set_fill_color(41, 128, 185)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 9)
    pdf.cell(58,7,"Prueba",border=1,fill=True,align="C")
    pdf.cell(18,7,"Codigo",border=1,fill=True,align="C")
    pdf.cell(68,7,"Respuesta",border=1,fill=True,align="C")
    pdf.cell(22,7,"Result.",border=1,fill=True,align="C",new_x="LMARGIN",new_y="NEXT")
    pdf.set_font("Helvetica","",8)
    for p,co,r,res in data:
        pdf.set_text_color(50,50,50)
        pdf.cell(58,6,p,border=1)
        pdf.cell(18,6,co,border=1,align="C")
        pdf.cell(68,6,r,border=1)
        if res=="PASS": pdf.set_text_color(39,174,96)
        elif res=="NOTA": pdf.set_text_color(243,156,18)
        else: pdf.set_text_color(231,76,60)
        pdf.set_font("Helvetica","B",8)
        pdf.cell(22,6,res,border=1,align="C",new_x="LMARGIN",new_y="NEXT")
        pdf.set_font("Helvetica","",8)

tabla_pruebas(pdf, "5.1 Pruebas de autenticacion", [
    ("GET /api/privado sin token","401","Token ausente o invalido","PASS"),
    ("GET /api/privado token correcto","200","auth OK","PASS"),
    ("GET /api/privado token incorrecto","401","Token ausente o invalido","PASS"),
    ("GET /api/privado header malformado","401","Token ausente o invalido","PASS"),
])

tabla_pruebas(pdf, "5.2 Pruebas de rutas y metodos", [
    ("GET /api/salud","200",'{"status": "OK"}',"PASS"),
    ("GET /api/productos","200","Lista de 3 productos","PASS"),
    ("GET /api/inexistente","404","Ruta no encontrada","PASS"),
    ("POST /api/salud","405","Metodo no permitido","PASS"),
    ("GET /../etc/passwd","404","Ruta no encontrada","PASS"),
])

tabla_pruebas(pdf, "5.3 Pruebas de inyeccion", [
    ("SQL Injection en query string","200","No afecta (sin DB)","PASS"),
    ("Header injection","401","Token rechazado","PASS"),
    ("Body POST grande (100KB)","405","Metodo no permitido","NOTA"),
])

# === MATRIZ DE RIESGOS ===
pdf.add_page()
pdf.seccion("6. MATRIZ DE RIESGOS")
pdf.txt("Clasificacion de hallazgos segun probabilidad de explotacion e impacto en el contexto academico.")
pdf.ln(2)

pdf.set_fill_color(41, 128, 185)
pdf.set_text_color(255, 255, 255)
pdf.set_font("Helvetica", "B", 9)
cols = [("ID",20),("Vulnerabilidad",52),("Severidad",24),("Probabilidad",28),("Impacto",24),("Riesgo",24)]
for name,w in cols:
    pdf.cell(w,8,name,border=1,fill=True,align="C")
pdf.ln()

matriz = [
    ("VUL-001","Token hardcodeado","MEDIA","Alta","Medio","Medio"),
    ("VUL-002","Sin headers seguridad","MEDIA","Media","Bajo","Bajo"),
    ("VUL-003","Version expuesta","MEDIA","Alta","Bajo","Bajo"),
    ("VUL-004","Sin rate limiting","BAJA","Baja","Medio","Bajo"),
    ("VUL-005","Sin politica CORS","BAJA","Baja","Bajo","Minimo"),
    ("VUL-006","Logging deshabilitado","INFO","N/A","Bajo","Nota"),
    ("VUL-007","Sin limite de body","INFO","Baja","Bajo","Nota"),
]
pdf.set_text_color(50,50,50)
pdf.set_font("Helvetica","",8)
for row in matriz:
    for i,(name,w) in enumerate(cols):
        pdf.cell(w,6,row[i],border=1,align="C" if i!=1 else "L")
    pdf.ln()

# === CONCLUSIONES ===
pdf.ln(5)
pdf.seccion("7. CONCLUSIONES Y RECOMENDACIONES")
pdf.txt(
    "La API MVC analizada demuestra un nivel de seguridad adecuado para su proposito "
    "academico. Las principales fortalezas incluyen el uso de compare_digest() para "
    "prevenir timing attacks, el binding exclusivo a loopback, la whitelist estricta "
    "de rutas y metodos, y la ausencia de deserializacion insegura."
)
pdf.txt(
    "Los hallazgos identificados son consistentes con una aplicacion de demostracion "
    "y no representan riesgos criticos en el contexto de un laboratorio academico. "
    "Se recomienda implementar las siguientes mejoras prioritarias:"
)
pdf.ln(2)
pdf.bullet("PRIORIDAD 1: Externalizar el token a una variable de entorno (VUL-001)")
pdf.bullet("PRIORIDAD 2: Agregar headers de seguridad HTTP basicos (VUL-002)")
pdf.bullet("PRIORIDAD 3: Ocultar la version del servidor (VUL-003)")
pdf.bullet("PRIORIDAD 4: Implementar logging selectivo sin datos sensibles (VUL-006)")
pdf.bullet("PRIORIDAD 5: Evaluar rate limiting y CORS segun el caso de uso (VUL-004, VUL-005)")

# === ASUNTOS PENDIENTES ===
pdf.ln(5)
pdf.seccion("8. ASUNTOS PENDIENTES (Fuera de Alcance)")
pdf.txt("Los siguientes aspectos no fueron evaluados y requieren analisis adicional:")
pdf.ln(2)
pdf.bullet("Pruebas de carga/estres: evaluar comportamiento bajo alta concurrencia.")
pdf.bullet("Analisis de dependencias: el entorno virtual (.venv) no fue auditado.")
pdf.bullet("Configuracion de despliegue: no se evaluo reverse proxy en produccion.")
pdf.bullet("Pruebas de fuzzing: no se realizaron pruebas de fuzzing automatizado.")
pdf.bullet("Analisis de API_ACT4: existe otra version de la API que no fue parte de este alcance.")

# === FIRMA ===
pdf.ln(10)
pdf.set_draw_color(41, 128, 185)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())
pdf.ln(5)
pdf.set_font("Helvetica", "I", 10)
pdf.set_text_color(100, 100, 100)
pdf.cell(0,6,"Reporte generado por el Agente de Auditoria de Seguridad",align="C",new_x="LMARGIN",new_y="NEXT")
pdf.cell(0,6,"Joaquin - Rakesh Cibersecurity | Tecmilenio",align="C",new_x="LMARGIN",new_y="NEXT")
pdf.cell(0,6,"Generado: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'),align="C",new_x="LMARGIN",new_y="NEXT")

out = "/home/rodrigo/Escritorio/CIBERSEGURIDAD/AGENT/REPORTE_AUDITORIA_API_MVC.pdf"
pdf.output(out)
print("PDF generado: " + out)
