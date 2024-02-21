from httpx import AsyncClient


async def test_get_perevals_added(ac: AsyncClient):
    response = await ac.get("pereval/get_perevals_added")
    assert response.status_code == 200


async def test_get_perevals_added(ac: AsyncClient):
    response = await ac.get("/pereval/get_pereval_added/1")
    assert response.status_code == 200


async def test_submit_pereval(ac: AsyncClient):
    response = await ac.post("/pereval/submitdata", json={
    "id": 1,
    "status": "accepted"
    })
    assert {"status": "ok"}
