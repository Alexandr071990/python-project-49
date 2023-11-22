#!/usr/bin/env python3


from brain_games.start_games import start_or_end_games
from brain_games.games_scripts import game_brain_progression


def main():
    start_or_end_games(game_brain_progression)


if __name__ == '__main__':
    main()
