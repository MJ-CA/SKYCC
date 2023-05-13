from slack_sdk import WebClient
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

# JSON 데이터를 가져오는 함수
def get_json_data(url):
    response = requests.get(url)
    json_data = response.json()
    return json_data

# 슬랙 봇에게 메시지를 보내는 함수
def send_message_to_slackbot(client, channel, message):
    response = client.chat_postMessage(channel=channel, text=message)
    return response

# JSON 데이터를 받아와서 처리하는 함수
def process_json_data(json_data, slack_token):
    url = json_data['url']
    tags = json_data['tag']
    title = json_data['title']
    
    # 메시지 생성
    message = f"Title: {title}\nTags: {', '.join(tags)}\nURL: {url}"
    
    # 슬랙 봇에게 메시지 보내기
    client = WebClient(token=slack_token)
    channel = "#일반"
    send_message_to_slackbot(client, channel, message)

json_data_url = "/slack"
slack_token = os.getenv('SLACK_BOT_TOKEN')
json_data = get_json_data(json_data_url)
process_json_data(json_data, slack_token)

