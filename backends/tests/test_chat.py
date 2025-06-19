import pytest
import json
from flask import jsonify
from pathlib import Path
from datetime import datetime
from unittest.mock import MagicMock, patch

@pytest.fixture
def client(app):
    """Fixture for Flask test client"""
    return app.test_client()

def test_multi_chat(client):
    """Test multi-chat"""
    # Test with multiple messages
    messages = [
        "同学们：今天的作业是：教材317页的“习题”，题3，题7，本周三交作业。",
        "添加教材第238-239页的习题，题4，题7，以及教材316-317页的习题，题1，题2，题5(1)"
        # "创建日程：明天下午3点开会",
        # "修改日程：明天下午3点的会议改为明天上午10点",
        # "删除刚才的日程",
        # "我后天晚上8点要交数值分析作业",
        # "我今晚8点到11点要进行软件工程试验任务",
        # "我想知道今天广州的天气如何",
        # "上一个日程取消了",
        # "我下周三09:30要考操作系统",
        # "我下周五09:30到11:30考人工智能",
        # "我不用考人工智能了",
        # "我想知道霸王茶姬有什么种类的奶茶",
        # "删除id为1的日程",
        # "我明天早上10点10分到11点50分上操作系统理论课最后一节课"
        # "我今晚9点要打球"
    ] # 13条信息
    
    for message in messages:
        response = client.post('/chat/', json={'message': message})
        assert response.status_code == 200
        assert 'messages' in response.json
        assert 'response' in response.json
        assert 'schedule' in response.json

        # Use `pytest -s` to see the print output
        print(f"\nMessage: {message}")
        print(f"Response: {response.json['response']}")
    
    # print(f"\nAll chat messages: \n{response.json['messages']}")
