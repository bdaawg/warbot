#!/usr/bin/env python3
"""
    WarBot: Run a Full (Simulated) Game
    ===================================

"""

import sys

sys.path.append("src/")

import warbot
import WorldSelector
import HistoricStatistician as hs



def main():
    """Run the full game."""

    print(__doc__)
    world_file = WorldSelector.select_world()
    wb = warbot.WarBot(world_file)
    wb.run()



if __name__ == "__main__":
    main()
