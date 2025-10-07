# Test MCP Server

A sample MCP (Model Context Protocol) server with three tools that fetch data from public APIs.

## Features

This server provides three tools:
- **get_quote**: Fetches random inspirational quotes
- **get_joke**: Fetches random programming jokes
- **get_advice**: Fetches random advice

## Installation

1. Clone this repository or download the files
2. Install dependencies:

```bash
pip install -r requirements.txt
```

Or using the package:

```bash
pip install -e .
```

## Usage

### With Claude Desktop

Add this configuration to your Claude Desktop config file:

**MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "test-mcp-server": {
      "command": "python",
      "args": ["/absolute/path/to/test-mcp/src/test_mcp_server.py"]
    }
  }
}
```

Replace `/absolute/path/to/test-mcp/` with the actual path to this directory.

### Running Standalone

You can also run the server directly:

```bash
python src/test_mcp_server.py
```

The server communicates via stdio and follows the MCP protocol.

## Requirements

- Python 3.10+
- mcp >= 1.0.0
- aiohttp >= 3.9.0

## Development

To modify or extend this server:

1. Edit `src/test_mcp_server.py`
2. Add new tools in the `list_tools()` function
3. Implement tool handlers in the `call_tool()` function

## License

MIT
