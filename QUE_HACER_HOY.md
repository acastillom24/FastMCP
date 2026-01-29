# ⚡ QUÉ HACER AHORA - DÍA 1

## 🎯 PLAN DE ESTA SESIÓN (2-3 horas)

```
ESTA SESIÓN:
├─ 00:00-00:15  Instalar FastMCP y verificar
├─ 00:15-00:45  Leer FUNDAMENTOS teórico
├─ 00:45-01:15  Ejecutar 01_hola_mundo.py
├─ 01:15-01:45  Ejecutar 02_conceptos.py
├─ 01:45-02:15  Ejecutar 03_tipos_de_datos.py
└─ 02:15-02:30  Tu primer servidor propio
```

---

## 1️⃣ INSTALAR FASTMCP (5 minutos)

### Paso 1: Abre una terminal en este directorio

En Windows PowerShell o CMD:
```bash
cd C:\Users\acastillom\Documents\personal\FastMCP
```

En macOS/Linux:
```bash
cd ~/Documents/personal/FastMCP
```

### Paso 2: Instala FastMCP

```bash
pip install fastmcp
```

Si no funciona, intenta:
```bash
pip install --upgrade pip
pip install fastmcp>=3.0.0
```

### Paso 3: Verifica instalación

```bash
python -c "import fastmcp; print(f'✓ FastMCP {fastmcp.__version__}')"
```

Deberías ver algo como: `✓ FastMCP 3.0.0`

---

## 2️⃣ LEER FUNDAMENTOS (15 minutos)

Lee este archivo despacio:

```bash
cat 01_fundamentos/README.md
```

O abre en tu editor: `01_fundamentos/README.md`

**Puntos clave a entender:**
- ¿Qué es MCP?
- ¿Qué es FastMCP?
- Los 3 pilares (Components, Providers, Transforms)
- Type hints y validación

---

## 3️⃣ EJECUTAR EJEMPLO 1 (15 minutos)

Tu primer servidor MCP en 10 líneas:

```bash
python 01_fundamentos/01_hola_mundo.py
```

**Qué deberías ver:**
```
Server started...
Ready to handle requests
```

El servidor está corriendo. ¡No cierres esta terminal todavía!

**En otra terminal, verifica:**
```bash
curl http://localhost:5000/health
```

O simplemente observa que el servidor está activo.

**Presiona Ctrl+C para detener el servidor**

---

## 4️⃣ ENTENDER LOS 3 PILARES (15 minutos)

Lee y ejecuta:

```bash
python 01_fundamentos/02_conceptos.py
```

Lee el archivo con atención:
```bash
cat 01_fundamentos/02_conceptos.py
```

**Observa:**
- Cómo se usan los decoradores @mcp.tool, @mcp.resource, @mcp.prompt
- Cómo se escriben los docstrings
- Cómo retornan diccionarios

---

## 5️⃣ TIPOS DE DATOS (15 minutos)

Ahora aprende sobre validación automática:

```bash
python 01_fundamentos/03_tipos_de_datos.py
```

Lee el archivo:
```bash
cat 01_fundamentos/03_tipos_de_datos.py
```

**Importante entender:**
- `str`, `int`, `float`, `bool`
- `List[int]`, `Dict[str, str]`
- `Optional[str]`
- Validación automática

---

## 6️⃣ TU PRIMER SERVIDOR PROPIO (15 minutos)

Ahora crea tu propio servidor. Copia este código en un archivo llamado `mi_primer_servidor.py`:

```python
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
@mcp.resource
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
```

Ejecuta:
```bash
python mi_primer_servidor.py
```

¡Felicidades! 🎉 Has creado tu primer servidor MCP

---

## ✅ CHECKLIST DÍA 1

- [ ] FastMCP instalado y verificado
- [ ] Leído `01_fundamentos/README.md`
- [ ] Ejecutado `01_hola_mundo.py`
- [ ] Entendido los 3 pilares
- [ ] Ejecutado `02_conceptos.py`
- [ ] Entendido tipos de datos
- [ ] Ejecutado `03_tipos_de_datos.py`
- [ ] Creado `mi_primer_servidor.py`
- [ ] Verificado que funciona

¿Todo ✅? ¡Excelente! Ahora listo para DÍA 2

---

## 📝 NOTAS IMPORTANTES

### Type Hints (Anotaciones de tipo)
```python
@mcp.tool
def sumar(a: int, b: int) -> int:  # type hints aquí
    return a + b
```

Los `int`, `str`, etc. después de `:` son type hints.
FastMCP valida automáticamente que el cliente envíe el tipo correcto.

### Docstrings (Documentación)
```python
@mcp.tool
def mi_tool(x: int) -> int:
    """Esta es la descripción.
    
    Args:
        x: Descripción del parámetro
        
    Returns:
        Descripción del retorno
    """
    return x * 2
```

El docstring se convierte en documentación que ve el cliente.

### Decoradores (Lo importante)
```python
@mcp.tool        # Herramienta ejecutable
@mcp.resource    # Dato de solo lectura
@mcp.prompt      # Instrucción
```

Los decoradores convierten funciones Python normales en componentes MCP.

---

## 🔍 SI ALGO FALLA

### Error: "ModuleNotFoundError: No module named 'fastmcp'"
```bash
pip install fastmcp
python -c "import fastmcp; print('OK')"
```

### Error: "Port already in use"
Otro servidor está usando el puerto 5000. Cambia:
```python
if __name__ == "__main__":
    mcp.run(port=8001)  # Usa otro puerto
```

### Error: "Syntax error"
Copia exactamente el código. No cambies nada aún.

### Error: "Python version"
Necesitas Python 3.11+:
```bash
python --version
```

---

## 🎯 FINAL DE DÍA 1

Cuando termines:

1. ✅ Tienes un servidor ejecutándose
2. ✅ Entiendes MCP y FastMCP
3. ✅ Sabes los 3 pilares
4. ✅ Has creado tu primer servidor propio
5. ✅ Entiendes type hints y docstrings

**Tiempo invertido:** 2-3 horas  
**Progreso:** 14% del curso

---

## 📅 DÍA 2

Mañana aprenderás sobre COMPONENTES:
- Tools en profundidad
- Resources con datos
- Prompts avanzados
- Patrones comunes

Empieza con: `02_componentes/README.md`

---

## 💪 MOTIVACIÓN

Acabas de:
1. Instalar un framework profesional
2. Entender un protocolo complejo
3. Crear tu primer servidor MCP
4. Dominar conceptos avanzados

¡No está mal para un día! 🎉

Mañana aprenderás los 3 tipos de componentes.
Dentro de 2 días tendrás un servidor profesional.
En 7 días será production-ready.

¡Adelante! 🚀
