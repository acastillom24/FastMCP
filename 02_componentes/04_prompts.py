"""
DÍA 3: COMPONENTES - PROMPTS (Instrucciones)
═══════════════════════════════════════════════════════════════════

Los Prompts son instrucciones reutilizables.
Son como plantillas o guías que el cliente puede invocar.

Tools = Acción (ejecuta)
Resources = Lectura (obtiene datos)
Prompts = Guía (instrucciones)
"""

from fastmcp import FastMCP

mcp = FastMCP("Prompts - DÍA 3 📝")

# ═══════════════════════════════════════════════════════════════════
# PROMPTS SIMPLES - SIN PARÁMETROS
# ═══════════════════════════════════════════════════════════════════

@mcp.prompt
def guia_inicio() -> str:
    """Guía de inicio rápido para principiantes.
    
    Returns:
        Una guía paso a paso
    """
    return """
╔════════════════════════════════════════════════════════╗
║              GUÍA DE INICIO RÁPIDO                     ║
╚════════════════════════════════════════════════════════╝

PASO 1: EXPLORA
--------
¿Qué recursos hay disponibles?
- Usa el resource 'obtener_documentacion' para ver la documentación
- Usa el resource 'obtener_estado_servidor' para ver el estado
- Usa el resource 'obtener_configuracion_servidor' para ver config

PASO 2: EXPERIMENTA
--------
¿Qué puedes hacer?
- Ejecuta algunas tools: calcular_suma(5, 3)
- Consulta datos con resources
- Invoca prompts para obtener instrucciones

PASO 3: APRENDE
--------
¿Cómo aprender más?
1. Lee toda la documentación (muy importante)
2. Consulta los ejemplos proporcionados
3. Experimenta con diferentes combinaciones
4. Revisa los tipos de datos esperados

PASO 4: INTEGRA
--------
¿Cómo construir algo real?
1. Combina tools con resources
2. Usa prompts como guías
3. Automatiza tareas frecuentes
4. ¡Comparte tus resultados!

¡Adelante! 🚀
"""


@mcp.prompt
def mejores_practicas() -> str:
    """Mejores prácticas para usar este servidor.
    
    Returns:
        Recomendaciones de mejores prácticas
    """
    return """
╔════════════════════════════════════════════════════════╗
║              MEJORES PRÁCTICAS                         ║
╚════════════════════════════════════════════════════════╝

1. NOMBRA BIEN TUS CONSULTAS
   ❌ No hagas: query(1)
   ✅ Haz:     obtener_usuarios_activos()
   
   Las funciones bien nombradas son self-documented.

2. VALIDA SIEMPRE LOS INPUTS
   ❌ No hagas: procesar_datos(x)  # x es cualquier cosa
   ✅ Haz:     procesar_datos(x: int)  # Type hints
   
   FastMCP valida automáticamente los tipos.

3. USA DOCSTRINGS COMPLETOS
   ❌ No hagas: 
       @mcp.tool
       def mi_tool(x):
           return x
   
   ✅ Haz:
       @mcp.tool
       def mi_tool(x: int) -> int:
           \"\"\"Descripción clara.
           
           Args:
               x: Descripción del parámetro
           
           Returns:
               Descripción del retorno
           \"\"\"
           return x

4. MANEJA ERRORES ELEGANTEMENTE
   ❌ No hagas:
       return None  # El cliente no sabe qué salió mal
   
   ✅ Haz:
       if valor < 0:
           raise ValueError("El valor debe ser positivo")

5. RETORNA DATOS ESTRUCTURADOS
   ❌ No hagas:
       return f"El resultado es {resultado}"  # String puro
   
   ✅ Haz:
       return {"status": "ok", "resultado": resultado}

6. DOCUMENTA EJEMPLOS
   ✅ Incluye ejemplos en docstrings
       Example:
           mi_tool(5) retorna 10

7. AGRUPA FUNCIONALIDADES
   ❌ No hagas:
       @mcp.tool
       def hacer_todo(): pass
   
   ✅ Haz:
       @mcp.tool
       def crear_usuario(): pass
       
       @mcp.tool
       def actualizar_usuario(): pass
       
       @mcp.tool
       def eliminar_usuario(): pass

8. MANTÉN LAS TOOLS SIMPLES
   Si una tool hace más de una cosa, divídela.
   Una tool = Una responsabilidad
"""


# ═══════════════════════════════════════════════════════════════════
# PROMPTS CON PARÁMETROS
# ═══════════════════════════════════════════════════════════════════

@mcp.prompt
def guia_bienvenida(nombre: str) -> str:
    """Crea una guía personalizada de bienvenida.
    
    Args:
        nombre: El nombre de la persona a saludar
        
    Returns:
        Una guía personalizada
        
    Example:
        guia_bienvenida("Juan") retorna guía para Juan
    """
    return f"""
╔════════════════════════════════════════════════════════╗
║         ¡BIENVENIDO, {nombre.upper()}!                   ║
╚════════════════════════════════════════════════════════╝

Hola {nombre}, nos alegra mucho que te unas a nosotros.

En los próximos pasos te mostraremos:

1. CÓMO USAR LAS HERRAMIENTAS
   Cada tool puede aceptar parámetros y retorna resultados.
   Ejemplo: sumar(5, 3) te da 8

2. CÓMO CONSULTAR RECURSOS
   Los resources son datos que puedes leer.
   Ejemplo: obtener_documentacion() te da la guía

3. CÓMO USAR PROMPTS
   Los prompts son instrucciones como esta.
   Ayudan a entender cómo usar el servidor.

4. CÓMO COMBINAR TODO
   Las herramientas poderosas combinan tools + resources.

Un consejo: Siempre lee el docstring de cada componente.
Contiene toda la información que necesitas.

¡Que disfrutes explorando! 🎉
"""


@mcp.prompt
def template_bug_report(titulo: str, descripcion: str) -> str:
    """Crea un reporte de bug bien formateado.
    
    Args:
        titulo: Título breve del bug
        descripcion: Descripción detallada
        
    Returns:
        Reporte de bug formateado
        
    Example:
        template_bug_report(
            "Error en validación",
            "La función valida_email rechaza emails válidos"
        )
    """
    from datetime import datetime
    
    return f"""
════════════════════════════════════════════════════════
REPORTE DE BUG
════════════════════════════════════════════════════════

Título: {titulo}

Fecha del reporte: {datetime.now().strftime('%d/%m/%Y %H:%M')}

Descripción:
-----------
{descripcion}

Pasos para reproducir:
---------------------
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

Comportamiento esperado:
------------------------
[Qué debería ocurrir]

Comportamiento actual:
-----------------------
[Qué está ocurriendo]

Entorno:
--------
- Versión: 3.0.0
- Sistema Operativo: [Tu SO]
- Python: 3.11+

Adjuntos:
---------
[Incluye logs, screenshots, etc.]

════════════════════════════════════════════════════════
"""


@mcp.prompt
def template_solicitud_feature(feature: str, razon: str) -> str:
    """Crea una solicitud de nueva funcionalidad.
    
    Args:
        feature: Qué funcionalidad solicitas
        razon: Por qué la necesitas
        
    Returns:
        Solicitud bien formateada
    """
    return f"""
════════════════════════════════════════════════════════
SOLICITUD DE NUEVA FUNCIONALIDAD
════════════════════════════════════════════════════════

Funcionalidad solicitada:
------------------------
{feature}

Razón / Caso de uso:
-------------------
{razon}

Beneficio:
----------
[Qué mejorará esto]

Impacto:
--------
[Afecta a qué usuarios]

Prioridad:
----------
[ ] Baja
[ ] Media
[ ] Alta
[ ] Crítica

Alternativas consideradas:
--------------------------
[Otras formas de resolver esto]

Contexto adicional:
-------------------
[Información extra relevante]

════════════════════════════════════════════════════════
"""


# ═══════════════════════════════════════════════════════════════════
# PROMPTS CON INSTRUCCIONES TÉCNICAS
# ═══════════════════════════════════════════════════════════════════

@mcp.prompt
def guia_debugging() -> str:
    """Guía para debuggear problemas comunes.
    
    Returns:
        Pasos para resolver problemas
    """
    return """
╔════════════════════════════════════════════════════════╗
║              GUÍA DE DEBUGGING                         ║
╚════════════════════════════════════════════════════════╝

PROBLEMA: "Mi tool retorna error"
SOLUCIÓN:
  1. Verifica que pasas los tipos correctos
  2. Revisa el docstring de la tool
  3. Consulta los logs del servidor
  4. Intenta con valores simples primero

PROBLEMA: "No veo mi nuevo tool"
SOLUCIÓN:
  1. Reinicia el servidor
  2. Verifica que tiene el decorador @mcp.tool
  3. Comprueba que hay docstring
  4. Revisa que no haya errores de sintaxis

PROBLEMA: "El resource retorna datos extraños"
SOLUCIÓN:
  1. Verifica que retorna un string
  2. Si es JSON, valida que sea JSON válido
  3. Prueba obtener_estado_servidor() para verificar
  4. Revisa los logs

PROBLEMA: "La validación rechaza mis datos"
SOLUCIÓN:
  1. Verifica los type hints del parámetro
  2. Asegúrate de pasar el tipo correcto
  3. Para int, no envíes "5", envía 5
  4. Para list, usa [1, 2, 3], no 1, 2, 3

HERRAMIENTAS DE DEBUG:
  • obtener_estado_servidor() - Ver logs actuales
  • obtener_cambios_recientes() - Ver qué cambió
  • validar_email() - Validar datos individuales
  • simular_consulta_bd() - Simular operaciones

ÚLTIMA OPCIÓN:
  Consulta la documentación en https://gofastmcp.com/
"""


@mcp.prompt
def checklist_antes_produccion() -> str:
    """Checklist antes de deployar a producción.
    
    Returns:
        Lista de verificación completa
    """
    return """
╔════════════════════════════════════════════════════════╗
║           CHECKLIST - ANTES DE PRODUCCIÓN              ║
╚════════════════════════════════════════════════════════╝

CÓDIGO
  [ ] Todos los type hints están presentes
  [ ] Todos los docstrings son completos
  [ ] El código sigue PEP 8 (Python style)
  [ ] No hay variables no utilizadas
  [ ] Los nombres son descriptivos
  [ ] El código está comentado donde es complejo

ERRORES & VALIDACIÓN
  [ ] Manejo de errores en todas las tools
  [ ] Validación de inputs
  [ ] Mensajes de error claros
  [ ] Logs de todas las operaciones importantes

TESTING
  [ ] Probé todas las tools con entrada válida
  [ ] Probé con entrada inválida
  [ ] Probé edge cases (valores 0, negativos, muy grandes)
  [ ] Probé con listas vacías si corresponde
  [ ] Probé la concurrencia (múltiples clientes)

DOCUMENTACIÓN
  [ ] README.md actualizado
  [ ] Docstrings completos
  [ ] Ejemplos de uso
  [ ] Troubleshooting común

SEGURIDAD
  [ ] No hay secretos en el código
  [ ] Inputs están validados
  [ ] No hay SQL injection
  [ ] Autenticación habilitada
  [ ] Rate limiting configurado

RENDIMIENTO
  [ ] Las tools son rápidas (< 1 segundo)
  [ ] Monitoreo está activado
  [ ] Logs no son excesivos
  [ ] Memoria está bajo control

DEPLOYMENT
  [ ] Docker image probada
  [ ] Variables de ambiente configuradas
  [ ] Base de datos respaldada
  [ ] Rollback plan preparado
  [ ] Monitoreo configurado

¡Si todo está en ✓, estás listo para producción! 🚀
"""


# ═══════════════════════════════════════════════════════════════════
# EJECUCIÓN
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════╗
║      PROMPTS - EJEMPLO 04 DE COMPONENTES              ║
╚════════════════════════════════════════════════════════╝

PROMPTS DISPONIBLES (Instrucciones):

📚 GUÍAS:
  • guia_inicio()
  • mejores_practicas()
  • guia_debugging()
  • checklist_antes_produccion()

👋 PERSONALIZADO:
  • guia_bienvenida(nombre)

📋 TEMPLATES:
  • template_bug_report(titulo, descripcion)
  • template_solicitud_feature(feature, razon)

Iniciando servidor...
""")
    
    mcp.run()


# ═══════════════════════════════════════════════════════════════════
# CUÁNDO USAR PROMPTS 🎯
# ═══════════════════════════════════════════════════════════════════

"""
PROMPTS SON ÚTILES PARA:

✅ Guías paso a paso
   guia_inicio() → pasos para empezar

✅ Plantillas reutilizables
   template_bug_report() → formulario de bug

✅ Instrucciones complejas
   mejores_practicas() → reglas y consejos

✅ Información contextual
   checklist_antes_produccion() → verificaciones

✅ Mensajes personalizados
   guia_bienvenida(nombre) → saludo personalizado

NO USES PROMPTS PARA:
  ❌ Cálculos → Usa TOOLS
  ❌ Datos dinámicos → Usa RESOURCES
  ❌ Cambiar estado → Usa TOOLS
  ❌ Parámetros complejos → Usa TOOLS

PROMPTS == INSTRUCCIONES PARA EL USUARIO
TOOLS == ACCIONES QUE EJECUTAS
RESOURCES == DATOS QUE CONSULTAS
"""
