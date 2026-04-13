# 先行技術・既発明調査フレームワーク

> AIコーディングエージェントが要件・設計・コードを書く**前に**、概念名・確立されたパターン・既存実装を特定するための軽量チェックリストとプロンプトセット。

## どんな問題を解決するか？

AIエージェント（と人間）はしばしば車輪の再発明をしてしまう：
- 「LLM推論 → 軽量ML学習」が**Knowledge Distillation**という名前の既存技術だと知らずに設計する
- **Circuit Breaker**パターンだと知らずにリトライ・バックオフの仕組みを設計する
- **CQRS**だと知らずに読み書き分離モデルを構築する

概念名を特定することで、1行もコードを書く前に既存のベストプラクティス・既知の失敗パターン・参照実装が手に入る。

## 構成

```
prior-art-investigation/
├── README.md                                     ← このファイル
├── setup-checklist.md                            ← 導入手順チェックリスト
├── templates/
│   └── research.md                               ← Named Conceptセクション付きresearch.mdテンプレート
│                                                    Kiro:        .kiro/settings/templates/specs/ にコピー
│                                                    スタンドアロン: そのまま使用、またはdocs/にコピー
├── github/
│   └── prompts/
│       └── prior-art-check.prompt.md             ← AIエージェントプロンプト（Kiro・スタンドアロン共用）
│                                                    .github/prompts/ にコピー
└── kiro/
    └── settings/
        └── rules/
            └── oss-evaluation.md                 ← メインルールファイル（Kiroが.kiro/から自動ロード）
                                                     .kiro/settings/rules/ にコピー
                                                     スタンドアロン: prior-art-check.prompt.md で代替
```

## 使い方

`setup-checklist.md` のステップバイステップ手順を参照。

### Option A: Kiro / cc-sdd と統合（推奨）

```bash
cp kiro/settings/rules/oss-evaluation.md          .kiro/settings/rules/
cp templates/research.md                          .kiro/settings/templates/specs/
cp github/prompts/prior-art-check.prompt.md       .github/prompts/
```

その後、`setup-checklist.md` のStep 3〜4に従い、要件フェーズにQ1+Q6、タスクフェーズにQ7のトリガーを追加する。

### Option B: スタンドアロン

`github/prompts/prior-art-check.prompt.md` を任意のIDEのAIエージェントプロンプトとして直接使用する。

## 調査構造

```
Phase A — 概念の特定（全フェーズ共通）
  A-0: 設計調査の7つの問い
  A-1: 概念名の特定
  A-2: ドメイン別調査の着眼点
  A-3: ドメイン別リサーチリソース
  A-4: research.mdへの記録

Phase B — OSS / 実装の探索
  B-1: 調査順序（プロジェクト内部 → エコシステム → 業界標準OSS）
  B-2: ライセンスTier分類（Tier 1〜4）
  B-3: OSSヘルスアセスメント
  B-4: Build vs Use意思決定マトリクス
```

## ライセンス

MIT
