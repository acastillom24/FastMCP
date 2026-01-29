"""
DÍA 3: COMPONENTES - RESOURCES (Recursos)
═══════════════════════════════════════════════════════════════════

Los Resources son datos que el cliente puede LEER.
Son diferentes a las Tools (que se EJECUTAN).

Resources = Datos para consultar
Tools = Acciones para ejecutar
"""

import json
from datetime import datetime

from fastmcp import FastMCP

mcp = FastMCP("Resources - DÍA 3 📚")

# ═══════════════════════════════════════════════════════════════════
# RECURSOS SIMPLES - TEXTO
# ═══════════════════════════════════════════════════════════════════

@mcp.resource
def obtener_mensaje_bienvenida() -> str:
    """Retorna el mensaje de bienvenida del servidor.
    
    Returns:
        Un mensaje de bienvenida amigable
    """
    return """
╔════════════════════════════════════════════════════════╗
║          ¡BIENVENIDO A FASTMCP!                        ║
╚════════════════════════════════════════════════════════╝

Este servidor MCP proporciona:
- Tools: Funciones que puedes EJECUTAR
- Resources: Datos que puedes CONSULTAR
- Prompts: Instrucciones que puedes USAR

¡Explora los recursos disponibles!
"""


@mcp.resource
def obtener_documentacion() -> str:
    """Documentación general del servidor.
    
    Returns:
        La documentación completa
    """
    return """
DOCUMENTACIÓN DEL SERVIDOR MCP

1. CONCEPTOS BÁSICOS
   - Tools: Funciones ejecutables
   - Resources: Datos de solo lectura
   - Prompts: Instrucciones reutilizables

2. CÓMO USAR
   - Llama a un tool con argumentos
   - Consulta un resource para obtener datos
   - Usa un prompt para guías

3. EJEMPLOS
   Ejecutar tool: calcular_suma(5, 3)
   Leer resource: obtener_documentacion()
   Ver prompt: guia_inicio()
"""


# ═══════════════════════════════════════════════════════════════════
# RECURSOS CON ESTADO DEL SISTEMA
# ═══════════════════════════════════════════════════════════════════

@mcp.resource
def obtener_estado_servidor() -> str:
    """Retorna el estado actual del servidor.
    
    Returns:
        Información sobre el estado del servidor
    """
    ahora = datetime.now()
    
    return f"""
ESTADO DEL SERVIDOR
═══════════════════════════════════════════════════════

Hora actual: {ahora.strftime('%H:%M:%S')}
Fecha: {ahora.strftime('%d/%m/%Y')}
Hora de inicio: 2025-01-26 10:00:00
Tiempo de actividad: 4 horas 30 minutos
Status: ✅ OPERATIVO

Conexiones activas: 5
Requests procesados: 342
Errores: 2
Tasa de éxito: 99.4%

Memoria: 45.2 MB / 512 MB (8.8%)
CPU: 2.3%
"""


@mcp.resource
def obtener_configuracion_servidor() -> str:
    """Retorna la configuración del servidor.
    
    Returns:
        Configuración actual
    """
    return """
CONFIGURACIÓN DEL SERVIDOR
═══════════════════════════════════════════════════════

Nombre: FastMCP Demo Server
Versión: 3.0.0
Entorno: producción
Idioma: Español

LÍMITES:
  - Máximo de conexiones: 100
  - Timeout de request: 30s
  - Máximo payload: 10MB
  - Rate limit: 1000 req/min

SEGURIDAD:
  - Autenticación: Token JWT
  - Encriptación: TLS 1.3
  - CORS: habilitado
  - Validación: automática

API_BASE_URL: https://api.fastmcp.local
WEBHOOK_ENDPOINT: https://webhook.fastmcp.local
LOGS_PATH: /var/log/fastmcp/
"""


# ═══════════════════════════════════════════════════════════════════
# RECURSOS CON DATOS ESTRUCTURADOS (JSON como string)
# ═══════════════════════════════════════════════════════════════════

@mcp.resource
def obtener_usuarios() -> str:
    """Retorna la lista de usuarios registrados.
    
    Returns:
        JSON string con los usuarios
    """
    usuarios = [
        {"id": "usr_001", "nombre": "Juan García", "email": "juan@example.com"},
        {"id": "usr_002", "nombre": "María López", "email": "maria@example.com"},
        {"id": "usr_003", "nombre": "Carlos Pérez", "email": "carlos@example.com"}
    ]
    
    return json.dumps(usuarios, indent=2, ensure_ascii=False)


@mcp.resource
def obtener_estadisticas() -> str:
    """Retorna estadísticas del sistema.
    
    Returns:
        JSON string con estadísticas
    """
    stats = {
        "usuarios_totales": 1250,
        "usuarios_activos": 890,
        "usuarios_inactivos": 360,
        "usuarios_nuevos_hoy": 45,
        "nuevos_esta_semana": 312,
        "tasa_retencion": "92.3%"
    }
    
    return json.dumps(stats, indent=2, ensure_ascii=False)


@mcp.resource
def obtener_cambios_recientes() -> str:
    """Retorna los cambios recientes del servidor.
    
    Returns:
        Historial de cambios formateado
    """
    cambios = [
        "2025-01-26 14:30:00 - Actualización de seguridad (v3.0.1)",
        "2025-01-26 12:15:00 - Mantenimiento completado",
        "2025-01-26 10:00:00 - Servidor iniciado",
        "2025-01-25 23:45:00 - Backup automático realizado",
        "2025-01-25 22:30:00 - Limpieza de logs antigua"
    ]
    
    return "\n".join([f"  {cambio}" for cambio in cambios])


# ═══════════════════════════════════════════════════════════════════
# RECURSOS DINÁMICOS
# ═══════════════════════════════════════════════════════════════════

@mcp.resource
def obtener_hora_formateada() -> str:
    """Retorna la hora actual en varios formatos.
    
    Returns:
        Hora en múltiples formatos
    """
    ahora = datetime.now()
    
    return f"""
HORA ACTUAL
═══════════════════════════════════════════════════════

Formato 24h:      {ahora.strftime('%H:%M:%S')}
Formato 12h:      {ahora.strftime('%I:%M:%S %p')}
ISO 8601:         {ahora.isoformat()}
Timestamp Unix:   {int(ahora.timestamp())}
Legible:          {ahora.strftime('%A, %d de %B de %Y a las %H:%M')}
"""


@mcp.resource
def obtener_informacion_api() -> str:
    """Retorna información sobre los endpoints disponibles.
    
    Returns:
        Documentación de API
    """
    return """
INFORMACIÓN DE API
═══════════════════════════════════════════════════════

ENDPOINTS DISPONIBLES:

GET /health
  Verifica que el servidor está activo
  Retorna: {"status": "ok"}

GET /stats
  Obtiene estadísticas del servidor
  Retorna: JSON con métricas

POST /execute-tool
  Ejecuta una herramienta
  Body: {"tool": "nombre", "args": {...}}

GET /resources
  Lista todos los recursos
  Retorna: JSON con recursos disponibles

POST /query
  Consulta datos
  Body: {"query": "..."}

CÓDIGOS DE ESTADO:
  200 - OK
  400 - Bad Request
  401 - Unauthorized
  500 - Server Error
"""


# ═══════════════════════════════════════════════════════════════════
# RECURSOS INFORMATIVOS
# ═══════════════════════════════════════════════════════════════════

@mcp.resource
def obtener_licencia() -> str:
    """Información de licencia del software.
    
    Returns:
        Texto de licencia
    """
    return """
LICENCIA
═══════════════════════════════════════════════════════

FastMCP - The fast, Pythonic way to build MCP servers and clients

Licensed under the MIT License

Copyright (c) 2024 Prefect Technologies, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.

PARA MÁS INFORMACIÓN:
- Documentación: https://gofastmcp.com/
- GitHub: https://github.com/jlowin/fastmcp
- Sitio web: https://www.prefect.io/
"""


@mcp.resource
def obtener_version() -> str:
    """Información de versión.
    
    Returns:
        Detalles de versión
    """
    return """
INFORMACIÓN DE VERSIÓN
═══════════════════════════════════════════════════════

FastMCP Version: 3.0.0
Python Version: 3.11.0
MCP Protocol Version: 1.0

Build: linux-x86_64
Architecture: x64
Timestamp: 2025-01-26T14:30:00Z

HISTORIAL DE VERSIONES:
v3.0.0 - Lanzamiento principal
v2.5.1 - Parches de seguridad
v2.5.0 - Nuevas características
"""


# ═══════════════════════════════════════════════════════════════════
# EJECUCIÓN
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════╗
║     RESOURCES - EJEMPLO 03 DE COMPONENTES             ║
╚════════════════════════════════════════════════════════╝

RESOURCES DISPONIBLES (Solo lectura):

📖 DOCUMENTACIÓN:
  • obtener_mensaje_bienvenida()
  • obtener_documentacion()
  • obtener_informacion_api()

🔧 CONFIGURACIÓN & ESTADO:
  • obtener_estado_servidor()
  • obtener_configuracion_servidor()
  • obtener_hora_formateada()

📊 DATOS:
  • obtener_usuarios()
  • obtener_estadisticas()
  • obtener_cambios_recientes()

⚖️ INFORMACIÓN LEGAL:
  • obtener_licencia()
  • obtener_version()

Iniciando servidor...
""")
    
    mcp.run()


# ═══════════════════════════════════════════════════════════════════
# DIFERENCIAS: TOOLS vs RESOURCES 🎯
# ═══════════════════════════════════════════════════════════════════

"""
TOOLS (@mcp.tool):
  ✅ El cliente puede EJECUTAR
  ✅ Pueden cambiar estado del servidor
  ✅ Aceptan parámetros
  ✅ Ejemplo: calcular(a, b), crear_usuario(...)
  
  @mcp.tool
  def calcular(a: int, b: int) -> int:
      return a + b

RESOURCES (@mcp.resource):
  ✅ El cliente puede LEER/CONSULTAR
  ✅ No cambian estado (lectura pura)
  ✅ No aceptan parámetros
  ✅ Ejemplo: obtener_documentacion(), obtener_estado()
  
  @mcp.resource
  def obtener_documentacion() -> str:
      return "..."

CUÁNDO USAR CADA UNO:

❓ "¿El cliente necesita HACER algo?"
   ✓ Respuesta SÍ → usa TOOL
   ✓ Respuesta NO → usa RESOURCE

❓ "¿La función toma parámetros?"
   ✓ Respuesta SÍ → usa TOOL
   ✓ Respuesta NO → usa RESOURCE

❓ "¿Puede cambiar estado del servidor?"
   ✓ Respuesta SÍ → usa TOOL
   ✓ Respuesta NO → usa RESOURCE
"""
