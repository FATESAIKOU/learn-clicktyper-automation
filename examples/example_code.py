#!/usr/bin/env python3
"""
範例用法腳本 - 展示 CLI 工具的各種功能
"""

def example_function():
    """這是一個範例函數"""
    print("Hello from example function!")
    return "success"

class ExampleClass:
    """這是一個範例類別"""
    
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}!"

if __name__ == "__main__":
    # 範例程式碼
    obj = ExampleClass("CLI學習者")
    print(obj.greet())
    example_function()
