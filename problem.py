import math

PURE_BLACK = (0,0,0)
PURE_WHITE = (255,255,255)
PURE_RED = (255, 0, 0)
PURE_GREEN = (0,255,255)
PURE_BLUE = (0,0,255)

COLORS = [ 
	{ 'color': 'Black', 'hexcode': (0,0,0) },
	{ 'color': 'White', 'hexcode': (255,255,255) },
	{ 'color': 'Red', 'hexcode': (255,0,0) },
	{ 'color': 'Green', 'hexcode': (0,255,255) },
	{ 'color': 'Blue', 'hexcode': (0,0,255) }
]

def third(text):
	return [from_bin_to_color(x) for x in [text[:8], text[8:16], text[16:]]]
def from_bin_to_color(text):
	return int(text, 2)
def get_euclidean_distance(color_1, color_2):
	return math.sqrt( ( color_1[0] - color_2[0] )**2 + ( color_1[1] - color_2[1] )**2 + ( color_1[2] - color_2[2] )**2 )
def get_rough_euclidean_distance(color_1, color_2):
	return ( color_1[0] - color_2[0] )**2 + ( color_1[1] - color_2[1] )**2 + ( color_1[2] - color_2[2] )**2
def ClosestColor( hexcodes):
	closestColors = []
	for hexcode in hexcodes:
		# Third it into the relevant colors
		hexcode = third(hexcode)
		results = []
		for color in COLORS:
			result = {}
			result['color'] = color['color']
			result['distance'] = get_euclidean_distance(hexcode, color['hexcode'])
			results.append(result)
		closestDistance = min([result['distance'] for result in results if result['distance'] != 0])
		closests = [result for result in results if result['distance']==closestDistance]
		if len(closests) > 1:
			closestColor = 'Ambiguous'
		else:
			closestColor = closests[0]['color']
		closestColors.append(closestColor)
	return closestColors

