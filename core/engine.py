class GameEngine:
    def __init__(self):
        self.games = {}

    def register_game(self, game_name, game_obj):
        self.games[game_name] = game_obj

    def launch(self, game_name):
        game = self.games.get(game_name)

        if game:
            try:
                game.start()
            except Exception as e:
                print(f"Error launching {game_name}: {e}")
        else:
            print(f"Game '{game_name}' not found")
