# 先行技術・既発明調査フレームワーク

> AIコーディングエージェントが要件・設計・コードを書く**前に**、概念名・確立されたパターン・既存実装を特定するための軽量チェックリストとプロンプトセット。

## どんな問題を解決するか？

AIエージェント（と人間）はしばしば車輪の再発明をしてしまう：
- 「LLM推論 → 軽量ML学習」が**Knowledge Distillation**という名前の既存技術だと知らずに設計する
- **Circuit Breaker**パターンだと知らずにリトライ・バックオフの仕組みを設計する
- **CQRS**だと知らずに読み書き分離モデルを構築する

概念名を特定することで、1行のコードを書く前に既存のベストプラクティス・既知の失敗パターン・参照実装が手に入る。

## 構成

```
docs/ja/
├── README.md                                     ← このファイル
├── setup-checklist.md                            ← 導入手順チェックリスト
├── templates/
│   └── research.md                               ← Named Conceptセクション付きresearch.mdテンプレート
├── github/
│   └── prompts/
│       └── prior-art-check.prompt.md             ← AIエージェントプロンプト
└── kiro/
    └── settings/
        └── rules/
            └── oss-evaluation.md                 ← メインルールファイル
```

## クイックスタート

[セットアップチェックリスト](setup-checklist.md) を参照してください。

### Option A: Kiro / cc-sdd と統合（推奨）

```bash
cp docs/ja/kiro/settings/rules/oss-evaluation.md     .kiro/settings/rules/
cp docs/ja/templates/research.md                     .kiro/settings/templates/specs/
cp docs/ja/github/prompts/prior-art-check.prompt.md  .github/prompts/
```

### Option B: スタンドアロン

`docs/ja/github/prompts/prior-art-check.prompt.md` を任意のIDEのAIエージェントプロンプトとして直接使用してください。

## 調査構造

**フェーズ A — 概念の特定**
- A-0: 設計調査の7つの問い
- A-1: 概念名の特定
- A-2: ドメイン別調査の着眼点
- A-3: ドメイン別リサーチリソース
- A-4: research.mdへの記録

**フェーズ B — OSS / 実装の探索**
- B-1: 調査順序（プロジェクト内部 → エコシステム → 業界標準OSS）
- B-2: ライセンスTier分類（Tier 1〜4）
- B-3: OSSヘルスアセスメント
- B-4: Build vs Use意思決定マトリクス

## リファレンス

- [設計調査の7つの問い](github/prompts/prior-art-check.prompt.md)
- [OSS評価ルール](kiro/settings/rules/oss-evaluation.md)
- [research.mdテンプレート](templates/research.md)

---

**戻る:** [言語選択](../../README.md)

## ライセンス

MIT
