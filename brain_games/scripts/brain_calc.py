#!/usr/bin/env python3


from brain_games.start_games import start_or_end_games
from brain_games.games import brain_calc


def main():
    start_or_end_games(brain_calc)


if __name__ == '__main__':
    main()
