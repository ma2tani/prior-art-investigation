#!/bin/bash
# prior-art-detect.sh
# Fires on UserPromptSubmit. Injects a lightweight reminder when the prompt
# looks like a design/architecture decision — no LLM judgment needed.
#
# Install: copy this script to ~/.copilot/hooks/scripts/prior-art-detect.sh
#          chmod +x ~/.copilot/hooks/scripts/prior-art-detect.sh
#
# Vocabulary matched (English + Japanese):
#   design, architecture, implement, spec, requirements, kiro-spec
#   設計, 実装, 要件, アーキテクチャ, 仕様

set -euo pipefail

INPUT=$(cat)
PROMPT=$(python3 -c "
import json, sys
data = json.load(sys.stdin)
print(data.get('prompt', ''))
" <<< "$INPUT" 2>/dev/null || echo "")

# Match design / architecture / spec activity in either language
if echo "$PROMPT" | grep -qiE \
  '/kiro-spec|spec-design|spec-requirement|spec-tasks|design\.md|requirements\.md|tasks\.md|architecture|implement|設計|実装|要件|アーキテクチャ|仕様'; then

  python3 -c "
import json
out = {
  'hookSpecificOutput': {
    'hookEventName': 'UserPromptSubmit',
    'additionalContext': (
      '💡 Prior art check recommended: this looks like a design or implementation decision. '
      'Before building, consider running: @prior-art full <your topic>  '
      '(checks concept names, OSS options, platform-native features, failure modes)'
    )
  }
}
print(json.dumps(out))
"
fi
# No output = no injection (hook is silent for unrelated prompts)
