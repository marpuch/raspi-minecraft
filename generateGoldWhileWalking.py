import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

while True:
    position = mc.player.getPos()
    mc.setBlock(position.x, position.y - 1, position.z, block.GOLD_BLOCK)
    time.sleep(0.5)
