"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from clubbucksapi.models import Student
from django.contrib.auth.models import User


class StudentView(ViewSet):
    """Honey Rae API students view"""

    def list(self, request):
        """Handle GET requests to get all students

        Returns:
            Response -- JSON serialized list of students
        """

        students = Student.objects.all()
        serialized = StudentSerializer(students, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single student

        Returns:
            Response -- JSON serialized student record
        """

        student = Student.objects.get(pk=pk)
        serialized = StudentSerializer(student)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    #TODO Create PUT request to edit student balances

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        student = Student.objects.get(pk=pk)

        #! How would I access student name?
        student.age = request.data["age"]
        student.grade_level = request.data["grade_level"]
        student.balance = request.data["balance"]
        student.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    # complete and test a destroy function for a student

    def destroy(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class StudentSerializer(serializers.ModelSerializer):
    """JSON serializer for students"""
    class Meta:
        model = Student
        fields = ('id', 'user', 'age', 'grade_level', 'balance', 'full_name')
        depth: 1