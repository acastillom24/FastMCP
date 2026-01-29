"""
DÍA 1-2: EJEMPLO 2 - LOS 3 PILARES EN ACCIÓN
═══════════════════════════════════════════

En este ejemplo vemos los 3 pilares de FastMCP:
1. COMPONENTS - Qué expones (tools, resources, prompts)
2. PROVIDERS - De dónde vienen (funciones decoradas)
3. TRANSFORMS - Qué ve cada cliente (opcional, versión simple)
"""

from fastmcp import FastMCP

# ═══════════════════════════════════════════════════════════════════
# PILAR 1: COMPONENTS
# ═══════════════════════════════════════════════════════════════════

mcp = FastMCP("Los 3 Pilares de FastMCP 🏛️")

# COMPONENT #1: TOOL (Herramienta)
# └─ El cliente puede ejecutarla
# └─ Acepta argumentos
# └─ Retorna resultados
@mcp.tool
def calcular_suma(a: int, b: int) -> int:
    """Suma dos números.
    
    Args:
        a: Primer número
        b: Segundo número
        
    Returns:
        La suma de a + b
        
    Ejemplo:
        calcular_suma(5, 3) retorna 8
    """
    return a + b


# COMPONENT #2: RESOURCE (Recurso)
# └─ El cliente puede LEER estos datos
# └─ NO son ejecutables como las tools
# └─ Útil para datos, archivos, config, etc.
@mcp.resource
def obtener_configuracion() -> dict:
    """Retorna la configuración del sistema.
    
    Returns:
        Un diccionario con la configuración
        
    Ejemplo:
        {
            "nombre_servidor": "Mi Servidor",
            "version": "1.0.0",
            "estado": "activo"
        }
    """
    return {
        "nombre_servidor": "Los 3 Pilares",
        "version": "1.0.0",
        "estado": "activo",
        "capacidad_maxima_usuarios": 100
    }


# COMPONENT #3: PROMPT (Instrucción)
# └─ Son instrucciones reutilizables
# └─ El cliente puede invocarlas
# └─ Útil para flujos complejos
@mcp.prompt
def guia_bienvenida(usuario: str) -> str:
    """Proporciona una guía de bienvenida personalizada.
    
    Args:
        usuario: Nombre del usuario nuevo
        
    Returns:
        Una guía de bienvenida paso a paso
        
    Ejemplo:
        guia_bienvenida("Juan") retorna una guía para Juan
    """
    return f"""
╔════════════════════════════════════════════════════════╗
║          ¡BIENVENIDO, {usuario.upper()}!                  ║
╚════════════════════════════════════════════════════════╝

Pasos para empezar:

1. EXPLORA
   └─ Mira las herramientas disponibles (calcular_suma)
   └─ Consulta los recursos (obtener_configuracion)

2. EXPERIMENTA  
   └─ Ejecuta calcular_suma(10, 20)
   └─ Prueba diferentes valores

3. APRENDE
   └─ Ve cómo FastMCP valida tipos automáticamente
   └─ Observa cómo se generan esquemas

Buena suerte, ¡que lo disfrutes!
"""


# ═══════════════════════════════════════════════════════════════════
# PILAR 2: PROVIDERS
# ═══════════════════════════════════════════════════════════════════

# En este ejemplo simple, estamos usando el PROVIDER más simple:
# "Decorated Functions" (Funciones decoradas)
#
# Los decoradores:
#   @mcp.tool     └─ Convierte función en herramienta ejecutable
#   @mcp.resource └─ Convierte función en recurso legible
#   @mcp.prompt   └─ Convierte función en instrucción
#
# FastMCP inspecciona automáticamente:
#   - Los parámetros (tipos)
#   - El retorno (tipo)
#   - El docstring (documentación)
#
# Y genera esquemas JSON válidos para el protocolo MCP

# NOTA: Existen otros providers (veremos en DÍA 4):
# - FileProvider: Lee herramientas de archivos
# - OpenAPIProvider: Desde especificaciones OpenAPI
# - RemoteProvider: Desde servidores MCP remotos
# - CustomProvider: Provider personalizado


# ═══════════════════════════════════════════════════════════════════
# PILAR 3: TRANSFORMS (Opcional en este ejemplo)
# ═══════════════════════════════════════════════════════════════════

# Los transforms permiten presentar el servidor diferente a cada cliente
# Ejemplos:
# - Mostrar solo ciertas herramientas a ciertos usuarios (autorización)
# - Agrupar herramientas bajo namespaces (organización)
# - Cambiar versiones del API dinámicamente
# - Filtrar recursos sensibles

# En este ejemplo simple NO usamos transforms, pero aquí iría:
# 
# @mcp.transform
# def filtro_por_usuario(cliente_id: str, components):
#     if cliente_id == "admin":
#         return components  # Admin ve todo
#     else:
#         return [c for c in components if not c.is_sensitive]
#
# Veremos esto en detalle en DÍA 5


# ═══════════════════════════════════════════════════════════════════
# EJECUCIÓN
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Info sobre el servidor
    print("""
╔════════════════════════════════════════════════════════╗
║          SERVIDOR MCP - LOS 3 PILARES                  ║
╚════════════════════════════════════════════════════════╝

COMPONENTES EXPUESTOS:
  
  1. TOOL: calcular_suma(a: int, b: int) -> int
     └─ Ejecutable, realiza cálculos

  2. RESOURCE: obtener_configuracion() -> dict
     └─ Legible, proporciona datos

  3. PROMPT: guia_bienvenida(usuario: str) -> str
     └─ Instrucción, guía al usuario

PROVIDER:
  └─ Decorated Functions (funciones con decoradores)

TRANSFORMS:
  └─ No configurados (se pueden agregar después)

Iniciando servidor...
""")
    
    mcp.run()


# ═══════════════════════════════════════════════════════════════════
# FLUJO COMPLETO
# ═══════════════════════════════════════════════════════════════════

# Cuando un cliente se conecta:
#
# 1. DESCUBRE COMPONENTES
#    Cliente: "¿Qué me ofreces?"
#    Servidor: "Te ofrezco 3 herramientas: calcular_suma, 
#               obtener_configuracion, guia_bienvenida"
#
# 2. EJECUTA HERRAMIENTAS
#    Cliente: "Ejecuta calcular_suma(5, 3)"
#    Servidor: "Valido tipos ✓, ejecuto función, retorno 8"
#
# 3. ACCEDE RECURSOS
#    Cliente: "Dame obtener_configuracion"
#    Servidor: "Ejecuto la función, retorno dict"
#
# 4. USA PROMPTS
#    Cliente: "Dame guia_bienvenida para 'Mariana'"
#    Servidor: "Retorno guía personalizada para Mariana"


# ═══════════════════════════════════════════════════════════════════
# CONCEPTOS CLAVE 🎯
# ═══════════════════════════════════════════════════════════════════

"""
COMPONENTS (Qué expones):
  ├─ Tools:     Funciones ejecutables (acción)
  ├─ Resources: Datos accesibles (lectura)
  └─ Prompts:   Instrucciones reutilizables (guía)

PROVIDERS (De dónde vienen):
  └─ En este ejemplo: Funciones decoradas
     (Hay más tipos que veremos después)

TRANSFORMS (Qué ve cada cliente):
  └─ Aún no usado (DÍA 5)
  └─ Permite autorización, filtrado, versioning

FastMCP maneja AUTOMÁTICAMENTE:
  ✓ Serialización/deserialización JSON
  ✓ Validación de tipos
  ✓ Generación de esquemas
  ✓ Manejo de errores
  ✓ Documentación
"""


# ═══════════════════════════════════════════════════════════════════
# EJERCICIO 🚀
# ═══════════════════════════════════════════════════════════════════

"""
Tarea:
1. Ejecuta este script: python 02_conceptos.py
2. Observa qué se imprime
3. Ahora, añade:
   - Una nueva TOOL que multiplique dos números
   - Un nuevo RESOURCE que retorne la hora actual
   - Un nuevo PROMPT que dé un resumen

Hint: Usa @mcp.tool, @mcp.resource, @mcp.prompt
"""
