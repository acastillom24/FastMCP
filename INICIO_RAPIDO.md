# 🚀 INICIO RÁPIDO - FASTMCP EN 7 DÍAS

## 📋 Estructura del Repositorio

```bash
FastMCP/
├── PLAN_APRENDIZAJE.md           ← Empieza aquí
├── pyproject.toml                ← Dependencias
├── main.py                       ← Archivo principal
├── 01_fundamentos/               ← DÍA 1-2
│   ├── README.md                 ← Conceptos teóricos
│   ├── 01_hola_mundo.py         ← Tu primer servidor (10 líneas)
│   ├── 02_conceptos.py          ← Los 3 pilares en acción
│   └── 03_tipos_de_datos.py     ← Validación automática
├── 02_componentes/               ← DÍA 3
├── 03_proveedores/               ← DÍA 4
├── 04_transforms/                ← DÍA 5
├── 05_clientes/                  ← DÍA 6
└── 06_deployment/                ← DÍA 7
```

---

## 🎯 PLAN DIARIO

### DÍA 1-2: FUNDAMENTOS ✅

**Duración:** 2-3 horas  
**Objetivo:** Entender qué es MCP y crear tu primer servidor  

1. Leer: [01_fundamentos/README.md](01_fundamentos/README.md)
2. Ejecutar: `python 01_fundamentos/01_hola_mundo.py`
3. Estudiar: `01_fundamentos/02_conceptos.py`
4. Explorar: `01_fundamentos/03_tipos_de_datos.py`

**Checkpoint:** ¿Puedes crear un servidor con 3 tools diferentes?

---

### DÍA 3: COMPONENTES (Próxima sesión)

**Duración:** 2-3 horas  
**Objetivo:** Dominar tools, resources y prompts  

- Tools simples y complejas
- Resources con datos
- Prompts dinámicos
- Documentación automática

---

### DÍA 4: PROVEEDORES (Próxima sesión)

**Duración:** 2-3 horas  
**Objetivo:** Entender de dónde vienen los componentes  

- Proveedores simples
- Proveedores desde archivos
- Proveedores OpenAPI
- Composición de proveedores

---

### DÍA 5: TRANSFORMACIONES (Próxima sesión)

**Duración:** 2-3 horas  
**Objetivo:** Controlar qué ve cada cliente  

- Namespacing (agrupación)
- Filtrado por cliente
- Autorización (control de acceso)
- Versioning de APIs

---

### DÍA 6: CLIENTES (Próxima sesión)

**Duración:** 2-3 horas  
**Objetivo:** Construir aplicaciones cliente-servidor  

- Cliente FastMCP
- Patrones complejos
- Manejo robusto de errores
- Testing

---

### DÍA 7: DEPLOYMENT (Próxima sesión)

**Duración:** 2-3 horas  
**Objetivo:** Llevar tu proyecto a producción  

- Deployment con Prefect Horizon
- Containerización
- Proyecto final integrado

---

## 💻 INSTALACIÓN (DÍA 1)

### Paso 1: Instalar FastMCP

**Opción A: Con pip** (Recomendado)

```bash
pip install fastmcp
```

**Opción B: Con uv** (Más rápido)

```bash
uv pip install fastmcp
```

**Opción C: Instalar desde el repositorio**

```bash
pip install -e .
```

### Paso 2: Verificar instalación

```bash
python -c "import fastmcp; print(f'✓ FastMCP {fastmcp.__version__}')"
```

Deberías ver: `✓ FastMCP 3.0.0` (o versión similar)

### Paso 3: Ejecutar tu primer servidor

```bash
cd 01_fundamentos
python 01_hola_mundo.py
```

Verás:

```
[INFO] Server started...
[INFO] Ready to handle requests
```

¡Tu primer servidor MCP está corriendo! 🎉

---

## 📚 RECURSOS

- **Documentación Oficial:** <https://gofastmcp.com/>
- **GitHub:** <https://github.com/jlowin/fastmcp>
- **Discord Community:** <https://discord.gg/uu8dJCgttd>
- **Prefect Horizon:** <https://www.prefect.io/horizon> (Hosting gratuito)

---

## 🔑 CONCEPTOS CLAVE

### Model Context Protocol (MCP)

Protocolo que permite conectar LLMs (Claude, GPT) con tus herramientas y datos.

### FastMCP

Framework Python que simplifica la construcción de servidores MCP.

### Los 3 Pilares

1. **Components:** Qué expones (tools, resources, prompts)
2. **Providers:** De dónde vienen (funciones, archivos, APIs)
3. **Transforms:** Qué ven los clientes (filtrado, autorización)

### Validación Automática

FastMCP valida tipos de datos automáticamente. No necesitas escribir código de validación.

---

## ⚠️ TRAMPA COMÚN

❌ **INCORRECTO:** Olvidar el docstring

```python
@mcp.tool
def mi_herramienta(x: int):  # ¡Sin docstring!
    return x * 2
```

✅ **CORRECTO:** Incluir docstring

```python
@mcp.tool
def mi_herramienta(x: int) -> int:
    """Multiplica un número por 2."""
    return x * 2
```

El docstring se convierte en documentación que ven los clientes.

---

## 🎓 FORMATO DE EJEMPLOS

Cada ejemplo tiene:

- 📌 **Conceptos clave** - Qué aprendes
- 💻 **Código ejecutable** - Pruébalo ahora
- 📖 **Explicación línea por línea** - Entiende cada parte
- ⚠️ **Trampa común** - Errores frecuentes
- ✅ **Checkpoint** - Verifica tu comprensión
- 🚀 **Reto** - Ejercicio de práctica

---

## ✅ CHECKLIST DÍA 1-2

- [ ] FastMCP instalado y verificado
- [ ] Leído `01_fundamentos/README.md`
- [ ] Ejecutado `01_hola_mundo.py`
- [ ] Entendido los 3 pilares
- [ ] Ejecutado `02_conceptos.py`
- [ ] Ejecutado `03_tipos_de_datos.py`
- [ ] Creado tu propio servidor con 3 tools
- [ ] Pasado el checkpoint de DÍA 2

---

## 🆘 SI TIENES PROBLEMAS

### "ModuleNotFoundError: No module named 'fastmcp'"

```bash
pip install fastmcp
```

### "Python version must be 3.11 or higher"

```bash
python --version  # Verifica tu versión
# Si es < 3.11, instala Python 3.11+
```

### "Port already in use"

FastMCP intenta usar un puerto que ya está ocupado. Cambia el puerto:

```python
mcp.run(port=8001)  # Usa puerto 8001 en lugar de 8000
```

### "What's the difference between a Tool and Resource?"

- **Tool:** Función que EL CLIENTE EJECUTA (acción)
- **Resource:** Datos que EL CLIENTE LEE (información)

---

## 🎬 PRÓXIMOS PASOS

Cuando termines DÍA 1-2:

1. ✅ Comprueba el checklist anterior
2. 📖 Lee `PLAN_APRENDIZAJE.md` para el flujo completo
3. 📅 Dedica 2-3 horas por día para los próximos 5 días
4. 💬 Únete al Discord para preguntas
5. 🚀 Al final del DÍA 7 tendrás un proyecto production-ready

---

## 💬 PREGUNTAS FRECUENTES

**P: ¿Cuánto tiempo toma aprender FastMCP?**  
R: Con este curso, 7 días dedicando 2-3 horas por día. Depende de tu experiencia con Python.

**P: ¿Necesito conocer MCP antes?**  
R: No, este curso comienza desde cero.

**P: ¿Puedo deployar FastMCP en AWS/Google Cloud?**  
R: Sí, pero es más fácil con Prefect Horizon (gratuito para usuarios de FastMCP).

**P: ¿FastMCP es solo para Claude?**  
R: No, funciona con cualquier cliente MCP (Claude, GPT, etc.).

---

¡Bienvenido al viaje de FastMCP! 🚀

Empieza con los comandos de instalación arriba. Cualquier pregunta, mira la documentación oficial o el Discord.

**¡A aprender!** 🎓
