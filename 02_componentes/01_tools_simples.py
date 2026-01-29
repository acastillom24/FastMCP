"""
DÍA 3: COMPONENTES - TOOLS SIMPLES
═══════════════════════════════════════════════════════════════════

Las herramientas (Tools) son funciones que tu servidor EXPONE
y que los clientes pueden EJECUTAR.

Este archivo muestra tools simples, útiles, y bien documentadas.
"""

import math
from datetime import datetime

from fastmcp import FastMCP

mcp = FastMCP("Tools Simples - DÍA 3 🛠️")

# ═══════════════════════════════════════════════════════════════════
# TOOLS MATEMÁTICAS
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def sumar(a: int, b: int) -> int:
    """Suma dos números.
    
    Args:
        a: El primer número
        b: El segundo número
        
    Returns:
        La suma de a + b
        
    Example:
        sumar(5, 3) retorna 8
    """
    return a + b


@mcp.tool
def calcular_promedio(numeros: list[int]) -> float:
    """Calcula el promedio de una lista de números.
    
    Args:
        numeros: Lista de números enteros
        
    Returns:
        El promedio como número decimal
        
    Example:
        calcular_promedio([2, 4, 6]) retorna 4.0
    """
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)


@mcp.tool
def potencia(base: float, exponente: float) -> float:
    """Calcula base elevado a exponente.
    
    Args:
        base: El número base
        exponente: El exponente
        
    Returns:
        El resultado de base^exponente
        
    Example:
        potencia(2, 3) retorna 8.0
    """
    return base ** exponente


@mcp.tool
def raiz_cuadrada(numero: float) -> float:
    """Calcula la raíz cuadrada.
    
    Args:
        numero: El número del cual calcular raíz
        
    Returns:
        La raíz cuadrada
        
    Raises:
        ValueError: Si el número es negativo
    """
    if numero < 0:
        raise ValueError("No se puede calcular raíz de número negativo")
    return math.sqrt(numero)


# ═══════════════════════════════════════════════════════════════════
# TOOLS DE TEXTO
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def convertir_mayusculas(texto: str) -> str:
    """Convierte texto a MAYÚSCULAS.
    
    Args:
        texto: El texto a convertir
        
    Returns:
        El texto en mayúsculas
        
    Example:
        convertir_mayusculas("hola") retorna "HOLA"
    """
    return texto.upper()


@mcp.tool
def invertir_texto(texto: str) -> str:
    """Invierte el orden de los caracteres.
    
    Args:
        texto: El texto a invertir
        
    Returns:
        El texto invertido
        
    Example:
        invertir_texto("hola") retorna "aloh"
    """
    return texto[::-1]


@mcp.tool
def contar_palabras(texto: str) -> int:
    """Cuenta cuántas palabras hay en el texto.
    
    Args:
        texto: El texto a analizar
        
    Returns:
        El número de palabras
        
    Example:
        contar_palabras("Hola mundo fastmcp") retorna 3
    """
    return len(texto.split())


@mcp.tool
def reemplazar_palabra(
    texto: str,
    palabra_original: str,
    palabra_nueva: str
) -> str:
    """Reemplaza una palabra por otra.
    
    Args:
        texto: El texto donde buscar
        palabra_original: La palabra a reemplazar
        palabra_nueva: La palabra nueva
        
    Returns:
        El texto con la palabra reemplazada
        
    Example:
        reemplazar_palabra("Hola mundo", "mundo", "FastMCP")
        retorna "Hola FastMCP"
    """
    return texto.replace(palabra_original, palabra_nueva)


# ═══════════════════════════════════════════════════════════════════
# TOOLS DE FECHA Y HORA
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def obtener_hora_actual() -> str:
    """Obtiene la hora actual.
    
    Returns:
        La hora actual en formato HH:MM:SS
        
    Example:
        obtener_hora_actual() retorna "14:30:45"
    """
    return datetime.now().strftime("%H:%M:%S")


@mcp.tool
def obtener_fecha_actual() -> str:
    """Obtiene la fecha actual.
    
    Returns:
        La fecha actual en formato DD/MM/YYYY
        
    Example:
        obtener_fecha_actual() retorna "26/01/2025"
    """
    return datetime.now().strftime("%d/%m/%Y")


@mcp.tool
def obtener_fecha_hora() -> str:
    """Obtiene la fecha y hora actual.
    
    Returns:
        Fecha y hora combinadas
        
    Example:
        obtener_fecha_hora() retorna "26/01/2025 14:30:45"
    """
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# ═══════════════════════════════════════════════════════════════════
# TOOLS DE VALIDACIÓN
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def es_numero_par(numero: int) -> bool:
    """Verifica si un número es par.
    
    Args:
        numero: El número a verificar
        
    Returns:
        True si es par, False si es impar
        
    Example:
        es_numero_par(4) retorna True
        es_numero_par(5) retorna False
    """
    return numero % 2 == 0


@mcp.tool
def es_palindromo(texto: str) -> bool:
    """Verifica si el texto es un palíndromo.
    
    Args:
        texto: El texto a verificar
        
    Returns:
        True si es palíndromo, False en caso contrario
        
    Example:
        es_palindromo("aba") retorna True
        es_palindromo("abc") retorna False
    """
    texto_limpio = texto.lower().replace(" ", "")
    return texto_limpio == texto_limpio[::-1]


# ═══════════════════════════════════════════════════════════════════
# TOOLS DE CONVERSIÓN
# ═══════════════════════════════════════════════════════════════════

@mcp.tool
def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte temperatura de Celsius a Fahrenheit.
    
    Args:
        celsius: Temperatura en Celsius
        
    Returns:
        La temperatura en Fahrenheit
        
    Example:
        celsius_a_fahrenheit(25) retorna 77.0
    """
    return (celsius * 9/5) + 32


@mcp.tool
def kilogramos_a_libras(kg: float) -> float:
    """Convierte peso de kilogramos a libras.
    
    Args:
        kg: Peso en kilogramos
        
    Returns:
        El peso en libras
        
    Example:
        kilogramos_a_libras(1) retorna 2.20462
    """
    return kg * 2.20462


# ═══════════════════════════════════════════════════════════════════
# EJECUCIÓN
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════╗
║     TOOLS SIMPLES - EJEMPLO 01 DE COMPONENTES         ║
╚════════════════════════════════════════════════════════╝

TOOLS DISPONIBLES:

📊 MATEMÁTICAS:
  • sumar(a, b) - Suma dos números
  • calcular_promedio(numeros) - Promedio de lista
  • potencia(base, exponente) - Calcula potencia
  • raiz_cuadrada(numero) - Raíz cuadrada

📝 TEXTO:
  • convertir_mayusculas(texto) - A MAYÚSCULAS
  • invertir_texto(texto) - Invierte orden
  • contar_palabras(texto) - Cuenta palabras
  • reemplazar_palabra(texto, orig, nuevo) - Reemplaza

⏰ FECHA/HORA:
  • obtener_hora_actual() - Hora HH:MM:SS
  • obtener_fecha_actual() - Fecha DD/MM/YYYY
  • obtener_fecha_hora() - Ambas

✅ VALIDACIÓN:
  • es_numero_par(numero) - ¿Es par?
  • es_palindromo(texto) - ¿Es palíndromo?

🔄 CONVERSIÓN:
  • celsius_a_fahrenheit(celsius) - °C a °F
  • kilogramos_a_libras(kg) - kg a libras

Iniciando servidor...
""")
    
    mcp.run()


# ═══════════════════════════════════════════════════════════════════
# PUNTOS CLAVE 🎯
# ═══════════════════════════════════════════════════════════════════

"""
1. NOMBRES DESCRIPTIVOS
   ❌ @mcp.tool def f(x): return x*2
   ✅ @mcp.tool def multiplicar(numero: int) -> int:

2. DOCSTRINGS DETALLADOS
   Los docstrings se convierten en documentación que ve el cliente

3. TYPE HINTS (Anotaciones de tipo)
   @mcp.tool def func(x: int, y: str) -> bool:
   └─ FastMCP valida automáticamente que los argumentos sean correctos

4. BUENAS PRÁCTICAS
   ✓ Una función = una tarea
   ✓ Nombres en español o inglés, pero consistentes
   ✓ Docstrings completos con Args, Returns, Example
   ✓ Validar entrada y retornar errores claros

5. ERROR HANDLING
   Si algo falla, lanza una excepción clara:
   raise ValueError("El número debe ser positivo")
"""
