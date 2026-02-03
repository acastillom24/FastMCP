import asyncio

from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_tools(*tool_calls):
    """
    Llama múltiples tools de forma secuencial
    tool_calls: tuplas de (nombre_tool, argumentos_dict)
    """
    async with client:
        results = []
        for tool_name, args in tool_calls:
            result = await client.call_tool(tool_name, args)
            results.append(result.data)
            print(f"{tool_name}: {result.data}")
        return results
    
async def ejecutar_servidor():
    client = Client("http://localhost:8000/mcp")
    
    async with client:
        # Definir qué es tool y qué es resource
        tools = [
            ("multiplicar", {"a": 3, "b": 5}),
            ("dividir", {"dividendo": 10, "divisor": 2}),
        ]
        
        resources = [
            "config://sistema"
        ]
        
        prompts = [
            "guia_uso"
        ]
        
        # Ejecutar tools
        print("=== TOOLS ===")
        for tool_name, args in tools:
            result = await client.call_tool(tool_name, args)
            print(f"{tool_name}: {result.data}")
        
        # Leer resources
        print("\n=== RESOURCES ===")
        for resource_uri in resources:
            result = await client.read_resource(resource_uri)
            print(f"{resource_uri}: {result[0].text}")
            
        # Obtener prompt
        print("\n=== PROMPTS ===")
        for prompt_name in prompts:
            prompt = await client.get_prompt(prompt_name)
            print(f"{prompt_name}:\n{prompt.messages[0].content.text}")

# asyncio.run(call_tools(
#     ("multiplicar", {"a": 5, "b": 3}),
#     ("dividir", {"dividendo": 10, "divisor": 2}),
# ))

asyncio.run(ejecutar_servidor())