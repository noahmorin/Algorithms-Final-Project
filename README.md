Our Project is a program written in Python that simulates a network employing the
Routing Information Protocol (RIP), which is a distance-vector protocol that uses the
Bellman-Ford Algorithm to compute the best path to a destination network. Furthermore, the
program implements Kruskal’s minimum spanning tree algorithm to create a minimum spanning
tree in the network.

Our program begins by taking the input of a file named network.txt which contains the
raw data for the graph of the network, stored in a text format. This data is taken in through an in
line for loop that takes node names and their respective values and writes them into a two
dimensional array. By storing our graph in this data structure, we are able to efficiently store
edge information and quickly access it through for loop iterations.

From this point the user is presented with a number of optional actions. They can modify
the graph in a number of ways, such as changing an edge, removing an edge, or removing an
entire node. Should the user decide to update any of the graph’s information, the text file can be
overwritten to reflect the changes. From this same menu, the user can also choose to print the
graph, where it will display in a text table format, listing all the relevant edge node names and
values. There are a number of other options as well, such as the ability to view our academic
integrity statement, or write any changes made into the file for future use.

When the user decides to run the computational algorithms portion of the program, it will
begin by entering the BFPrep function, which prepares the graph data to be run through the
Bellman-Ford algorithm. It does so by passing the appropriate data into the necessary variables,
such as vertices and edges. From here it will pass the data into the Bellman-Ford function,
where we use the Bellman-Ford algorithm to calculate the shortest path to each destination
node in the network. For the case of this program, we selected Oshawa as the source node to
calculate the costs to each destination.

The user will also have the option to calculate the minimum spanning tree using
Kruskal’s MST algorithm, which is an algorithm that computes the minimum spanning tree on a
given graph including a list of edges and vertices. To begin the process, much like the
Bellman-Ford algorithm before it, certain values and variables must be prepared. To do this it
goes into the KruskalPrep function, where it assigns vertices and formats the data to be
processed. Once that is completed the data is passed into the Kruskal function, where it uses
the algorithm to find the minimum spanning tree for the given graph input into it. This results in
the lowest cost for travelling to every single node on the graph. In the context of a real world
network using Kruskal's algorithm with RIP, a higher bandwidth would be preferred. To reflect
this, the minimum spanning tree is reversed to reflect the preference towards higher bandwidth
links (higher bandwidth, lower cost).
