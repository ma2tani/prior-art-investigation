# 先行技術調査フレームワーク — v1.0.0

> あなたの機能概念が既に存在するか、何と呼ばれているか、どの OSS が利用可能かを素早く特定する — **コードを書く前に**。

---

## どんな問題を解決するか？

機能を設計する際、既に与えられている以下のことを知らずに新規開発することが多い：
- **確立された名前** — 「LLM 推論 → 軽量 ML」= *Knowledge Distillation*
- **既知の失敗パターン** — 「リトライ + バックオフ」= *Circuit Breaker パターン*
- **参照実装** — 「読み書き分離モデル」= *CQRS*
- **既存 OSS** — 既に誰かが解決している

コードを書く**前に**概念を特定することで、ベストプラクティス、既知のトレードオフ、使用可能なソリューションが手に入る。

---

## 🚀 3 つの使用方法

### 方法 1: VS Code Copilot（最速）
```
@prior-art-investigation minimal
リアルタイムグルーヴ推薦機能が必要
```
**セットアップ**: 0 分 | **実行**: 5-10 分 | **コスト**: ~150 トークン

---

### 方法 2: Claude Desktop (MCP サーバー)
```bash
# 1. 設定（5 分）
# ~/.../Claude/claude_desktop_config.json
{
  "mcpServers": {
    "prior-art-investigation": {
      "command": "python3",
      "args": ["/path/to/mcp/server_lite.py"]
    }
  }
}

# 2. Claude Desktop を再起動
# 3. ツールを使用: @prior-art-investigation load_minimal など
```
**セットアップ**: 5 分 | **ツール**: 3 個（load_minimal, load_full, load_selector）

---

### 方法 3: npm パッケージ（プログラマティック）
```bash
npm install @ma2tani/prior-art-investigation

import minimalPrompt from '@ma2tani/prior-art-investigation/prompts/minimal';
```
**セットアップ**: 1 分 | **用途**: Node.js、バンドラー、パイプライン

---

## 📊 フレームワーク概要

| フェーズ | プロンプト | 時間 | トークン | 質問 |
|---------|----------|------|---------|------|
| **要件定義** | MINIMAL | 5-10 分 | ~150 | Q1, Q6 |
| **設計** | FULL | 20-40 分 | ~500 | Q1-Q7 |
| **不明** | SELECTOR | 1-2 分 | ~100 | 自動ルーティング |

**トークン削減**: MINIMAL は FULL の **70% 削減** を達成（150 vs 500 トークン）

---

## 📚 ドキュメント構成

```
docs/ja/
├── README.md                           ← このファイル
├── NAVIGATION.md                       ← ディスカバリーハブ
├── setup-checklist.md                 ← 導入手順
├── templates/
│   └── research.md                    ← 出力テンプレート
├── github/
│   └── prompts/
│       ├── minimal.prompt.md          ← Q1+Q6 フレームワーク
│       ├── full.prompt.md             ← Q1-Q7 フレームワーク
│       └── selector.prompt.md         ← 自動ルーティング
└── kiro/
    └── settings/
        └── rules/
            └── oss-evaluation.md      ← OSS フレームワーク
```

---

## ✨ 主な機能 (v1.0.0)

- ✅ **フェーズ分割プロンプト** — MINIMAL / FULL / SELECTOR（3 オプション）
- ✅ **70% トークン削減** — MINIMAL は 150 トークン（vs 500 フル）
- ✅ **3 つの配布チャネル** — Agent Skills / MCP / npm
- ✅ **ゼロ依存関係** — MCP サーバーは Python stdlib のみ
- ✅ **バイリンガル** — English + 日本語
- ✅ **Kiro SDD 対応** — 出力を `.kiro/specs/` に保存
- ✅ **本番環境対応** — テスト済み、ドキュメント完備、デプロイ完了

---

## 🎯 どのプロンプトを使う？

### MINIMAL（要件定義フェーズ）
**使用時**: 問題を定義していて、クイックな検証が必要  
**質問**: Q1（第一原理）+ Q6（反転/リスク）  
**時間**: 5-10 分  
**トークン**: ~150  
**出力**: 概念名確定 + 主要リスク特定

### FULL（設計フェーズ）
**使用時**: アーキテクチャ設計または新規サブシステム設計  
**質問**: Q1-Q7 完全調査  
**時間**: 20-40 分  
**トークン**: ~500  
**出力**: 概念名 + OSS オプション + アーキテクチャ決定 + リスク

### SELECTOR（フェーズ不明）
**使用時**: 自分がどのフェーズにいるか不明  
**質問**: 自動ルーティング質問  
**時間**: 1-2 分  
**トークン**: ~100  
**出力**: MINIMAL または FULL を実行する推奨

---

## 📖 ナビゲーション

**役割別:**
- **プロダクトマネージャー**: [NAVIGATION.md](./NAVIGATION.md) → MINIMAL プロンプト
- **アーキテクト**: [NAVIGATION.md](./NAVIGATION.md) → FULL プロンプト
- **VS Code ユーザー**: [AGENT-SKILLS-USAGE.md](../en/AGENT-SKILLS-USAGE.md)（先行技術調査）
- **Claude Desktop ユーザー**: [CLAUDE-DESKTOP-SETUP.md](../en/CLAUDE-DESKTOP-SETUP.md)（先行技術調査）
- **Kiro SDD チーム**: [MCP-SETUP.md](../en/MCP-SETUP.md#kiro-sdd-integration) を参照

---

## ✅ サポートプラットフォーム

| プラットフォーム | ステータス | セットアップ | 統合 |
|------------|----------|----------|------|
| **VS Code Copilot** | ✅ 準備完了 | 0 分 | Agent Skills |
| **Claude Desktop** | ✅ 準備完了 | 5 分 | MCP サーバー |
| **ChatGPT / Claude.ai** | ✅ 動作 | n/a | コピー/貼り付け |
| **npm** | ✅ 準備完了 | 1 分 | `npm install` |
| **Kiro SDD** | ✅ 対応 | n/a | フェーズ統合 |

---

## 📈 ロードマップ

**v1.0.0**（現在）
- ✅ フェーズ分割プロンプト（MINIMAL/FULL/SELECTOR）
- ✅ Agent Skills サポート
- ✅ MCP サーバー実装
- ✅ npm 配布

**v1.1.0**（Q2 2026）
- [ ] Smithery MCP レジストリ
- [ ] Docker コンテナ
- [ ] GitHub Actions CI（トークン計測）
- [ ] コミュニティフィードバック統合

**v1.2.0**（Q3 2026）
- [ ] 高度な Agent Skills パーソナリティ
- [ ] Kiro SDD 深層統合
- [ ] ワークスペース自動保存

---

## 🔗 クイックリンク

- **完全ナビゲーション**: [NAVIGATION.md](NAVIGATION.md)
- **リリースノート**: [RELEASE.md](../RELEASE.md)
- **CHANGELOG**: [CHANGELOG.md](../CHANGELOG.md)
- **GitHub リポジトリ**: https://github.com/ma2tani/prior-art-investigation
- **npm パッケージ**: https://www.npmjs.com/package/@ma2tani/prior-art-investigation

---

## 💡 例

### 例 1: クイック要件チェック（5 分）
```
ユーザー: "@prior-art-investigation minimal リアルタイムメトリクスダッシュボードが必要"

エージェント:
- Q1 第一原理: 「メトリクス表示」それとも「リアルタイムデータ同期」を解決中？
- Q6 リスク: レイテンシー仮定。確認: データ更新が 1 秒以下でできる？
- 概念: 「リアルタイムダッシュボード」または「ライブ分析」
- オプション: Databricks、Grafana、Tableau
- ステータス: 設計フェーズに進める準備完了 ✓
```

### 例 2: 深層アーキテクチャ調査（20 分）
```
ユーザー: "@prior-art-investigation full ML ベースのリズム検出を設計中"

エージェント: (Q1-Q7 調査)
- 概念: 「Onset 検出」または「ビート追跡」
- 既存 OSS: librosa、madmom、essentia
- アーキテクチャ: バッチ vs リアルタイムトレードオフ
- リスク: モデル精度、レイテンシー、バージョニング
- 推奨: librosa ベースラインで開始
- ステータス: .kiro/specs/rhythm-detection/docs/research.md に保存 ✓
```

---

## 📝 ライセンス

MIT

---

**バージョン**: 1.0.0  
**ステータス**: 本番環境対応 ✅  
**最終更新**: 2026-04-14  

**[← 言語選択に戻る](../../README.md)**
