from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from scalar_fastapi import get_scalar_api_reference

from app.routers import users

app = FastAPI()

#setup middleware 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"]
)


app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )