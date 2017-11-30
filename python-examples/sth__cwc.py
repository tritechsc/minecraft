from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import math

def init(): 
    mc = Minecraft.create("192.168.1.13", 4711)
    x, y, z = mc.player.getPos()  
    return mc

def clear_with_air(mc, x, y, z,h,k,l):
	air = 0
	mc.setBlocks(x-h, y-k, z-l, x+h, y+k, z+l, air) 
	
def deck (mc, x, y, z,w,m):
	x2, y2, z2 = mc.player.getPos() 
	wadj = int(w/2)
	yadj = y - 1
	mc.setBlocks(x-wadj,yadj,z-wadj,x+wadj,yadj,z+wadj,m) #base

	
	#poles
	mc.setBlocks(x-wadj+1,yadj+3,z-wadj,x-wadj,yadj-100,z-wadj+1,21)# - -
	mc.setBlocks(x-wadj+1,yadj+3,z+wadj,x-wadj,yadj-100,z+wadj-1,21)# - +
	mc.setBlocks(x+wadj-1,yadj+3,z+wadj,x+wadj,yadj-100,z+wadj-1,21)# + +
	mc.setBlocks(x+wadj-1,yadj+3,z-wadj,x+wadj,yadj-100,z-wadj+1,21)# + -
	t = 0
	k = 0
	mc.player.setPos(x2, y2, z2)
	while t < (8 * math.pi):
		t = t + math.pi / 8
		h = x+ math.cos(t)*5
		l = z+math.sin(t)*5
		print(t,h,l)
		mc.setBlocks(h-2,k,l-2,h+2,k,l+2,22)
		k = k + 1
	mc.setBlocks(x-wadj,k,z-wadj,x+wadj,k,z+wadj,7) 
	mc.player.setPos(x2, y2, z2)
	
	
def main():
	mc = init()
	x, y, z = mc.player.getPos()  
	mc.player.setPos(x, y, z)
	h,k,l = 30,30,30
	#clear_with_air(mc, x,y,z,h,k,l)
	m = 20 # glass = 20
	w = 20 # width of deck
	deck(mc,x,y,z,w,m)
	
	
main()
# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
