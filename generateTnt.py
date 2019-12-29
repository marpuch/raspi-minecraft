import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

position = mc.player.getPos()

for i in range(0, 100):
    mc.setBlock(position.x, position.y - i, position.z, block.TNT)

