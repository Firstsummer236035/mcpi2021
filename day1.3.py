from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat('X:' + str(x) + '  Y:' + str(y) + '  Z:' + str(z))



while True:
    import random
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y+1,z,95,int(random.randint(0,15)))
    mc.setBlock(x,y+2,z,95,int(random.randint(0,15)))
    mc.setBlock(x,y+3,z,95,int(random.randint(0,15)))
    mc.setBlock(x,y+4,z,95,int(random.randint(0,15)))
    mc.setBlock(x,y+5,z,95,int(random.randint(0,15)))
    mc.setBlock(x,y+6,z,95,int(random.randint(0,15)))
    mc.setBlock(x,y+7,z,95,int(random.randint(0,15)))

x,y,z = mc.player.getTilePos()
mc.setBlock(x+1,y,z,95)
mc.setBlock(x-1,y,z,95)
mc.setBlock(x,y,z+1,95)
mc.setBlock(x,y,z-1,95)
mc.setBlock(x+1,y,z+1,95)
mc.setBlock(x-1,y,z-1,95)
mc.setBlock(x+1,y,z-1,95)
mc.setBlock(x-1,y,z+1,95)

import random
while True:
    x,y,z = mc.player.getTilePos()
    r=random.randint(0,15)
    mc.setBlocks(x+2,y-1,z+2,x-2,y-1,z-2,95,r)