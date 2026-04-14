# Claude Desktop に MCP サーバーをセットアップする

Prior Art Investigation Framework を Claude Desktop の Model Context Protocol (MCP) サーバーとして設定します。

---

## 📋 前提条件

- Claude Desktop インストール済み
- Python 3.6+
- テキストエディター

---

## 🚀 セットアップ手順

### ステップ 1: リポジトリをクローン

```bash
git clone https://github.com/ma2tani/prior-art-investigation.git
cd prior-art-investigation
```

### ステップ 2: MCP 設定ファイルを準備

Claude Desktop は MCP サーバーを `claude_desktop_config.json` で設定します。

**macOS/Linux**:
```bash
nano ~/.claude/claude_desktop_config.json
```

**Windows**:
```powershell
notepad $env:APPDATA\Claude\claude_desktop_config.json
```

### ステップ 3: 設定を追加

既存の設定に以下を追加（リポジトリパスを調整）：

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

### ステップ 4: Claude Desktop を再起動

MCP サーバーをリロードするため Claude を再起動します。

```bash
# macOS
pkill -f "Claude"
open /Applications/Claude.app

# Linux
pkill -f claude-app

# Windows
taskkill /IM claude.exe /F
```

### ステップ 5: 確認

Claude のチャットウィンドウで以下を確認：

1. **ツールメニュー** をクリック
2. **MCP サーバー** セクションを展開
3. **prior-art-investigation** が表示されていることを確認
4. テストコール：
```
Call @prior-art-investigation selector
```

---

## 🧪 トラブルシューティング

### MCP サーバーが接続されない

**確認事項**:
1. JSON 設定ファイルのパスが正しいか
2. Python 3.6+ がインストールされているか
3. スクリプトファイル権限を確認：
```bash
chmod +x /path/to/prior-art-investigation/mcp/server_lite.py
```

### ツールが表示されない

**solution**:
1. Claude Desktop ログを確認（Console.app で「Claude」検索）
2. MCP サーバーが起動しているか確認：
```bash
python3 /path/to/prior-art-investigation/mcp/server_lite.py
```

### エラーメッセージが出る

**common causes**:
- Python パスが不正
- ファイルパスに空白が含まれている（クォート処理が必要）
- MCP サーバーのプロセス起動失敗

**対処法**:
```bash
# Python パスを確認
which python3

# プロセスが起動するか test
python3 /path/to/.../server_lite.py
```

---

## 🔍 MCP サーバーの仕組み

MCP サーバーは以下の 3 つのツールを提供します：

| ツール | 説明 | Token 数 |
|--------|------|---------|
| **load_minimal** | 最小限の Q&A セット | 150 |
| **load_full** | 完全な質問集 | 500 |
| **load_selector** | 自動ルーター | 100 |

---

## 📚 関連ドキュメント

- [README.md](./README.md) — 概要・全体ガイド
- [AGENT-SKILLS-SETUP.md](./AGENT-SKILLS-SETUP.md) — VS Code 向けセットアップ

---

**バージョン**: 1.0.0  
**Protocol**: JSON-RPC 2.0  
**Last Updated**: 2026-04
