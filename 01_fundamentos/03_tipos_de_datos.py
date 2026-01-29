"""
DÍA 1-2: EJEMPLO 3 - TIPOS DE DATOS EN FASTMCP
═══════════════════════════════════════════════

FastMCP valida AUTOMÁTICAMENTE los tipos de datos.
Aprende cómo usar tipos complejos y cómo FastMCP los maneja.
"""

from datetime import datetime
from typing import Dict, List, Optional

from fastmcp import FastMCP

mcp = FastMCP("Tipos de Datos en FastMCP 📊")


# ═══════════════════════════════════════════════════════════════════
# TIPOS BÁSICOS
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def procesar_texto(texto: str) -> str:
    """Procesa un texto."""
    return f"Texto procesado: {texto.upper()}"


@mcp.tool
def contar_numeros(cantidad: int) -> str:
    """Cuenta números del 1 al N."""
    return f"Números: {', '.join(map(str, range(1, cantidad + 1)))}"


@mcp.tool
def es_verdadero(valor: bool) -> str:
    """Retorna el valor booleano."""
    return f"El valor es: {'Verdadero' if valor else 'Falso'}"


@mcp.tool
def procesar_decimal(numero: float) -> float:
    """Realiza operación con decimal."""
    return numero * 2.5


# ═══════════════════════════════════════════════════════════════════
# TIPOS OPCIONALES (pueden ser None)
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def saludar_opcional(nombre: str, apellido: Optional[str] = None) -> str:
    """Saluda a una persona.
    
    Args:
        nombre: El nombre (obligatorio)
        apellido: El apellido (opcional)
        
    Returns:
        Un saludo personalizado
    """
    if apellido:
        return f"¡Hola {nombre} {apellido}!"
    else:
        return f"¡Hola {nombre}!"


# ═══════════════════════════════════════════════════════════════════
# COLECCIONES: LISTAS
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def sumar_lista(numeros: List[int]) -> int:
    """Suma una lista de números.
    
    Args:
        numeros: Lista de números enteros
        
    Returns:
        La suma total
        
    Ejemplo:
        sumar_lista([1, 2, 3, 4, 5]) retorna 15
    """
    return sum(numeros)


@mcp.tool
def procesar_nombres(nombres: List[str]) -> str:
    """Procesa una lista de nombres.
    
    Args:
        nombres: Lista de nombres
        
    Returns:
        Un resumen de los nombres
    """
    return f"Total: {len(nombres)} nombres - {', '.join(nombres)}"


# ═══════════════════════════════════════════════════════════════════
# DICCIONARIOS (Objetos JSON)
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def procesar_usuario(datos_usuario: Dict[str, str]) -> str:
    """Procesa datos de un usuario.
    
    Args:
        datos_usuario: Diccionario con los datos del usuario
        
    Returns:
        Resumen de los datos
        
    Ejemplo:
        procesar_usuario({
            "nombre": "Juan",
            "email": "juan@example.com",
            "ciudad": "Madrid"
        })
    """
    nombre = datos_usuario.get("nombre", "Desconocido")
    email = datos_usuario.get("email", "No especificado")
    ciudad = datos_usuario.get("ciudad", "No especificada")
    
    return f"""
Usuario: {nombre}
Email: {email}
Ciudad: {ciudad}
"""


# ═══════════════════════════════════════════════════════════════════
# TIPOS COMPLEJOS ANIDADOS
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def procesador_complejo(
    nombre: str,
    numeros: List[int],
    configuracion: Dict[str, bool],
    es_activo: bool
) -> Dict[str, str]:
    """Procesa datos complejos.
    
    Args:
        nombre: Nombre del usuario
        numeros: Lista de números
        configuracion: Diccionario de configuración
        es_activo: Si el usuario está activo
        
    Returns:
        Diccionario con el resultado del procesamiento
        
    Ejemplo:
        procesador_complejo(
            "Juan",
            [1, 2, 3, 4, 5],
            {"notificaciones": True, "privado": False},
            True
        )
    """
    suma_numeros = sum(numeros)
    config_activa = sum(1 for v in configuracion.values() if v)
    
    return {
        "usuario": nombre,
        "suma": str(suma_numeros),
        "promedio": str(suma_numeros / len(numeros) if numeros else 0),
        "configuraciones_activas": str(config_activa),
        "estado": "Activo" if es_activo else "Inactivo"
    }


# ═══════════════════════════════════════════════════════════════════
# VALIDACIÓN AUTOMÁTICA
# ═══════════════════════════════════════════════════════════════════

"""
IMPORTANTE: FastMCP valida automáticamente los tipos

Si un cliente envía:
  - Un string donde se espera int: ❌ ERROR
  - Un int donde se espera float: ✓ Conversión automática
  - Una lista vacía donde se espera List[int]: ✓ Permitido
  - null/None donde se espera string: ❌ ERROR
  - null/None donde se espera Optional[string]: ✓ Permitido

Esto significa que tus funciones SIEMPRE reciben datos válidos.
No necesitas validar manualmente.
"""


# ═══════════════════════════════════════════════════════════════════
# DOCSTRINGS = DOCUMENTACIÓN AUTOMÁTICA
# ═══════════════════════════════════════════════════════════════════

"""
El docstring de cada función se convierte en documentación:

"""
@mcp.tool
def ejemplo_bien_documentado(
    email: str,
    edad: int,
    intereses: Optional[List[str]] = None
) -> Dict[str, str]:
    """Registra un nuevo usuario con validación automática.
    
    Este es un ejemplo PERFECTO de documentación en FastMCP.
    Observa cómo el docstring estructura la información:
    
    Args:
        email: El email del usuario (formato: usuario@dominio.com)
        edad: Edad del usuario (rango: 13-120)
        intereses: Lista opcional de intereses del usuario
        
    Returns:
        Diccionario con el resumen del registro
        
    Raises:
        ValueError: Si el email no es válido
        ValueError: Si la edad está fuera de rango
        
    Example:
        >>> ejemplo_bien_documentado(
        ...     "juan@example.com",
        ...     25,
        ...     ["programacion", "IA"]
        ... )
        {
            "estado": "Registrado",
            "email": "juan@example.com",
            "edad": "25",
            "intereses": "2"
        }
        
    Note:
        FastMCP usa este docstring para generar documentación
        automática que ve el cliente MCP.
    """
    return {
        "estado": "Registrado",
        "email": email,
        "edad": str(edad),
        "intereses": str(len(intereses)) if intereses else "0"
    }


# ═══════════════════════════════════════════════════════════════════
# EJECUCIÓN
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════╗
║          TIPOS DE DATOS EN FASTMCP                     ║
╚════════════════════════════════════════════════════════╝

TIPOS SOPORTADOS:

✅ BÁSICOS:
   - str (texto)
   - int (números enteros)
   - float (números decimales)
   - bool (verdadero/falso)

✅ OPCIONALES:
   - Optional[str] (puede ser None)
   - Optional[int]
   - etc.

✅ COLECCIONES:
   - List[int], List[str], List[float]
   - Dict[str, str], Dict[str, int]
   - etc.

✅ COMPLEJOS:
   - List[Dict[str, int]]
   - Dict[str, List[str]]
   - etc.

VALIDACIÓN:
  ✓ Automática en cada llamada
  ✓ No necesitas validar manualmente
  ✓ Los clientes reciben errores claros

Iniciando servidor...
""")
    
    mcp.run()


# ═══════════════════════════════════════════════════════════════════
# RESUMEN 🎯
# ═══════════════════════════════════════════════════════════════════

"""
REGLA DE ORO:

"Usa type hints en Python, FastMCP se encarga del resto"

La validación automática significa:
1. Código más limpio (sin validación manual)
2. Menos bugs (tipos garantizados)
3. Documentación automática (desde los tipos)
4. Esquemas JSON válidos (generados automáticamente)
5. Mejor seguridad (cliente no puede enviar datos inválidos)
"""
