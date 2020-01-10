"""
Tunnel generator

Generates actually two tunnels. One of glass
(so we can see through), on of air (so we can walk inside).

Positioning of player can still be improved.
"""

import mcpi.minecraft as minecraft
import mcpi.block as block


def generate_tunnel():
    mc = minecraft.Minecraft.create()
    position = mc.player.getPos()
    mc.setBlocks(position.x, position.y, position.z,
                 position.x+3, position.y+3, position.z+100,
                 block.GLASS)

    mc.setBlocks(position.x+1, position.y+1, position.z,
                 position.x+2, position.y+2, position.z+100,
                 block.AIR)


if __name__ == '__main__':
    generate_tunnel()
