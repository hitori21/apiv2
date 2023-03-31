import uvicorn

from core.config.settings import APP as app

if __name__ == '__main__':
	uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)