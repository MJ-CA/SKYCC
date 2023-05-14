from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from slack_sdk import WebClient
import os

load_dotenv()
slack_token = os.getenv('SLACK_BOT_TOKEN')


app = FastAPI()

origins = [ "*" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def send_message_to_slackbot(client, channel, message):
    response = client.chat_postMessage(channel=channel, text=message)
    return response


# class MyModel(BaseModel):
#     labels: list
#     sequences: list
    
class MyModel(BaseModel):
    url: str
    tag: list
    title: str

@app.post("/slack")
async def your_endpoint(model: MyModel):
    url = model.url
    tag = model.tag
    title = model.title

    message = f"Title: {title}\nTags: {', '.join(tag)}\nURL: {url}"
    client = WebClient(token=slack_token)
    channel = "#일반"
    send_message_to_slackbot(client, channel, message)    

    print(model)

    return model
    # sequences = model.sequences
    # JSON 데이터 활용 코드 작성

#조금 더 포괄적인 json 데이터 받는 코드
@app.post("/receive_json")
async def receive_json(json_data: dict):
    return json_data
