"""
Click CLI 範例 - 一個簡單的文字處理工具

這個檔案展示了如何使用 Click 創建命令列介面。
Click 是一個 Python 命令列介面創建工具包，功能強大且靈活。
"""

import click
from pathlib import Path

# 創建主要的 Click 群組
@click.group()
@click.version_option(version='1.0.0')
def cli():
    """一個簡單的文字處理 CLI 工具 (使用 Click)"""
    pass

@cli.command()
@click.argument('name')
@click.option('--count', '-c', default=1, help='重複問候的次數')
@click.option('--polite', '-p', is_flag=True, help='使用禮貌的問候方式')
def greet(name, count, polite):
    """
    問候指定的人
    """
    greeting = "您好" if polite else "你好"
    for _ in range(count):
        click.echo(f"{greeting}, {name}!")


@cli.command()
@click.argument('name')
@click.argument('mom_name')
@click.option('--count', '-c', default=1, help='重複問候的次數')
@click.option('--polite', '-p', is_flag=True, help='使用禮貌的問候方式')
def greet_mom(name, mom_name, count, polite):
    """
    問候指定的人和他的媽媽
    """
    greeting = "您好" if polite else "你好"
    for _ in range(count):
        click.echo(f"{greeting}, {name}!")
        click.echo(f"{greeting}, {mom_name}!")


@cli.command()
@click.argument('names', nargs=-1) # 模仿 mv 的 srcs
@click.argument('title') # 模仿 mv 的 dest
@click.option('--prefix', '-p', default='>>> ', help='問候詞前綴') # 普通 optional
@click.option('--greeting', '-g', multiple=True, help='多種問候詞') # 陣列 optional
def greet_all(names, prefix, title, greeting):
    """
    綜合測試：問候 + 多選項 + 類似 mv 介面
    """
    click.echo(f"人名列表: {', '.join(names)}")
    click.echo(f"稱謂: {title}")
    click.echo(f"prefix: {prefix}")
    click.echo(f"問候詞: {', '.join(greeting)}")
    click.echo("===== 問候結果 =====")
    
    for name in names:
        for g in greeting:
            click.echo(f"{prefix} {g}, {title} {name}!")

@cli.command()
@click.argument('text')
@click.option('--chars', '-c', is_flag=True, help='同時顯示字元數')
def count_words(text, chars):
    """
    計算文字的字數
    """
    words = len(text.split())
    click.echo(f"字數: {words}")
    
    if chars:
        char_count = len(text)
        click.echo(f"字元數: {char_count}")

@cli.command()
@click.argument('file_path', type=click.Path(exists=True, path_type=Path))
@click.option('--output', '-o', type=click.Path(path_type=Path), help='輸出檔案路徑')
@click.option('--uppercase', '-u', is_flag=True, help='轉換為大寫')
@click.option('--line-numbers', '-n', is_flag=True, help='加上行號')
def process_file(file_path, output, uppercase, line_numbers):
    """
    處理文字檔案
    """
    try:
        # 讀取檔案
        content = file_path.read_text(encoding='utf-8')
        lines = content.splitlines()
        
        # 處理內容
        processed_lines = []
        for i, line in enumerate(lines, 1):
            processed_line = line.upper() if uppercase else line
            if line_numbers:
                processed_line = f"{i:3}: {processed_line}"
            processed_lines.append(processed_line)
        
        result = '\n'.join(processed_lines)
        
        # 輸出結果
        if output:
            output.write_text(result, encoding='utf-8')
            click.echo(f"處理完成，結果已儲存至: {output}")
        else:
            click.echo(result)
            
    except Exception as e:
        click.echo(f"錯誤: {e}", err=True)
        raise click.Abort()

@cli.command()
@click.argument('operation', type=click.Choice(['add', 'sub', 'mul', 'div']))
@click.argument('a', type=float)
@click.argument('b', type=float)
def calc(operation, a, b):
    """
    簡單的計算器
    
    OPERATION: 運算操作 (add/sub/mul/div)
    A: 第一個數字
    B: 第二個數字
    """
    operations = {
        'add': lambda x, y: x + y,
        'sub': lambda x, y: x - y,
        'mul': lambda x, y: x * y,
        'div': lambda x, y: x / y if y != 0 else None
    }
    
    result = operations[operation](a, b)
    if result is None:
        click.echo("錯誤: 除數不能為零", err=True)
        raise click.Abort()
    
    op_symbols = {'add': '+', 'sub': '-', 'mul': '*', 'div': '/'}
    click.echo(f"{a} {op_symbols[operation]} {b} = {result}")

@cli.command()
@click.option('--format', '-f', 'output_format', 
              type=click.Choice(['json', 'csv', 'text']), 
              default='text',
              help='輸出格式')
@click.argument('items', nargs=-1, required=True)
def list_items(items, output_format):
    """
    列出並格式化項目
    
    ITEMS: 要列出的項目 (可以是多個)
    """
    if output_format == 'json':
        import json
        result = json.dumps(list(items), ensure_ascii=False, indent=2)
    elif output_format == 'csv':
        result = ','.join(items)
    else:  # text
        result = '\n'.join(f"- {item}" for item in items)
    
    click.echo(result)

@cli.command()
@click.argument('file_path', type=click.Path(exists=True, path_type=Path))
@click.argument('search_term')
@click.argument('replace_term')
@click.option('--output', '-o', type=click.Path(path_type=Path), help='輸出檔案路徑')
@click.option('--case-sensitive/--ignore-case', default=True, help='區分大小寫')
def search_replace(file_path, search_term, replace_term, output, case_sensitive):
    """
    在檔案中搜尋並替換文字
    
    FILE_PATH: 要搜尋的檔案路徑
    SEARCH_TERM: 要搜尋的文字
    REPLACE_TERM: 要替換的文字
    """
    try:
        content = file_path.read_text(encoding='utf-8')
        
        if case_sensitive:
            new_content = content.replace(search_term, replace_term)
            count = content.count(search_term)
        else:
            import re
            new_content = re.sub(re.escape(search_term), replace_term, content, flags=re.IGNORECASE)
            count = len(re.findall(re.escape(search_term), content, re.IGNORECASE))
        
        if output:
            output.write_text(new_content, encoding='utf-8')
            click.echo(f"已替換 {count} 處，結果儲存至: {output}")
        else:
            click.echo(new_content)
            click.echo(f"\n已替換 {count} 處", err=True)
            
    except Exception as e:
        click.echo(f"錯誤: {e}", err=True)
        raise click.Abort()

@cli.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, path_type=Path), default='.')
@click.option('--pattern', '-p', default='*.py', help='檔案模式 (例如: *.py, *.txt)')
@click.option('--format', '-f', 'output_format', type=click.Choice(['text', 'json']), default='text', help='輸出格式')
def generate_report(directory, pattern, output_format):
    """
    生成目錄中檔案的統計報告
    
    DIRECTORY: 要分析的目錄路徑
    """
    import glob
    import json
    from datetime import datetime
    
    try:
        pattern_path = str(directory / pattern)
        files = glob.glob(pattern_path, recursive=True)
        
        report_data = {
            "生成時間": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "目錄": str(directory),
            "檔案模式": pattern,
            "檔案數量": len(files),
            "檔案詳情": []
        }
        
        total_lines = 0
        total_size = 0
        
        for file_path in files:
            try:
                path_obj = Path(file_path)
                stat = path_obj.stat()
                lines = len(path_obj.read_text(encoding='utf-8').splitlines())
                
                file_info = {
                    "檔案名": path_obj.name,
                    "路徑": str(path_obj),
                    "大小(bytes)": stat.st_size,
                    "行數": lines,
                    "修改時間": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                }
                
                report_data["檔案詳情"].append(file_info)
                total_lines += lines
                total_size += stat.st_size
                
            except Exception as e:
                click.echo(f"警告: 無法處理檔案 {file_path}: {e}", err=True)
        
        report_data["總行數"] = total_lines
        report_data["總大小(bytes)"] = total_size
        
        if output_format == "json":
            click.echo(json.dumps(report_data, ensure_ascii=False, indent=2))
        else:
            click.echo(f"📊 檔案分析報告")
            click.echo(f"=" * 40)
            click.echo(f"生成時間: {report_data['生成時間']}")
            click.echo(f"分析目錄: {report_data['目錄']}")
            click.echo(f"檔案模式: {report_data['檔案模式']}")
            click.echo(f"檔案數量: {report_data['檔案數量']}")
            click.echo(f"總行數: {report_data['總行數']:,}")
            click.echo(f"總大小: {report_data['總大小(bytes)']:,} bytes")
            click.echo(f"\n📁 檔案詳情:")
            for file_info in report_data["檔案詳情"]:
                click.echo(f"  • {file_info['檔案名']} ({file_info['行數']} 行, {file_info['大小(bytes)']} bytes)")
        
    except Exception as e:
        click.echo(f"錯誤: {e}", err=True)
        raise click.Abort()

@cli.command()
def interactive_demo():
    """
    互動式示範 - 展示 Click 的進階功能
    """
    click.echo("🎉 歡迎使用 Click 互動式示範！")
    
    # 使用 click.prompt 獲取用戶輸入
    name = click.prompt("請輸入您的名字")
    
    # 使用 click.confirm 獲取確認
    is_student = click.confirm("您是學生嗎？")
    
    # 使用帶預設值的 prompt
    age = click.prompt("請輸入您的年齡", type=int, default=25)
    
    # 使用密碼輸入
    if click.confirm("要設置一個示範密碼嗎？", default=False):
        password = click.prompt("請輸入密碼", hide_input=True, confirmation_prompt=True)
        click.echo("✅ 密碼設置成功！")
    
    # 選擇選項
    click.echo("\n請選擇您喜歡的程式語言:")
    languages = ["Python", "JavaScript", "Go", "Rust", "TypeScript"]
    for i, lang in enumerate(languages, 1):
        click.echo(f"  {i}. {lang}")
    
    choice = click.prompt("請輸入選項編號", type=int)
    if 1 <= choice <= len(languages):
        favorite_lang = languages[choice - 1]
    else:
        favorite_lang = "未知"
    
    # 顯示進度條示範
    click.echo("\n🔄 處理您的資料...")
    import time
    with click.progressbar(range(100), label="處理中") as bar:
        for item in bar:
            time.sleep(0.01)  # 模擬工作
    
    # 顯示結果
    click.echo("\n📋 您的資料摘要:")
    click.echo(f"姓名: {name}")
    click.echo(f"年齡: {age}")
    click.echo(f"身份: {'學生' if is_student else '非學生'}")
    click.echo(f"喜歡的程式語言: {favorite_lang}")
    
    # 使用 click.style 添加顏色
    success_msg = click.style("✨ 示範完成！感謝您的參與！", fg='green', bold=True)
    click.echo(success_msg)

@cli.command()
@click.option('--count', '-c', default=5, help='要生成的隨機數數量')
@click.option('--min-val', default=1, help='最小值')
@click.option('--max-val', default=100, help='最大值')
@click.option('--sort/--no-sort', default=False, help='是否排序結果')
def random_numbers(count, min_val, max_val, sort):
    """
    生成隨機數字
    """
    import random
    
    if min_val >= max_val:
        click.echo("錯誤: 最小值必須小於最大值", err=True)
        raise click.Abort()
    
    numbers = [random.randint(min_val, max_val) for _ in range(count)]
    
    if sort:
        numbers.sort()
    
    click.echo(f"生成 {count} 個隨機數字 (範圍: {min_val}-{max_val}):")
    for i, num in enumerate(numbers, 1):
        click.echo(f"  {i:2d}. {num}")
    
    # 統計資訊
    click.echo(f"\n📊 統計:")
    click.echo(f"  平均值: {sum(numbers) / len(numbers):.2f}")
    click.echo(f"  最大值: {max(numbers)}")
    click.echo(f"  最小值: {min(numbers)}")

if __name__ == "__main__":
    cli()
