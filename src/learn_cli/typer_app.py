"""
Typer CLI 範例 - 一個簡單的文字處理工具

這個檔案展示了如何使用 Typer 創建命令列介面。
Typer 是基於 type hints 的 CLI 框架，語法簡潔易懂。
"""

from pathlib import Path

import typer

# 創建主要的 Typer 應用程式
app = typer.Typer(help="一個簡單的文字處理 CLI 工具 (使用 Typer)")


@app.command()
def greet(
    name: str = typer.Argument(..., help="要問候的人的名字"),
    count: int = typer.Option(1, "--count", "-c", help="重複問候的次數"),
    polite: bool = typer.Option(False, "--polite", "-p", help="使用禮貌的問候方式"),
):
    """
    問候指定的人
    """
    greeting = "您好" if polite else "你好"
    for _ in range(count):
        typer.echo(f"{greeting}, {name}!")


@app.command()
def greet_all(
    prefix: str = typer.Argument(">>> ", help="問候詞前綴"),
    names: list[str] = typer.Argument(..., help="要問候的人名列表（模仿 mv 的 srcs）"),
    title: str = typer.Option(
        "先生/小姐", "--title", "-t", help="稱謂"
    ),  # typer 不支援 narg -1 的選項，所以用 Option
    greeting: list[str] | None = typer.Option(
        None, "--greeting", "-g", help="多種問候詞"
    ),
):
    """
    綜合測試：問候 + 多選項 + 類似 mv 介面
    """
    typer.echo(f"prefix: {prefix}")
    typer.echo(f"人名列表: {names}")
    typer.echo(f"稱謂: {title}")
    typer.echo(f"問候詞: {greeting}")
    typer.echo("===== 問候結果 =====")
    for name in names:
        for g in greeting:
            typer.echo(f"{prefix}{g}, {title} {name}!")


@app.command()
def count_words(
    text: str = typer.Argument(..., help="要計算字數的文字"),
    show_chars: bool = typer.Option(False, "--chars", "-c", help="同時顯示字元數"),
):
    """
    計算文字的字數
    """
    words = len(text.split())
    typer.echo(f"字數: {words}")

    if show_chars:
        chars = len(text)
        typer.echo(f"字元數: {chars}")


@app.command()
def process_file(
    file_path: Path = typer.Argument(..., help="要處理的檔案路徑"),
    output: Path | None = typer.Option(None, "--output", "-o", help="輸出檔案路徑"),
    uppercase: bool = typer.Option(False, "--uppercase", "-u", help="轉換為大寫"),
    line_numbers: bool = typer.Option(False, "--line-numbers", "-n", help="加上行號"),
):
    """
    處理文字檔案
    """
    try:
        # 讀取檔案
        content = file_path.read_text(encoding="utf-8")
        lines = content.splitlines()

        # 處理內容
        processed_lines = []
        for i, line in enumerate(lines, 1):
            processed_line = line.upper() if uppercase else line
            if line_numbers:
                processed_line = f"{i:3}: {processed_line}"
            processed_lines.append(processed_line)

        result = "\n".join(processed_lines)

        # 輸出結果
        if output:
            output.write_text(result, encoding="utf-8")
            typer.echo(f"處理完成，結果已儲存至: {output}")
        else:
            typer.echo(result)

    except FileNotFoundError:
        typer.echo(f"錯誤: 找不到檔案 {file_path}", err=True)
        raise typer.Exit(1) from None
    except Exception as e:
        typer.echo(f"錯誤: {e}", err=True)
        raise typer.Exit(1) from e


@app.command()
def calc(
    operation: str = typer.Argument(..., help="運算操作 (add/sub/mul/div)"),
    a: float = typer.Argument(..., help="第一個數字"),
    b: float = typer.Argument(..., help="第二個數字"),
):
    """
    簡單的計算器
    """
    operations = {
        "add": lambda x, y: x + y,
        "sub": lambda x, y: x - y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x / y if y != 0 else None,
    }

    if operation not in operations:
        typer.echo(
            f"錯誤: 不支援的操作 '{operation}'。支援的操作: {', '.join(operations.keys())}",
            err=True,
        )
        raise typer.Exit(1)

    result = operations[operation](a, b)
    if result is None:
        typer.echo("錯誤: 除數不能為零", err=True)
        raise typer.Exit(1)

    op_symbols = {"add": "+", "sub": "-", "mul": "*", "div": "/"}
    typer.echo(f"{a} {op_symbols[operation]} {b} = {result}")


@app.command()
def search_replace(
    file_path: Path = typer.Argument(..., help="要搜尋的檔案路徑"),
    search_term: str = typer.Argument(..., help="要搜尋的文字"),
    replace_term: str = typer.Argument(..., help="要替換的文字"),
    output: Path | None = typer.Option(None, "--output", "-o", help="輸出檔案路徑"),
    case_sensitive: bool = typer.Option(
        True, "--case-sensitive/--ignore-case", help="區分大小寫"
    ),
):
    """
    在檔案中搜尋並替換文字
    """
    try:
        content = file_path.read_text(encoding="utf-8")

        if case_sensitive:
            new_content = content.replace(search_term, replace_term)
        else:
            # 大小寫不敏感的替換
            import re

            new_content = re.sub(
                re.escape(search_term), replace_term, content, flags=re.IGNORECASE
            )

        count = (
            content.count(search_term)
            if case_sensitive
            else len(re.findall(re.escape(search_term), content, re.IGNORECASE))
        )

        if output:
            output.write_text(new_content, encoding="utf-8")
            typer.echo(f"已替換 {count} 處，結果儲存至: {output}")
        else:
            typer.echo(new_content)
            typer.echo(f"\n已替換 {count} 處", err=True)

    except FileNotFoundError:
        typer.echo(f"錯誤: 找不到檔案 {file_path}", err=True)
        raise typer.Exit(1) from None
    except Exception as e:
        typer.echo(f"錯誤: {e}", err=True)
        raise typer.Exit(1) from e


@app.command()
def generate_report(
    directory: Path = typer.Argument(Path("."), help="要分析的目錄路徑"),
    file_pattern: str = typer.Option(
        "*.py", "--pattern", "-p", help="檔案模式 (例如: *.py, *.txt)"
    ),
    output_format: str = typer.Option(
        "text", "--format", "-f", help="輸出格式 (text/json)"
    ),
):
    """
    生成目錄中檔案的統計報告
    """
    import glob
    import json
    from datetime import datetime

    try:
        pattern = str(directory / file_pattern)
        files = glob.glob(pattern, recursive=True)

        report_data = {
            "生成時間": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "目錄": str(directory),
            "檔案模式": file_pattern,
            "檔案數量": len(files),
            "檔案詳情": [],
        }

        total_lines = 0
        total_size = 0

        for file_path in files:
            try:
                path_obj = Path(file_path)
                stat = path_obj.stat()
                lines = len(path_obj.read_text(encoding="utf-8").splitlines())

                file_info = {
                    "檔案名": path_obj.name,
                    "路徑": str(path_obj),
                    "大小(bytes)": stat.st_size,
                    "行數": lines,
                    "修改時間": datetime.fromtimestamp(stat.st_mtime).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                }

                report_data["檔案詳情"].append(file_info)
                total_lines += lines
                total_size += stat.st_size

            except Exception as e:
                typer.echo(f"警告: 無法處理檔案 {file_path}: {e}", err=True)

        report_data["總行數"] = total_lines
        report_data["總大小(bytes)"] = total_size

        if output_format == "json":
            typer.echo(json.dumps(report_data, ensure_ascii=False, indent=2))
        else:
            typer.echo("📊 檔案分析報告")
            typer.echo("=" * 40)
            typer.echo(f"生成時間: {report_data['生成時間']}")
            typer.echo(f"分析目錄: {report_data['目錄']}")
            typer.echo(f"檔案模式: {report_data['檔案模式']}")
            typer.echo(f"檔案數量: {report_data['檔案數量']}")
            typer.echo(f"總行數: {report_data['總行數']:,}")
            typer.echo(f"總大小: {report_data['總大小(bytes)']:,} bytes")
            typer.echo("\n📁 檔案詳情:")
            for file_info in report_data["檔案詳情"]:
                typer.echo(
                    f"  • {file_info['檔案名']} ({file_info['行數']} 行, {file_info['大小(bytes)']} bytes)"
                )

    except Exception as e:
        typer.echo(f"錯誤: {e}", err=True)
        raise typer.Exit(1) from e


@app.command()
def interactive_demo():
    """
    互動式示範 - 展示 Typer 的進階功能
    """
    typer.echo("🎉 歡迎使用 Typer 互動式示範！")

    # 使用 typer.prompt 獲取用戶輸入
    name = typer.prompt("請輸入您的名字")

    # 使用 typer.confirm 獲取確認
    is_student = typer.confirm("您是學生嗎？")

    # 使用帶預設值的 prompt
    age = typer.prompt("請輸入您的年齡", type=int, default=25)

    # 使用密碼輸入
    if typer.confirm("要設置一個示範密碼嗎？", default=False):
        _password = typer.prompt(
            "請輸入密碼", hide_input=True, confirmation_prompt=True
        )
        typer.echo("✅ 密碼設置成功！")

    # 選擇選項
    typer.echo("\n請選擇您喜歡的程式語言:")
    languages = ["Python", "JavaScript", "Go", "Rust", "TypeScript"]
    for i, lang in enumerate(languages, 1):
        typer.echo(f"  {i}. {lang}")

    choice = typer.prompt("請輸入選項編號", type=int)
    if 1 <= choice <= len(languages):
        favorite_lang = languages[choice - 1]
    else:
        favorite_lang = "未知"

    # 顯示進度條示範
    typer.echo("\n🔄 處理您的資料...")
    import time

    with typer.progressbar(range(100), label="處理中") as progress:
        for _value in progress:
            time.sleep(0.01)  # 模擬工作

    # 顯示結果
    typer.echo("\n📋 您的資料摘要:")
    typer.echo(f"姓名: {name}")
    typer.echo(f"年齡: {age}")
    typer.echo(f"身份: {'學生' if is_student else '非學生'}")
    typer.echo(f"喜歡的程式語言: {favorite_lang}")

    # 使用 typer.style 添加顏色
    success_msg = typer.style(
        "✨ 示範完成！感謝您的參與！", fg=typer.colors.GREEN, bold=True
    )
    typer.echo(success_msg)


if __name__ == "__main__":
    app()
