from django.shortcuts import render
from django.http import JsonResponse, Http404

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from.serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer
from .models import Project, Issue, Comment, Contributor


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Projects list (GET) and Create project (POST)': '/projects/',
        'Get project details  (GET), Update (PUT) and Delete (DELETE) a project': '/projects/<str:pk>',
        'Users list (GET) and Add a user to a project (POST)': '/projects/<str:pk>/users/',
        'Delete a user from a project (DELETE)': '/projects/<str:pk>/users/<str:pk>',
        'Issues list for a project (GET) and Create an issue for a project (POST)': '/projects/<str:pk>/issues/',
        'Update (PUT) and Delete (DELETE) an issue for a project (PUT)': '/projects/<str:pk>/issues/<str:pk>',
        'Comments List for an issue (GET) and Create comment about an issue (POST)': '/projects/<str:pk>/issues/<str:pk>/comments/',
        'Update (PUT) and Delete (DELETE) a comment ': '/projects/<str:pk>/issues/<str:pk>/comments/<str:pk>',
        'Get a comments with its id (GET)': '/projects/<str:pk>/issues/<str:pk>/comments/<str:pk>',
    }
    return Response(api_urls)


class ProjectsList(APIView):
    """
    List all projects, or create a new project
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    """
    Retrieve, update or delete a project instance
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(instance=project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectUsersList(APIView):
    """
    List all users for a given project(pk), or create a new user for a given project(pk)
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, pk, format=None):
        contributors = Contributor.objects.filter(project_id=pk)
        serializer = ContributorSerializer(contributors, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        serializer = ContributorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectUserDelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, format=None):
        pass


class ProjectIssuesList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass


class ProjectIssueModify(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, format=None):
        pass

    def delete(self, request, format=None):
        pass


class IssueCommentsList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass


class IssueCommentDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        pass

    def put(self, request, format=None):
        pass

    def delete(self, request, format=None):
        pass
