"""
DÍA 3: COMPONENTES - TOOLS COMPLEJAS
═══════════════════════════════════════════════════════════════════

Aquí aprenderás a crear tools más complejas:
- Tools que retornan diccionarios
- Tools que aceptan listas de objetos
- Tools con validaciones avanzadas
- Tools que simulan operaciones reales
"""

from typing import Dict, List, Optional

from fastmcp import FastMCP

mcp = FastMCP("Tools Complejas - DÍA 3 🚀")

# ═══════════════════════════════════════════════════════════════════
# TOOLS QUE RETORNAN DICCIONARIOS (JSON)
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def crear_perfil_usuario(
    nombre: str,
    email: str,
    edad: int
) -> Dict[str, str]:
    """Crea un perfil de usuario.
    
    Args:
        nombre: Nombre completo del usuario
        email: Email del usuario
        edad: Edad del usuario
        
    Returns:
        Diccionario con el perfil creado
        
    Example:
        crear_perfil_usuario("Juan", "juan@example.com", 25)
        retorna:
        {
            "id": "usr_12345",
            "nombre": "Juan",
            "email": "juan@example.com",
            "edad": "25",
            "estado": "activo"
        }
    """
    if edad < 13:
        raise ValueError("El usuario debe tener al menos 13 años")
    
    return {
        "id": f"usr_{nombre[:3].lower()}_{edad}",
        "nombre": nombre,
        "email": email,
        "edad": str(edad),
        "estado": "activo",
        "fecha_creacion": "2025-01-26"
    }


@mcp.tool
def analizar_texto(texto: str) -> Dict[str, str]:
    """Analiza un texto y retorna estadísticas.
    
    Args:
        texto: El texto a analizar
        
    Returns:
        Diccionario con análisis del texto
    """
    palabras = texto.split()
    caracteres = len(texto)
    
    return {
        "total_caracteres": str(caracteres),
        "total_palabras": str(len(palabras)),
        "promedio_caracteres_por_palabra": f"{caracteres/len(palabras):.2f}" if palabras else "0",
        "primera_palabra": palabras[0] if palabras else "",
        "ultima_palabra": palabras[-1] if palabras else "",
        "tiene_numeros": "sí" if any(c.isdigit() for c in texto) else "no"
    }


@mcp.tool
def obtener_info_vehiculo(marca: str, modelo: str, año: int) -> Dict[str, str]:
    """Retorna información sobre un vehículo.
    
    Args:
        marca: Marca del vehículo (ej: Toyota)
        modelo: Modelo (ej: Corolla)
        año: Año de fabricación
        
    Returns:
        Diccionario con información del vehículo
    """
    años_antiguo = 2025 - año
    
    return {
        "marca": marca,
        "modelo": modelo,
        "año": str(año),
        "edad_años": str(años_antiguo),
        "categoria": "nuevo" if años_antiguo < 2 else "usado" if años_antiguo < 10 else "antiguo",
        "requiere_revision": "no" if años_antiguo < 1 else "sí"
    }


# ═══════════════════════════════════════════════════════════════════
# TOOLS QUE ACEPTAN LISTAS DE DATOS
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def procesar_ordenes(ordenes: List[Dict[str, str]]) -> Dict[str, str]:
    """Procesa una lista de órdenes.
    
    Args:
        ordenes: Lista de diccionarios con ordenes
                 Cada orden debe tener: producto, cantidad, precio
        
    Returns:
        Resumen del procesamiento
        
    Example:
        procesar_ordenes([
            {"producto": "Laptop", "cantidad": "1", "precio": "1000"},
            {"producto": "Mouse", "cantidad": "2", "precio": "25"}
        ])
    """
    if not ordenes:
        return {"error": "No hay ordenes para procesar"}
    
    total_ordenes = len(ordenes)
    total_cantidad = 0
    total_costo = 0.0
    
    for orden in ordenes:
        try:
            cantidad = int(orden.get("cantidad", 0))
            precio = float(orden.get("precio", 0))
            total_cantidad += cantidad
            total_costo += cantidad * precio
        except (ValueError, TypeError):
            pass
    
    return {
        "total_ordenes_procesadas": str(total_ordenes),
        "total_articulos": str(total_cantidad),
        "costo_total": f"${total_costo:.2f}",
        "costo_promedio_orden": f"${total_costo/total_ordenes:.2f}" if total_ordenes > 0 else "$0.00"
    }


@mcp.tool
def filtrar_numeros_pares(numeros: List[int]) -> Dict[str, str]:
    """Filtra números pares de una lista.
    
    Args:
        numeros: Lista de números
        
    Returns:
        Diccionario con resultados del filtrado
        
    Example:
        filtrar_numeros_pares([1, 2, 3, 4, 5, 6])
        retorna:
        {
            "total_original": "6",
            "pares_encontrados": "3",
            "numeros_pares": "2, 4, 6"
        }
    """
    pares = [n for n in numeros if n % 2 == 0]
    
    return {
        "total_original": str(len(numeros)),
        "pares_encontrados": str(len(pares)),
        "numeros_pares": ", ".join(map(str, pares)) if pares else "ninguno",
        "porcentaje_pares": f"{(len(pares)/len(numeros)*100):.1f}%" if numeros else "0%"
    }


# ═══════════════════════════════════════════════════════════════════
# TOOLS CON VALIDACIONES AVANZADAS
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def validar_email(email: str) -> Dict[str, str]:
    """Valida si un email tiene formato correcto.
    
    Args:
        email: El email a validar
        
    Returns:
        Diccionario con resultado de validación
    """
    es_valido = "@" in email and "." in email.split("@")[-1]
    
    return {
        "email": email,
        "es_valido": "sí" if es_valido else "no",
        "tiene_arroba": "sí" if "@" in email else "no",
        "tiene_dominio": "sí" if "." in email else "no"
    }


@mcp.tool
def evaluar_contraseña(contraseña: str) -> Dict[str, str]:
    """Evalúa la fortaleza de una contraseña.
    
    Args:
        contraseña: La contraseña a evaluar
        
    Returns:
        Diccionario con evaluación de seguridad
        
    Example:
        evaluar_contraseña("MyPassword123!")
    """
    puntos = 0
    
    if len(contraseña) >= 8:
        puntos += 1
    if any(c.isupper() for c in contraseña):
        puntos += 1
    if any(c.islower() for c in contraseña):
        puntos += 1
    if any(c.isdigit() for c in contraseña):
        puntos += 1
    if any(c in "!@#$%^&*()" for c in contraseña):
        puntos += 1
    
    fortaleza_map = {
        0: "muy débil",
        1: "débil",
        2: "regular",
        3: "buena",
        4: "fuerte",
        5: "muy fuerte"
    }
    
    return {
        "longitud": str(len(contraseña)),
        "tiene_mayusculas": "sí" if any(c.isupper() for c in contraseña) else "no",
        "tiene_minusculas": "sí" if any(c.islower() for c in contraseña) else "no",
        "tiene_numeros": "sí" if any(c.isdigit() for c in contraseña) else "no",
        "tiene_caracteres_especiales": "sí" if any(c in "!@#$%^&*()" for c in contraseña) else "no",
        "fortaleza": fortaleza_map[puntos],
        "puntuacion": f"{puntos}/5"
    }


# ═══════════════════════════════════════════════════════════════════
# TOOLS QUE SIMULAN OPERACIONES REALES
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def simular_consulta_bd(
    tabla: str,
    filtro: Optional[str] = None
) -> Dict[str, str]:
    """Simula una consulta a base de datos.
    
    Args:
        tabla: Nombre de la tabla (ej: usuarios, productos)
        filtro: Filtro opcional (ej: edad>18)
        
    Returns:
        Resultado simulado de la consulta
    """
    resultados_simulados = {
        "usuarios": "3450 registros encontrados",
        "productos": "1200 registros encontrados",
        "ordenes": "890 registros encontrados"
    }
    
    registros = resultados_simulados.get(tabla, "tabla no encontrada")
    
    return {
        "tabla_consultada": tabla,
        "filtro_aplicado": filtro or "ninguno",
        "resultado": registros,
        "tiempo_consulta_ms": "145",
        "estado": "exitoso" if "tabla no encontrada" not in registros else "error"
    }


@mcp.tool
def procesar_pago(
    monto: float,
    moneda: str = "USD"
) -> Dict[str, str]:
    """Simula el procesamiento de un pago.
    
    Args:
        monto: Monto a pagar
        moneda: Moneda (USD, EUR, ARS)
        
    Returns:
        Resultado del procesamiento
    """
    id_transaccion = f"TXN_{int(monto*100):08d}"
    
    return {
        "id_transaccion": id_transaccion,
        "monto": f"{monto:.2f}",
        "moneda": moneda,
        "estado": "procesado" if monto > 0 else "rechazado",
        "fecha_procesamiento": "2025-01-26 14:30:45",
        "referencia_banco": f"REF{id_transaccion[-4:]}"
    }


# ═══════════════════════════════════════════════════════════════════
# EJECUCIÓN
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════╗
║    TOOLS COMPLEJAS - EJEMPLO 02 DE COMPONENTES       ║
╚════════════════════════════════════════════════════════╝

TOOLS COMPLEJAS DISPONIBLES:

👤 USUARIO & PERFIL:
  • crear_perfil_usuario(nombre, email, edad)
  • analizar_texto(texto)
  • obtener_info_vehiculo(marca, modelo, año)

📋 PROCESAMIENTO DE LISTAS:
  • procesar_ordenes(ordenes)
  • filtrar_numeros_pares(numeros)

✅ VALIDACIONES:
  • validar_email(email)
  • evaluar_contraseña(contraseña)

🔍 OPERACIONES SIMULADAS:
  • simular_consulta_bd(tabla, filtro?)
  • procesar_pago(monto, moneda?)

Iniciando servidor...
""")
    
    mcp.run()


# ═══════════════════════════════════════════════════════════════════
# PATRONES IMPORTANTES 🎯
# ═══════════════════════════════════════════════════════════════════

"""
PATRÓN 1: RETORNAR DICCIONARIOS
  ✅ return {"key": "value", "status": "ok"}
  └─ Fácil de parsear en cliente
  └─ Información estructurada

PATRÓN 2: ACEPTAR LISTAS DE OBJETOS
  ✅ ordenes: List[Dict[str, str]]
  └─ Flexible para múltiples items
  └─ Cliente puede enviar cualquier cantidad

PATRÓN 3: PARÁMETROS OPCIONALES
  ✅ filtro: Optional[str] = None
  └─ Cliente puede no enviar si no necesita
  └─ Valor por defecto si no lo proporciona

PATRÓN 4: VALIDACIÓN Y ERRORES
  ✅ if edad < 13: raise ValueError(...)
  └─ FastMCP maneja el error automáticamente
  └─ Cliente ve el mensaje de error claro

PATRÓN 5: RETORNAR STRINGS EN LUGAR DE NÚMEROS
  ✅ return {"cantidad": str(cantidad)}
  └─ JSON solo soporta ciertos tipos
  └─ Mejor convertir todo a string en dict
  └─ Cliente puede convertir como necesite
"""
