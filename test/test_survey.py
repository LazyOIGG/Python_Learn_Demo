import sys
import os

# 获取当前文件所在目录的父目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

#导入待测试模块
from src.survey import AnonymousSurvey

def test_store_single_response():
    """测试单个答案是否会被妥善存储"""
    question = "What languages do you speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_multiple_responses():
    """测试多个答案是否会被妥善存储"""
    question = "What languages do you speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']

    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
