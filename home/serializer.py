from rest_framework import serializers
from .models import *
import shutil
from dropShare.settings import MEDIA_ROOT, STATICFILES_DIR

class FileListSerializer(serializers.Serializer):
    file = serializers.ListField(
        child = serializers.FileField(max_length = 1000000, allow_empty_file = False, use_url = False)
    )
    folder = serializers.CharField(required = False)
    # public\static\3f239742-6c91-49f8-8b9a-6256a40fb6e7 E:\Developer_Zone\dropShare\dropShare\public\static\3f239742-6c91-49f8-8b9a-6256a40fb6e7\Bhilai_Institute_of_Technology_Durg_1.xlsx
    def zip_files(self,folder):
        shutil.make_archive(f'public/static/zip/{folder}' , 'zip' ,f'public/static/{folder}' )

    def create(self, validated_data):
        folder_s = Folders.objects.create()
        files = validated_data.pop('file')
        file_list = []
        for item in files:
            file_object = Files.objects.create(folders = folder_s, file = item)
            file_list.append(file_object)
        # return file_list
        self.zip_files(folder_s.uid)
        return {'file' : {}, 'folder' : str(folder_s.uid)}


class GetFileListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Files
        fields='__all__'

    def create(self, validated_data):
        return super().create(validated_data)