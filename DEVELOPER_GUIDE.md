# 🔧 開發者指南：程式碼品質工具

本指南說明如何使用專案中配置的程式碼品質工具。

## 🚀 快速開始

### 自動設置 (推薦)

```bash
# 克隆專案後自動安裝所有依賴和 pre-commit hooks
make setup
```

### 手動設置

```bash
# 安裝依賴
uv sync --dev

# 安裝 pre-commit hooks
uv run pre-commit install
```

## 🛠️ 可用工具

### 核心工具

| 工具         | 功能                      | 命令                  |
| ------------ | ------------------------- | --------------------- |
| **Ruff**     | 快速 linting + formatting | `make lint`           |
| **Black**    | 程式碼格式化              | `make format`         |
| **isort**    | 導入語句排序              | `make sort-imports`   |
| **Bandit**   | 安全問題檢查              | `make security-check` |
| **Prettier** | 格式化文檔檔案            | `make format-docs`    |

### 整合命令

```bash
# 執行所有檢查
make check-all

# 修復所有可自動修復的問題
make fix-all

# 執行測試 + 覆蓋率
make test

# 清理快取檔案
make clean
```

## 🔄 Pre-commit Hooks

### 自動執行

每次 `git commit` 時，以下檢查會自動執行：

1. **Ruff linting** - 檢查程式碼問題並自動修復
2. **Ruff formatting** - 統一程式碼格式
3. **Black formatting** - 確保一致的程式碼風格
4. **isort** - 排序導入語句
5. **基本檢查**:
   - 移除尾隨空白
   - 檔案結尾換行
   - YAML/TOML/JSON 語法檢查
   - 大檔案檢查
   - 合併衝突檢查
6. **Bandit** - 安全問題掃描
7. **Prettier** - 格式化文檔檔案

### 手動執行

```bash
# 在所有檔案上執行 pre-commit
uv run pre-commit run --all-files

# 執行特定 hook
uv run pre-commit run ruff --all-files
uv run pre-commit run black --all-files
```

## 📋 常見使用情境

### 開發過程中

```bash
# 開發時持續檢查
make lint-watch  # 監看檔案變化並自動 lint

# 修復格式問題
make fix-format

# 檢查安全問題
make security-check
```

### 提交前檢查

```bash
# 完整檢查 (CI 流程)
make ci-check

# 快速檢查
make quick-check
```

### 新增檔案後

```bash
# 檢查新檔案
make lint-new

# 格式化新檔案
make format-new
```

## ⚙️ 配置說明

### pyproject.toml

所有工具的配置都在 `pyproject.toml` 中：

```toml
[tool.ruff]
target-version = "py313"
line-length = 88

[tool.ruff.lint]
select = ["E", "W", "F", "I", "B", "C4", "UP"]
ignore = ["E501", "B008"]

[tool.black]
line-length = 88
target-version = ['py313']

[tool.isort]
profile = "black"
line_length = 88

[tool.bandit]
exclude_dirs = ["tests", ".venv", "venv"]
```

### .pre-commit-config.yaml

Pre-commit hooks 的配置，可以自定義：

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.0
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format
```

## 🚫 跳過檢查

### 緊急情況下跳過 pre-commit

```bash
git commit --no-verify -m "緊急修復"
```

### 跳過特定規則

```python
# 在程式碼中跳過特定規則
import os  # noqa: F401  # 跳過未使用導入的檢查

def function():
    password = "secret"  # nosec B105  # 跳過 Bandit 檢查
```

## 🔧 自定義配置

### 修改 linting 規則

編輯 `pyproject.toml` 中的 `[tool.ruff.lint]` 區段：

```toml
[tool.ruff.lint]
select = ["E", "W", "F", "I", "B", "C4", "UP", "D"]  # 新增 D (docstring)
ignore = ["E501", "B008", "D100"]  # 忽略特定規則
```

### 新增 pre-commit hook

編輯 `.pre-commit-config.yaml`：

```yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.16.0
    hooks:
      - id: mypy
```

## 📊 品質指標

### 目標指標

- **Ruff violations**: 0
- **Black formatting issues**: 0
- **Security issues (Bandit)**: 0
- **Test coverage**: > 80%
- **Import sorting**: 正確

### 檢查狀態

```bash
# 取得品質報告
make quality-report
```

## 🤝 團隊協作

### 新成員加入

1. `git clone` 專案
2. `make setup` 自動設置
3. `make check-all` 確認環境正常

### 程式碼審查

- Pre-commit hooks 確保基本品質
- CI 執行完整檢查
- 人工審查專注在邏輯和設計

### 最佳實踐

1. **小批次提交** - 更容易通過檢查
2. **及早修復** - 不要累積 linting 問題
3. **使用 make 命令** - 統一的執行方式
4. **定期更新工具** - `make update-tools`

## 🆘 故障排除

### 常見問題

**Q: Pre-commit hook 執行失敗**

```bash
# 更新 pre-commit hooks
uv run pre-commit autoupdate

# 重新安裝
uv run pre-commit uninstall
uv run pre-commit install
```

**Q: Ruff 和 Black 衝突**

- 配置已確保兼容性
- 如有問題，執行 `make fix-format`

**Q: 檔案格式化後仍有問題**

```bash
# 清理快取並重新檢查
make clean
make check-all
```

**Q: 特定檔案一直報錯**

```bash
# 檢查特定檔案
uv run ruff check path/to/file.py --diff
uv run black --check path/to/file.py
```

## 📈 進階使用

### CI/CD 整合

```yaml
# GitHub Actions 範例
- name: Lint and format check
  run: |
    uv run pre-commit run --all-files
    make test
```

### IDE 整合

建議在 VS Code 中安裝：

- Ruff extension
- Black formatter
- isort extension

### 自動修復腳本

```bash
#!/bin/bash
# scripts/auto-fix.sh
make fix-all
make test
git add -A
echo "程式碼已自動修復並測試通過"
```

---

## 🎯 總結

這個設置提供：

- **一致的程式碼風格**
- **自動錯誤檢測**
- **安全問題預防**
- **團隊協作效率**
- **維護成本降低**

遵循這些工具和流程，團隊可以專注在功能開發上，而不用擔心程式碼品質問題。
