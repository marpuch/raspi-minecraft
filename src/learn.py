import mcpi.block as block
import mcpi.minecraft as minecraft
from collections import namedtuple

block = block
Point = namedtuple("Point", "x y z")


class MC:
    def __init__(self, x, y, z, address="localhost", port=4711):
        self.mc = minecraft.Minecraft.create(address, port)
        self.pos = Point(x, y, z)
        self.box_size = 10

    def put(self, x, y, z, b=block.STONE):
        if x > self.box_size or x < 0 or \
           y > self.box_size or y < 0 or \
           z > self.box_size or z < 0:
            print("Block must be in the box of size {} {}".format(self.box_size, (x, y, z)))
            return
        self.mc.setBlock(self.pos.x + x, self.pos.y + y, self.pos.z + z, b)

    def clean(self):
        self.mc.setBlocks(self.pos.x, self.pos.y-1, self.pos.z,
                          self.pos.x + self.box_size, self.pos.y-self.box_size, self.pos.z + self.box_size,
                          block.GLOWSTONE_BLOCK)
        self.mc.setBlocks(self.pos.x, self.pos.y, self.pos.z,
                          self.pos.x + self.box_size, self.pos.y+self.box_size, self.pos.z + self.box_size,
                          block.AIR)
        self.mc.setBlocks(self.pos.x-1, self.pos.y, self.pos.z-1,
                          self.pos.x+self.box_size+1, self.pos.y+self.box_size+1, self.pos.z+self.box_size+1,
                          block.GLASS)
        self.mc.setBlocks(self.pos.x-1, self.pos.y, self.pos.z,
                          self.pos.x+self.box_size+1, self.pos.y+self.box_size, self.pos.z+self.box_size,
                          block.AIR)
        self.mc.setBlocks(self.pos.x, self.pos.y, self.pos.z-1,
                          self.pos.x+self.box_size, self.pos.y+self.box_size, self.pos.z+self.box_size+1,
                          block.AIR)

    def say(self, text="Hello World!"):
        self.mc.postToChat(text)
