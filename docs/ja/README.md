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
/prior-art full LLM の出力を使って小さい ML モデルを学習させたい
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

**入力**: `/prior-art full LLM の出力を使って小さい ML モデルを学習させたい`

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

## クイックスタート

```bash
git clone https://github.com/as-we/prior-art-investigation
cd prior-art-investigation
make install
```

**1回だけ実行すれば全プロジェクトで有効。** VS Code + Copilot Chat で `/prior-art` が使えるようになります。`#web` を付けると学習カットオフを突破したライブ検索で調査できます。

- 詳細なセットアップ（Kiro / Claude Desktop / カスタムエージェント）→ [セットアップガイド](./SETUP.md)
- 使い方・調査結果の読み方・スキップ判断 → [使い方ガイド](./USAGE.md)

---

**バージョン**: 1.0.0 | **ライセンス**: MIT

---

## ドキュメント

| | 日本語 | English |
|-|---------|--------|
| 概要 | [docs/ja/README.md](./README.md) | [docs/en/README.md](../en/README.md) |
| 使い方ガイド（SDD ワークフロー） | [docs/ja/USAGE.md](./USAGE.md) | [docs/en/USAGE.md](../en/USAGE.md) |
| セットアップガイド（インストール） | [docs/ja/SETUP.md](./SETUP.md) | [docs/en/SETUP.md](../en/SETUP.md) |
| Q1-Q8 解説 | [docs/ja/QUESTIONS.md](./QUESTIONS.md) | [docs/en/QUESTIONS.md](../en/QUESTIONS.md) |

---

## ライセンス

MIT

- **GitHub**: https://github.com/as-we/prior-art-investigation
- **Release**: https://github.com/as-we/prior-art-investigation/releases/tag/v1.1.0
