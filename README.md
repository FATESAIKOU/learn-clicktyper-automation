# Learn CLI - Typer 和 Click 學習專案

一個專門學習 Python CLI 框架的專案，展示了 Typer 和 Click 兩個熱門的命令列介面工具。

## 🎯 專案目的

這個專案旨在幫助你學習和比較兩個 Python CLI 框架：

- **Typer**: 基於 type hints 的現代 CLI 框架，語法簡潔
- **Click**: 功能強大且靈活的 CLI 工具包，廣泛使用

## 📦 安裝與設置

這個專案使用 `uv` 作為 Python 包管理工具。

### 前置條件

確保你已安裝 `uv`:
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或使用 pip
pip install uv
```

### 安裝專案

```bash
# 克隆專案
git clone <repository-url>
cd learn-clicktyper-automation

# 安裝依賴
uv sync
```

## 🚀 使用方式

### 基本命令結構

```bash
# 使用 Typer 版本
learn-clicktyper-automation typer [命令] [選項]

# 使用 Click 版本  
learn-clicktyper-automation click [命令] [選項]
```

### 查看幫助

```bash
# 查看主幫助
learn-clicktyper-automation

# 查看 Typer 版本幫助
learn-clicktyper-automation typer --help

# 查看 Click 版本幫助
learn-clicktyper-automation click --help
```

## 🛠️ 功能範例

### 1. 問候功能
```bash
# 基本問候
learn-clicktyper-automation typer greet Alice
learn-clicktyper-automation click greet Bob

# 重複問候
learn-clicktyper-automation typer greet Alice --count 3

# 禮貌問候
learn-clicktyper-automation click greet Alice --polite
```

### 2. 文字處理
```bash
# 字數統計
learn-clicktyper-automation typer count-words "這是一個測試文字"

# 字數統計包含字元數
learn-clicktyper-automation click count-words "測試文字" --chars
```

### 3. 檔案處理
```bash
# 轉換為大寫
learn-clicktyper-automation typer process-file input.txt --uppercase

# 加上行號
learn-clicktyper-automation click process-file input.txt --line-numbers

# 儲存到輸出檔案
learn-clicktyper-automation typer process-file input.txt --output output.txt --uppercase
```

### 4. 計算功能
```bash
# 基本計算
learn-clicktyper-automation typer calc add 10 5
learn-clicktyper-automation click calc mul 3 7
learn-clicktyper-automation typer calc div 15 3
```

### 5. 檔案搜尋替換
```bash
# 搜尋並替換文字
learn-clicktyper-automation typer search-replace input.txt "舊文字" "新文字"

# 大小寫不敏感替換
learn-clicktyper-automation click search-replace input.txt "old" "new" --ignore-case

# 儲存到新檔案
learn-clicktyper-automation typer search-replace input.txt "查找" "替換" --output result.txt
```

### 6. 檔案分析報告
```bash
# 分析目錄中的檔案
learn-clicktyper-automation typer generate-report . --pattern "*.py"

# 以 JSON 格式輸出
learn-clicktyper-automation click generate-report examples --format json

# 分析特定類型檔案
learn-clicktyper-automation typer generate-report src --pattern "*.py" --format text
```

### 7. 互動式功能
```bash
# Typer 互動式示範（包含進度條、提示輸入等）
learn-clicktyper-automation typer interactive-demo

# Click 互動式示範
learn-clicktyper-automation click interactive-demo
```

### 8. Click 專有功能
```bash
# 列表格式化
learn-clicktyper-automation click list-items 項目1 項目2 項目3
learn-clicktyper-automation click list-items --format json A B C
learn-clicktyper-automation click list-items --format csv X Y Z

# 生成隨機數字
learn-clicktyper-automation click random-numbers --count 10 --min-val 1 --max-val 100
learn-clicktyper-automation click random-numbers --count 5 --sort
```

## 🧪 測試

專案包含完整的測試套件：

```bash
# 運行所有測試
uv run pytest

# 運行特定測試
uv run pytest tests/test_cli.py::TestTyperApp

# 顯示測試覆蓋率
uv run pytest --cov=src

# 詳細輸出
uv run pytest -v
```

## 📁 專案結構

```
learn-clicktyper-automation/
├── README.md                 # 專案說明
├── QUICKSTART.md            # 快速開始指南
├── pyproject.toml           # 專案配置
├── uv.lock                  # 依賴鎖定檔案
├── .gitignore              # Git 忽略檔案
├── sample.txt              # 範例文字檔案
├── src/
│   ├── learn_cli/
│   │   ├── typer_app.py     # Typer CLI 應用程式
│   │   └── click_app.py     # Click CLI 應用程式
│   └── learn_clicktyper_automation/
│       └── __init__.py      # 主進入點
├── tests/
│   ├── __init__.py
│   └── test_cli.py          # CLI 測試
└── examples/
    ├── README.md            # 範例說明
    ├── python_info.txt      # 範例文字檔案
    └── example_code.py      # 範例程式碼
```

## 📚 學習重點

### Typer 特色
- 基於 Python type hints，自動生成幫助文件
- 語法簡潔，易於學習
- 自動參數驗證
- 豐富的輸出格式支援（透過 Rich）
- 內建進度條和互動式提示
- 優雅的錯誤處理

### Click 特色
- 靈活的裝飾器語法
- 強大的參數類型系統
- 支援複雜的命令群組
- 豐富的生態系統
- 成熟穩定的框架
- 廣泛的第三方插件支援

### 主要差異對比

| 特性 | Typer | Click |
|------|-------|-------|
| 語法風格 | Type hints | 裝飾器 |
| 學習曲線 | 較緩 | 中等 |
| 功能豐富度 | 現代化 | 全面 |
| 社群支援 | 新興 | 成熟 |
| 自動生成幫助 | 優秀 | 良好 |
| 互動式功能 | 內建 | 需額外配置 |
| 進度條支援 | 內建 | 內建 |

## 🔧 開發工具

- **包管理**: uv
- **測試框架**: pytest
- **類型檢查**: 內建 type hints
- **代碼品質**: 包含完整測試

## 🤝 貢獻

歡迎提交 issue 和 pull request 來改善這個學習專案！

## 📄 授權

MIT License

---

**快樂學習 CLI 開發！** 🎉