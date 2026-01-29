# 🔍 GUÍA RÁPIDA DE REFERENCIA

## ⚡ 10 COMANDOS ESENCIALES

```bash
# 1. Instalar FastMCP
pip install fastmcp

# 2. Verificar instalación
python -c "import fastmcp; print(fastmcp.__version__)"

# 3. Ejecutar un servidor
python mi_servidor.py

# 4. Crear archivo nuevo
touch mi_servidor.py

# 5. Listar ejemplos
ls 01_fundamentos/
ls 02_componentes/

# 6. Ver archivo
cat 01_fundamentos/01_hola_mundo.py

# 7. Editar archivo (elige tu editor)
code 01_fundamentos/01_hola_mundo.py  # VS Code
nano 01_fundamentos/01_hola_mundo.py  # Terminal

# 8. Listar puertos en uso (si hay conflicto)
lsof -i :5000  # macOS/Linux
netstat -ano | findstr :5000  # Windows

# 9. Ver documentación
python -m http.server 8000  # Inicia servidor local

# 10. Instalar dependencias dev
pip install -e .[dev]
```

---

## 📝 PLANTILLA BÁSICA DE SERVIDOR

```python
from fastmcp import FastMCP

# 1. Crear instancia
mcp = FastMCP("Mi Servidor 🚀")

# 2. Agregar tool
@mcp.tool
def mi_tool(param: str) -> str:
    """Descripción de mi tool.
    
    Args:
        param: Descripción del parámetro
        
    Returns:
        Descripción del retorno
    """
    return f"Resultado: {param}"

# 3. Agregar resource
@mcp.resource
def mi_recurso() -> str:
    """Descripción del recurso."""
    return "datos"

# 4. Agregar prompt
@mcp.prompt
def mi_prompt() -> str:
    """Descripción del prompt."""
    return "instrucción"

# 5. Ejecutar
if __name__ == "__main__":
    mcp.run()
```

---

## 🎨 DECORADORES RÁPIDOS

### Tool (Herramienta ejecutable)
```python
@mcp.tool
def mi_herramienta(x: int) -> int:
    """Descripción que ve el cliente."""
    return x * 2
```

### Resource (Dato de solo lectura)
```python
@mcp.resource
def mi_dato() -> str:
    """Descripción que ve el cliente."""
    return "información"
```

### Prompt (Instrucción)
```python
@mcp.prompt
def mi_instruccion() -> str:
    """Descripción que ve el cliente."""
    return "pasos a seguir..."
```

---

## 📊 TIPOS DE DATOS COMUNES

```python
# Básicos
x: int           # número entero
x: float         # número decimal
x: str           # texto
x: bool          # verdadero/falso

# Opcionales (pueden ser None)
x: Optional[int]
x: Optional[str]

# Colecciones
x: List[int]              # [1, 2, 3]
x: Dict[str, str]         # {"key": "value"}
x: List[Dict[str, str]]   # [{"a": "1"}, {"b": "2"}]

# Retornos
def mi_func() -> int:             # retorna int
def mi_func() -> str:             # retorna str
def mi_func() -> Dict[str, str]:  # retorna dict
def mi_func() -> None:            # no retorna nada
```

---

## 🎯 DIFERENCIAS CLAVE

### Tool vs Resource
```python
# TOOL - El cliente EJECUTA
@mcp.tool
def hacer_algo(param: str) -> str:
    return "resultado"

# RESOURCE - El cliente LEE
@mcp.resource
def obtener_datos() -> str:
    return "datos"
```

### Tool vs Prompt
```python
# TOOL - Retorna datos procesados
@mcp.tool
def calcular(x: int) -> int:
    return x * 2

# PROMPT - Retorna instrucciones
@mcp.prompt
def guia() -> str:
    return "pasos para usar el servidor..."
```

---

## ⚠️ ERRORES COMUNES Y SOLUCIONES

### Error: No docstring
❌ 
```python
@mcp.tool
def mi_tool(x):
    return x
```

✅ 
```python
@mcp.tool
def mi_tool(x: int) -> int:
    """Descripción clara."""
    return x
```

### Error: Sin type hints
❌ 
```python
@mcp.tool
def sumar(a, b):
    return a + b
```

✅ 
```python
@mcp.tool
def sumar(a: int, b: int) -> int:
    """Suma dos números."""
    return a + b
```

### Error: Resource toma parámetros
❌ 
```python
@mcp.resource
def obtener_datos(usuario_id: int) -> str:  # ¡INCORRECTO!
    return f"datos de {usuario_id}"
```

✅ 
```python
@mcp.tool  # Usa @mcp.tool si necesita parámetros
def obtener_datos(usuario_id: int) -> str:
    return f"datos de {usuario_id}"
```

### Error: Prompt sin descripción
❌ 
```python
@mcp.prompt
def mi_prompt(x: int) -> str:
    return "instrucción"
```

✅ 
```python
@mcp.prompt
def mi_prompt(x: int) -> str:
    """Prompt personalizado para el usuario.
    
    Args:
        x: Parámetro de entrada
        
    Returns:
        Instrucción formateada
    """
    return f"instrucción para {x}"
```

---

## 🚨 CUANDO ALGO FALLA

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: fastmcp` | FastMCP no instalado | `pip install fastmcp` |
| `Port 5000 already in use` | Otro servidor corriendo | `mcp.run(port=8001)` |
| `SyntaxError` | Error en el código | Revisa colchetes, comillas |
| `TypeError` | Tipo incorrecto | Verifica type hints |
| `AttributeError` | Método no existe | Verifica la sintaxis |

---

## 🔧 DEBUGGING RÁPIDO

```python
# Ver qué hace tu tool
@mcp.tool
def mi_tool(x: int) -> int:
    print(f"Recibí: {x}")  # Debug
    resultado = x * 2
    print(f"Retornando: {resultado}")  # Debug
    return resultado

# Validar entrada
@mcp.tool
def validado(x: int) -> int:
    """Tool con validación."""
    if x < 0:
        raise ValueError("x debe ser positivo")
    return x * 2

# Retornar información útil
@mcp.tool
def con_info(x: int) -> Dict[str, str]:
    """Tool que retorna info detallada."""
    return {
        "entrada": str(x),
        "salida": str(x * 2),
        "tipo": "multiplicación"
    }
```

---

## 📖 ESTRUCTURA DE DOCSTRING PERFECTA

```python
@mcp.tool
def mi_herramienta(param1: str, param2: int) -> Dict[str, str]:
    """Descripción breve de una línea.
    
    Descripción más larga si es necesario. Puede ocupar
    múltiples líneas y explicar en detalle qué hace.
    
    Args:
        param1: Descripción del primer parámetro
        param2: Descripción del segundo parámetro
        
    Returns:
        Descripción de qué retorna
        
    Raises:
        ValueError: Cuándo se lanza este error
        TypeError: Cuándo se lanza este error
        
    Example:
        >>> mi_herramienta("texto", 42)
        {'resultado': '...'}
        
    Note:
        Información adicional importante
    """
    # Tu código aquí
    return {"resultado": "..."}
```

---

## 🔗 MAPEO RÁPIDO DE ARCHIVOS

| Quiero aprender | Lee |
|-----------------|-----|
| Primeros pasos | [00_EMPIEZA_AQUI.md](00_EMPIEZA_AQUI.md) |
| Plan diario | [QUE_HACER_HOY.md](QUE_HACER_HOY.md) |
| Configuración | [INICIO_RAPIDO.md](INICIO_RAPIDO.md) |
| Servidor simple | [01_fundamentos/01_hola_mundo.py](01_fundamentos/01_hola_mundo.py) |
| Los 3 pilares | [01_fundamentos/02_conceptos.py](01_fundamentos/02_conceptos.py) |
| Tipos de datos | [01_fundamentos/03_tipos_de_datos.py](01_fundamentos/03_tipos_de_datos.py) |
| Tools | [02_componentes/01_tools_simples.py](02_componentes/01_tools_simples.py) |
| Resources | [02_componentes/03_resources.py](02_componentes/03_resources.py) |
| Prompts | [02_componentes/04_prompts.py](02_componentes/04_prompts.py) |
| Completo | [MAPA_COMPLETO.md](MAPA_COMPLETO.md) |

---

## ✅ CHECKLIST ANTES DE EJECUTAR

Antes de ejecutar tu servidor:

- [ ] FastMCP instalado (`pip install fastmcp`)
- [ ] Archivo tiene extensión `.py`
- [ ] Tiene `from fastmcp import FastMCP`
- [ ] Tiene `mcp = FastMCP("nombre")`
- [ ] Tiene `@mcp.tool` o similar
- [ ] Cada función tiene docstring
- [ ] Cada función tiene type hints
- [ ] Tiene `if __name__ == "__main__": mcp.run()`

Si todo ✅, puedes ejecutar:
```bash
python mi_servidor.py
```

---

## 🎯 CÓMO CREAR UN SERVIDOR EN 2 MINUTOS

1. **Crea archivo** `mi_servidor.py`
2. **Copia plantilla:**
```python
from fastmcp import FastMCP
mcp = FastMCP("Mi Servidor")

@mcp.tool
def hola(nombre: str) -> str:
    """Saluda a alguien."""
    return f"¡Hola {nombre}!"

if __name__ == "__main__":
    mcp.run()
```
3. **Ejecuta:**
```bash
python mi_servidor.py
```

¡Listo! 🎉

---

## 📞 SOPORTE RÁPIDO

**Si no funciona:**
1. ¿Python 3.11+? `python --version`
2. ¿FastMCP instalado? `pip install fastmcp`
3. ¿Docstrings? Todos los `@mcp.tool` necesitan docstring
4. ¿Type hints? `def func(x: int) -> int:`
5. ¿mcp.run()? Necesita estar en `if __name__ == "__main__"`

**Documentación:**
- https://gofastmcp.com/

---

**¿Necesitas más ayuda?** Ve a [README.md](README.md) para el índice completo.
