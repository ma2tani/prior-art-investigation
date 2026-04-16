# セットアップガイド

Prior Art Investigation Framework のインストール方法を、使いたいツールに応じて選んでください。

---

## クイックスタート（推奨）

```bash
git clone https://github.com/as-we/prior-art-investigation
cd prior-art-investigation
make install
```

これだけで **第1層（Agent Skills）+ 第2層（自動検知フック）** が両方インストールされます。

---

## A. VS Code Copilot Chat — Agent Skills

### インストール

```bash
make install-skills
```

または手動：

```bash
# macOS
cp .instructions.md \
  ~/Library/Application\ Support/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art-investigation.md

# Linux
cp .instructions.md \
  ~/.config/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art-investigation.md

# Windows (PowerShell)
$dir = "$env:APPDATA\Code\User\globalStorage\github.copilot-chat\agent-skills"
New-Item -ItemType Directory -Force -Path $dir | Out-Null
Copy-Item ".instructions.md" "$dir\prior-art-investigation.md"
```

VS Code を再起動して反映。

### 使い方

```
@prior-art-investigation minimal  API のレート制限を実装したい
@prior-art-investigation full     分散キャッシュのアーキテクチャを設計したい
@prior-art-investigation selector ← どちらか迷ったとき、自動振り分け
```

> **なぜ `.instructions.md`（英語版）を使うのか**  
> Agent Skills はそのままLLMへのプロンプトとして送信されます。英語の方がトークン数が少なく（同内容で約20〜30%削減）、GPT/Claude いずれも英語プロンプトの方が調査精度が高いため、英語版を推奨します。日本語での回答が必要な場合は、呼び出し時に「日本語で回答して」と付け加えるか、以下のように使います。  
> ```
> @prior-art-investigation full LLMを使った知識蒸留の設計 (回答は日本語で)
> ```

### トラブルシューティング

| 症状 | 対処 |
|------|------|
| エージェントが表示されない | ファイルのコピー確認 → VS Code を完全再起動 |
| エラーが返る | Copilot Chat を最新版に更新 |

---

## B. 自動検知フック（VS Code / UserPromptSubmit）

### インストール

```bash
make install-hook
```

VS Code 設定に追加：

```json
"chat.hookFilesLocations": { "~/.copilot/hooks": true }
```

### 動作

設計・実装に関係するプロンプトを送ると、自動でリマインダーが1行挿入されます：

> 💡 Prior art check recommended: this looks like a design or implementation decision...

フックは `~/.copilot/hooks/` に配置されるため、**プロジェクトのファイルを汚しません**。

### アンインストール

```bash
make uninstall
# または手動
rm ~/.copilot/hooks/prior-art-detect.json
rm ~/.copilot/hooks/scripts/prior-art-detect.sh
```

---

## C. Claude Desktop（MCP サーバー）

### インストール

`~/.claude/claude_desktop_config.json`（Windows: `%APPDATA%\Claude\claude_desktop_config.json`）に追加：

```json
{
  "mcpServers": {
    "prior-art-investigation": {
      "command": "python3",
      "args": ["/path/to/prior-art-investigation/mcp/server_lite.py"]
    }
  }
}
```

Claude Desktop を再起動。

### 使えるツール

| ツール | 用途 |
|--------|------|
| `load_minimal` | Q1+Q6 のみ — 要件定義フェーズ向け |
| `load_full` | Q1-Q8 全体 — 設計フェーズ向け |
| `load_selector` | 自動振り分け |

### トラブルシューティング

```bash
# Python パスの確認
which python3

# サーバーが単体で起動するか確認
python3 /path/to/prior-art-investigation/mcp/server_lite.py

# ファイル権限確認
chmod +x /path/to/prior-art-investigation/mcp/server_lite.py
```

Claude Desktop ログ（macOS: Console.app で「Claude」検索）も確認してください。

---

## D. Kiro IDE — フック・パーソナリティ

```bash
cp -r .kiro/hooks /your-project/.kiro/
cp -r .kiro/personalities /your-project/.kiro/
```

要件定義（`/kiro-spec-requirements`）・設計（`/kiro-spec-design`）フェーズで自動的に先行技術調査が実行されます。

---

## E. VS Code カスタムエージェント（プロジェクト単位）

チームでリポジトリに設定を含めたい場合：

```bash
mkdir -p .github/agents
cp path/to/prior-art-investigation/.github/agents/prior-art.agent.md .github/agents/
```

Copilot Chat のエージェントドロップダウンから **Prior Art Investigation** を選択。

---

## 調査の内容について

Q1〜Q8 の詳細（各質問の意図・サンプル出力）は [QUESTIONS.md](./QUESTIONS.md) を参照してください。
