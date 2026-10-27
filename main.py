from fastapi import FastAPI, Request, Cookie

app = FastAPI()


@app.post("/header")
async def path_paramerter(
    request: Request,
    Cookie_1: str = Cookie(),
    Cookie_2: str = Cookie(),
):
    cookie = dict(request.cookies)
    return {
        "message": "success",
        "data": {"cookie1": Cookie_1, "cookie2": Cookie_2, "cookie": cookie},
    }
