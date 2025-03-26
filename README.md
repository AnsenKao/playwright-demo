
# Playwright API Demo

這是一個簡單的自動化測試專案，使用 Python + Playwright 搭配 GitHub Actions，針對公開網站（例如：AUO 履歷系統）進行基本的 UI 測試行為，例如：註冊、登入、忘記密碼按鈕跳轉。

同時整合了 SonarQube 靜態分析功能，可在 CI 流程中同時進行前端 UI 測試與程式碼品質檢查。

---

## 📦 安裝依賴

```bash
pip install -r requirements.txt
```

---

## 🧪 執行測試（本地）

```bash
pytest --html=report.html
```

---

## ⚙️ CI/CD 整合（GitHub Actions）

每次 push / pull request，GitHub Actions 會自動：

- 安裝 Python 依賴與 Playwright runtime
- 執行 UI 自動化測試（Playwright）
- 執行程式碼靜態分析（SonarQube）
- 產出測試報告（HTML）與品質分析報告

---

## 🔍 SonarQube 說明

本專案整合 SonarQube CLI 與 GitHub Actions，支援自動掃描 Python 專案的：

- Code Smells
- Bugs
- Duplications
- Security Hotspots

你可以透過 CI 設定將分析結果上傳至 [SonarCloud](https://sonarcloud.io) 或自架的 SonarQube Server。

---

## 📁 專案結構示意

```
.
├── tests/                    # 放置 Playwright 測試腳本
│   └── test_homepage.py
│   └── test_math_util.py
├── .github/
│   └── workflows/            # CI 自動執行流程
│       └── sanity-check.yml
│       └── sonar-ci.yml
├── myapp/                    # 簡單 app util 測試 coverage
│   └── __init__.py
│   └── math_util.py
├── requirements.txt
├── README.md
└── pytest.ini
```
