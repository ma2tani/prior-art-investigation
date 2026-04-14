# 先行技術調査フレームワーク 導入チェックリスト

新規プロジェクトへの導入時に使用する。

---

## 前提確認

- [ ] GitHub Copilot（agentモード）または同等のAI IDEが利用可能か確認
- [ ] `.kiro/` ディレクトリが存在するか確認（なければ作成）
- [ ] `.github/prompts/` ディレクトリが存在するか確認（なければ作成）

---

## Option A: Kiro / cc-sdd に組み込む（推奨）

### Step 1: Kiroルールファイルのコピー

- [ ] `kiro/settings/rules/oss-evaluation.md` を `.kiro/settings/rules/` にコピー

```bash
cp kiro/settings/rules/oss-evaluation.md .kiro/settings/rules/
```

> このファイルが核心。設計調査の7つの問い（Phase A-0）と Phase A → Phase B の全調査プロセスが入っている。

### Step 2: research.mdテンプレートへのNamed Conceptセクション追加

- [ ] `templates/research.md` の内容を既存の `research.md` テンプレートにマージ

既存の `research.md` テンプレートがある場合: `Named Concept / 先行技術` セクションのみ追加する。  
テンプレートがない場合: ファイルをそのままコピー。

```bash
# テンプレートがない場合
cp templates/research.md .kiro/settings/templates/specs/
```

### Step 3: design-discovery-full.md への組み込み（cc-sddの場合）

プロジェクトに `design-discovery-full.md` がある場合、Step 3aに以下の参照を追加する:

```markdown
### Step 3a: 先行技術・既発明調査

`.kiro/settings/rules/oss-evaluation.md` の Phase A → Phase B を実行:
- Phase A: 概念の命名（既知のアルゴリズム名・パターン名が存在するか？）
- Phase B: OSS実装の探索（概念名が特定できた後にのみ実行）
```

> `design-discovery-full.md` がない場合はこの手順をスキップ。

### Step 4: 各フェーズトリガーの追加（任意・推奨）

要件フェーズ（`kiro-spec-requirements.prompt.md`）に追加:

```markdown
## Quick Prior Art Check（要件確定前に必ず自問）
> 詳細調査は設計フェーズ。ここでは問題の枠組みを正す2問のみ。
> 完全な調査ルール → `.kiro/settings/rules/oss-evaluation.md`
- **Q1（第一原理）**: この要件の問題設定は正しいか？
- **Q6（反転）**: この機能が最悪の形で失敗するとしたら何が原因か？
- 概念名の候補が浮かんだ場合 → `[Named Concept: 要確認]` とメモし設計フェーズに委ねる
```

タスクフェーズ（`kiro-spec-tasks.prompt.md`）に追加:

```markdown
## Q7「So What」チェック（タスク確定前に自問）
> 完全なルール → `.kiro/settings/rules/oss-evaluation.md` A-0
各非自明タスクに問う:「このタスクはresearch.mdの先行技術調査結果を反映しているか？」
→ 未反映 → タスク修正 / OSSを採用したのにゼロから実装するタスク → 削除またはラッパーに置換
```

---

## Option B: スタンドアロン（Kiro / cc-sddなし）

- [ ] `github/prompts/prior-art-check.prompt.md` をプロジェクトの `.github/prompts/` にコピー
- [ ] `templates/research.md` をチームが使う設計メモの場所（`docs/` など）にコピー
- [ ] AIエージェントに「`prior-art-check.prompt.md` を実行して」と指示するだけで動作する

---

## 確認

- [ ] `.kiro/settings/rules/oss-evaluation.md` がターゲットプロジェクトに存在する
- [ ] 設計フェーズで `oss-evaluation.md` が参照されている（または `prior-art-check.prompt.md` で代替）
- [ ] `research.md` テンプレートに Named Concept / 先行技術 セクションがある
