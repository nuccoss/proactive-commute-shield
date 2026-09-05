# 🚇 Proactive Commute Shield Enterprise — ピッチ用技術解説（最終版）

> 💡 **2h制限時間MVP**: 本リポジトリおよび技術仕様は、2026/09/05(土)にGoogle渋谷にて開催された『[第5回 Agentic AI Hackathon with Google Cloud](https://zenn.dev/hackathons/google-cloud-japan-ai-hackathon-vol5)のスピンオフイベント：ミニハッカソン 渋谷（渋谷ストリーム）』にて、2時間制限時間内で完成させたMVP（Minimum Viable Product）の記録です。

**これはStreamlitですか？WebMCPですか？** → **Streamlit です（WebMCP ではありません）**

---

## 🏗️ 4層技術アーキテクチャ（ピッチ説明フレーム）

```
┌─────────────────────────────────────────────────────────┐
│  Layer 4: UI Layer（見た目）                             │
│  ▶ Streamlit（Python製ブラウザアプリ / localhost:8501）  │
│    単一の app.py → Chrome上で動作する3カラムダッシュボード│
│    WebMCP ではなく、Python製データアプリフレームワーク    │
├─────────────────────────────────────────────────────────┤
│  Layer 3: Orchestration Layer（司令塔）                  │
│  ▶ Google Gemini 2.5 Flash on Vertex AI                 │
│    ReAct（Reasoning + Acting）ループで5ステップを自律制御 │
│    vertex_agent.py がThought/Action/Observationを生成   │
├─────────────────────────────────────────────────────────┤
│  Layer 2: MCP Tool Calling Layer（ツール呼出し）         │
│  ▶ Anthropic Model Context Protocol (MCP) パターン適用  │
│    ekispert_mcp_client.py: 駅すぱあとRESTをMCPツール化   │
│    youcam_mcp_client.py:   YouCam APIをMCPツール化       │
│    ※「WebMCP」=MCPをWeb上で動かす構成。本製品はローカル  │
│      Pythonプロセス内でMCPパターンを実装（in-process）   │
├─────────────────────────────────────────────────────────┤
│  Layer 1: Security & Inference Layer（守護・推論）       │
│  ▶ TrendAI LEARN Blueprint (0ms In-Memory Guard)        │
│    GMI Cloud NVIDIA H100（64ms 超爆速 / Zero-Retention）│
│    trendai_client.py / gmi_client.py                   │
└─────────────────────────────────────────────────────────┘
```

> ※注記1: トレンドマイクロ様（Trend Micro）のTrendAPIについて、無料クレジット分の登録が間に合わなかったため、パンフレットのMermaid図からPythonで機能を再現しました。無料クレジットは本番環境で有難く利用させていただきます。  
> ※注記2: ~~設定エラーにより、駅すぱあとMCP設定まわりが不完全です。~~  
> ※【解決】ヴァル研究所様からの公式回答により、UserConsoleは有償契約専用でありMCPサーバーへの接続は不要であることが確認されました。本プロジェクトでは、公式 Streamable HTTP エンドポイント仕様（https://api-mcp.ekispert.jp/mcp）に準拠し、APIキーなしでも全機能が動作する Fast-Mock（0ms）と、[90日無料評価版](https://api-info.ekispert.com/form/trial/) キーによる本番接続のハイブリッド構成を採用しています。


---

## ✅ 「WebMCPではなくStreamlit」の根拠

| 比較点 | 本製品の実装 | WebMCP |
|:---|:---|:---|
| **UIフレームワーク** | Streamlit (Python, `app.py`) | 別途WebMCPサーバー |
| **通信方式** | In-Process Python呼び出し | stdio / HTTP + SSE |
| **起動方法** | `streamlit run app.py` | MCPサーバー起動 + クライアント |
| **プロセス構成** | 単一Pythonプロセス | 複数プロセス協調 |
| **「MCP」の意味** | Anthropic MCPの**アーキテクチャパターン**を適用 | MCP**プロトコル**そのもので通信 |

**一言まとめ**: 「UIはStreamlit、内部の設計思想はMCPのツール呼び出しパターン」

---

## 🎤 4分ピッチ用 技術説明スクリプト（30秒版）

> 「このアプリは **Streamlit** というPythonフレームワークで作ったブラウザアプリです。  
> 見た目は1画面ですが、内部では **4つの技術層**が協調しています。  
>
> まず、**協賛（Mainスポンサー）Google Cloud の Gemini 2.5 Flash**がReActループで全体を司令。  
> 次に、**Brought by the sponsor (提供サービス) のヴァル研究所（駅すぱあと API）とパーフェクト（YouCam API）**をAnthropicのMCPパターンでツール化し、AIから呼び出せるようにしました。  
> お詫び文の生成は**Brought by the sponsor (提供サービス) GMI Cloud の NVIDIA H100**が64ミリ秒でセキュアに処理。  
> そして、すべての通信を**Brought by the sponsor (提供サービス) TrendAI™ の LEARN Blueprint**が0ミリ秒でリアルタイム防御します。  
>
> 4層が1ボタンで連動し、突発遅延から商談まで人を守り抜く——  
> これが Proactive Commute Shield Enterprise です。」

---

## 📊 公式協賛（Mainスポンサー）✕ Brought by the sponsor (提供サービス 4社 4製品) 統合アーキテクチャマップ

本製品は、**主催：Zenn（クラスメソッド株式会社）** が提供するコンテスト基盤の上で、**協賛（Mainスポンサー）：グーグル・クラウド・ジャパン合同会社（Google Cloud）** の最上位オーケストレーションAIと、**Brought by the sponsor (提供サービス 4社 4製品)** の特化型テクノロジーを階層的に統合しています。

### 公式スポンサーシップ・タクソノミー（Sponsorship Taxonomy）

| 階層 / 役割 | スポンサー種別 | 正式企業名 | 提供プロダクト / API | アーキテクチャ実装 |
|:---|:---|:---|:---|:---|
| **Platform** | **主催** | **Zenn（クラスメソッド株式会社）** | 公式コンテスト基盤 | 技術知見共有 & イベントプラットフォーム |
| **Commander** | **協賛（Mainスポンサー）** | **グーグル・クラウド・ジャパン合同会社** | **Google Cloud (Vertex AI Gemini 2.5 Flash)** | **Layer 3: Autonomous Orchestrator**<br>自律ReAct推論ループによる総合意思決定 |
| **Tool: Mobility** | **Brought by the sponsor (提供サービス)** | **株式会社ヴァル研究所** | **駅すぱあと API** | **Layer 2: Ekispert MCP Client**<br>運行支障検知・地下迂回路線探索<br>~~設定エラーにより、駅すぱあとMCP設定まわりが不完全です。~~<br>※【解決】ヴァル研究所様からの公式回答により、UserConsoleは有償契約専用でありMCPサーバーへの接続は不要であることが確認されました。本プロジェクトでは、公式 Streamable HTTP エンドポイント仕様（https://api-mcp.ekispert.jp/mcp）に準拠し、APIキーなしでも全機能が動作する Fast-Mock（0ms）と、[90日無料評価版](https://api-info.ekispert.com/form/trial/) キーによる本番接続のハイブリッド構成を採用しています。 |
| **Tool: Presence** | **Brought by the sponsor (提供サービス)** | **パーフェクト株式会社 (PERFECT Corp.)** | **YouCam API** | **Layer 2: YouCam MCP Client**<br>50種AIによる表情・身だしなみ即時診断 |
| **Private GPU** | **Brought by the sponsor (提供サービス)** | **GMI (GMI Cloud)** | **GMI Cloud NVIDIA H100** | **Layer 1: Private LLM Engine**<br>Zero Data Retention / 64ms 機密お詫び文生成 |
| **Cybersecurity** | **Brought by the sponsor (提供サービス)** | **TrendAI™ (AI Fearlessly / TrendAI)** | **TrendAI™ Security Blueprint** | **Layer 1: In-Memory Shield**<br>0ms インジェクション遮断 / PII マスキング |

> ※注記1: トレンドマイクロ様（Trend Micro）のTrendAPIについて、無料クレジット分の登録が間に合わなかったため、パンフレットのMermaid図からPythonで機能を再現しました。無料クレジットは本番環境で有難く利用させていただきます。  
> ※注記2: ~~設定エラーにより、駅すぱあとMCP設定まわりが不完全です。~~  
> ※【解決】ヴァル研究所様からの公式回答により、UserConsoleは有償契約専用でありMCPサーバーへの接続は不要であることが確認されました。本プロジェクトでは、公式 Streamable HTTP エンドポイント仕様（https://api-mcp.ekispert.jp/mcp）に準拠し、APIキーなしでも全機能が動作する Fast-Mock（0ms）と、[90日無料評価版](https://api-info.ekispert.com/form/trial/) キーによる本番接続のハイブリッド構成を採用しています。

### システム統合フロー図

```
主催: Zenn (クラスメソッド株式会社) / 期間: 2026.08.20 - 10.15 (310 Entries)
─────────────────────────────────────────────────────────────────────────────
ユーザー（突発的な移動遅延が発生）
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 【協賛: Mainスポンサー】グーグル・クラウド・ジャパン合同会社 (Google Cloud)       │
│ 🧠 Gemini 2.5 Flash on Vertex AI ─── Autonomous ReAct Orchestrator      │
│    Thought ➔ Action ➔ Observation 意思決定ループで全ツールを統括指揮     │
└───────┬──────────────────────┬──────────────────────┬───────────────────┘
        │                      │                      │
        ▼                      ▼                      ▼
┌──────────────────┐   ┌──────────────────┐   ┌───────────────────────────┐
│【提供サービス】    │   │【提供サービス】    │   │【提供サービス】           │
│株式会社ヴァル研究所 │   │パーフェクト株式会社  │   │GMI (GMI Cloud)            │
│🚇 駅すぱあと API  │   │✨ YouCam API     │   │⚡ NVIDIA H100 Dedicated   │
│(Ekispert MCP)    │   │(50+ Specialized) │   │(Zero Data Retention)      │
│地下迂回路線探索  │   │表情・印象度診断  │   │機密お詫び文高速起票(64ms) │
└───────┬──────────┘   └───────┬──────────┘   └─────────────┬─────────────┘
        │                      │                            │
        └──────────────────────┼────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│【Brought by the sponsor (提供サービス)】TrendAI™ (Trend Micro)          │
│🛡️ TrendAI™ LEARN Security Blueprint ─── 0ms インメモリ・ファイアウォール│
│全入出力の Prompt Injection 遮断、PII 秘匿化、MCP 引数サニタイズを完全保証│
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Layer 4: Presentation Layer (Streamlit Mission Control UI / app.py)    │
│  全スポンサー連携の実行状況・レイテンシ・ログを1画面ダッシュボードに可視化│
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🤝 本戦に向けた共同開発アーキテクチャ（準備中モジュール）

本ハッカソンピッチ版（PoC）の成功を踏まえ、10月15日締切の Google Cloud ハッカソン本戦（賞金総額175万円）に向けたエンタープライズ大規模拡張モジュールを設計しています。現在、共同開発チームメンバーを募集中です。

### 🚀 拡張準備中モジュール
- [Cloud Run + Eventarc イベント駆動連携仕様 (準備中)](#)
- [TrendMicro TrendAPI クラウド連携モジュール (準備中)](#)
- [Redis 分散ステートフル・キャッシュ (準備中)](#)

### 👥 チーム開発メンバー募集（Co-Development Recruitment）
本戦に向け、Google Cloud インフラ構築、セキュリティ連携、フロントエンド/エージェント拡張を共に推進するチームメンバーを歓迎します。
- **応募・コンタクト**: Discord DM よりご連絡ください
  - **Discord 連絡先**: [nuccoss (ID: 793115360533413919)](https://discord.com/users/793115360533413919)
- **選考プロセス**: オンラインでの顔合わせ・カジュアル面談を実施の上、役割分担を決定いたします。

---

**Architecture Lead**: CommuteShield Engineering Team (nuccoss)  
**Event**: Zenn AI Hackathon (Organizer: Classmethod / Main Sponsor: Google Cloud)  
**Purpose**: Proactive Commute Shield Technical Architecture Specification  
**License**: MIT License  
