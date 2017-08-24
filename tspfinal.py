import math
import itertools
import re
import time
import matplotlib.pyplot as plt
import copy
cities_set = []
cities_tups = []
cities_dict = {}
cities_dist = []


def read_tsp_data(tsp_name):
    tsp_name = tsp_name
    with open(tsp_name) as f:
        content = f.read().splitlines()
        cleaned = [x.lstrip() for x in content if x != ""]
        return cleaned


def detect_dimension(in_list):
    non_numeric = re.compile(r'[^\d]+')
    for element in in_list:
        if element.startswith("DIMENSION"):
            return non_numeric.sub("", element)


def get_cities(list, dimension):
    dimension = int(dimension)
    for item in list:
        for num in range(1, dimension + 1):
            if item.startswith(str(num)):
                index, space, rest = item.partition(' ')
                if rest not in cities_set:
                    cities_set.append(rest)
    return cities_set


def cities_list(cities_tup):
    r = [list(x)[1] for x in cities_tup]
    return r


def city_tup(list):
    for item in list:
        first_coord, space, second_coord = item.partition(' ')
        cities_tups.append((first_coord.strip(), second_coord.strip()))
    return cities_tups


def intmaker(strt):

    r = []
    # for x in cc:
    #     l.append(list(x))
    # # cc = list(map(int, cc))
    strt2 =  []
    for i in range(0, len(strt)):
        strt2.append(list(map(float, strt[i])))
    return (strt2)


def create_cities_dict(cities_tups):
    return zip((range(1, len(cities_tups) + 1)), cities_tups)


def distance(route):
    disum = 0

    len_route = (len(route[0]))
    # print(route[0][0])
    for j in route:
        # print(j)
        j = list(j)
        # print(j)
        # j.append(route[0][0])

        for i in range(len(j)):
            # try:
            #     print(i, len(j))

                if(i == len(j)-1):
                    r1 = route[0][i]
                    r2 = route[0][0]
                    j = list(j)
                    disum += math.sqrt((r1[0]-r2[0])**2 + (r1[1]-r2[1])**2)
                    # print(j)
                    j.append(route[0][0])
                    # print("yes")
                    cities_dist.append([j, disum])
                    # print(cities_dist)
                else:
                    r1 = route[0][i]
                    r2 = route[0][i+1]
                    disum += math.sqrt((r1[0]-r2[0])**2 + (r1[1]-r2[1])**2)
                    j = list(j)
                    # print(type(j))
                    cities_dist.append([j, disum])

            # except IndexError:
            #     # pass
            #     # print("yesy")
            #     r1 = route[0][i]
            #     r2 = route[0][0]
            #     j = list(j)
            #     disum += math.sqrt((r1[0]-r2[0])**2 + (r1[1]-r2[1])**2)
            #     # j.append(route[0][0])
            #     cities_dist.append([j, disum])
    print(cities_dist)
    return cities_dist

def cost(route):
    sum = 0
    # Go back to the start when done.
    route.append(route[0])
    while len(route) > 1:
        p0, *route = route
        sum += math.sqrt((int(p0[0]) - int(route[0][0]))**2 + (int(p0[1]) - int(route[0][1]))**2)
    return [route, sum]


def final(file="berlin5.tsp"):

    start = time.time()
    data = read_tsp_data(file)
    dimension = detect_dimension(data)
    cities_set = get_cities(data, dimension)
    cities_tups = city_tup(cities_set)
    cities_dict = list(create_cities_dict(cities_tups))
    # print(cities_tups)
    ct = cities_list(cities_dict)
    ci = list(intmaker(ct))
    route = list(itertools.permutations(ci))
    # print(route)
    dr = distance(route)
    # print(dr)
    d = float("inf")
    cbs = []

    for r in dr:
        if(r[1] < d):
            cbs = r[0]
            d = r[1]
            print(cbs)
            # print(r[0])
            # print(type(r[0]))
            plotter(r[0], nw=True, cb=cbs)
        else:
            plotter(r[0],cb=cbs)
    # for p in itertools.permutations(ci):
    #     # print(p)
    #     c = cost(list(p))
    #     if c[1] <= d:
    #         d = c[1]
    #         pmin = p
    #         plotter(pmin,sum = d)

    # print("Optimal route:", pmin)
    print("Length:", d)


def plotter(lst, cb=None, nw=False, stop=False, sum=None):

    cv = list(zip(*lst))
    cbs = list(zip(*cb))
    ccv = copy.deepcopy(cv)
    if(nw == True):
        plt.figure(1)
        plt.ion()
        plt.clf()
        plt.subplot(211)             # the first subplot in the first figure
        plt.scatter(*cbs)
        plt.plot(*cbs)
        plt.subplot(212)             # the second subplot in the first figure
        plt.scatter(*cbs)
        plt.plot(*cbs)
    else:
        plt.figure(1)
        plt.ioff()
        plt.clf()
        plt.subplot(211)             # the first subplot in the first figure
        plt.scatter(*cv)
        plt.plot(*cv)
        plt.subplot(212)             # the second subplot in the first figure
        plt.scatter(*cbs)
        plt.plot(*cbs)
    # plt.plot([40, 5, 6])
    # print(cv)
    # if(nw == True):
    #     plt.figure(1)
    #     plt.subplot(222)
    #     # plt.close(3)
    #     # plt.figure()
    #     # plt.ion()
    #     # plt.clf()
    #     plt.scatter(*cv)
    #     plt.plot(*cv)
    #     plt.show()
    #     # plt.pause(10000000)
    #     # plt.close()
    # else:
    #     plt.figure(1)
    #     plt.subplot(211)
    #     plt.ion()
    #     plt.clf()
    #     plt.scatter(*cv)
    #     plt.plot(*cv)
    #     plt.text(500, 500, sum)
    #     plt.show()
    # if(stop == True):
    #     pass
    plt.pause(0.00001)


if __name__ == '__main__':
    final()
    # time.sleep(90)
