"""
DÍA 1-2: EJEMPLO 1 - TU PRIMER SERVIDOR MCP
═══════════════════════════════════════════

Este es el servidor MCP más simple posible.
Copia este código, ejecuta: python 01_hola_mundo.py

¿Qué pasa?
- FastMCP crea un servidor MCP completo con una herramienta
- El servidor se ejecuta y espera conexiones
- Se generan esquemas JSON automáticamente
- El protocolo MCP se maneja completamente detrás de escenas

TODO lo que necesitas es:
1. Crear una instancia de FastMCP
2. Decorar una función con @mcp.tool
3. Ejecutar con mcp.run()
"""

from fastmcp import FastMCP

# Paso 1: Crear instancia del servidor
mcp = FastMCP("Mi Primer Servidor 🚀")


# Paso 2: Decorar una función como herramienta (tool)
@mcp.tool
def saludar(nombre: str) -> str:
    """Saluda a una persona.
    
    Args:
        nombre: El nombre de la persona a saludar
        
    Returns:
        Un saludo personalizado
    """
    return f"¡Hola {nombre}! 👋 Bienvenido a FastMCP"


# Paso 3: Ejecutar el servidor
if __name__ == "__main__":
    mcp.run()


# ═══════════════════════════════════════════════════════════════════
# EXPLICACIÓN LÍNEA POR LÍNEA
# ═══════════════════════════════════════════════════════════════════

# FastMCP("Mi Primer Servidor 🚀")
#   └─ Crea un servidor MCP con ese nombre
#   └─ FastMCP maneja automáticamente:
#      ✓ Serialización JSON
#      ✓ Validación de tipos (int, str, bool, etc.)
#      ✓ Generación de esquemas
#      ✓ Manejo de errores
#      ✓ Documentación automática

# @mcp.tool
#   └─ Decorador que expone la función como herramienta
#   └─ El cliente puede ejecutarla remotamente
#   └─ Los tipos (nombre: str) se usan para validación

# def saludar(nombre: str) -> str:
#   └─ Función normal de Python
#   └─ FastMCP inspecciona los tipos y crea esquemas
#   └─ Retorna str: el tipo de dato que devuelve

# """Docstring"""
#   └─ SE CONVIERTE EN DOCUMENTACIÓN automáticamente
#   └─ El cliente ve esta descripción

# mcp.run()
#   └─ Inicia el servidor
#   └─ Escucha conexiones MCP
#   └─ Maneja protocolo automáticamente


# ═══════════════════════════════════════════════════════════════════
# CÓMO EJECUTAR
# ═══════════════════════════════════════════════════════════════════

# Terminal:
# $ python 01_hola_mundo.py

# Verás algo como:
# ```
# [INFO] Server started...
# [INFO] Ready to handle requests
# ```

# ¡El servidor está corriendo! Para probarlo necesitas un cliente MCP


# ═══════════════════════════════════════════════════════════════════
# PUNTO CLAVE 🌟
# ═══════════════════════════════════════════════════════════════════

# FastMCP + Decoradores = MCP Production-Ready
#
# Sin FastMCP necesitarías 200+ líneas de código complejo
# Con FastMCP son 15 líneas claras y simples


print("""
════════════════════════════════════════════════════════════════
         🎉 ¡FELICIDADES! 🎉
════════════════════════════════════════════════════════════════

Has creado tu primer servidor MCP. Este servidor:

✅ Acepta conexiones de clientes MCP
✅ Expone la herramienta "saludar" 
✅ Valida automáticamente tipos (nombre debe ser string)
✅ Maneja errores automáticamente
✅ Genera esquemas JSON válidos
✅ Es production-ready

SIGUIENTE: Ve a 02_conceptos.py para aprender más sobre
herramientas, recursos y prompts.
════════════════════════════════════════════════════════════════
""")
