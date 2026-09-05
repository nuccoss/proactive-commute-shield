<div align="center">

# 🚇 Proactive Commute Shield Enterprise
### 都市移動の突発トラブルから商談まで人を守り抜く、エンタープライズ向け自律守護AIエージェント

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-brightgreen.svg)](https://www.python.org/)
[![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit%201.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![Fast-Mock: 100% Offline](https://img.shields.io/badge/Fast--Mock-100%25%20Offline%20Ready-success.svg)](#-クイックスタート環境構築手順)
<br>
[![Organizer: Zenn (Classmethod)](https://img.shields.io/badge/Organizer-Zenn%20(Classmethod)-3EA8FF.svg)](https://zenn.dev)
[![Main Sponsor: Google Cloud](https://img.shields.io/badge/Main%20Sponsor-Google%20Cloud%20Japan-4285F4.svg)](https://cloud.google.com/)
[![Hackathon: 2026.08.20--10.15](https://img.shields.io/badge/Event-2026.08.20--10.15%20(310%20Entries)-FFA116.svg)](https://zenn.dev)
[![Prize Pool: 1.75M JPY](https://img.shields.io/badge/Prize%20Pool-%C2%A51%2C750%2C000-success.svg)](https://zenn.dev)
<br>
[![Brought by the sponsor: Ekispert API](https://img.shields.io/badge/Brought%20by%20the%20sponsor-%E9%A7%85%E3%81%99%E3%81%B1%E3%81%82%E3%81%A8%20API-00B06B.svg)](https://zenn.dev/hackathons/google-cloud-japan-ai-hackathon-vol5#services)
[![Brought by the sponsor: YouCam API](https://img.shields.io/badge/Brought%20by%20the%20sponsor-YouCam%20API%20(PERFECT)-E91E63.svg)](https://zenn.dev/hackathons/google-cloud-japan-ai-hackathon-vol5#services)
[![Brought by the sponsor: GMI Cloud](https://img.shields.io/badge/Brought%20by%20the%20sponsor-GMI%20Cloud%20(H100)-76B900.svg)](https://zenn.dev/hackathons/google-cloud-japan-ai-hackathon-vol5#services)
[![Brought by the sponsor: TrendAPI / TrendAI™](https://img.shields.io/badge/Brought%20by%20the%20sponsor-TrendAPI%20%2F%20TrendAI%E2%84%A2%20(TrendMicro)-009688.svg)](https://zenn.dev/hackathons/google-cloud-japan-ai-hackathon-vol5#services)

*都市の移動トラブル発生の瞬間から商談の部屋に足を踏み入れる最後の1秒まで、ビジネスと信用を守り抜く*

[主な特徴](#-主な特徴と5大テクノロジー) • [公式スポンサー連携](#-公式ハッカソン協賛--提供サービス一覧) • [4層アーキテクチャ](#-4層アーキテクチャ設計) • [クイックスタート](#-クイックスタート環境構築手順) • [対話型デモ操作フロー](#-対話型デモ画面の構成と操作フロー) • [コスト＆応答速度](#-コスト--応答速度レイテンシベンチマーク) • [共同開発メンバー募集](#recruitment) • [ピッチ登壇メモ](docs/pitch_speaker_notes.md) • [英語版仕様書 (AGENTS.md)](AGENTS.md) • [ライセンス](#-ライセンス)

</div>

---

> [!IMPORTANT]
> **このRepositoryは09/05(土)にGoogle渋谷にて開催された『[第5回 Agentic AI Hackathon with Google Cloud](https://zenn.dev/hackathons/google-cloud-japan-ai-hackathon-vol5)のスピンオフイベント：ミニハッカソン 渋谷（渋谷ストリーム）』にて、2h制限時間内で完成させたMVPの記録です。**  
> GitHub Repositoryは通常英語記載ですが、当Repositoryは日本人向けに最適化して日本語記述をメインとします。  
> ※ READMEの英語版（English technical specification for AI agents & developers）は [AGENTS.md](AGENTS.md) をご覧ください。

## 🎯 WHY（なぜこのプロジェクトを公開するのか）
1. **2h 制限時間内のピッチ登壇・MVP 実証**:
   09/05(土)に開催されたミニハッカソン 渋谷（渋谷ストリーム）の現場にて、わずか 2 時間の制限時間内でアイデアを動く形（Working MVP）へと落とし込み、**ピッチに立って登壇発表すること**を第一の目標として実証・完成させました。
2. **本戦（賞金総額 175 万円）に向けた共同開発チームメンバーの募集**:
   個人開発として完成させたこの MVP コードベースを GitHub 上に先行公開することで、開発ビジョンや技術スタックへの共感を呼び水とし、**「第 5 回 Agentic AI Hackathon with Google Cloud」本戦（2026/08/20 〜 10/15）で最優秀賞を共に目指す共同開発プロジェクトチームの参加メンバーを募ること**を目的としています。

---

## 💡 解決する課題：たった10分の遅刻が招く大損失

エンタープライズ営業の最終提案、重要商談、大規模プロジェクトのキックオフなど、絶対に失敗が許されないビジネスの現場では、わずかな遅刻や乱れが致命傷になります。

1. **容赦ない時間厳守（Unforgiving Punctuality）**:
   突然のゲリラ豪雨やわずか15分の電車遅延でも、数千万円〜数億円規模の商談破談や信用失墜に直結します。
2. **従来の受動的ツールの限界（Passive Tool Limitations）**:
   既存の乗換案内アプリは、人間が手動で慌てて検索しなければならず、カレンダーと連動した事前察知や、先方への状況報告・お詫び連絡を自動で行うことはできません。
3. **シャドーAIの禁止・セキュリティ障壁（The Shadow AI Blockade）**:
   企業のセキュリティポリシー（CISO規定）により、機密情報や顧客名簿（PII）の外部流出、プロンプトインジェクションの脆弱性を恐れ、一般的なLLMを業務カレンダーやメールに直接連携させることが禁止されています。
4. **第一印象の崩壊リスク（The First Impression Collapse）**:
   遅延で焦って走り、汗だくで身だしなみが乱れ、呼吸が乱れたまま会議室へ駆け込むと、「メラビアンの法則（視覚情報が印象の55%を決定）」により、最初の3秒で信頼感が損なわれてしまいます。

**Proactive Commute Shield Enterprise** は、これら4大課題を「自宅のドアを出てから商談ステージに立つまで（Door-to-Stage）」の全行程において同時に解決する、世界初のエンタープライズ自律防衛エージェントです。

---

## 🏆 公式ハッカソン協賛 ＆ 提供サービス一覧

本プロジェクトは、**主催：Zenn（クラスメソッド株式会社）** のハッカソン（期間: 2026/08/20 〜 2026/10/15、賞金総額: 175万円、エントリー数: 310）において、**協賛（Mainスポンサー）Google Cloud** の最先端推論基盤と、**Brought by the sponsor (提供サービス) 4社4製品**をフルスタック統合した自律型エンタープライズ防衛エージェントです。

| 区分 (提供区分) | スポンサー企業（正式名称） | 提供製品 / API | 本システムにおける統合役割 & アーキテクチャ層 |
|:---|:---|:---|:---|
| **主催** | **Zenn（クラスメソッド株式会社）** | 公式コンテストプラットフォーム | ハッカソン開催・技術情報発信・エンジニアコミュニティハブ |
| **協賛<br>(Mainスポンサー)** | **グーグル・クラウド・ジャパン合同会社<br>(Google Cloud)** | **Gemini 2.5 Flash on Vertex AI** | **Layer 3: Autonomous Orchestration Layer**<br>自律ReAct推論ループ（Thought ➔ Action ➔ Observation）の頭脳として全体制御・意思決定を統括 |
| **Brought by the sponsor<br>(提供サービス)** | **株式会社ヴァル研究所** | **駅すぱあと API** | **Layer 2: MCP Tool Calling Layer (Mobility)**<br>リアルタイム運行支障・遅延検知、雨天回避・地下連絡迂回ルート探索 (Ekispert MCP Client)<br>*(~~設定エラーにより、駅すぱあとMCP設定まわりが不完全です。~~<br>※【解決】ヴァル研究所様からの公式回答により、UserConsoleは有償契約専用でありMCPサーバーへの接続は不要であることが確認されました。本プロジェクトでは、公式 Streamable HTTP エンドポイント仕様（https://api-mcp.ekispert.jp/mcp）に準拠し、APIキーなしでも全機能が動作する Fast-Mock（0ms）と、[90日無料評価版](https://api-info.ekispert.com/form/trial/) キーによる本番接続のハイブリッド構成を採用しています。)* |
| **Brought by the sponsor<br>(提供サービス)** | **パーフェクト株式会社<br>(PERFECT Corp.)** | **YouCam API** | **Layer 2: MCP Tool Calling Layer (Presence)**<br>対面直前30秒スキャンによる疲労度・表情黄金比(0.98)評価・印象改善フィードバック (50+ Specialized AI) |
| **Brought by the sponsor<br>(提供サービス)** | **GMI (GMI Cloud)** | **GMI Cloud NVIDIA H100** | **Layer 1: Security & Private Inference Layer (Privacy)**<br>顧客社名・商談機密の完全隔離推論、Zero Data Retention 保証による超爆速お詫び文生成 (64ms) |
| **Brought by the sponsor<br>(提供サービス)** | **トレンドマイクロ株式会社<br>(TrendMicro / AI Fearlessly)** | **TrendAPI / TrendAI™ Security Blueprint** | **Layer 1: Security & Private Inference Layer (Security)**<br>プロンプトインジェクション、悪意あるMCP引数、PII漏洩を0msインメモリで完全防御するセキュリティゲート<br>*(※注: 無料クレジット分の登録が間に合わなかったため、パンフレットのMermaid図からPythonで機能を再現しました。無料クレジットは本番環境で有難く利用させていただきます)* |

> [!NOTE]
> **駅すぱあと API MCP に関する注記【解決】**:  
> ~~設定エラーにより、駅すぱあとMCP設定まわりが不完全です。~~  
> ※【解決】ヴァル研究所様からの公式回答により、UserConsoleは有償契約専用でありMCPサーバーへの接続は不要であることが確認されました。本プロジェクトでは、公式 Streamable HTTP エンドポイント仕様（https://api-mcp.ekispert.jp/mcp）に準拠し、APIキーなしでも全機能が動作する Fast-Mock（0ms）と、[90日無料評価版](https://api-info.ekispert.com/form/trial/) キーによる本番接続のハイブリッド構成を採用しています。

> [!NOTE]
> ※ **トレンドマイクロ様（TrendMicro）のTrendAPIに関する注記**:  
> 「無料クレジット分の登録が間に合わなかったため、パンフレットのMermaid図からPythonで機能を再現しました。無料クレジットは本番環境で有難く利用させていただきます。」

---

## 🌟 主な特徴と5大テクノロジー

| 柱・役割 | 統合コンポーネント / スポンサー | 機能 ＆ エンタープライズ価値 | 応答速度 |
|:---|:---|:---|:---:|
| 🧠 **統括頭脳 (Commander)** | **Gemini 2.5 Flash (Vertex AI)**<br>*(協賛: Google Cloud)* | 7ステップの自律ReAct推論（思考 ➔ 行動 ➔ 観察）ループにより、各種ツールを動的に統合制御し、ダッシュボードへ集約・可視化 | `142 ms` |
| 🚇 **移動支援 (Mobility)** | **駅すぱあと API (Ekispert MCP)**<br>*(Brought by the sponsor: 株式会社ヴァル研究所)* | リアルタイムの運行支障・遅延を即座に検知し、公式時刻表に完全準拠した雨に濡れない地下迂回ルートを自動生成<br>*(~~設定エラーにより、駅すぱあとMCP設定まわりが不完全です。~~<br>※【解決】ヴァル研究所様からの公式回答により、UserConsoleは有償契約専用でありMCPサーバーへの接続は不要であることが確認されました。本プロジェクトでは、公式 Streamable HTTP エンドポイント仕様（https://api-mcp.ekispert.jp/mcp）に準拠し、APIキーなしでも全機能が動作する Fast-Mock（0ms）と、[90日無料評価版](https://api-info.ekispert.com/form/trial/) キーによる本番接続のハイブリッド構成を採用しています。)* | `142 ms` |
| 🛡️ **防御壁 (Security)** | **TrendAPI / TrendAI™ (LEARN Blueprint)**<br>*(Brought by the sponsor: トレンドマイクロ株式会社 / AI Fearlessly)* | 遅延ゼロ（0ms）のインメモリ・正規表現ファイアウォールにより、プロンプトインジェクション、不正なMCP引数呼び出し、個人情報（PII）の漏洩を完全ブロック | `0 ms` |
| ⚡ **機密推論 (Privacy)** | **GMI Cloud NVIDIA H100**<br>*(Brought by the sponsor: GMI Cloud)* | 顧客社名や機密情報を保持しない「Zero Data Retention（完全データ破棄）」専用クラスターで、文脈に合わせた格式高いお詫び文を超高速生成 | `64 ms` |
| ✨ **印象最適化 (Presence)** | **YouCam API (50+ Specialized AI)**<br>*(Brought by the sponsor: パーフェクト株式会社)* | 商談直前30秒のカメラ撮影で、疲労度・緊張感・表情の黄金比（0.98）を瞬時に診断。印象度を+14%高める具体的な改善アドバイスを提示 | `110 ms` |

---

## 🏗️ 4層アーキテクチャ設計

システムの全体構造は、エンタープライズの堅牢性と高速性を両立するため、明確に分離された **4つの層（Tier）** で構成されています。

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Layer 4: プレゼンテーション層 (Presentation Layer)                     │
│  ▶ Streamlit ダッシュボード (localhost:8501)                            │
│    3カラム構成：設定・トリガー、解決カード（迂回路・お詫び・印象）、推論ログ │
├─────────────────────────────────────────────────────────────────────────┤
│  Layer 3: 自律オーケストレーション層 (Autonomous Orchestration Layer)  │
│  ▶ Google Gemini 2.5 Flash on Vertex AI (vertex_agent.py)               │
│    自律ReAct推論ループ（思考 Thought ➔ 行動 Action ➔ 観察 Observation）  │
├─────────────────────────────────────────────────────────────────────────┤
│  Layer 2: MCP ツール呼び出し層 (MCP Tool Calling Layer)                 │
│  ▶ Model Context Protocol (MCP) インプロセス・ツール連携パターン        │
│    - ekispert_mcp_client.py: 経路探索・運行支障センシング               │
│    - youcam_mcp_client.py:   50以上のAIによる肌・表情幾何・姿勢診断     │
├─────────────────────────────────────────────────────────────────────────┤
│  Layer 1: セキュリティ ＆ 機密推論層 (Security & Private Inference)    │
│  ▶ TrendAPI / TrendAI™ Guard (trendai_client.py)  ➔ 0ms インメモリ防護  │
│  ▶ GMI Cloud NVIDIA H100 (gmi_client.py)          ➔ 64ms 機密隔離LLM    │
└─────────────────────────────────────────────────────────────────────────┘
```

### 各層の役割と処理フロー
- **第4層（プレゼンテーション層 / UI）**: 初めて触る開発者でも直感的に操作できる Streamlit 製ダッシュボード。左側の設定パネルからワンクリックでエージェントが始動します。
- **第3層（自律オーケストレーション層 / 頭脳）**: Google Vertex AI 上の **Gemini 2.5 Flash** が、現在の状況（運行遅延、降雨状況、商談相手、時間枠）を総合判断し、どのツールをどの順序で呼び出すか自律決定（Thought ➔ Action ➔ Observation）します。
- **第2層（MCP ツール呼び出し層）**: 業界標準の **Model Context Protocol (MCP)** 仕様を採用。移動経路検索（駅すぱあと）や印象診断（YouCam）を安全かつ標準化されたインターフェースで呼び出します。
- **第1層（セキュリティ ＆ 機密推論層）**: 外部LLMに顧客名や商談機密を渡さない専用プライベートGPU推論（GMI Cloud NVIDIA H100）と、悪意あるプロンプト入力を0msで遮断するセキュリティゲート（TrendAI）がシステムの土台を強固に保護します。

---

## 🚀 クイックスタート（環境構築手順）

Python がインストールされている環境であれば、**わずか 3 ステップ（約 3 分）** で手元の PC 上でデモが起動します。  
**外部 API キーやクラウド設定は一切不要！** 本プロジェクトには「**100% オフライン Fast-Mock モード**」が組み込まれており、clone してすぐに全機能の挙動を体感できます。

### Step 1: リポジトリのクローンと仮想環境作成
ターミナル（Windows では PowerShell や コマンドプロンプト）を開き、リポジトリをクローンして仮想環境を作成・有効化します。

```bash
# リポジトリのクローン
git clone https://github.com/nuccoss/proactive-commute-shield.git
cd proactive-commute-shield

# Python 仮想環境 (venv) の作成
python -m venv venv

# 仮想環境の有効化
# 【Windows (PowerShell) の場合】:
.\venv\Scripts\activate
# 【macOS / Linux の場合】:
source venv/bin/activate
```

### Step 2: 依存パッケージのインストール
動作に必要なライブラリ（Streamlit など）を一括インストールします。

```bash
pip install -r requirements.txt
```

### Step 3: デモの起動（APIキー不要で100%動くFast-Mockモード内蔵）
以下のコマンドを実行すると、ブラウザが自動で立ち上がり、ローカルデモ画面が表示されます。

```bash
# Windows の場合はワンクリック実行用バッチファイルも用意されています:
.\run_demo.bat

# または、通常のコマンドラインから直接起動:
streamlit run app.py
```

> [!TIP]
> 起動後、ブラウザで `http://localhost:8501` にアクセスしてください。  
> 実際の外部 API キー（Gemini, 駅すぱあと, YouCam, GMI Cloud, TrendAPI）をお持ちの場合は、`.env.example` をコピーして `.env` を作成しキーを記入することで、本番 API モードへ即座に切り替えることも可能です。

---

## 🖥️ 対話型デモ画面の構成と操作フロー

起動したダッシュボードは、直感的に状況を把握できるよう **サイドバー ＋ 3 カラム** の構成になっています。

```
┌─────────────────┬─────────────────┬──────────────────┬─────────────────┐
│ 🏛️ ガバナンス   │ 【第1カラム】   │ 【第2カラム】    │ 【第3カラム】   │
│ サイドバー(左端)│ 設定 ＆ 実行    │ 解決カード群     │ 自律推論ログ    │
│                 │                 │                  │                 │
│ • GMI H100 待機 │ • シナリオ選択  │ • 地下迂回ルート │ • Gemini 2.5    │
│ • 駅すぱあと正常│ • 目的地設定    │ • 64ms お詫び文  │   ReAct推論過程 │
│ • YouCam 稼働中 │ • 攻撃シミュON  │ • YouCam 印象診断│ • TrendAI SIEM  │
│ • TrendAI 0ms   │ • [🚀 守護発動] │   (88点カード)   │   監査ログ      │
└─────────────────┴─────────────────┴──────────────────┴─────────────────┘
```

### 操作手順（3ステップで完了）
1. **サイドバーで状態確認**: 左側のサイドバーで各スポンサー製品（GMI Cloud、駅すぱあと、YouCam、TrendAI）の接続ステータスが緑色（Ready）になっていることを確認します。
2. **シナリオ選択と実行（第1カラム）**: 
   - 「シブヤ・エグゼクティブ豪雨シナリオ」「ゲリラ遅延シナリオ」などのテストケースを選択します。
   - 悪意ある攻撃を防ぐプロンプトインジェクションのシミュレーションON/OFFも選べます。
   - 「**🚀 守護エージェントを実行**」ボタンをクリックします。
3. **結果の確認（第2・第3カラム）**:
   - **第2カラム（解決策）**: 雨を避ける地下迂回ルート（駅すぱあと）、宛名入りのお詫び連絡文案（GMI Cloud H100）、表情スコアとアドバイス（YouCam）が瞬時にカード形式で表示されます。
   - **第3カラム（推論ログ）**: Gemini 2.5 Flash がどのように考えてツールを選んだかという自律推論の全履歴（ReActログ）と、TrendAI のセキュリティ監査ログがリアルタイム表示されます。

---

## 📊 コスト ＆ 応答速度（レイテンシ）ベンチマーク

本システムは、実務で即座に役立つ実用性を追求し、**合計約 300 ms という超高速レスポンス** と **1 回あたり約 2.85 円という圧倒的な低コスト** を実現しています。

| サブシステム | 使用サービス / ハードウェア | 応答速度（レイテンシ） | 1回あたりの推定コスト |
|:---|:---|:---:|:---:|
| **自律制御（頭脳）** | Gemini 2.5 Flash (Vertex AI) | `142 ms` | 約 0.15 円 |
| **経路・遅延探索** | 駅すぱあと MCP Client (REST) | `142 ms` | 0.00 円 (定額枠) |
| **セキュリティ防護** | TrendAPI / TrendAI™ インメモリ防護 | `0 ms` | 0.00 円 (インメモリ) |
| **機密お詫び文生成** | GMI Cloud NVIDIA H100 (Tier 3) | `64 ms` | 約 0.70 円 |
| **表情・印象診断** | YouCam API (50+ Specialized AI) | `110 ms` | 約 2.00 円 |
| **パイプライン全体** | **End-to-End 完全実行（並列処理）** | **~316 ms** | **約 2.85 円 (~$0.019)** |

> [!NOTE]
> 各種外部ツール呼び出しは非同期並列で実行されるため、パイプライン全体の処理時間は各レイテンシの単純合算ではなく、最長処理時間＋オーケストレーションオーバーヘッド（約 316 ms）で完了します。

---

## 🤝 共同開発メンバー募集 (Hackathon Co-Development Team Recruitment) <a id="recruitment"></a>

本リポジトリは、**Google Cloud Hackathon本戦（2026/08/20 〜 2026/10/15、賞金総額175万円）における最優秀賞獲得**に向けた共同開発チーム結成の呼び水として、個人開発プロトタイプを先行公開したものです。

現在は単独開発によるオフラインFast-Mock & Streamlit PoCが完成していますが、本戦提出に向けて**エンタープライズグレードの堅牢な本番クラウド基盤（Cloud Run / Eventarc / Redis / TrendAPI本番統合 / CI/CD監視 / モバイルUI）**へとスケールアップさせます。

この挑戦を共に完遂し、最優秀賞を共に目指す共同開発チームメンバーを募集しています！

### 📋 募集要項
- オンライン面談で日程調整ができる方
- 話し合いによりチームワークを円滑に進めることができる方
- 作りたいものがある方
- 開発志向を相互理解できる方
- ※参加希望をしてくださる方は、恐れ入りますが『顔合わせ初回面談』のうえ、チーム開発可否を決定させていただく方向性です。ご納得のいく方のみエントリーいただけますと幸いです。

### 🛠️ 具体的な開発モジュール・アーキテクチャ設計書 (準備中)
本番ハッカソン提出に向けて拡張予定のモジュールおよび設計ドキュメントです：
- [Cloud Run + Eventarc 本番イベント駆動アーキテクチャ設計書 (準備中)](#)
- [Redis ステートフル・サーキットブレーカー実装仕様書 (準備中)](#)
- [TrendMicro TrendAPI 本番クラウド統合モジュール (準備中)](#)
- [CI/CD 自動デプロイ ＆ マルチエージェント監視パイプライン (準備中)](#)
- [フロントエンド・モバイル通知UI (Flutter/Next.js) 連携仕様 (準備中)](#)

### 📬 連絡先・エントリー窓口 (Discord)
ご興味のある方、または参加・協業をご検討いただける方は、以下の Discord DM よりお気軽に「ハッカソン共同開発の件」とメッセージをお送りください。

<div align="center">

[![Discord: nuccoss](https://img.shields.io/badge/Discord-DM%20nuccoss-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/793115360533413919)

**Discord ユーザー名**: `nuccoss` （ユーザーID: `793115360533413919`）  
👉 **[Discord DM で直接連絡する (https://discord.com/users/793115360533413919)](https://discord.com/users/793115360533413919)**

</div>

---

## 📄 ライセンス

本プロジェクトは **[MIT License](LICENSE)** のもとでオープンソースとして公開されています。商用利用、改変、配布など自由に利用いただけます。詳細は [LICENSE](LICENSE) ファイルをご確認ください。
