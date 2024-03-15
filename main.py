import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/")
def list_items():
    return [
        'Item1',
        'Item2',
    ]


@app.get('/items/{items_id}')
def get_item_by_id(item_id):
    return {
        'item': {
            id: item_id
        }
    }


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
