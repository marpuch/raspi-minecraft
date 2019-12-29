import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

p = mc.player.getPos()
s = 10
h = 8

mc.setBlocks(p.x, p.y-1, p.z, p.x+s, p.y+h, p.z+s, block.STONE)
mc.setBlocks(p.x+1, p.y, p.z+1, p.x+s-1, p.y+h-1, p.z+s-1, block.AIR)

mc.setBlocks(p.x+s/2, p.y, p.z, p.x+s/2, p.y+1, p.z, block.DOOR_IRON)

mc.setBlock(p.x+s/2-1, p.y+1, p.z+1, block.TORCH)
mc.setBlock(p.x+s/2-1, p.y+1, p.z-1, block.TORCH)
mc.setBlock(p.x+s/2+1, p.y+1, p.z+1, block.TORCH)
mc.setBlock(p.x+s/2+1, p.y+1, p.z-1, block.TORCH)

mc.setBlock(p.x+2, p.y, p.z+2, block.BED)
mc.setBlock(p.x+2, p.y, p.z+1, block.BED)
