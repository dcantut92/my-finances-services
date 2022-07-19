from rest_framework.decorators import api_view


@api_view(['POST'])
def singup(request):
    """
    Register Users

    :param request: contains the information of the user

    :return: Json response
        - status 200 if you can save the user
        - status 500 if there is an error
    """