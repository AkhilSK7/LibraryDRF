from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from books.models import Book
from books.serializers import BookSerializer,UserSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class LibraryView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SearchAPIView(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if query:
            b=Book.objects.filter(Q(title__icontains=query)|Q(author__icontains=query)|Q(page__icontains=query)|Q(price__icontains=query)|Q(language__icontains=query))
            if not b.exists():#Queryset empty
                return Response({'msg':'No Results'},status=status.HTTP_204_NO_CONTENT)
            books=BookSerializer(b,many=True)
            return Response(books.data,status=status.HTTP_200_OK)
        else:
            return Response({'msg':'No Results'},status=status.HTTP_204_NO_CONTENT)

class RegisterAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':'logout successfully completed'},status=status.HTTP_200_OK)