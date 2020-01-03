"""
Generate gold while walking

Short script to turn into gold everything the user walks on.
Even air... Seriously. Not a bug, a feature.
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

if __name__ == "__main__":
    while True:
        position = mc.player.getPos()
        mc.setBlock(position.x, position.y - 1, position.z, block.GOLD_BLOCK)
        time.sleep(0.1)
