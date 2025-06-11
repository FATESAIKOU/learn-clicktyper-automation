# 快速啟動指南

## 🚀 快速開始

### 1. 安裝專案

```bash
cd learn-clicktyper-automation
uv sync
```

### 2. 測試基本功能

```bash
# 查看幫助
uv run learn-clicktyper-automation

# Typer 範例
uv run learn-clicktyper-automation typer greet "你的名字"
uv run learn-clicktyper-automation typer calc add 10 5
uv run learn-clicktyper-automation typer count-words "這是測試文字"

# Click 範例
uv run learn-clicktyper-automation click greet "你的名字" --polite
uv run learn-clicktyper-automation click calc mul 3 7
uv run learn-clicktyper-automation click list-items --format json A B C
```

### 3. 檔案處理範例

```bash
# 使用提供的範例檔案
uv run learn-clicktyper-automation typer process-file sample.txt --line-numbers
uv run learn-clicktyper-automation click process-file sample.txt --uppercase
```

### 4. 運行測試

```bash
uv run pytest tests/ -v
```

## 💡 學習重點

1. **Typer**: 注意 type hints 如何自動生成幫助文件
2. **Click**: 觀察裝飾器語法的使用方式
3. **比較**: 同樣的功能在兩個框架中的不同實現方式

## 🎯 下一步

- 嘗試修改現有命令
- 添加新的命令
- 比較兩個框架的語法差異
- 閱讀 README.md 瞭解更多詳細資訊
