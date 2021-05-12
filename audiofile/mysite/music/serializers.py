from rest_framework import serializers
from .models import song,podcast,audiobook

class song_Serializer(serializers.ModelSerializer):

    class Meta:
         model =song 
         fields =['id','s_name','s_duation','s_uploaded_time']


class podcast_Serializer(serializers.ModelSerializer):

    class Meta:
        model = podcast       
        fields =['id','p_name','p_duation','p_uploaded_time','p_host','p_participants']

class audiobook_Serializer(serializers.ModelSerializer):

    class Meta:
        model = audiobook
        fields = ['id','a_title','a_author','a_narrator','a_duration','a_uploaded_time']
        
         
         
         
    
