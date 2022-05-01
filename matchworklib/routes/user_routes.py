from fastapi import APIRouter

router = APIRouter()


@router.post('/users')
def post_create_user():
    # request = PostCreateUserRequestModel(user)
    # interactor = PostCreateUserInteractor(request, adapter)

    # result = interactor.run()

    return {}
