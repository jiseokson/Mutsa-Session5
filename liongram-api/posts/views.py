from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import models
from . import serializer

class PostModelViewSet(ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializer.PostListModelSerializer

@api_view(['GET'])
def calculator(request):
    num1 = request.GET.get('num1', 0)
    num2 = request.GET.get('num2', 0)
    operators = request.GET.get('operators')
    print(num1, num2, operators)
    if operators == 'plus':
        result = int(num1) + int(num2)
    elif operators == 'sub':
        result = int(num1) - int(num2)
    elif operators == 'mul':
        result = int(num1) * int(num2)
    elif operators == 'div':
        result = int(num1) / int(num2)
    else:
        result = 0
    data = {
        'type': 'FBV',
        'result': result,
    }
    return Response(data)

class CalculatorAPIView(APIView):
    def get(self, request):
        num1 = request.GET.get('num1', 0)
        num2 = request.GET.get('num2', 0)
        operators = request.GET.get('operators')
        print(num1, num2, operators)
        if operators == 'plus':
            result = int(num1) + int(num2)
        elif operators == 'sub':
            result = int(num1) - int(num2)
        elif operators == 'mul':
            result = int(num1) * int(num2)
        elif operators == 'div':
            result = int(num1) / int(num2)
        else:
            result = 0
        data = {
            'type': 'CBV',
            'result': result,
        }
        return Response(data)