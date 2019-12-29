import mcpi.block as block
import mcpi.minecraft as minecraft


class Castle:

    c = [
        '                                           ',
        '   xxx                               xxx   ',
        '  xlllxt                           txlllx  ',
        ' xlllllxxxxxxxxxxxxxxxxxxxxxxxxxxxxxlllllx ',
        ' xlllllllllllllllllllllllllllllllllllllllx ',
        ' xllllllxxxxxxxxxxxxxxxxxxxxxxxxxxxllllllx ',
        ' txllllx                           xllllxt ',
        '   xlxxt                           txxlx   ',
        '   xlx                               xlx   ',
        '   xlx                               xlx   ',
        '   xlx                               xlx   ',
        '   xlx           xxxxxxxxxx          xlx   ',
        '   xlx           x        x          xlx   ',
        '   xlx           x        x          xlx   ',
        '   xlx           x        x          xlx   ',
        '   xlx           x        x          xlx   ',
        '   xlx           xxxxxxxxxx          xlx   ',
        '   xlx                               xlx   ',
        '   xlx                               xlx   ',
        '   xlxx                             xxlx   ',
        ' txllllxt                         txllllxt ',
        ' xllllllx                         xllllllx ',
        ' xllllllxxxxxxxxxxxxxxxxxxxxxxxxxxxllllllx ',
        ' xlllllllllllllllllllllllllllllllllllllllx ',
        '  xllllxxxxxxxxxxxxxxxxxxxxxxxxxxxxxllllx  ',
        '   xxxxt                           txxxx   ',
        '                                           '
    ]

    c1 = [
        '   xxx                               xxx   ',
        '  xxxxx                             xxxxx  ',
        ' xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ',
        'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        ' xxxxxxx                           xxxxxxx ',
        '  xxxxx                             xxxxx  ',
        '  xxxx                               xxxx  ',
        '  xxxx                               xxxx  ',
        '  xxxx                               xxxx  ',
        '  xxxx           xxxxxxxxxx          xxxx  ',
        '  xxxx           xxxxxxxxxx          xxxx  ',
        '  xxxx           xxxxxxxxxx          xxxx  ',
        '  xxxx           xxxxxxxxxx          xxxx  ',
        '  xxxx           xxxxxxxxxx          xxxx  ',
        '  xxxx           xxxxxxxxxx          xxxx  ',
        '  xxxx                               xxxx  ',
        '  xxxx                               xxxx  ',
        '  xxxxx                             xxxxx  ',
        ' xxxxxxx                           xxxxxxx ',
        'xxxxxxxxx                         xxxxxxxxx',
        'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        ' xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ',
        '  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  ',
        '   xxx                               xxx   '
    ]

    c2 = [
        '   xxx                               xxx   ',
        '  x   x                             x   x  ',
        ' x     xxxxxxxxxxxxxxxxxxxxxxxxxxxxx     x ',
        'x                                         x',
        'x                                         x',
        'x                                         x',
        ' x                                       x ',
        '  x                                     x  ',
        '  x                                     x  ',
        '  x                                     x  ',
        '  x                                     x  ',
        '  x              xxxxxxxxxx             x  ',
        '  x              xxxxxxxxxx             x  ',
        '  x              xxxxxxxxxx             x  ',
        '  x              xxxxxxxxxx             x  ',
        '  x              xxxxxxxxxx             x  ',
        '  x              xxxxxxxxxx             x  ',
        '  x                                     x  ',
        '  x                                     x  ',
        '  x                                     x  ',
        ' x                                       x ',
        'x                                         x',
        'x                                         x',
        'x                                         x',
        ' x                                       x ',
        '  x   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   x  ',
        '   xxx                               xxx   '
    ]

    c3 = [
        '   x x                               x x   ',
        '  x                                     t  ',
        ' t     xtx x x x x x x x x x x x xtx     x ',
        'x                                          ',
        '                                          x',
        'x                                          ',
        '                                         x ',
        '  x                                     t  ',
        '  t                                     x  ',
        '  x                                        ',
        '                                        x  ',
        '  x              xxxxxxxxxx                ',
        '                 xxxxxxxxxx             x  ',
        '  x              xxxxxxxxxx                ',
        '                 xxxxxxxxxx             x  ',
        '  x              xxxxxxxxxx                ',
        '                 xxxxxxxxxx             x  ',
        '  x                                        ',
        '                                        x  ',
        '  x                                     t  ',
        '  t                                      x ',
        'x                                          ',
        '                                          x',
        'x                                          ',
        ' t                                       x ',
        '  x   x x x x x x x x x x x x x x x x   t  ',
        '    x                                x x   '
    ]

    c4 = [
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                 xxxxxxxxxx                ',
        '                 x        x                ',
        '                 x        x                ',
        '                 x        x                ',
        '                 x        x                ',
        '                 xxxxxxxxxx                ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           '
    ]

    c5 = [
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                xxxxxxxxxxxx               ',
        '                xxxxxxxxxxxx               ',
        '                xxxxxxxxxxxx               ',
        '                xxxxxxxxxxxx               ',
        '                xxxxxxxxxxxx               ',
        '                xxxxxxxxxxxx               ',
        '                xxxxxxxxxxxx               ',
        '                xxxxxxxxxxxx               ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           '
    ]

    c6 = [
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                xxxxxxxxxxxx               ',
        '                x          x               ',
        '                x          x               ',
        '                x          x               ',
        '                x          x               ',
        '                x          x               ',
        '                x          x               ',
        '                xxxxxxxxxxxx               ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           '
    ]

    c7= [
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                x x x x x xt               ',
        '                           x               ',
        '                x                          ',
        '                           x               ',
        '                x                          ',
        '                           x               ',
        '                x                          ',
        '                tx x x x x x               ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           ',
        '                                           '
    ]

    def __init__(self, mc: minecraft.Minecraft):
        self.height = 10
        self.p = mc.player.getPos()
        self.mc = mc

    def build(self):
        """
        Builds a castle.
        """
        self.build_floor()
        self.build_walls(self.c, 0, self.height)
        self.build_l1_floor()
        self.build_l2_floor()

    def build_l1_floor(self):
        self.build_walls(self.c1, self.height+1, self.height+1)
        self.build_walls(self.c2, self.height+2, self.height+2)
        self.build_walls(self.c3, self.height+3, self.height+3)

    def build_l2_floor(self):
        self.build_walls(self.c4, self.height + 4, self.height + 8)
        self.build_walls(self.c5, self.height + 9, self.height + 9)
        self.build_walls(self.c6, self.height + 10, self.height + 10)
        self.build_walls(self.c7, self.height + 11, self.height + 11)

    def build_floor(self):
        self.build_blocks(0, -1, 0,
                          len(self.c[0]), -1, len(self.c))

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


mc = minecraft.Minecraft.create()
castle = Castle(mc)
castle.build()
