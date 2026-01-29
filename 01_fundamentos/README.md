# DÍA 1-2: FUNDAMENTOS DE FASTMCP

## 📌 ¿Qué es Model Context Protocol (MCP)?

MCP es un protocolo abierto que permite:
- 🔌 **Conectar** modelos de IA (Claude, GPT, etc.) con herramientas tuyas
- 📊 **Compartir** datos y recursos de forma segura
- 🎯 **Controlar** exactamente qué expones a cada usuario/cliente
- 🔄 **Comunicación bidireccional** entre cliente y servidor

## 📌 ¿Por qué FastMCP?

Sin FastMCP, construir un servidor MCP requiere:
- ✗ Manejo manual de serialización/deserialización JSON
- ✗ Validación compleja de esquemas
- ✗ Implementación del protocolo MCP completo
- ✗ Manejo de errores y edge cases
- ✗ Documentación y generación de esquemas

Con FastMCP:
- ✅ Decoradores simples (como Flask/FastAPI)
- ✅ Validación automática
- ✅ Protocolo manejado automáticamente
- ✅ Esquemas generados dinámicamente
- ✅ Documentación automática

## 📌 Los 3 Pilares de FastMCP

### 1. **COMPONENTS** (Qué expones)
Son los elementos que tu servidor ofrece:
- **Tools:** Funciones que el cliente puede ejecutar
- **Resources:** Datos o archivos que el cliente puede acceder
- **Prompts:** Instrucciones predefinidas para usar tu servidor

```python
@mcp.tool
def mi_herramienta(param: str) -> str:
    """Descripción de qué hace"""
    return f"Resultado: {param}"

@mcp.resource
def mi_recurso() -> str:
    """Descripción del recurso"""
    return "datos importantes"

@mcp.prompt
def mi_prompt(nombre: str) -> str:
    """Instrucción para el usuario"""
    return f"Hola {nombre}, aquí está la guía..."
```

### 2. **PROVIDERS** (De dónde vienen)
Especifican cómo se crean los componentes:
- Funciones decoradas (lo más común)
- Archivos en disco
- Especificaciones OpenAPI
- Servidores MCP remotos
- Fuentes dinámicas

```python
# Provider simple: decorador
@mcp.tool
def herramienta():
    return "datos"

# Provider complejo: desde archivos
from fastmcp.providers import FileProvider
provider = FileProvider(path="/mi/ruta")
```

### 3. **TRANSFORMS** (Qué ven los clientes)
Modifican qué ve cada cliente:
- **Namespacing:** Agrupar herramientas por categoría
- **Filtering:** Mostrar solo ciertas herramientas a ciertos usuarios
- **Authorization:** Control de acceso
- **Versioning:** Diferentes versiones del API

```python
# Un servidor presenta diferente según el cliente
if cliente == "admin":
    exponer_todas_herramientas()
else:
    exponer_herramientas_publicas()
```

---

## 🚀 INSTALACIÓN

### Opción 1: Con pip (Recomendado)
```bash
pip install fastmcp
```

### Opción 2: Con uv (Más rápido)
```bash
uv pip install fastmcp
```

### Opción 3: Desde source (Desarrollo)
```bash
git clone https://github.com/jlowin/fastmcp.git
cd fastmcp
pip install -e .
```

### Verificar instalación
```bash
python -c "import fastmcp; print(fastmcp.__version__)"
```

---

## 💻 Tu Primer Servidor MCP

¡Ahora vamos a crear tu primer servidor en 10 líneas!

Mira el archivo: `01_hola_mundo.py`

---

## ✅ CHECKPOINT 1 - CONCEPTOS

Antes de continuar, responde:

1. ¿Qué diferencia hay entre MCP y FastMCP?
   - MCP es el protocolo, FastMCP es el framework que lo simplifica

2. ¿Cuáles son los 3 pilares?
   - Components (qué), Providers (de dónde), Transforms (qué ven)

3. ¿Qué es un Tool?
   - Una función que expones para que el cliente la ejecute

4. ¿Para qué sirven los Transforms?
   - Para controlar qué ve cada cliente (filtrado, autorización, etc.)

---

## 🚀 RETO 1

Antes de ir a ejemplos más complejos, trata de:
1. Instalar FastMCP
2. Crear un servidor simple con 2 tools
3. Ejecutarlo y ver la salida

