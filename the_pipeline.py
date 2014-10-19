import math
 
def reconstruct_path(came_from, current_node):
        if current_node in came_from:
                p = (reconstruct_path(came_from, came_from[current_node]))
                return (p + current_node)
        else:
                return current_node

def count_path(path_list):
	z = 0
	count = 0
 	while z < len(path_list):
		count += city[path_list[z]][path_list[z+1]]
		z += 2

	return count

 
def heuristic_cost_estimate(start, goal):
        d1 = start[0] - goal[0]
        d2 = start[1] - goal[1]
        return int(math.fabs(d1 + d2))
        #return 0
 
def neighbors_nodes(node):
        neighbors = list()
        if node[0]-1 >= 0:
                neighbors.append((node[0]-1, node[1]))
       
        if node[1]-1 >= 0:
                neighbors.append((node[0], node[1]-1))
 
        if node[0]+1 < matrix_size:
                neighbors.append((node[0]+1, node[1]))
 
        if node[1]+1 < matrix_size:
                neighbors.append((node[0], node[1]+1))

	#print(neighbors) 
        return neighbors
 
#Get the size of the matrix
matrix_size = int(raw_input())
 
p = list()

minpath = list()
 
#Raise an error if the size is < 1 or > 1000
try:
        if matrix_size  < 1 or matrix_size > 1000:
                raise ValueError()
except ValueError:
        print("Matrix size error")
 
#Input the city matrix and check the digging cost
city = []
 
try:
        for i in xrange(matrix_size):
                city.append([int(x) for x in raw_input().split(" ")])
                for j in city[-1]:
                        if j < 0 or j > 1000000:
                                raise ValueError()
except ValueError:
        print("Cost of digging error")
 
# A*
for i in xrange(matrix_size):
        for j in xrange(matrix_size):
		#print("i" + str(i) + "j" + str(j))
                closedset = set()
                openset = set()
                openset.add((i, 0))
                came_from = {}
 
                g_score = {}
                g_score[(i, 0)] = city[i][0]
                f_score = {}
                f_score[(i, 0)] = g_score[(i, 0)]

                while openset != set():
			#print("i : "+str(i))
			#print("j : "+str(j))
			current = (i, j)
			current_value = math.pow(matrix_size, 2)

			
                        for elem in openset:
				if len(openset) == 1:
					current = elem
					current_value = f_score[elem]
					continue
	
                                if f_score[elem] <= current_value:
                                        current = elem
					current_value = f_score[elem]
               
                        if current == (j, matrix_size-1):
				minpath.append(count_path(reconstruct_path(came_from, (j, matrix_size-1))))
			
			#print(current)
			
			#print(closedset) 
                        openset.remove(current)
                        closedset.add(current)
 			              
                        for neighbor in neighbors_nodes(current):
                                if neighbor in closedset:
                                        continue
 
                                tentative_g_score = g_score[current] + city[neighbor[0]][neighbor[1]]

                                if neighbor not in openset or tentative_g_score < g_score[neighbor]:
                                        came_from[neighbor] = current
                                        g_score[neighbor] = tentative_g_score
                                        f_score[neighbor] = g_score[neighbor]
                                        if neighbor not in openset:
                                                openset.add(neighbor)


print(min(minpath))







