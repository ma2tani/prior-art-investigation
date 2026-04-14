# VS Code Agent Skills セットアップガイド

VS Code Copilot Chat で Prior Art Investigation Framework を Agent Skill として登録します。

---

## 📋 前提条件

- Visual Studio Code (最新版)
- Copilot Chat 拡張機能
- テキストエディター

---

## 🚀 セットアップ手順

### ステップ 1: ファイルをコピー

``.instructions.md`` ファイルを VS Code の Agent Skill 設定ディレクトリにコピーします。

```bash
# macOS
mkdir -p ~/Library/Application\ Support/Code/User/globalStorage/github.copilot-chat/agent-skills
cp .instructions.md ~/Library/Application\ Support/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art-investigation.md

# Linux
mkdir -p ~/.config/Code/User/globalStorage/github.copilot-chat/agent-skills
cp .instructions.md ~/.config/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art-investigation.md

# Windows (PowerShell)
$skillsDir = "$env:APPDATA\Code\User\globalStorage\github.copilot-chat\agent-skills"
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null
Copy-Item ".instructions.md" "$skillsDir\prior-art-investigation.md"
```

### ステップ 2: VS Code を再起動

Copilot Chat の Agent Skill を再度読み込むために VS Code を再起動します。

```bash
code .
```

### ステップ 3: 確認

VS Code で Copilot Chat をオープンし、エージェントが利用可能か確認します（`Cmd+Shift+I`）。

---

## 🧪 使用方法

起動後、以下のコマンドで Agent Skill を実行できます：

### Minimal（最小構成）
```
@prior-art-investigation minimal
```

### Full（完全版）
```
@prior-art-investigation full
```

### Selector（自動選択）
```
@prior-art-investigation selector
```

---

## ✅ トラブルシューティング

### Agent Skill が表示されない

**solution**:
1. ファイルがコピーされているか確認
2. VS Code を完全に再起動
3. Copilot Chat 拡張機能の再インストール

### エラーが多く返される

**solution**:
1. Copilot Chat のバージョンを確認（最新版推奨）
2. `.instructions.md` ファイルが完全か確認
3. 日本語エンコーディングが正しいか確認

---

## 📚 関連ドキュメント

- [README.md](./README.md) — 概要・全体ガイド
- [MCP-SETUP.md](./MCP-SETUP.md) — Claude Desktop 向けセットアップ

---

**バージョン**: 1.0.0  
**Last Updated**: 2026-04
