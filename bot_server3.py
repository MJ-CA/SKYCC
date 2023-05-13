from fastapi import FastAPI, Request

app = FastAPI()

@app.post('/slack')
async def slack_events(request: Request):
    data = await request.json()

    response = {'text': '슬랙 봇 응답'}
    return response


@app.get('/test')
def test():
	return "Hello"