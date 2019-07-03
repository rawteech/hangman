# Python imports
import random

# Django core imports
from django.shortcuts import get_object_or_404

# Third party packages
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Built-in packages
from .models import Game
from .serializers import GameSerializer


def get_word():
    """
    Select a word randomly from the list and define the space it takes
    Return both the word and the space
    """
    word_list = [
        'simba', 'marvin', 'print', 'filament', 'order', 'layer', 'captain'
    ]
    rand_index = random.randrange(len(word_list))
    # Select a word and convert it into a list
    selected = word_list[rand_index]
    space = "_" * len(selected)
    return selected, space


class GameView(APIView):
    permission_classes = (IsAuthenticated,)

    def play_game(self, game=None):
        selected = list(game.selected_word)
        space = list(game.space_filled)

        # Identify user and accept input
        user_input = self.request.data['letter']
        chances = game.chance_remaining
        score = game.score

        # Replace space if correct letter is guessed
        if user_input in selected:
            # Give a score if the new letter is guessed
            # correctly and is unique
            if user_input not in space:
                score += chances

            for loc, letter in enumerate(selected):
                if user_input == letter:
                    space[loc] = letter
        else:
            # Reduce the chances the user has
            # TODO: Indicate chances remaining
            chances -= 1

        new_space = ''.join(space)
        game.chance_remaining = chances
        game.space_filled = new_space
        game.score = score
        game.save()
        data = {
            "player": self.request.user.username,
            "game_id": game.id,
            "letter": "",
            "chances": game.chance_remaining,
            "spaces": game.space_filled,
            "score": game.score
        }
        return data

    def get(self, request, game_id=None):
        """
        Initialize game
        """
        if game_id:
            game = get_object_or_404(Game, id=game_id)
            data = {
                "player": self.request.user.username,
                "game_id": game.id,
                "letter": "",
                "chances": game.chance_remaining,
                "spaces": game.space_filled,
                "score": game.score
            }
            game_serializer = GameSerializer(data)
            return Response(game_serializer.data)

        selected, space = get_word()
        new_game = Game.objects.create(
            chance_remaining=5,
            selected_word=selected,
            space_filled=space,
            user=self.request.user
        )
        data = {
                "player": self.request.user.username,
                "game_id": new_game.id,
                "letter": "",
                "chances": new_game.chance_remaining,
                "spaces": new_game.space_filled,
                "score": new_game.score
            }
        game_serializer = GameSerializer(data)
        return Response(game_serializer.data)

    def post(self, request, game_id):
        """
        Handles the game play.
        Receives the game id, retrieves the game then handles
        the game logic by passing the game as an argument
        """
        game = get_object_or_404(Game, id=game_id)
        chances = game.chance_remaining
        if chances <= 0:
            return Response("Sorry, no more chances left!")

        data = self.play_game(game)
        game_serializer = GameSerializer(data)
        return Response(game_serializer.data)


class HomeView(APIView):
    """
    The home page
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response()
