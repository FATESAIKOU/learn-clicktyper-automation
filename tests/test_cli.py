"""
測試 Typer 和 Click CLI 應用程式

這個檔案包含針對兩個 CLI 框架的基本功能測試。
"""

import pytest
import sys
from pathlib import Path
from typer.testing import CliRunner as TyperCliRunner
from click.testing import CliRunner as ClickCliRunner

# 添加 src 目錄到 Python 路徑
current_dir = Path(__file__).parent
src_path = current_dir.parent / "src"
sys.path.insert(0, str(src_path))

from learn_cli.typer_app import app as typer_app
from learn_cli.click_app import cli as click_app


def test_typer_greet_basic():
    """測試 Typer 基本問候命令"""
    runner = TyperCliRunner()
    result = runner.invoke(typer_app, ["greet", "世界"])
    assert result.exit_code == 0
    assert "你好, 世界!" in result.stdout


def test_typer_greet_with_count():
    """測試 Typer 帶計數的問候命令"""
    runner = TyperCliRunner()
    result = runner.invoke(typer_app, ["greet", "Alice", "--count", "2"])
    assert result.exit_code == 0
    assert result.stdout.count("你好, Alice!") == 2


def test_typer_calc_add():
    """測試 Typer 加法計算"""
    runner = TyperCliRunner()
    result = runner.invoke(typer_app, ["calc", "add", "5", "3"])
    assert result.exit_code == 0
    assert "5.0 + 3.0 = 8.0" in result.stdout


def test_click_greet_basic():
    """測試 Click 基本問候命令"""
    runner = ClickCliRunner()
    result = runner.invoke(click_app, ["greet", "世界"])
    assert result.exit_code == 0
    assert "你好, 世界!" in result.output


def test_click_greet_with_count():
    """測試 Click 帶計數的問候命令"""
    runner = ClickCliRunner()
    result = runner.invoke(click_app, ["greet", "Alice", "--count", "2"])
    assert result.exit_code == 0
    assert result.output.count("你好, Alice!") == 2


def test_click_calc_add():
    """測試 Click 加法計算"""
    runner = ClickCliRunner()
    result = runner.invoke(click_app, ["calc", "add", "5", "3"])
    assert result.exit_code == 0
    assert "5.0 + 3.0 = 8.0" in result.output


def test_click_list_items_json():
    """測試 Click 項目列表 JSON 格式"""
    runner = ClickCliRunner()
    result = runner.invoke(click_app, ["list-items", "--format", "json", "項目1", "項目2"])
    assert result.exit_code == 0
    assert "項目1" in result.output
    assert "項目2" in result.output


def test_typer_interactive_demo():
    """測試 Typer 互動式示範功能"""
    runner = TyperCliRunner()
    # 測試不互動的部分 - 由於互動式命令需要用戶輸入，我們只測試命令存在
    result = runner.invoke(typer_app, ["--help"])
    assert result.exit_code == 0
    assert "interactive-demo" in result.stdout


def test_typer_generate_report():
    """測試 Typer 檔案報告生成"""
    runner = TyperCliRunner()
    with runner.isolated_filesystem():
        # 創建測試檔案
        with open("test.py", "w", encoding="utf-8") as f:
            f.write("print('hello')\nprint('world')")
        
        result = runner.invoke(typer_app, ["generate-report", ".", "--pattern", "*.py", "--format", "json"])
        assert result.exit_code == 0
        assert "test.py" in result.stdout


def test_typer_search_replace():
    """測試 Typer 搜尋替換功能"""
    runner = TyperCliRunner()
    with runner.isolated_filesystem():
        # 創建測試檔案
        test_content = "Hello world\nHello Python\nGoodbye world"
        with open("test.txt", "w", encoding="utf-8") as f:
            f.write(test_content)
        
        result = runner.invoke(typer_app, ["search-replace", "test.txt", "Hello", "Hi"])
        assert result.exit_code == 0
        assert "Hi world" in result.stdout
        assert "Hi Python" in result.stdout


def test_click_interactive_demo():
    """測試 Click 互動式示範功能"""
    runner = ClickCliRunner()
    # 測試不互動的部分 - 由於互動式命令需要用戶輸入，我們只測試命令存在
    result = runner.invoke(click_app, ["--help"])
    assert result.exit_code == 0
    assert "interactive-demo" in result.output


def test_click_random_numbers():
    """測試 Click 隨機數生成功能"""
    runner = ClickCliRunner()
    result = runner.invoke(click_app, ["random-numbers", "--count", "3", "--min-val", "1", "--max-val", "10"])
    assert result.exit_code == 0
    assert "生成 3 個隨機數字" in result.output
    assert "統計:" in result.output


def test_click_generate_report():
    """測試 Click 檔案報告生成"""
    runner = ClickCliRunner()
    with runner.isolated_filesystem():
        # 創建測試檔案
        with open("test.py", "w", encoding="utf-8") as f:
            f.write("print('hello')\nprint('world')")
        
        result = runner.invoke(click_app, ["generate-report", ".", "--pattern", "*.py", "--format", "json"])
        assert result.exit_code == 0
        assert "test.py" in result.output


def test_click_search_replace():
    """測試 Click 搜尋替換功能"""
    runner = ClickCliRunner()
    with runner.isolated_filesystem():
        # 創建測試檔案
        test_content = "Hello world\nHello Python\nGoodbye world"
        with open("test.txt", "w", encoding="utf-8") as f:
            f.write(test_content)
        
        result = runner.invoke(click_app, ["search-replace", "test.txt", "Hello", "Hi"])
        assert result.exit_code == 0
        assert "Hi world" in result.output
        assert "Hi Python" in result.output


def test_typer_greet_all():
    """測試 Typer 綜合問候命令"""
    runner = TyperCliRunner()
    result = runner.invoke(typer_app, [
        "greet-all", 
        ">>> ", 
        "Alice", "Bob", "--title", "女士", 
        "--greeting", "你好",
        "-g", "您好"
    ])
    assert result.exit_code == 0
    assert "prefix: >>> " in result.stdout
    assert "人名列表: ['Alice', 'Bob']" in result.stdout
    assert "稱謂: 女士" in result.stdout
    assert "問候詞: ['你好', '您好']" in result.stdout
    assert "===== 問候結果 =====" in result.stdout
    assert ">>> 你好, 女士 Alice!" in result.stdout
    assert ">>> 您好, 女士 Alice!" in result.stdout
    assert ">>> 你好, 女士 Bob!" in result.stdout
    assert ">>> 您好, 女士 Bob!" in result.stdout


def test_click_greet_all():
    """測試 Click 綜合問候命令"""
    runner = ClickCliRunner()
    result = runner.invoke(click_app, [
        "greet-all", 
        "Alice", "Bob", "女士", 
        "--prefix", ">>> ", 
        "--greeting", "你好",
        "-g", "您好"
    ])
    assert result.exit_code == 0
    assert "prefix: >>> " in result.output
    assert "人名列表: ('Alice', 'Bob')" in result.output
    assert "稱謂: 女士" in result.output
    assert "問候詞: ('你好', '您好')" in result.output
    assert "===== 問候結果 =====" in result.output
    assert ">>> 你好, 女士 Alice!" in result.output
    assert ">>> 您好, 女士 Alice!" in result.output
    assert ">>> 你好, 女士 Bob!" in result.output
    assert ">>> 您好, 女士 Bob!" in result.output