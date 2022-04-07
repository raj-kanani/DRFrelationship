from .models import Singer, Song
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True, read_only=True)

    # generate hyper linked for song
    # view_name in model name of (song-detail)
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # slug field dispaly title in letter
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    # nested serializer
    # show all the data of songserializer (id,title,duration,singer)
    song = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']
