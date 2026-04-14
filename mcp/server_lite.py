#!/usr/bin/env python3
"""
Prior Art Investigation MCP Server — No external dependencies

Embeds prompts inline (no file dependencies).
Provides three tools: load_minimal, load_full, load_selector.
"""

import json
import sys
from typing import Any, Dict

# ── Inline prompts (zero file dependencies) ──────────────────────────────────

PROMPT_MINIMAL = """
# Prior Art Investigation — Requirements Phase (MINIMAL / Q1+Q6)

> Use when: you have a problem statement and want a quick concept check before design.
> Time: 5-10 min | Tokens: ~150

## Q1: First Principles
- Is the problem statement correct?
- Are we solving the right problem or a surface symptom?
- Reframe in the simplest possible terms (remove jargon).

## Q6: Inversion
- If this fails spectacularly in 6 months, what causes it?
- What core assumptions might be wrong?
- What should we verify **before** proceeding?

Answer both questions concisely for the given feature concept.
""".strip()

PROMPT_FULL = """
# Prior Art Investigation — Design Phase (FULL / Q1-Q7)

> Use when: you are designing an architecture or new subsystem.
> Time: 20-40 min | Tokens: ~500

## Q1: First Principles
- Is the problem statement correct? Simplest reframing.

## Q2: Concept Name
- What is this technically called in the field?
- What established patterns or paradigms apply?

## Q3: Technical Options
- What approaches / algorithms / architectures exist?

## Q4: OSS Ecosystem
For each relevant OSS project (3-5 top options), provide a table with these columns:
- **Tool** — project name
- **License** — MIT, Apache-2.0, GPL, etc. (note commercial-use restrictions if any)
- **Maintainer** — organization (Meta / Google / HF / academic) or individual; signals continuity risk
- **Updated** — actively maintained or stale? (last release cadence)
- **Data Prep Effort** — how much setup / data wrangling before it's usable (Low / Medium / High)
- **Best For** — one-line fit description
- **Source** — GitHub URL or paper link (mandatory — always include)

Note: include additional domain-specific columns if relevant (e.g., cloud cost, language support, inference latency).

## Q5: Architecture Choice
- Which OSS or approach to build on and why?
- Build vs. adopt trade-offs.

## Q6: Inversion
- What failure modes exist? What assumptions might be wrong?

## Q7: Next Steps
- Concrete, prioritized action items to move forward.

Provide thorough investigation across all 7 questions.
""".strip()

PROMPT_SELECTOR = """
# Prior Art Investigation — Selector (auto-route)

> Detect the current development phase and route accordingly.
> Time: 1-2 min | Tokens: ~100

## Phase Detection

Ask the user ONE question:
"Are you in the **Requirements** phase (problem statement, before design) or the **Design** phase (architecture decisions, new subsystem)?"

- **Requirements** → run MINIMAL (Q1+Q6, ~150 tokens, 5-10 min)
- **Design** → run FULL (Q1-Q7, ~500 tokens, 20-40 min)
- **Unsure** → default to MINIMAL first, offer FULL after

Then proceed with the appropriate investigation.
""".strip()

PROMPTS = {
    "load_minimal": PROMPT_MINIMAL,
    "load_full": PROMPT_FULL,
    "load_selector": PROMPT_SELECTOR,
}

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
            
            if tool_name in PROMPTS:
                content = PROMPTS[tool_name]
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
    print("🔧 Tools: load_minimal, load_full, load_selector", file=sys.stderr)
    
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
