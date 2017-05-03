from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create()

mc.postToChat("Hello world")
x, y, z = mc.player.getTilePos()                                                  
x, y, z = mc.player.getPos()  

#mc.postToChat("LEAVES")
#mc.setBlock(x+5, y, z, 18)

#mc.postToChat("WOOD")
#mc.setBlock(x, y+5, z, 17)
#mc.postToChat("COAL_ORE")
#mc.setBlock(x, y+5, z+1, 16)
#mc.setBlocks(x,y+4, z, x+4, y+4, z+4, block.GRASS.id)
mc.setBlocks(x,y, z+2, x+4, y+4, z+2, block.IRON_BLOCK.id)
mc.setBlocks(x-1,y, z+2, x-1, y+4, z+6, block.DIAMOND_ORE.id)



#COAL_ORE             16
#WOOD                 17
#LEAVES               18
