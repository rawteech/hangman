from rest_framework import serializers


class GameSerializer(serializers.Serializer):
    letter = serializers.CharField(max_length=1)
    game_id = serializers.IntegerField()
    chances = serializers.IntegerField()
    spaces = serializers.CharField(max_length=30)
    score = serializers.IntegerField()
