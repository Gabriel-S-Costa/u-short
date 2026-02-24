from fastapi import APIRouter

router = APIRouter(prefix='/accounts', tags=['login'])


@router.get('/sign-in')
async def sign_in():
    return {'message': 'Make signIn'}


@router.post('/sign-up')
async def sign_up():
    return {'message': 'Make signUp'}
