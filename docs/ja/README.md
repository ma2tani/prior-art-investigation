# 先行技術調査フレームワーク

コードを書く前に、機能の概念名・既存パターン・OSS を素早く特定する。

**[English](../en/README.md)**

---

## 何ができるか

SDD（仕様駆動開発）を使えば、やりたいことベースで要件定義・設計・実装を進められます。

たとえば：
> 「LLM で推論理由を出力させて、その結果を使って小さい ML モデルを学習させたい」

この一文だけで開発は進みます。**ただし、このやり方には盲点があります。**

「知識蒸留（Knowledge Distillation）」という確立した研究分野がすでに存在し、10年以上の論文・OSS・失敗事例の蓄積があります。それを知らないまま実装を進めると、既存の成果を自分で再発明することになります。「自分で考えた」と思い込んだまま。

**このフレームワークは、設計を始める前にその盲点を埋めます。**

```
@prior-art full LLM の出力を使って小さい ML モデルを学習させたい
```

返ってくる情報：

- **技術名** — 「知識蒸留（Knowledge Distillation）」（2015年 Hinton らが提案した既存研究）
- **研究発展の流れ** — モデル圧縮 → ニューラルネット蒸留 → 2023年以降は LLM 蒸留が急増
- **既存 OSS** — DistilBERT、LLaMA-Factory、Hugging Face transformers など、評価マトリクス付き
- **よくある落とし穴** — 教師データの品質依存、バイアス継承、訓練不安定性

---

## 使い方

| モード | 使いどき | 返ってくるもの |
|--------|----------|---------------|
| `minimal` | 設計前の初期チェック | 技術名 + 簡易 OSS リスト + リスクフラグ |
| `full` | アーキテクチャ決定・新規サブシステム設計 | 研究系譜 + OSS マトリクス + トレードオフ + 失敗モード |
| `selector` | どちらか迷ったとき | minimal か full に自動振り分け |

<details>
<summary><strong>例：full モード出力</strong></summary>

**入力**: `@prior-art full LLM の出力を使って小さい ML モデルを学習させたい`

**出力**:

**技術名**: 知識蒸留（Knowledge Distillation）

> この技術は 10 年以上の歴史があります。元々はモデル圧縮手法（[Hinton ら 2015年](https://arxiv.org/abs/1503.02531)「Distilling the Knowledge in a Neural Network」）だったのが、[DistilBERT](https://arxiv.org/abs/1910.01108)（2019年）、[MiniLM](https://arxiv.org/abs/2002.10957)（2021年）を経て、2023年から LLM 応用が爆発的に増えました。核心は：小さいモデルが大きいモデルの出力 + 推論を学ぶと、計算量 10% で性能 90% を達成できるということ。

**研究系譜**:
| 年 | 論文 | 重要な洞察 |
|----|------|----------|
| 2015 | Hinton ら ["Distilling the Knowledge in a Neural Network"](https://arxiv.org/abs/1503.02531) | 温度付きソフトマックスで知識転移が可能 |
| 2019 | Sanh ら ["DistilBERT"](https://arxiv.org/abs/1910.01108) | BERT スケールの蒸留が実用的 |
| 2021 | Wang ら ["MiniLM"](https://arxiv.org/abs/2002.10957) | 層間マッチングで小モデルが改善 |
| 2023 | Li ら ["Distilling Step-by-Step"](https://arxiv.org/abs/2212.10071) | LLM の推論プロセス自体を蒸留可能 |
| 2024 | Zheng ら ["LLaMA-Factory"](https://arxiv.org/abs/2403.13372) | 本番対応蒸留パイプライン |

**OSS 評価マトリクス**:
| ツール | ライセンス | メンテナー | 更新頻度 | データ準備 | 向いてる用途 | ソース |
|------|----------|----------|---------|----------|------------|------|
| Hugging Face transformers | Apache-2.0 | Hugging Face（組織） | 活発（毎週） | 低 | 標準 BERT スケール蒸留 | [GitHub](https://github.com/huggingface/transformers) |
| LLaMA-Factory | Apache-2.0 | HKUST / 清華大学（学術組織） | 活発（毎月） | 中 | LLM 蒸留エンドツーエンド | [GitHub](https://github.com/hiyouga/LLaMA-Factory) |
| 論文提供コード | 様々 | 個人研究者 | 停滞気味 | 高 | 研究・カスタムアーキテクチャ | [arXiv](https://arxiv.org/abs/2212.10071) |

**よくある落とし穴**:
- **教師バイアス**: 小モデルが教師の誤りとバイアスを引き継ぐ
- **データ品質**: 推論ラベルの質がなければ蒸留は失敗
- **訓練不安定**: 温度調整と損失加重が敏感
- **検証必須**: 直接訓練とA/Bテストで常に比較

</details>

---

## 使い方

### A. VS Code カスタムエージェント — セットアップ不要（推奨）

> 必要なもの: VS Code + GitHub Copilot Chat

このリポジトリに含まれる `.github/agents/prior-art.agent.md` は **VS Code カスタムエージェント** ファイルです（VS Code 1.99 / 2025年4月導入、2026年4月スキーマ更新）。

**このリポジトリで使う場合** — チャットのドロップダウンから選ぶだけ：

1. Copilot Chat を開く（`⌃⌘I`）
2. エージェントセレクター → **Prior Art Investigation** を選択
3. `git diff HEAD` を自動確認し、spec ファイルが変更されていれば調査を実行

**自分のプロジェクトで使う場合** — エージェントファイルをコピー：

```bash
mkdir -p .github/agents
cp path/to/prior-art-investigation/.github/agents/prior-art.agent.md .github/agents/
```

Copilot Chat のドロップダウンから **Prior Art Investigation** を選択するだけ。

> **注意**: `.chatmode.md` は旧形式（廃止済み）です。VS Code 1.99+ は `.github/agents/*.agent.md` を使用します。古い `.chatmode.md` があれば名前を変更してください。

---

### B. VS Code Agent Skills（ワークスペース横断）— 2 分

**この方法は複数プロジェクトをまたいで使いたい場合**に向いています。`.instructions.md` を Agent Skills フォルダにコピーして VS Code を再起動：

```bash
# macOS
cp .instructions.md \
  ~/Library/Application\ Support/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art.md

# Linux
cp .instructions.md \
  ~/.config/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art.md
```

Copilot Chat で使う：

```
@prior-art minimal リアルタイム検索機能を設計したい
```

→ [詳細セットアップ](./SETUP.md)

---

## クイックインストール

```bash
git clone https://github.com/as-we/prior-art-investigation
cd prior-art-investigation
make install
```

`make install` で以下の2層をまとめてセットアップ。**1回だけ実行すれば全プロジェクトで有効。**

---

## 使い方

### 第1層 — Agent Skills: 明示的呼び出し

一度インストールすれば全プロジェクトで使える：

```bash
make install-skills
# または手動:
cp .instructions.md \
  ~/Library/Application\ Support/Code/User/globalStorage/github.copilot-chat/agent-skills/prior-art.md
```

Copilot Chat から呼び出す：

```
@prior-art full LLM の出力を使って小さい ML モデルを学習させたい
@prior-art minimal リアルタイムキャッシュ設計について
@prior-art selector  ← minimal か full に自動振り分け
```

**対応ツール**: VS Code Copilot Chat, Kiro IDE, Cursor, Windsurf  
**トークン消費**: 明示的に呼んだときだけ

→ [詳細セットアップ](./SETUP.md)

---

### 第2層 — 自動検知フック: ゼロ操作リマインダー

`UserPromptSubmit` フックがプロンプトを監視し、設計・アーキテクチャに関係する内容なら1行だけリマインダーを挿入する。**LLM 不使用・シェルスクリプトによる決定論的判断。**

一度インストールすれば全セッションで有効：

```bash
make install-hook
```

VS Code 設定でユーザースコープフックを有効化：
```json
"chat.hookFilesLocations": { "~/.copilot/hooks": true }
```

**動作**: `design`, `architecture`, `requirements.md`, `/kiro-spec-design`, `設計`, `実装` などのキーワードを含むプロンプトに対して：

> 💡 Prior art check recommended: this looks like a design or implementation decision. Before building, consider running: `@prior-art full <topic>`

**トークン消費**: ほぼゼロ（フック自体はシェルスクリプト実行のみ）  
フックは `~/.copilot/hooks/` に配置されるため、**プロジェクトのファイルを汚さない。**

---

### 第3層 — MCP サーバー: Claude Desktop / その他クライアント

```json
{
  "mcpServers": {
    "prior-art": {
      "command": "python3",
      "args": ["/path/to/prior-art-investigation/mcp/server_lite.py"]
    }
  }
}
```

Claude Desktop を再起動 → ツール `load_minimal` / `load_full` / `load_selector` が使用可能。

→ [詳細セットアップ](./SETUP.md)

---

### 第4層 — VS Code カスタムエージェント（プロジェクト単位）

`.github/agents/prior-art.agent.md` をプロジェクトにコピーして使う：

```bash
mkdir -p .github/agents
cp path/to/prior-art-investigation/.github/agents/prior-art.agent.md .github/agents/
```

Copilot Chat のドロップダウンから **Prior Art Investigation** を選択するだけ。

> チームでエージェント設定をリポジトリ管理したい場合や、プロジェクト単位で制御したい場合に使う。

---

### 第5層 — Kiro SDD フック（プロジェクト単位、Kiro IDE）

```bash
cp -r .kiro/hooks /your-project/.kiro/
cp -r .kiro/personalities /your-project/.kiro/
```

Kiro IDE では要件定義・設計フェーズで自動的に先行技術調査が実行される（`after_kiro_spec_requirements`, `after_kiro_spec_design`）。

VS Code 向け `.kiro.hook` も同梱（デフォルト無効 — 第2層推奨）。

---

## オプション：フック実行の制御

第2層はキーワードマッチ時にリマインダーを1行挿入するだけ（フル調査は実行しない）。無効化したい場合：

```bash
rm ~/.copilot/hooks/prior-art-detect.json
rm ~/.copilot/hooks/scripts/prior-art-detect.sh
```

**フル調査が有効な場面**：
- ゼロイチ・新規開発 — 未知の領域、発見価値が高い
- アーキテクチャ決定 — 新しいサブシステム、依存関係・技術の選定

**スキップしてよい場面**：
- 保守・リファクタリング — 既存コード、新しい概念なし
- よく知っている領域 — 調査不要

---

## パーソナリティ一覧（Kiro SDD 用）

パーソナリティは「**どの観点から調査するか**」を切り替える設定で、Kiro IDE の SDD フックで使われます。フェーズによってデフォルトが異なります。

| パーソナリティ | 得意な調査 | Kiro デフォルトフェーズ |
|--------------|-----------|----------------------|
| `startup-hunter` | 市場検証・競合分析・スタートアップ動向 | 要件定義 |
| `tech-auditor` | 技術的深度・アーキテクチャ・エンジニアリングBP | 設計 |
| `researcher` | 学術論文・引用・既存研究 | — |
| `patent-search` | IP リスク・特許景観・先行技術クレーム | — |
| `team-internal` | 社内ナレッジ・既存ドキュメント・社内パターン | — |
| `platform-expert` | IDE・ランタイムのネイティブ API・SDK 機能 — プラットフォームが既に持つ機能の再発明を防ぐ | — |

フックの `personality` フィールドで指定します（`.kiro/hooks/*.json`）。詳細は [SETUP.md § パーソナリティの変更](./SETUP.md#パーソナリティの変更) を参照。

---

## カスタマイズ

### 質問フレームワーク（Q1〜Q8）

`minimal` は Q1（第一原理）+ Q6（反転リスク）のみ使用。  
`full` は Q1〜Q8 の全質問を使用。Q8 はプラットフォームネイティブ機能の調査（IDE・SDK・ランタイムが既に持つ機能の確認）。

質問の内容は `.instructions.md` を直接編集して変更できる（`.instructions.ja.md` は非推奨）。

→ [Q1-Q8 詳細解説](./QUESTIONS.md)

### パーソナリティのカスタマイズ

`.kiro/personalities/` 内の JSON ファイルを編集するか、新規作成：

```json
{
  "name": "my-custom",
  "label": "My Custom Researcher",
  "description": "Focus on ...",
  "questions": ["What ...?", "Are there ...?"],
  "web_sources": ["GitHub", "arXiv"]
}
```

→ 詳細（フック設定・環境変数・カスタム例）は [SETUP.md](./SETUP.md) を参照。

---

**バージョン**: 1.0.0 | **ライセンス**: MIT

---

## ドキュメント

| | 日本語 | English |
|-|---------|--------|
| 概要 | [docs/ja/README.md](./README.md) | [docs/en/README.md](../en/README.md) |
| セットアップガイド | [docs/ja/SETUP.md](./SETUP.md) | [docs/en/SETUP.md](../en/SETUP.md) |
| Q1-Q8 解説 | [docs/ja/QUESTIONS.md](./QUESTIONS.md) | [docs/en/QUESTIONS.md](../en/QUESTIONS.md) |

---

## ライセンス

MIT

- **GitHub**: https://github.com/as-we/prior-art-investigation
- **Release**: https://github.com/as-we/prior-art-investigation/releases/tag/v1.1.0
