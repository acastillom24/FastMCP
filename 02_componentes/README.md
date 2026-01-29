# DÍA 3: COMPONENTES - TOOLS, RESOURCES, PROMPTS

## 📌 ¿Qué son los componentes?

Los componentes son los elementos que tu servidor MCP **EXPONE** a los clientes:

| Componente | Tipo | Descripción | Ejemplo |
|-----------|------|-------------|---------|
| **Tool** | Acción | Función que el cliente EJECUTA | Calcular suma |
| **Resource** | Lectura | Datos que el cliente LEE | Archivo de config |
| **Prompt** | Instrucción | Guía reutilizable para el cliente | "Cómo usar..." |

---

## 1️⃣ TOOLS - Las Herramientas

### ¿Qué es un Tool?
- Función que el **cliente puede EJECUTAR**
- Acepta argumentos
- Retorna resultados
- Se valida automáticamente

### Sintaxis Basic
```python
@mcp.tool
def mi_herramienta(parametro: str) -> str:
    """Descripción de qué hace.
    
    Args:
        parametro: Descripción del parámetro
        
    Returns:
        Descripción del retorno
    """
    return f"Resultado: {parametro}"
```

### Ejemplo Real - Ver: `01_tools_simples.py`

---

## 2️⃣ RESOURCES - Los Recursos

### ¿Qué es un Resource?
- Datos que el **cliente puede LEE**R
- NO son ejecutables
- Útil para datos, archivos, estado del sistema
- Se comportan como endpoints de solo lectura

### Sintaxis Básica
```python
@mcp.resource
def mi_recurso() -> str:
    """Descripción del recurso.
    
    Returns:
        El contenido del recurso
    """
    return "Datos importantes"
```

### Ejemplo Real - Ver: `02_resources.py`

---

## 3️⃣ PROMPTS - Las Instrucciones

### ¿Qué es un Prompt?
- Instrucciones reutilizables
- El cliente puede invocarlo
- Útil para flujos complejos, guías, templates
- Similar a una herramienta pero enfocada en texto

### Sintaxis Básica
```python
@mcp.prompt
def mi_instruccion(parametro: str) -> str:
    """Descripción de la instrucción.
    
    Args:
        parametro: Parámetro de entrada
        
    Returns:
        La instrucción formateada
    """
    return f"Instrucción para {parametro}"
```

### Ejemplo Real - Ver: `03_prompts.py`

---

## 🎯 Checklist DÍA 3

- [ ] Entendido la diferencia entre Tools, Resources, Prompts
- [ ] Ejecutado `01_tools_simples.py`
- [ ] Ejecutado `01_tools_complejas.py`
- [ ] Ejecutado `02_resources.py`
- [ ] Ejecutado `03_prompts.py`
- [ ] Creado tus propios componentes
- [ ] Pasado el reto de DÍA 3

---

## 🚀 Reto DÍA 3

Crea un servidor con:
- ✅ 3 Tools (calcular, buscar, procesar)
- ✅ 2 Resources (status, config)
- ✅ 2 Prompts (guía, template)

Entonces deberías poder ver 7 componentes expuestos.
