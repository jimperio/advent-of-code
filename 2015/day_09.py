import itertools


def solve(input):
    all_places, roads = parse_input(input)
    min_distance = None
    max_distance = None
    for route in itertools.permutations(all_places):
        distance = get_route_distance(route, roads)
        if distance is None:
            continue
        if min_distance is None or distance < min_distance:
            min_distance = distance
        if max_distance is None or distance > max_distance:
            max_distance = distance
    print min_distance
    print max_distance


def get_route_distance(route, roads):
    i = 2
    distance = 0
    while i < len(route) + 1:
        key = tuple(sorted(route[i - 2 : i]))
        if key not in roads:
            return None
        distance += roads[key]
        i += 1
    return distance


def parse_input(input):
    all_places = set()
    roads = {}
    for spec in input.split("\n"):
        places, distance = spec.split(" = ")
        a, b = places.split(" to ")
        all_places.add(a)
        all_places.add(b)
        road_key = tuple(sorted((a, b)))
        roads[road_key] = int(distance)
    return all_places, roads


input = """AlphaCentauri to Snowdin = 66
AlphaCentauri to Tambi = 28
AlphaCentauri to Faerun = 60
AlphaCentauri to Norrath = 34
AlphaCentauri to Straylight = 34
AlphaCentauri to Tristram = 3
AlphaCentauri to Arbre = 108
Snowdin to Tambi = 22
Snowdin to Faerun = 12
Snowdin to Norrath = 91
Snowdin to Straylight = 121
Snowdin to Tristram = 111
Snowdin to Arbre = 71
Tambi to Faerun = 39
Tambi to Norrath = 113
Tambi to Straylight = 130
Tambi to Tristram = 35
Tambi to Arbre = 40
Faerun to Norrath = 63
Faerun to Straylight = 21
Faerun to Tristram = 57
Faerun to Arbre = 83
Norrath to Straylight = 9
Norrath to Tristram = 50
Norrath to Arbre = 60
Straylight to Tristram = 27
Straylight to Arbre = 81
Tristram to Arbre = 90"""


if __name__ == "__main__":
    solve(input)
