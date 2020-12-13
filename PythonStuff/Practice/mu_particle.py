def find_path(points):
	points_to_children = sorted(points, key=lambda x:x[0])

	points_x = sorted(points, key=lambda x:x[0])
	points_y = sorted(points, key=lambda x:x[1])
	for point in points_x:
		

