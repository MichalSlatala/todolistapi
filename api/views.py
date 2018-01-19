from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.forms import ModelForm
from django.views.generic import CreateView
from django.http import HttpResponseRedirect


from . import models
from . import serializers
from . import forms

# Create your views here.
class OperationCreateAPIView(ListCreateAPIView):
    serializer_class = serializers.UserOperationsSerializer
    queryset = models.Todo.objects.all()


class GetUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UserOperationsSerializer
    queryset = models.Todo.objects.all()
    lookup_field='id'


class TasksList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self,request):
        queryset = models.Todo.objects.all()
        return Response({'todos':queryset})


class TaskDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'details.html'

    def get(self, request, id):
        todo = get_object_or_404(models.Todo, id = id)
        serializer = serializers.UserOperationsSerializer(todo)
        return Response({'serializer':serializer, 'todo':todo})

    def post(self, request, id):
        todo = get_object_or_404(models.Todo, id = id)
        serializer = serializers.UserOperationsSerializer(todo,data={'finish':1},partial=True)
        if not serializer.is_valid():
            return Response({'serializer':serializer, 'todo':todo})
        serializer.save()


class TaskUpdate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'details.html'

    def get(self, request, id):
        todo = get_object_or_404(models.Todo, id = id)
        serializer = serializers.UserOperationsSerializer(todo,data={'finish':1},partial=True)
        return Response({'serializer':serializer, 'todo':todo})


class TaskDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'deleted.html'

    def get(self, request, id):
        todo = get_object_or_404(models.Todo, id = id)
        serializer = serializers.UserOperationsSerializer(todo)
        todo.delete()
        return Response({'serializer':serializer, 'todo':todo})


class TaskCreate(CreateView):
    form_class = forms.TaskForm
    todo = models
    template_name = 'add.html'


#defs


def finish(request,id):
    todo = get_object_or_404(models.Todo, id = id)
    if(todo.finish == True):
        todo.finish = False
    else:
        todo.finish = True
    todo.save()
    return HttpResponseRedirect('/api/details/'+str(id))

    # def delete(self, request, id):
    #     todo = self.get_object(id)
    #     todo.delete()
    #     return Response(stataus=status.HTTP_204_NO_CONTENT)
