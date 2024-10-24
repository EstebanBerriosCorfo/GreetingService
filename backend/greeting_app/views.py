from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Greeting
from .serializers import GreetingSerializer



"""
Explicación del método para crear un saludo:
1. Se verifica que el método HTTP sea POST.
2. Se obtienen los datos del cuerpo de la solicitud.
3. Se serializan los datos.
4. Se verifica si la serialización es válida.
5. Se guardan los datos en la base de datos.
6. Se devuelve una respuesta con los datos serializados y un código de estado 201.
7. Si la serialización no es válida, se devuelve una respuesta con los errores y un código de estado 400.
"""
# Create a new greeting
@api_view(['POST'])
def create_greeting(request):
    if request.method == 'POST':
        serializer = GreetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Explicación del método para obtener todos los saludos:
1. Se verifica que el método HTTP sea GET.
2. Se obtienen todos los saludos de la base de datos.
3. Se serializan los saludos.
4. Se devuelve una respuesta con los saludos serializados.
"""
# Retrieve all greetings
@api_view(['GET'])
def get_greetings(request):
    if request.method == 'GET':
        greetings = Greeting.objects.all()
        serializer = GreetingSerializer(greetings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


"""
Explicación del método para obtener un saludo:
1. Se verifica que el método HTTP sea GET.
2. Se obtiene el saludo con el ID especificado.
3. Se serializa el saludo.
4. Se devuelve una respuesta con el saludo serializado y un código de estado 200.
5. Si no se encuentra el saludo, se devuelve una respuesta con un código de estado 404.
"""
# Retrieve a single greeting
@api_view(['GET'])
def get_greeting(request, pk):
    greeting = get_object_or_404(Greeting, pk=pk)
    if request.method == 'GET':
        serializer = GreetingSerializer(greeting)
        return Response(serializer.data, status=status.HTTP_200_OK)


"""
Explicación del método para actualizar un saludo:
1. Se verifica que el método HTTP sea PUT.
2. Se obtiene el saludo con el ID especificado.
3. Se obtienen los datos del cuerpo de la solicitud.
4. Se serializan los datos.
5. Se verifica si la serialización es válida.
6. Se guardan los datos actualizados en la base de datos.
7. Se devuelve una respuesta con los datos serializados y un código de estado 200.
8. Si la serialización no es válida, se devuelve una respuesta con los errores y un código de estado 400.
"""
# Update a greeting
@api_view(['PUT'])
def update_greeting(request, pk):
    greeting = get_object_or_404(Greeting, pk=pk)
    if request.method == 'PUT':
        serializer = GreetingSerializer(greeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Explicación del método para eliminar un saludo:
1. Se verifica que el método HTTP sea DELETE.
2. Se obtiene el saludo con el ID especificado.
3. Se elimina el saludo de la base de datos.
4. Se devuelve una respuesta con un código de estado 204.
5. Si no se encuentra el saludo, se devuelve una respuesta con un código de estado 404.
"""
# Delete a greeting
@api_view(['DELETE'])
def delete_greeting(request, pk):
    greeting = get_object_or_404(Greeting, pk=pk)
    if request.method == 'DELETE':
        greeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)