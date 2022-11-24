from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
# Create your views here.



class HandleFileUpload(APIView):
    def post(self , request):
            data = request.data
            current_user = request.user

            if current_user.is_authenticated:
                serializer = FileListSerializer(data = data, context= {
                    'request': request
                })
        
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
            else:
                return Response({
                'message' : 'somethign went wrong',
                }, status= status.HTTP_401_UNAUTHORIZED)
    
    def get(self, request):
        User = request.user

        if User.is_authenticated:
            try:
                folders = Folders.objects.filter(user = User)
                serializers = GetFolderListSerializers(folders, many = True)
                return Response(data= serializers.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    'message': str(e)
                }, status= status.HTTP_400_BAD_REQUEST)
        else:
                return Response({
                'message' : 'UNAUTHORIZED',
                },status= status.HTTP_401_UNAUTHORIZED)

class HandelShare(APIView):
    def get(self, request):
        id = request.query_params['id']
        User = request.user
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
        if request.user.is_authenticated:
            try:
                folder = Folders.objects.get(uid= id)
                
                print(folder.access_by )
                if folder.access_by in User.email:
                    files = Files.objects.filter(folders = id)
                    serializers = GetFileListSerializer(files, many= True)
                    return Response({
                    'data': serializers.data
                    })
                else :
                    return Response({
                    'message' : 'Access Denied',
                 }, status= status.HTTP_401_UNAUTHORIZED)
            except Exception as e:
                return Response({
                'status' : 400,
                'message' : 'No Data Found',
                }, status= 400)
        else:
            return Response({
                'status' : 400,
                'message' : 'User not login',
                }, status= status.HTTP_401_UNAUTHORIZED)
    

class DownloadZip(APIView):

    def zip_files(self,folder):
        shutil.make_archive(f'public/static/zip/{folder}' , 'zip' ,f'public/static/{folder}' )
        

    def get(self, request):
        id = request.query_params['id']
        User = request.user
        
        if User.is_authenticated:
            folder = Folders.objects.get(uid= id)
            self.zip_files(folder.uid)
            print(request)
            return HttpResponseRedirect(redirect_to="https://www.youtube.com/")
