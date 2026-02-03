from fastmcp import FastMCP

mcp = FastMCP("Mi Primer Servidor 🎉")

# Tool 1: Multiplicar
@mcp.tool
def multiplicar(a: int, b: int) -> int:
    """Multiplica dos números.
    
    Args:
        a: Primer número
        b: Segundo número
        
    Returns:
        El producto a * b
    """
    return a * b

# Tool 2: Dividir
@mcp.tool
def dividir(dividendo: float, divisor: float) -> float:
    """Divide dos números.
    
    Args:
        dividendo: El número a dividir
        divisor: El número por el que dividir
        
    Returns:
        El resultado de la división
        
    Raises:
        ValueError: Si el divisor es 0
    """
    if divisor == 0:
        raise ValueError("No se puede dividir por cero")
    return dividendo / divisor

# Resource: Status
@mcp.resource("config://sistema")
def obtener_status() -> str:
    """Retorna el estado del servidor.
    
    Returns:
        Un string con el estado
    """
    return "✅ Servidor funcionando correctamente"

# Prompt: Guía
@mcp.prompt
def guia_uso() -> str:
    """Guía de uso del servidor.
    
    Returns:
        Una guía paso a paso
    """
    return """
    Este servidor tiene:
    - multiplicar(a, b): Multiplica dos números
    - dividir(dividendo, divisor): Divide dos números
    - obtener_status(): Ve el estado
    """

if __name__ == "__main__":
    print("Tu primer servidor está iniciando...")
    mcp.run()