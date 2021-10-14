# Ryan Manzie (100743508)
# Blake Whiting (100743587)
# Noah Morin (100740090)
# Final Project for INFR 2820U
# April 9, 2021

import re
import os
# import various libraries needed for the program

def clearScreen():  # clear screen function, clears the console window dependant on user's OS
    if os.name == 'posix': # MacOS and Linux
        os.system('clear')
    else:
        os.system('cls') # Windows

def systemPause():
    try:
        os.system('pause') # Windows
    except:
        os.system('read -p "Press ANY key to return to menu"') # Linux

# Lines 24-69 include various headers to display menus and other such things

def printMainHeader():
    clearScreen()
    print("=======================================================================\n")
    print(" . . . . . . . . . A L G O R I T H M S   F I N A L . . . . . . . . . . \n")
    print(" . . . . Group Members: Ryan Manzie, Noah Morin, Blake Whiting . . . . \n")
    print(" . . . . . . Student ID's: 100743508, 100740090, 100743587 . . . . . . \n")
    print("=======================================================================\n\n")

def printIntegrityHeader():
    clearScreen()
    print("=======================================================================\n")
    print(" . . . . . . . . . . . . .  A C A D E M I C  . . . . . . . . . . . . . \n")
    print(" . . . . . . . . . . . . . I N T E G R I T Y . . . . . . . . . . . . . \n")
    print(" . . . . . . . . . . . . . S T A T E M E N T . . . . . . . . . . . . . \n")
    print("=======================================================================\n\n")

def academicIntegrity(): # Displays a page with our Academic Integrity Statement
    printIntegrityHeader()
    print("As  a  member  of  the  Ontario  Tech  University  community,  I  share  our  community’s commitment  to  the  highest  standards  of  academic  integrity  and  excellence  in  all dimensions of our work. \n\nI therefore promise that I will not lie, cheat, or use any unauthorized aids or assistance to complete any of my essays, assignments, and exams. I further promise that I will not offer any  unauthorized  assistance  to  any  of  my  fellow  students,  and  I  promise  that  I  will  not ask  any  of  my  fellow  students  for  unauthorized  assistance.  \n\nI  promise  that  the  work  I submit  is  my  own  and  that  where  I  have  drawn  on  the  work  of  others,  I  have  included proper attribution for my sources.\n")
    print("Signed, \nRyan Manzie, Noah Morin, Blake Whiting\t ---\tApril 9th, 2021\n")
    systemPause()

def printKruskalHeader():
    clearScreen()
    print("=======================================================================\n")
    print(" . . . . . . K R U S K A L ' S   A L G O R I T H M   M S T . . . . . . \n")
    print("=======================================================================\n")
    print("Input a minimum bandwidth cap (ignore links with lower bandwidth)")

def printBFHeader():
    clearScreen()
    print("=======================================================================\n")
    print(" . . B E L L M A N - F O R D  S H O R T E S T  P A T H  F I R S T  . . \n")
    print("=======================================================================\n")

def printUpdateHeader():
    clearScreen()
    print("=======================================================================\n")
    print(" . . . . . . . . . . U P D A T E  T H E  G R A P H . . . . . . . . . . \n")
    print("=======================================================================\n")

def printDisplayHeader():
    clearScreen()
    print("=======================================================================\n")
    print(" . . . . . . . . . D I S P L A Y  T H E  G R A P H . . . . . . . . . . \n")
    print("=======================================================================\n")

def writeToFile(graph):  # writeToFile function, updates graph information to the network.txt file
    try:
        with open("network.txt", 'w') as file:
            for edge in graph:
                file.write(edge[0] + " " + edge[1] + " " + str(edge[2]) + " " + str(edge[3]) + "\n")
            file.close()
        # opens a file writer to "network.txt" file, iterates through the graph 2D Array and writes the information formatted to network.txt
        print("\nFile Written Successfully")
        systemPause()
    except:
        print("\nError writing file")
        systemPause()

# UPDATE FUNCTIONS, changeEdge, removeEdge, removeNode =========================

def update(graph):  # update function, prints the menu and accepts inputs for the different update features
    while True:
        printUpdateHeader()
        print("[1] - Change the Metric and Bandwidth of an edge\n[2] - Remove an edge\n[3] - Remove a node\n[4] - Return to main menu")
        selection = input()
        # accepts the users input, calls the respective function based on the user's choice
        if(selection == '1'):
            graph = ChangeEdge(graph)
        elif(selection == '2'):
            graph = RemoveEdge(graph)
        elif(selection == '3'):
            graph = RemoveNode(graph)
        elif(selection == '4'):
            return graph
        else:
            print("Unexpected input. Please enter a proper menu item.")

def ChangeEdge(graph):  # ChangeEdge function, allows the user to change metric and bandwidth values on an edge
    print("\nWhich Edge do you want to change the values for? (i.e 'Oshawa-Ottawa')")
    edgeStr = input()
    edgeList = edgeStr.split("-")
    errorCheck = False
    # Accepts an input from the user, splits the string by a "-" and places both items into a list
    if len(edgeList) == 2:
        for edge in graph:
            if edge[0] == edgeList[0]:
                if edge[1] == edgeList[1]:
                    print("\nWhat do you want to change the metric value to?")
                    # if the two edges the user input are in the graph, ask the user to input a metric
                    try: # try to convert the user's input to a string, if it fails, execute except statement
                        changeMetric = input()
                        edge[2] = int(changeMetric)
                    except:
                        errorCheck = True
                        print("Metric not accepted")
                        systemPause()
                        return
                        # if the try statement fails, set error check to true, print error message, return to menu

                    print("\nWhat do you want to change the bandwidth value to?")
                    try: # try to convert the user's input to a string, if it fails, execute except statement
                        changeBandW = input()
                        edge[3] = int(changeBandW)
                    except:
                        print("Bandwidth not accepted")
                        errorCheck = True
                        systemPause()
                        return
                        # if the try statement fails, set error check to true, print error message, return to menu

                    if errorCheck != True:
                        print("\nValues have been updated")
                        systemPause()
                        return graph
                        # if no errors have been found, print a success message and return the graph

        print("Edge not found")
        systemPause()
        return graph
        # if the code does not execute properly, print error message, return graph
    else:
        print("Please input a proper Edge")
        systemPause()
        return graph
        # if the user did not input a correct edge, print error message, return graph
def RemoveEdge(graph):  # removeedge function, allows the user to remove an edge from the graph
    print("\nWhich Edge do you want to remove from the graph? (i.e 'Oshawa-Ottawa')")
    edgeStr = input()
    edgeList = edgeStr.split("-")
    # Accepts an input from the user, splits the string by a "-" and places both items into a list

    if len(edgeList) == 2:
        for edge in graph:
            if edge[0] == edgeList[0]:
                if edge[1] == edgeList[1]:
                    graph.pop(graph.index(edge))
                    print("\nEdge", edgeStr, "was removed from the graph\n")
                    systemPause()
                    return graph
                    # if the user enters an edge which is found in the graph, pop that edge from the graph and return the graph

        print("\nEdge not found")
        systemPause()
        return graph
        # if the code does not execute properly, print error message, return graph
    else:
        print("\nPlease input a proper Edge\n")
        systemPause()
        return graph
        # if the user did not input a correct edge, print error message, return graph
def RemoveNode(graph):
    vertices = createListVertices(graph)  # create a list, vertices, using the createListVertices function
    print("\nWhich node do you want to remove from the graph? (i.e 'Ottawa')")
    nodeRemove = input()
    # prompt the user to choce a node to remove from the graph
    try:
        graph = list(node for node in graph if nodeRemove not in node)
        # creates a new 2D list which follows these rules:
        # create a copy of the original 2D array that does not include any list which includes the provided node, nodeRemove
        print("\n" + nodeRemove, "was removed from the graph\n")
        systemPause()
        return graph
        # If code is executed correctly, print success message, return the new graph
    except:
        print("\nNode not found")
        systemPause()
        return graph
        # if try statement raises an error, return error message and return the original graph

def createListVertices(graph):  # createListVertices function, creates a list of unique vertices found in the 2D Array, graph
    setVert = set()  # create a new set, setVert
    for edge in graph:
        setVert.add(edge[0])
        setVert.add(edge[1])
    # for loop which iterates through each edge in the graph, adds edge[0] and edge[1] (both nodes) to the setVert
    # since a set consists of unique elements, only unique nodes will be stored in this set
    listVertices = list() # create an empty list, listVertices
    for x in setVert:
        listVertices.append(x)
    # iterate through the unique elements in setVert, append them to listVertices

    return listVertices

def printGraph(graph): # printGraph function... does what it says
    printDisplayHeader()
    for edge in graph:
        print("Edge:", edge[0], "-", edge[1], "\n\t\t\tMetric:", edge[2], "\n\t\t\tBandwidth:", edge[3], "\n")
    print("=======================================================================\n")
    systemPause()

def BFPrep(graph): # Prepares the data to be processed by the Bellman-Ford function
    listVertices = createListVertices(graph)
    listEdges = graph.copy()
    return listVertices, listEdges

def BellmanFord(vertices, edges): # Bellman-Ford, accepts a list of unique vertices and a list of edges as parameters
# used by the greatest routing protocol of alltime, RIP.
# Pseudocode for the BellmanFord algorithm referenced from Wikipedia, source included in the final document
    printBFHeader()
    distance = dict()
    predecessor = dict()
    source = "Oshawa"
    # create two empty dictionaries, distance and predecessor, set the source as Oshawa

    for v in vertices:
        distance[v] = 1000000
        predecessor[v] = None
    # create a key for each unique vertex in the network, assign it a value of 100000 (aritruary high number) and none

    distance[source] = 0 # set the distance to the source as 0

    for x in range(len(vertices) - 1):
        for edge in edges:
            # u = edge[0]
            # v = edge[1]
            # w = edge[2]
            # as per the pseudocode, these are the respective keys.
            if (distance[edge[0]] + edge[2]) < distance[edge[1]]: # if the distance currently assigned to nodeA, plus the metric, is less than the distance to nodeB
                distance[edge[1]] = distance[edge[0]] + edge[2] # set the distance to nodeB, as the distance to nodeA plus the metric
                predecessor[edge[1]] = edge[0] # set the predecessar to nodeB as nodeA

    print("From Oshawa, the shortest path to each destination is as follows:\n")
    print("Location  Distance  Predecessor:")
    for key in distance:
        print(key, distance[key], predecessor[key])
    print("\n")
    systemPause()
    # print the output of the Bellman-Ford algorithm formatted by iterating through the loop and printhing the key, and the key's value

def KruskalPrep(graphCopy):  # KruskalPrep function, accepts a copy of the graph as a paramter and prepares the data for the KruskalMST function
    setVert = set()
    for edge in graphCopy:
        setVert.add(edge[0])
        setVert.add(edge[1])
    listVertices = list()
    for x in setVert:
        listVertices.append(x)
    # Similar to BFPrep function, creates a list of unique vertices by appending all the nodes in graph to a set and appending the items in the set to a list

    return graphCopy, listVertices

def Kruskal(graphCopy, listVertices): # Kruskal's MST function, accepts graphCopy and listVertices as parameters. Computes the minimum spanning tree with a given list of edges (graph)
    printKruskalHeader()
    BandwidthCap = input()
    try: # prompt the user to provide a bandwidth, attempt to convert it to an integer
        BandwidthCap = int(BandwidthCap)
    except: # if the try statement fails, print an error message and return the user to the menu
        print("\nBandwidth not accepted")
        systemPause()
        return


    lowestEdgeBandwidth = 100000
    listVertices2 = listVertices
    KSPF2D = [[]]
    ASPathCheck = dict()
    treeCheck = False
    # variable decleration for variables used in the function
    for node in listVertices:
        ASPathCheck[node] = 1
    # "ASPathCheck", reference to BGP attribute, contains a dictionary of keys (names of unique vertices)and assigns them a value of 1, which represents if they have been visted before
    for x in range(len(graphCopy)): # for loop that iterates through the length of graphCopy
        try:  # large try statement which encompases the entirety of Kruskal's algorithm
            for edge in graphCopy: # for loop which iterates through the edge lists in graphCopy
                if edge[3] < lowestEdgeBandwidth: # if the bandwidth on the current edge is less than the lowestEdgeBandwidth (initialized as an arbitruarily large number)
                    if len(listVertices) == 0: # if the length of listVertices (unique nodes), is 0
                        print("\nThe minimum spanning tree (MST) for the graph is as follows:\n")
                        print("NodeA  NodeB  Bandwidth:")
                        # print a message that states the graph was completed
                        KSPF2D.pop(0) # pop the first element (holds blank space)
                        KSPF2D.reverse() # reverses the order of the MST, see document for explenation
                        for SPFedge in KSPF2D:
                            print(SPFedge[0], SPFedge[1], SPFedge[3])
                        print("\n")
                        systemPause()
                        return
                        # prints the order of the edges in the MST along with formatting
                    else: # if the length of listVertices (unique nodes), is not equal to 0
                        if edge[3] > BandwidthCap:  # if the bandwidth of the current edge is greater than the bandwidth cap (bandwidth provided by user)
                            if ASPathCheck[edge[0]] + ASPathCheck[edge[1]] > 0: # if both Node A and Node B on the current edge have not been visited (as per the ASPATHCHECK dictionary key value)
                                lowestEdgeBandwidth = edge[3] # the lowest edge bandwidth is replaced by the bandwidth of the current edge
                                lowestEdge = edge # the lowest edge is replaced by the current edge
            for item in lowestEdge:  # iterate through lowestEdge with item as the object reference
                if item in listVertices:  # if the item is in listVertices (unique nodes)
                    listVertices.remove(item)
                    ASPathCheck[item] -= 1
                    # remove the item from listVertices, set the value of the edge's ASPATHCHECK key to -= 1
                    # this code allows the program to know which vertices have already been visited
            del graphCopy[graphCopy.index(lowestEdge)] # delete the lowestEdge from the graph
            KSPF2D.append(lowestEdge) # append the lowestEdge to KSPF2D (Kruskal's SPF 2D Array)
            lowestEdgeBandwidth = 100000 # reset the lowest Bandwidth to 1000000
            # the entire algorithm than repeats itself until all the unique vertices have been visisted once, to which line 292 completes the Algorithm
            # in the case where not every node is reachable, an error is raised which calls the except Statement
            
        except:  # if the code in the try statement raises an error, exectute this code
            print("\nA minimum spanning tree (MST) was not completed for the graph.")
            print("Not enough edges to complete to graph, the incomplete graph is as follows:\n")
            print("NodeA  NodeB  Bandwidth:")
            # prints an error message which states that the algorithm was unable to complete
            KSPF2D.pop(0) # pop the first element (holds blank space)
            KSPF2D.reverse() # reverses the order of the MST, see document for explenation
            for SPFedge in KSPF2D:
                print(SPFedge[0], SPFedge[1], SPFedge[3])
            print("\n")
            systemPause()
            return
            # print the portion of the graph which was able to be calculate

def main():

    # graph = [["Ottawa", "Montreal", 199, 40], ["Ottawa", "Kingston", 196, 16], ["Ottawa", "Whitby", 9, 29], ["Oshawa", "Toronto", 61, 27], ["Oshawa", "Kingston", 205, 220], ["Oshawa", "Ottawa", 5, 114]]
    graph = [[]] # Empty 2D list that will have the data from the file writen into it
    print("Reading from network.txt") # Reads the text file
    try: # Error catch
        with open("network.txt", 'r') as networkFile: # Open network file to read
            graph = [i.split() for i in networkFile] # Insert each word from a line into the list

        for edge in graph: # Converts str to int
            edge[2], edge[3] = int(edge[2]), int(edge[3])
        print("File Read Successfully") # Confirm the file was read successfully
    except:
        print("Error reading file") # Error handler


    while True: # Loop until the user exits
        printMainHeader() # Print the main program banner
        # Menu Options displayed
        print("[1] - Update the graph\n[2] - Display the graph\n[3] - Display shortest path to all vertices, Bellman-Ford SPF\n[4] - Display the minimum spanning tree, Kruskal's Algorithm MST\n[5] - Save the graph to a text file\n[6] - Academic Integrity Statement \n[7] - Quit the program")
        selection = input()
        if(selection == '1'):
            graph = update(graph) # Pass the graph to the updateGraph function
        elif(selection == '2'):
            printGraph(graph) # Pass the graph to the printGrpah function
        elif(selection == '3'):
            vertices, edges = BFPrep(graph) # Pass the graph to the BFPrep function
            BellmanFord(vertices, edges) # Perform the Bellman-Ford algorithm
        elif(selection == '4'):
            graphCopy = graph.copy() # Create a copy of the original grpah
            graphCopy, listVertices = KruskalPrep(graphCopy) # Prepare the graph for Kruskal's MST Algorithm
            Kruskal(graphCopy, listVertices) # Perform Kruskal's MST Algorithm
        elif(selection == '5'):
            writeToFile(graph) # Save the edited graph to the file. This will overwrite the original file
        elif(selection == '6'):
            academicIntegrity() # Print the academic Integrity statement
        elif(selection == '7'):
            exit() # Exit the program
        else: # Error Handler
            print("You didn't follow the instructions and there was an error.")

main()
