#!/usr/bin/env python3
"""
Test MCP Server with 10 sample tools
"""
import asyncio
import json
from typing import Any
import aiohttp
from mcp.server import Server
from mcp.types import Tool, TextContent
from mcp.server.stdio import stdio_server

app = Server("test-mcp-server")

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools"""
    return [
        Tool(
            name="get_quote",
            description="Get a random inspirational quote from an API",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_joke",
            description="Get a random programming joke from an API",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_advice",
            description="Get random advice from an API",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls"""

    if name == "get_quote":
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.quotable.io/random") as response:
                    if response.status == 200:
                        data = await response.json()
                        quote = data.get("content", "")
                        author = data.get("author", "Unknown")
                        return [TextContent(type="text", text=f'"{quote}" - {author}')]
                    else:
                        return [TextContent(type="text", text=f"Error: API returned status {response.status}")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error fetching quote: {str(e)}")]

    elif name == "get_joke":
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://official-joke-api.appspot.com/random_joke") as response:
                    if response.status == 200:
                        data = await response.json()
                        setup = data.get("setup", "")
                        punchline = data.get("punchline", "")
                        return [TextContent(type="text", text=f"{setup}\n{punchline}")]
                    else:
                        return [TextContent(type="text", text=f"Error: API returned status {response.status}")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error fetching joke: {str(e)}")]

    elif name == "get_advice":
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.adviceslip.com/advice") as response:
                    if response.status == 200:
                        data = await response.json()
                        advice = data.get("slip", {}).get("advice", "")
                        return [TextContent(type="text", text=f"Advice: {advice}")]
                    else:
                        return [TextContent(type="text", text=f"Error: API returned status {response.status}")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error fetching advice: {str(e)}")]

    else:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]

async def main():
    """Run the MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
