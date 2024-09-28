#!/usr/bin/env python3

import click
import time

import os

ascii_art = """
  ______  __    __  .______    _______   ______      ___      .______       _______  
 /      ||  |  |  | |   _  \  |   ____| /      |    /   \     |   _  \     |       \ 
|  ,----'|  |  |  | |  |_)  | |  |__   |  ,----'   /  ^  \    |  |_)  |    |  .--.  |
|  |     |  |  |  | |   _  <  |   __|  |  |       /  /_\  \   |      /     |  |  |  |
|  `----.|  `--'  | |  |_)  | |  |____ |  `----. /  _____  \  |  |\  \----.|  '--'  |
 \______| \______/  |______/  |_______| \______|/__/     \__\ | _| `._____||_______/ 
                                                                                     
"""

@click.command()
def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    while True:
        for colour in colours:
            type_ascii(colour)
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')


def type_ascii(colour):
    for char in ascii_art:
        click.echo(click.style(char, fg=colour), nl=False)
        time.sleep(0.001)

if __name__ == '__main__':
    main()

