#!/usr/bin/env python3
"""
Minimal MCP Server Implementation - No FastMCP dependency

Uses standard library + json-rpc for protocol compatibility.
Can be tested locally and integrated into Claude Desktop.
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict


# Get repo root
REPO_ROOT = Path(__file__).parent.parent
PROMPTS_DIR = REPO_ROOT / "docs" / "en" / "github" / "prompts"


def load_prompt_file(filename: str) -> str:
    """Load prompt file content, handle multiple languages."""
    file_path = PROMPTS_DIR / filename
    if not file_path.exists():
        # Try Japanese version if English not found
        file_path = REPO_ROOT / "docs" / "ja" / "github" / "prompts" / filename
    
    if not file_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {filename}")
    
    return file_path.read_text(encoding="utf-8")


def handle_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """Process JSON-RPC request."""
    method = request.get("method")
    request_id = request.get("id")
    
    try:
        if method == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "tools": [
                        {
                            "name": "load_minimal",
                            "description": "Load MINIMAL prompt (Q1+Q6 only, ~150 tokens, 5-10 min)",
                            "inputSchema": {"type": "object", "properties": {}, "required": []},
                        },
                        {
                            "name": "load_full",
                            "description": "Load FULL prompt (Q1-Q7 complete, ~500 tokens, 20-40 min)",
                            "inputSchema": {"type": "object", "properties": {}, "required": []},
                        },
                        {
                            "name": "load_selector",
                            "description": "Load SELECTOR prompt (auto-router, ~100 tokens, 1-2 min)",
                            "inputSchema": {"type": "object", "properties": {}, "required": []},
                        },
                    ]
                },
            }
        
        elif method == "tools/call":
            tool_name = request.get("params", {}).get("name")
            
            if tool_name == "load_minimal":
                content = load_prompt_file("minimal.prompt.md")
            elif tool_name == "load_full":
                content = load_prompt_file("full.prompt.md")
            elif tool_name == "load_selector":
                content = load_prompt_file("selector.prompt.md")
            else:
                raise ValueError(f"Unknown tool: {tool_name}")
            
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [{"type": "text", "text": content}]
                },
            }
        
        else:
            raise ValueError(f"Unknown method: {method}")
    
    except Exception as e:
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {
                "code": -1,
                "message": str(e),
            },
        }


def main():
    """Start MCP server (stdio protocol)."""
    print("✅ Prior Art Investigation MCP Server started", file=sys.stderr)
    print(f"📂 Prompts directory: {PROMPTS_DIR}", file=sys.stderr)
    print("🔧 Tools available: load_minimal, load_full, load_selector", file=sys.stderr)
    
    # Read JSON-RPC requests from stdin
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            
            request = json.loads(line)
            response = handle_request(request)
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
        
        except json.JSONDecodeError as e:
            print(f"❌ JSON decode error: {e}", file=sys.stderr)
        except Exception as e:
            print(f"❌ Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
