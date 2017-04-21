
def rect_intersection(rect1, rect2):
	# since we know x1 < x2 and y1 < y2, so we dont need to
	# check rect1_x1 against rect2_x2
	rect1_x1 = rect1['left_x']
	rect1_x2 = rect1_x1 + rect1['width']
	rect1_y1 = rect1['bottom_y']
	rect1_y2 = rect1_y1 + rect1['height']

	rect2_x1 = rect2['left_x']
	rect2_x2 = rect2_x1 + rect2['width']
	rect2_y1 = rect2['bottom_y']
	rect2_y2 = rect2_y1 + rect2['height']

	result_rect = {}
	x_overlap = overlap((rect1_x1, rect1_x2), (rect2_x1, rect2_x2))
	y_overlap = overlap((rect1_y1, rect1_y2), (rect2_y1, rect2_y2))

	if x_overlap and y_overlap:
		result_rect['left_x'] = x_overlap[0]
		result_rect['width'] = x_overlap[1] - x_overlap[0]
		result_rect['bottom_y'] = y_overlap[0]
		result_rect['height'] = y_overlap[1] - y_overlap[0]

	return result_rect

def overlap(seg1, seg2):
	if seg1[0] > seg2[0]:
		return overlap(seg2, seg1)
	start, end = 0, 0
	if seg1[0] <= seg2[0] <=seg1[1]:
		start = seg2[0]
		end = min(seg1[1], seg2[1]) 

	if end - start > 0:
		return (start, end)
	else:
		return None


rect1 = {
 'left_x': 1,
 'bottom_y': 5,
 'width': 10,
 'height': 4,
}

rect2 = {
 'left_x': 2,
 'bottom_y': 7,
 'width': 10,
 'height': 4,
}

print rect_intersection(rect1, rect2)