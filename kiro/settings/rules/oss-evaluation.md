# OSS評価ルール

> **スコープ**: このルールは、先行技術調査（Phase A/B）全体を通じたOSS評価に適用される。
> **スタンドアロン対応**: Kiro SDD不要。任意の開発ワークフローで使用可能。

---

## Phase A: 概念レベルの調査

### A-0: 調査開始の7つの問い

設計を開始する前に以下の問いに答える。全問への回答がなければ設計に進んではならない。

| # | 問い |
|---|-----|
| Q1 | この問題の枠組みは正しいか？解くべき問題を解いているか？ |
| Q2 | なぜこのアプローチは既に普及していないのか？ |
| Q3 | このアプローチで失敗した人は何人いるか？どのように失敗したか？ |
| Q4 | このドメインを最も深く考えている人は誰か？その言葉はどこにあるか？ |
| Q5 | 一次資料（論文・RFC・コミットログ・Issue）を読んだか？ |
| Q6 | これが最悪の形で失敗するとしたら何が原因か？ |
| Q7 | 概念名が分かった。これが設計をどう変えるか？ |

### A-1: 命名規則

- **概念名の特定**: 既知のアルゴリズム名・パターン名・技術名を特定する
- **複数の参照名の確認**: 同じ概念が複数名を持つことがある（例: "KD" vs "Knowledge Distillation"）
- **発表年の記録**: 概念の将来的な陳腐化リスクを測るために必要
- **成熟度評価**: Production Ready / Experimental / Theoretical / Deprecated で分類

### A-2: ドメイン別の調査範囲

| ドメイン | 調査すべき概念の例 |
|--------|----------------|
| ML / AI | Knowledge Distillation・LoRA・RAG・Active Learning・RLHF・Vector Stores |
| Webバックエンド | CQRS・Event Sourcing・Saga・Circuit Breaker・BFF・Hexagonal Architecture |
| Webフロントエンド | Island Architecture・Optimistic UI・PRPLパターン・Micro Frontends |
| モバイル | Offline-first・MVVM/MVI・単方向データフロー・Composable Navigation |
| インフラ | Blue-Green Deploy・カナリアリリース・GitOps・Cell-based Architecture・eBPF |
| データプラットフォーム | Medallion Architecture・Data Mesh・Lambda/Kappa・CDC・dbt Metrics |
| セキュリティ | RBAC/ABAC・Zero Trust・PKCE・CSP・SSRF Protection |

### A-3: 調査リソース

| カテゴリ | URL | 用途 |
|--------|-----|-----|
| ML プレプリント | https://arxiv.org/list/cs.LG/recent | 最新MLアルゴリズム |
| 実装付き論文 | https://paperswithcode.com/ | 論文 + OSS対応表 |
| 論文検索 | https://www.semanticscholar.org/ | 引用数・関連研究 |
| 設計パターン | https://martinfowler.com/ | バックエンド・DDD・マイクロサービス |
| マイクロサービス | https://microservices.io/ | パターンライブラリ |
| 業界レーダー | https://www.thoughtworks.com/radar | Adopt/Trial/Assess/Hold分類 |
| クラウドネイティブ | https://landscape.cncf.io/ | インフラパターン |
| フロントエンド | https://web.dev/ | ブラウザ・パフォーマンスパターン |
| セキュリティ | https://owasp.org/ | 脆弱性・セキュリティ標準 |

### A-4: 概念結果の記録

`templates/research.md`の「Named Concept / 先行技術」セクションに記録する。

**必須項目**:
- 概念名（発見した場合）または「概念名なし — 新規の組み合わせ」（未発見の場合）
- 一次資料のURL
- 発表年と成熟度
- Q7の回答: この概念名が設計を変える理由

---

## Phase B: OSSレベルの評価

### B-1: 調査順序（厳守）

1. プロジェクト内部の再利用可能モジュールを最初に確認する
2. エコシステムの公式パッケージを確認する（npm・PyPI・crates.io・Hex）
3. 業界標準OSSを確認する
4. 参照実装のみをレビューする（採用なし）

### B-2: ライセンスTier分類

全てのOSS候補をSPDX識別子でライセンスを記録し、Tierを分類する。

| Tier | SPDX ライセンス例 | 判断 |
|------|----------------|------|
| **Tier 1** ✅ 採用可 | MIT・BSD-2-Clause・BSD-3-Clause・Apache-2.0・ISC・0BSD | オーバーライドなしで採用可 |
| **Tier 2** ⚠️ 条件付き | LGPL-2.1-only・LGPL-3.0-only・MPL-2.0・EPL-2.0・CDDL-1.0 | 利用形態（ライブラリ/アプリ）を要確認 |
| **Tier 3** 🔴 法的レビュー必要 | GPL-2.0-only・GPL-3.0-only・AGPL-3.0-only・OSL-3.0 | 法務クリアなしで採用禁止 |
| **Tier 4** ❌ 採用禁止 | SSPL-1.0・Commons Clause・BSL-1.1・CC-BY-NC-*・独自 | 採用禁止 |

**ライセンスが見つからない場合**: そのOSSを採用してはならない。

### B-3: OSSヘルス評価

ライセンスがTier 1またはTier 2であっても以下を評価する:
- **最終コミット**: 12ヶ月以内が必須（2年以上でフラグ）
- **コントリビュータ数**: 1人のプロジェクトはリスク（2人以上を推奨）
- **オープンIssue数**: 機能リクエストのみを多数抱えるより、バグIssueが少ない方が望ましい
- **後継プロジェクト**: アーカイブ済みの場合、後継プロジェクトに乗り換えを検討

### B-4: Build vs Use の判断マトリクス

| 判断基準 | スコア +1（既存採用）| スコア −1（自前実装）|
|--------|-------------------|------------------|
| 機能適合度 | 要件の80%以上をカバー | 60%未満またはフォーク必要 |
| ライセンス | Tier 1 | Tier 3以上 |
| 最終コミット | 12ヶ月以内 | 2年以上前 |
| 戦略的差別化 | 非コア（ユーティリティ/インフラ） | プロダクトのコアバリュー |
| 自前実装量 | 200行超 | 50行以下 |

**合計スコア ≥ +2 → 既存OSS採用を推奨**  
**合計スコア ≤ 0 → 自前実装を推奨（調査結果で理由を明記）**

---

## 完了チェックリスト

**Phase A（概念レベル）**
- [ ] Q1〜Q7の全問に答えた（設計フェーズ）またはQ1+Q6のみ（要件フェーズ）
- [ ] 概念名を検索した（結果: 発見 / 未発見）
- [ ] 発見した場合: 名前・URL・発表年・成熟度をresearch.mdに記録した
- [ ] 未発見の場合: 「概念名なし — 新規の組み合わせ」と根拠を記録した
- [ ] ThoughtWorks Tech Radarの分類を確認した

**Phase B（OSSレベル）**
- [ ] プロジェクト内部の再利用を確認した
- [ ] 1〜3件のOSS候補を評価した
- [ ] 全候補をSPDX License Tierで分類した
- [ ] OSSヘルスを評価した（最終コミット・コントリビュータ数）
- [ ] Build vs Useマトリクスを適用した
- [ ] URLを含む調査結果をresearch.mdに記録した
- [ ] 採用判断（採用 / 自前実装 / 該当なし）を設計ドキュメントに反映した
