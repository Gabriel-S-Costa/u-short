from fastapi import APIRouter

router = APIRouter(prefix='/links', tags=['links'])


@router.get('/')
async def get_links():
    return {'message': 'Hello World'}


@router.post('/')
async def create_link():
    return {'message': 'Hello World'}


@router.put('/{code}')
async def update_link():
    return 'update links'
