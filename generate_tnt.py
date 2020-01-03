"""
Generate TNT

Generates a column of TNT in the players position
going 100 blocks deep.
"""

import mcpi.minecraft as minecraft
import mcpi.block as block

if __name__ == '__main__':
    mc = minecraft.Minecraft.create()
    position = mc.player.getPos()
    for i in range(0, 100):
        mc.setBlock(position.x, position.y - i, position.z, block.TNT)
