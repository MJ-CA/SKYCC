from fastapi import FastAPI, Request

app = FastAPI()

@app.post('/slack')
async def slack_events(request: Request):
    data = await request.json()

    response = {'url': "http://...", 'tag': ["개발", "연애"], 'title': "연픽"}
    return response


@app.get('/test')
def test():
	return "Hello"
