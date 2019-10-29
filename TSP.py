import itertools
import googlemaps


def dynamic_tsp(points):
    all_distances = points
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
    cnt = len(points)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
        A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    print(res[1])


gmaps = googlemaps.Client(key='AIzaSyCVPMMMznJdP43cUMeDFski1_WMhibifdY')
#n=int(input("Enter the number of places\n"))
#places=[0 for i in range(n)]
#print("Enter the places\n")
#for i in range(0,n):
#    places[i]=input()
places=['New York','Los Angeles','Chicago','Minneapolis','Denver','Dallas','Seattle','Boston','San Francisco','St. Louis',' Houston','Phoenix','Salt Lake City']
matrix=[[0 for col in range(13)] for row in range(13)]
for i in range(0,13):
    for j in range(0,13):
        if(i!=j):
            my_dist = gmaps.distance_matrix(places[i],places[j])['rows'][0]['elements'][0]
            print('{} to {}:\nDistance={}\nDuration={}\n'.format(places[i],places[j],my_dist['distance']['text'],my_dist['duration']['text']))
            if my_dist['status'] == 'ZERO_RESULTS':
                continue
            matrix[i][j]=float(my_dist['distance']['text'].replace(" km","").replace(",",""))

dynamic_tsp(matrix)
