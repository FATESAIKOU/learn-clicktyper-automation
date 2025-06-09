"""
Learn CLI - Typer 和 Click 學習專案

這個專案展示了如何使用 Typer 和 Click 兩個不同的 Python CLI 框架。

使用方式:
- typer: 使用 Typer 框架的 CLI 應用程式
- click: 使用 Click 框架的 CLI 應用程式
"""

__version__ = "0.1.0"

def main() -> None:
    """
    主要進入點 - 讓使用者選擇要使用哪個 CLI 框架
    """
    import sys
    import importlib.util
    from pathlib import Path
    
    # 動態導入 CLI 模組
    def import_module_from_path(module_name, file_path):
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    
    if len(sys.argv) < 2:
        print("學習 Typer 和 Click CLI 框架")
        print("")
        print("使用方式:")
        print("  learn-clicktyper-automation typer [命令]  # 使用 Typer 版本")
        print("  learn-clicktyper-automation click [命令]  # 使用 Click 版本")
        print("")
        print("範例:")
        print("  learn-clicktyper-automation typer greet Alice")
        print("  learn-clicktyper-automation click greet Bob")
        print("  learn-clicktyper-automation typer --help")
        print("  learn-clicktyper-automation click --help")
        return
    
    framework = sys.argv[1]
    
    # 找到 CLI 模組的路徑
    current_dir = Path(__file__).parent.parent
    typer_path = current_dir / "learn_cli" / "typer_app.py"
    click_path = current_dir / "learn_cli" / "click_app.py"
    
    if framework == "typer":
        # 移除 'typer' 參數，讓 typer 處理剩餘的參數
        sys.argv = [sys.argv[0]] + sys.argv[2:]
        if typer_path.exists():
            typer_module = import_module_from_path("typer_app", typer_path)
            typer_module.app()
        else:
            print("錯誤: 找不到 typer_app.py")
            sys.exit(1)
    elif framework == "click":
        # 移除 'click' 參數，讓 click 處理剩餘的參數
        sys.argv = [sys.argv[0]] + sys.argv[2:]
        if click_path.exists():
            click_module = import_module_from_path("click_app", click_path)
            click_module.cli()
        else:
            print("錯誤: 找不到 click_app.py")
            sys.exit(1)
    else:
        print(f"錯誤: 未知的框架 '{framework}'. 請使用 'typer' 或 'click'")
        sys.exit(1)
