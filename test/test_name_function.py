import sys
import os

# 获取当前文件所在目录的父目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

#导入待测试模块
from src.name_function import get_formatted_name

def test_first_last_name():
    """能正确处理Janis Joplin这样的名字吗？"""
    formatted_name = get_formatted_name("janis", "joplin")
    assert formatted_name == "Janis Joplin" # assert判断并返回结果True还是False

def test_first_middle_last_name():
    """能正确处理Janis Middle Joplin这样的名字吗？"""
    formatted_name = get_formatted_name("janis", "joplin", "middle")
    assert formatted_name == "Janis Middle Joplin"
