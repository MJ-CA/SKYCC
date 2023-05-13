from fastapi import FastAPI, Request

app = FastAPI()

@app.post('43.200.213.0')
async def slack_events(request: Request):
    data = await request.json()

    response = {'text': '슬랙 봇 응답'}
    return response

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

@app.get('test')
def test():
	return "Hello"