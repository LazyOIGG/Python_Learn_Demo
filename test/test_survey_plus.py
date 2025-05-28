import sys
import os
import pytest

# 获取当前文件所在目录的父目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# 导入待测试模块
from src.survey import AnonymousSurvey

@pytest.fixture
def survey_fixture():
    """提供一个默认的调查实例作为测试夹具"""
    question = "What languages do you speak?"
    return AnonymousSurvey(question)

@pytest.fixture
def multiple_responses():
    """提供多个测试响应作为夹具"""
    return ['English', 'Spanish', 'Mandarin']

def test_store_single_response(survey_fixture):
    """测试单个答案是否会被妥善存储"""
    survey_fixture.store_response('English')
    assert 'English' in survey_fixture.responses

def test_store_multiple_responses(survey_fixture, multiple_responses):
    """测试多个答案是否会被妥善存储"""
    for response in multiple_responses:
        survey_fixture.store_response(response)

    for response in multiple_responses:
        assert response in survey_fixture.responses

def test_response_count(survey_fixture, multiple_responses):
    """测试响应计数是否正确"""
    initial_count = len(survey_fixture.responses)

    for response in multiple_responses:
        survey_fixture.store_response(response)

    assert len(survey_fixture.responses) == initial_count + len(multiple_responses)
