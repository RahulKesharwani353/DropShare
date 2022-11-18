from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
# Create your views here.



class HandleFileUpload(APIView):
    def post(self , request):
            data = request.data

            serializer = FileListSerializer(data = data)
        
            if serializer.is_valid():
                serializer.save()

                return Response({
                    'status' : 200,
                    'message' : 'files uploaded successfully',
                    'data' : serializer.data
                })
                
            
            return Response({
                'status' : 400,
                'message' : 'somethign went wrong',
                'data'  : serializer.errors
            })
    
    def get(self, request, pk):
        id = pk
        # files = Files.objects.get(id = id)
        # serializers = GetFileListSerializer(data =files)
        # if serializers.is_valid():
        #     return Response({
        #         'status': 200,
        #         'data': serializers.data
        #     })
        # return Response({
        #         'status' : 400,
        #         'message' : 'somethign went wrong',
        #         'data'  : serializers.errors
        #     }, status= 400)
        #-------------------------------------------method 2--------------------------
        # try:
        #     files = Files.objects.get(id= id)
        #     serializers = GetFileListSerializer(files, many = True )
        #     return Response({
        #          'status': 200,
        #          'data': serializers.data
        #      })
        # except Exception:
        #     return Response({
        #     'status' : 400,
        #     'message' : 'somethign went wrong',
        #     'data'  : serializers.errors
        #      }, status= 400)

    #---------------------------------------------3--------------------------------
     
        try:
            files = Files.objects.filter(folders = id)
            serializers = GetFileListSerializer(files, many= True)
            return Response({
                'status': 200,
                'data': serializers.data
            })
        except Exception as e:
            return Response({
                'status' : 400,
                'message' : 'No Data Found',
            }, status= 400)

