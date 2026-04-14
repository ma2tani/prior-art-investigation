# 先行技術調査フレームワーク

コードを書く前に、機能の概念名・既存パターン・OSS を素早く特定する。

**[English](../en/README.md)**

---

## 何ができるか

機能を設計するとき、こんな問いに答える：

- 「この機能、すでに名前がついてる概念じゃないか？」→ 技術的な概念名を特定
- 「参考にできる OSS はあるか？」→ 既存ソリューションをリストアップ
- 「何が失敗しやすいか？」→ よくある落とし穴と前提条件を明確化

使用するタイミングは **要件定義・設計フェーズの冒頭**。

| モード | 使いどき | 時間 | トークン |
|--------|----------|------|---------|
| `minimal` | 要件定義フェーズ（素早い概念チェック） | 5-10 分 | ~150 |
| `full` | 設計フェーズ（OSS 比較・アーキテクチャ調査） | 20-40 分 | ~500 |
| `selector` | どちらか迷ったとき（自動ルーティング） | 1-2 分 | ~100 |

---

## 使い方

### A. VS Code Copilot — セットアップ不要

`.instructions.md` を Agent Skills フォルダにコピーして VS Code を再起動：

```bash
# macOS
cp .instructions.md \
  ~/Library/Application\ Support/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art-investigation.md

# Linux
cp .instructions.md \
  ~/.config/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art-investigation.md
```

Copilot Chat で使う：

```
@prior-art-investigation minimal リアルタイム検索機能を設計したい
```

→ [詳細セットアップ](./AGENT-SKILLS-SETUP.md)

---

### B. Claude Desktop (MCP) — 5 分

`claude_desktop_config.json` に追加：

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

Claude Desktop を再起動 → ツール `load_minimal` / `load_full` / `load_selector` が使用可能。

→ [詳細セットアップ](./MCP-SETUP.md)

---

### C. Kiro SDD — フック・パーソナリティをコピー

```bash
cp -r .kiro/hooks /your-project/.kiro/
cp -r .kiro/personalities /your-project/.kiro/
```

要件定義・設計フェーズで先行技術調査が自動的に実行される。

---

## パーソナリティ一覧（Kiro SDD 用）

調査の観点をパーソナリティで切り替える：

| パーソナリティ | 得意な調査 |
|--------------|-----------|
| `researcher` | 学術論文・引用・既存研究 |
| `startup-hunter` | 市場検証・競合分析・スタートアップ動向 |
| `tech-auditor` | 技術的深度・アーキテクチャ・エンジニアリングベストプラクティス |
| `patent-search` | IP リスク・特許景観・先行技術クレーム |
| `team-internal` | 社内ナレッジ・既存ドキュメント・社内パターン |

---

## カスタマイズ

### 質問フレームワーク（Q1〜Q7）

`minimal` は Q1（第一原理）+ Q6（反転リスク）のみ使用。  
`full` は Q1〜Q7 の全質問を使用。

質問の内容は `.instructions.md` または `.instructions.ja.md` を直接編集して変更できる。

### パーソナリティのカスタマイズ

`.kiro/personalities/` 内の JSON ファイルを編集する：

```json
{
  "name": "my-custom",
  "label": "My Custom Researcher",
  "description": "Focus on ...",
  "questions": ["What ...?", "Are there ...?"]
}
```

---

**バージョン**: 1.0.0 | **ライセンス**: MIT
