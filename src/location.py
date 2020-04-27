import mcpi.minecraft as minecraft


mc = minecraft.Minecraft.create()
position = mc.player.getPos()
print(position)
