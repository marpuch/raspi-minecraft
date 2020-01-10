import mcpi.block as block
import mcpi.minecraft as minecraft


class Model:
    def __init__(self, mcraft: minecraft.Minecraft):
        self.p = mcraft.player.getPos()
        self.mc = mcraft

    def build_walls(self, plan, y0, y1):
        for pos_z, z in enumerate(plan):
            for pos_x, x in enumerate(z):
                if x == 'x':
                    self.build_blocks(pos_x, y0, pos_z,
                                      pos_x, y1, pos_z)
                elif x == 'l':
                    self.build_blocks(pos_x, y0, pos_z,
                                      pos_x, y1, pos_z, block.LAVA_FLOWING)
                elif x == 't':
                    self.build_blocks(pos_x, y0, pos_z,
                                      pos_x, y1, pos_z, block.AIR)
                    self.build_blocks(pos_x, y0, pos_z,
                                      pos_x, y0, pos_z, block.TORCH)
                elif x == ' ':
                    self.build_blocks(pos_x, y0, pos_z,
                                      pos_x, y1, pos_z, block.AIR)

    def build_blocks(self, x0, y0, z0, x1, y1, z1, b=block.STONE):
        self.mc.setBlocks(self.p.x + x0, self.p.y + y0, self.p.z + z0,
                          self.p.x + x1, self.p.y + y1, self.p.z + z1,
                          b)
