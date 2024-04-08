from classes import ChampInfo


def distance_validation(info: ChampInfo) -> bool:
    actual = info.distance

    max_dist = '50m'
    for dist in info.swimmers[0].distances:
        if len(dist.distance) > len(max_dist) or int(dist.distance[0]) > int(max_dist[0]):
            max_dist = dist.distance

    return is_valid_distance(actual=actual, max_dist=max_dist)


def is_valid_distance(actual: str, max_dist: str) -> bool:
    if actual not in ['50m', '100m', '200m', '400m']:
        return False
    
    actual = actual[:len(actual)-1]
    max_dist = max_dist[:len(max_dist)-1]

    return int(actual) == int(max_dist)


def min_to_sec_convert(full_info: ChampInfo):
    for person in full_info.swimmers:
        for distance in person.distances:
            if ':' in distance.time:
                distance.time = min_to_sec(distance.time)
            if ':' in distance.total:
                distance.total = min_to_sec(distance.total)


def min_to_sec(time: str) -> str:
    mins_time = time.split(':')
    secs_split = mins_time[1].split('.')

    secs = int(mins_time[0]) * 60 + int(secs_split[0])

    return str(secs) + '.' + secs_split[1]
