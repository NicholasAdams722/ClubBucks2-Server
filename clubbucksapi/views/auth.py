from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from clubbucksapi.models import Student

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
    request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=username, password=password)

    # If authentication was successful, respond with their token
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key,
            'staff': authenticated_user.is_staff
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
    request -- The full HTTP request object
    '''

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    try: 
        new_user = User.objects.create_user(
            username=request.data['username'],
            password=request.data['password'],
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            is_staff = request.data['is_staff']
        )
            #! If user.is_staff == false then save extra info in the student table.  If true, only create a new user
        # If student, do this
        if not new_user.is_staff:
        # Now save the extra info in the clubbucksapi_student table
            student = Student.objects.create(
                user=new_user,
                age = request.data['age'],
                grade_level = request.data['grade_level'],
                balance = 0

        )

            # Use the REST Framework's token generator on the new user account
            token = Token.objects.create(user=student.user)
            # Return the token to the client
            data = {
                    'valid': True,
                    'token': token.key,
                    'staff': new_user.is_staff
                     }
            return Response(data)
    
        else:
            token = Token.objects.create(user=new_user)
            # Return the token to the client
            data = {
                    'valid': True,
                    'token': token.key,
                    'staff': new_user.is_staff 
                    }
            return Response(data)  # Add a response here for staff users
    except Exception as error:
        data = {'error': str(error)}  # Return an error response in case of exception
        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
