from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()  
    return mc
	
		
def gun(mc,x,y,z,direction,mussle_length): 
	print("mussle_length ",mussle_length)
	#WOOD_PLANKS  5  GLASS 20 gold 41
	m = 20 # glass
	if direction == "n" or direction ==  "s":
		#change z
		if direction == "n":
			p = 1 #p is parity
		else:
			p = -1
		print(" x,y,z ",x,y,z)
		mc.postToChat("THE CANNON")
		mc.setBlocks(x-2,y,z-2,x+2,y+5,z+2,41)
		mc.setBlocks(x-1,y-1,z-1,x+1,y+5,z+1,0)
		mc.setBlock(x,y+4,z-2,20)
		mc.setBlock(x,y+4,z+2,20)
		mc.setBlock(x+2,y+4,z-2,20)
		mc.setBlock(x-2,y+4,z+2,20)
		for l in range(2,mussle_length):
			ld = l * p
			m = 42
			mc.setBlock(x-1,y+3,z+ld,41)
			mc.setBlock(x,y+1,z+ld,41)
			mc.setBlock(x+1,y+3,z+ld,41)
			print(ld)
		
	if direction == "w" or direction == "e": 
		pass
	
def main():
	mc = init()
	#mc.player.setPos(0, 50, 0)
	x, y, z = mc.player.getPos()  
	mc.player.setPos(x, y, z)
	direction = input("Input dock direction n, s, e or w ")
	mussle_length = 10
	gun(mc,x,y,z,direction,mussle_length)
	
main()
# multiple line comment
"""xc
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
