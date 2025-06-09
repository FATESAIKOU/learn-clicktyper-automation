# CLI 使用範例

這個目錄包含了各種範例檔案，可以用來測試 CLI 工具的功能。

## 範例檔案

- `python_info.txt` - 包含關於 Python 的中文文字，適合測試文字處理功能
- `example_code.py` - Python 程式碼範例，適合測試檔案分析功能

## 使用範例

### 1. 文字處理範例

```bash
# 字數統計
uv run learn-clicktyper-automation typer count-words "這是一個測試句子"

# 檔案處理 - 加上行號
uv run learn-clicktyper-automation typer process-file examples/python_info.txt --line-numbers

# 檔案處理 - 轉為大寫
uv run learn-clicktyper-automation click process-file examples/python_info.txt --uppercase
```

### 2. 檔案分析範例

```bash
# 分析 Python 檔案
uv run learn-clicktyper-automation typer generate-report examples --pattern "*.py"

# 以 JSON 格式輸出
uv run learn-clicktyper-automation click generate-report examples --pattern "*.txt" --format json
```

### 3. 搜尋替換範例

```bash
# 替換文字
uv run learn-clicktyper-automation typer search-replace examples/python_info.txt "Python" "程式語言Python"

# 大小寫不敏感替換
uv run learn-clicktyper-automation click search-replace examples/python_info.txt "python" "程式語言" --ignore-case
```

### 4. 互動式功能

```bash
# Typer 互動式示範
uv run learn-clicktyper-automation typer interactive-demo

# Click 互動式示範
uv run learn-clicktyper-automation click interactive-demo
```

### 5. Click 特有功能

```bash
# 生成隨機數字
uv run learn-clicktyper-automation click random-numbers --count 10 --min-val 1 --max-val 100 --sort

# 格式化列表
uv run learn-clicktyper-automation click list-items --format json 項目1 項目2 項目3
```
