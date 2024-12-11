import pandas as pd
import numpy as np
import sys
import time
from bridges.bridges import Bridges
from bridges.polyline import Polyline
from bridges.circle import Circle
from bridges.symbol_collection import SymbolCollection
from itertools import cycle
#landon ward

def load_dataset(file_path):
    data = pd.read_csv(file_path)
    # print(data.head())
    return data

file_path = "uscities.csv"
cities_data = load_dataset(file_path)
# filter dataset for however many
large_cities = cities_data[cities_data['population'] > 0]
method = sys.argv[1] 
state_id = sys.argv[2] if len(sys.argv) > 2 else None
if state_id:
    filtered_cities = large_cities[large_cities['state_id'] == state_id]
else:
    filtered_cities = large_cities[
        (large_cities['lat'] >= 24) &  
        (large_cities['lat'] <= 50) & 
        (large_cities['lng'] >= -125) &  
        (large_cities['lng'] <= -66)
    ]
coordinates = filtered_cities[['lat', 'lng']].values
# see the number of cities being plotted
print(f"Number of cities: {len(coordinates)}")

def brute_force(points):
    n = len(points)
    # empty list for edges
    hull_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            
            # ax + by = c
            a = p2[1] - p1[1]  # y2-y1
            b = p1[0] - p2[0]  # x1-x2
            c = p1[0] * p2[1] - p1[1] * p2[0]  # cross product
            
            # Check if all points are on the same side of the line
            previous_sign = None
            # assume it is part of hull unless shown it is not
            is_hull_edge = True
            for point in points:
                if (point == p1).all() or (point == p2).all():
                    continue
                sign = a * point[0] + b * point[1] - c
                if previous_sign is None:
                    previous_sign = sign
                # check if the signs are different and if they are then do not add it to the hull edges
                # if you get through these two if statements then it is a hull edge
                elif (previous_sign > 0 and sign < 0) or (previous_sign < 0 and sign > 0):
                    is_hull_edge = False
                    break
            
            # If all points are on the same side, add the edge to the hull
            if is_hull_edge:
                hull_edges.append((p1, p2))
    
    return hull_edges


def sort_points_for_hull(hull_edges):
    points = []
    seen = set() 
    # this code is to get all unique pairs of points into a single list so that we can sort by angle
    for edge in hull_edges:
        for point in edge:
            point_tuple = tuple(point)
            if point_tuple not in seen:
                seen.add(point_tuple)
                points.append(point_tuple)

    start_point = min(points, key=lambda p: (p[1], p[0]))
    # returns as radians
    # o -> 2 pie smallest to biggest for the counter clockwise, p[0], p[1] act for tiebreakers
    points.sort(key=lambda p: (np.arctan2(p[1] - start_point[1], p[0] - start_point[0]), p[0], p[1]))

    return points




def is_above_line(p, p1, p2):
    # the sign of this equation tells us whether the point is above or below the line so we know if its an edge or not
    return (p2[0] - p1[0]) * (p[1] - p1[1]) - (p2[1] - p1[1]) * (p[0] - p1[0]) > 0

def create_hull(line, points, hull):
    if not points:
        return
    # get endpoints
    p1, p2 = line
    max_dist = -1
    pmax = None

    for p in points:
        # use distance formula to get the distance from the line, farthest point gets added to the convex hull
        dist = abs((p2[1] - p1[1]) * p[0] - (p2[0] - p1[0]) * p[1] + p2[0] * p1[1] - p2[1] * p1[0]) / (
            ((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2) ** 0.5
        )
        if dist > max_dist:
            max_dist = dist
            pmax = p

    # recusively call create hull to continue until you get to smallest set of points
    # get convex left of pmax and right of pmax
    left_line = [p for p in points if is_above_line(p, p1, pmax)]
    create_hull((p1, pmax), left_line, hull)
    # add it after to get the correct order or edges
    hull.append(pmax)

    right_line = [p for p in points if is_above_line(p, pmax, p2)]
    create_hull((pmax, p2), right_line, hull)


def divide_and_conquer(points):
    # sort lattitude coordinates(x coord)
    points = sorted(points, key=lambda p: (p[0], p[1]))
    # left most and right most points on the hull
    p1, p2 = points[0], points[-1]
    # start building what is the hull on the upper with the left most point, p1 as the first edge
    upper_hull = [p1]
    # getting all the points that is on the upper hull
    upper = [p for p in points if is_above_line(p, p1, p2)]
    # build the convex hull for all the points that are above the line p1 to p2
    create_hull((p1, p2), upper, upper_hull)
    upper_hull.append(p2)
    # start the lower hull
    lower_hull = [p2]
    lower = [p for p in points if is_above_line(p, p2, p1)]
    create_hull((p2, p1), lower, lower_hull)
    lower_hull.append(p1)

    hull = upper_hull + lower_hull[1:-1] # combine the two hulls, remove duplicates, already in order, but we still call sort just to be surea
    # this makes it so it turns the points into a list of edges that way you know the endooints which have the line segment
    return [(hull[i], hull[(i + 1) % len(hull)]) for i in range(len(hull))]

def visualize_with_bridges(coordinates, hull_edges):
    bridges = Bridges(233, "lrw0404", "548580948654")
    bridges.title = "Convex Hull of Continental US Cities"

    symbol_collection = SymbolCollection()

    for coord in coordinates:
        circle = Circle()
        circle.set_circle(coord[1], coord[0], 0.1) 
        circle.fill_color = "red"
        symbol_collection.add_symbol(circle)

    sorted_hull_points = sort_points_for_hull(hull_edges)

    polyline = Polyline()
    for point in sorted_hull_points:
        polyline.add_point(point[1], point[0]) 
    # verif that points are in correct order
    polyline.add_point(sorted_hull_points[0][1], sorted_hull_points[0][0])
    polyline.stroke_width = 0.1
    polyline.stroke_color = "orange"
    symbol_collection.add_symbol(polyline)

    bridges.set_data_structure(symbol_collection)
    bridges.visualize()

# to run the program do either python project.py brute_force or python project.py divide_and_conquer
if method == "brute_force":
    print("Running Brute Force:")
    start_time = time.time()
    hull_edges = brute_force(coordinates)
    end_time = time.time()
    print(f"Brute Force Execution Time: {end_time - start_time:.4f} seconds")
elif method == "divide_and_conquer":
    print("Running Divide and Conquer:")
    start_time = time.time()
    hull_edges = divide_and_conquer(coordinates)
    end_time = time.time()
    print(f"Divide and Conquer Execution Time: {end_time - start_time:.4f} seconds")
visualize_with_bridges(coordinates, hull_edges)
