def add_connection(neighbourList, toNode): #WARNING TIS IS MUTABLE
    tabletestcell = [toNode[0], 1]
    #name = toNode[0]
    neighbourList.append(tabletestcell)



def generate_navmesh(width, height, navmesh_nodes, neighbour_list):
    index = 0
    #Defines the mesh neighbours 
    for row in range(height):
        for column in range(width):
            currentNode = navmesh_nodes[index]
            nearbyList = [currentNode[0]]

            if (row == 0 and column == 0): #EDGE CASE: Bottom Left Corner
                print("Bottom left corner")
                sublist = []
                add_connection(sublist, navmesh_nodes[row * width + (column+1)])
                add_connection(sublist, navmesh_nodes[(row+1) * width + (column+1)])
                add_connection(sublist, navmesh_nodes[(row+1) * width + column])
                nearbyList.append(sublist)
            elif (row == 0 and column == width-1): #EDGE CASE: Top Left Corner
                print("Top left corner")
                sublist = []
                add_connection(sublist, navmesh_nodes[(row+1) * height + column])
                add_connection(sublist, navmesh_nodes[(row+1) * height + (column-1)])
                add_connection(sublist, navmesh_nodes[row * height + (column-1)])
                nearbyList.append(sublist)
            elif (row == height-1 and column == 0): #EDGE CASE: Bottom Right Corner
                sublist = []
                add_connection(sublist, navmesh_nodes[(row-1) * width + column])
                add_connection(sublist, navmesh_nodes[(row-1) * width + (column+1)])
                add_connection(sublist, navmesh_nodes[row * width + (column+1)])
                nearbyList.append(sublist)
            elif (row == height-1 and column == width-1): #EDGE CASE: Top Right Corner
                print("Top right corner")
                sublist = []
                add_connection(sublist, navmesh_nodes[(row-1) * width + column])
                add_connection(sublist, navmesh_nodes[(row-1) * width + (column-1)])
                add_connection(sublist, navmesh_nodes[row * width + (column-1)])
                nearbyList.append(sublist)
            elif (row == 0): #EDGE CASE: Left Edge
                print("Left Edge")
                sublist = []
                add_connection(sublist, navmesh_nodes[row * width + (column+1)])
                add_connection(sublist, navmesh_nodes[(row+1) * width + (column+1)])
                add_connection(sublist, navmesh_nodes[(row+1) * width + column])
                add_connection(sublist, navmesh_nodes[(row+1) * width + (column-1)])
                add_connection(sublist, navmesh_nodes[row * width + (column-1)])
                nearbyList.append(sublist)
            elif (column == 0): #EDGE CASE: Bottom Edge
                print("Bottom Edge")
                sublist = []
                add_connection(sublist, navmesh_nodes[(row-1) * width + column])
                add_connection(sublist, navmesh_nodes[(row-1) * width + (column+1)])
                add_connection(sublist, navmesh_nodes[row * width + (column+1)])
                add_connection(sublist, navmesh_nodes[(row+1) * width + (column+1)])
                add_connection(sublist, navmesh_nodes[(row+1) * width + column])
                nearbyList.append(sublist) 
            elif (column == width-1): #EDGE CASE: Top Row
                print("Top Row")
                sublist = []
                add_connection(sublist, navmesh_nodes[(row+1) * width + column])
                add_connection(sublist, navmesh_nodes[(row+1) * width + (column-1)])
                add_connection(sublist, navmesh_nodes[row * width + (column-1)])
                add_connection(sublist, navmesh_nodes[(row-1) * width + (column-1)])
                add_connection(sublist, navmesh_nodes[(row-1) * width + column])
                nearbyList.append(sublist)
            elif (row == height-1): #EDGE CASE: Right Edge
                print("Right edge")
                sublist = []
                add_connection(sublist, navmesh_nodes[row * width + (column+1)])
                add_connection(sublist, navmesh_nodes[(row-1) * width + (column+1)])
                add_connection(sublist, navmesh_nodes[(row-1) * width + column])
                add_connection(sublist, navmesh_nodes[(row-1) * width + (column-1)])
                add_connection(sublist, navmesh_nodes[row * width + (column-1)])
                nearbyList.append(sublist)
            else: #NORMAL CASE
                print("Normal case")
                sublist = []
                add_connection(sublist, navmesh_nodes[row * width + (column+1)])
                add_connection(sublist, navmesh_nodes[(row+1) * width + (column+1)])
                add_connection(sublist, navmesh_nodes[(row+1) * width + column])
                add_connection(sublist, navmesh_nodes[(row+1) * width + (column-1)])
                add_connection(sublist, navmesh_nodes[row * width + (column-1)])
                add_connection(sublist, navmesh_nodes[(row-1) * width + (column+1)])
                add_connection(sublist, navmesh_nodes[(row-1) * width + column])
                add_connection(sublist, navmesh_nodes[(row-1) * width + (column-1)])
                nearbyList.append(sublist)
            neighbour_list.append(nearbyList)
            print(nearbyList)
            index += 1