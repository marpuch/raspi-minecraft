"""
Tadeks' ball

As the name implies generates a giant ball.
Guess what, the ball is square.
And it's made of TNT.

Property of Tadek.
"""

import mcpi.minecraft as minecraft
import mcpi.block as block


def generate_ball():
    mc = minecraft.Minecraft.create()
    position = mc.player.getPos()
    mc.setBlocks(position.x, position.y, position.z,
                 position.x + 10, position.y - 10, position.z + 10,
                 block.TNT)


if __name__ == '__main__':
    generate_ball()
