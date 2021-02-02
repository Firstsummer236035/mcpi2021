from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
r=random.randint(0,5)
x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+15,y+5,z+10,5,r)
mc.setBlocks(x+1,y+1,z+1,x+14,y+4,z+9,7)
mc.setBlocks(x+2,y+2,z+2,x+13,y+3,z+8,28)



import time
import random

while True:
    r=random.randint(0,8)
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,38,r)
    time.sleep(0.5)
    
    
import time  
while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    time.sleep(0.2)
    mc.setBlock(x,y-1,z,19)
    time.sleep(5)
    
    
import random
while True:
    x,y,z = mc.player.getTilePos()
    a = mc.getBlock(x+10,y-1,z) 
    b = mc.getBlock(x-10,y-1,z)
    c = mc.getBlock(x,y-1,z+10)
    d = mc.getBlock(x,y-1,z-10)
    r=random.randint(0,15)
    
    if a == 8 or a == 9 or b == 8 or b == 9 or c == 8 or c == 9 or d == 8 or d == 9:
        mc.setBlocks(x-3,y-1,z-3,x+3,y-1,z+3,95,r)
        
        
x,y,z = mc.player.getTilePos()

a = 0
while a < 10:
    mc.setBlocks(x+10,y-1,z,x-5,y-5,z,19)
    z = z+5
    a = a+1
    
    
    
x,y,z = mc.player.getTilePos()
a = int(input('What block do you want to put?'))
mc.setBlock(x,y,z,a)








name = input('your name:')
message = input('your message:')
mc.postToChat('<' + name + '> ' + message)











x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,'@#!F!@##','%^&U^&^%','*^%C$%^','$%^K!@#')
           
           
while True:          
    x,y,z = mc.player.getTilePos()
    
    a = mc.getBlockWithData(x,y-1,z)
    if a.data == 15:
        mc.postToChat('死路')
        
    if a.data == 11:
        mc.postToChat('右轉')
        
        
        
        
        
        
        

while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z 
        block = mc.getBlock(x,y,z)
        mc.postToChat("BLOCK ID: " + str(block))
        
        
        
        
        
        
while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z 
        block = mc.getBlock(x,y,z)
        
        if block == 1:
            mc.setBlock(x,y,z,41)
            
        if block == 2:
            mc.setBlock(x,y,z,57)
            
        if block == 3:
            mc.setBlock(x,y,z,133)
            
            
            
while True:            
    x,y,z = mc.player.getTilePos()
    mc.spawnEntity(x,y,z,93)