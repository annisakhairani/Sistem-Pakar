# Sistem-Pakar
Annisa Khairani Febrianti
# NPM : 1184071
# Kelas : D4 TI 3C
##% BFS dan DFS
# Persoalan yang akan kita selesaikan dengan metode BFS dan DFS yaitu
# Bagaimana antrian tercepat dari beberapa negara yaitu 'Sao Paolo', 'Mountain View', 
#'San Francisco', 'London', 'Shanghai', 'Berlin'. Maka disini kita akan
# mencoba metode BFS dan DFS untuk melihat antrian mana yang tercepat dari beberapa negara.

# mengimport sebagian data antrian
import queue

class Node(object):
#kerangka untuk membentuk suatu objek pada class node
    def __init__(self, value):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama
#kali dijalankan.(sebuah variabel yang menyatakan kelas itu sendiri dan berisi value)
        self.value = value
        self.edges = []
        self.visited = False

class Edge(object):
#kerangka untuk membentuk suatu objek pada class edge
    def __init__(self, value, node_from, node_to):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama
#kali dijalankan (sebuah variabel yang menyatakan kelas itu sendiri berisi value dan node from dan to)
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

# You only need to change code with docs strings that have TODO.
# Specifically: Graph.dfs_helper and Graph.bfs
# New methods have been added to associate node numbers with names
# Specifically: Graph.set_node_names
# and the methods ending in "_names" which will print names instead
# of node numbers

class Graph(object):
#kerangka untuk membentuk suatu objek pada class Graph
#Graph merupakan salah satu metode pemetaan data dengan memberikan informasi pada 
#kumpulan titik (node) yang dihubungkan dengan segmen garis.
    def __init__(self, nodes=None, edges=None):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama
#kali dijalankan dan sebuah variabel yang menyatakan kelas itu sendiri
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = []
        self._node_map = {}

    def set_node_names(self, names):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama
#kali dijalankan pada class set_node_name dan menyatakan kelas itu sendiri pada names
        """The Nth name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)
#sebuah variabel yang menyatakan kelas itu sendiri pada class node_names.
    def insert_node(self, new_node_val):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama
#kali dijalankan pada class insert_node (sebuah variabel yang menyatakan kelas itu sendiri berisi new_node_val)
        "Insert a new node with value new_node_val"
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama
#kali dijalankan pada class insert_edge (sebuah variabel yang menyatakan kelas itu sendiri)
        "Insert a new edge, creating new nodes if necessary"
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
#perulangan for pada class node pada sebuah variabel yang menyatakan kelas itu sendiri
            if node.value in nodes:
# if digunakan untuk mengeksekusi kode jika kondisi bernilai benar True atau false 
                nodes[node.value] = node
                if all(nodes.values()):
                    break
# break digunakan untuk menghentikan jalannya proses iterasi pada statemen for atau while.
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama
#kali dijalankan pada class get_edge_list (sebuah variabel yang menyatakan kelas itu sendiri)
        """Return a list of triples that looks like this:
        (Edge Value, From Node, To Node)"""
        return [(e.value, e.node_from.value, e.node_to.value)
                for e in self.edges]

    def get_edge_list_names(self):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama
#kali dijalankan pada class get_edge_list_names (sebuah variabel yang menyatakan kelas itu sendiri)
        """Return a list of triples that looks like this:
        (Edge Value, From Node Name, To Node Name)"""
        return [(edge.value,
                 self.node_names[edge.node_from.value],
                 self.node_names[edge.node_to.value])
                for edge in self.edges]

    def get_adjacency_list(self):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama
#kali dijalankan pada class get_adjacency_list (sebuah variabel yang menyatakan kelas itu sendiri)
        """Return a list of lists.
        The indecies of the outer list represent "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        max_index = self.find_max_index()
        adjacency_list = [[] for _ in range(max_index)]
        for edg in self.edges:
            from_value, to_value = edg.node_from.value, edg.node_to.value
            adjacency_list[from_value].append((to_value, edg.value))
        return [a or None for a in adjacency_list] # replace []'s with None

    def get_adjacency_list_names(self):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama
#kali dijalankan pada class get_adjacency_list_names (sebuah variabel yang menyatakan kelas itu sendiri)
        """Each section in the list will store a list
        of tuples that looks like this:
        (To Node Name, Edge Value).
        Node names should come from the names set
        with set_node_names."""
        adjacency_list = self.get_adjacency_list()
        def convert_to_names(pair, graph=self):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama kali dijalankan 
#pada class convert_to_names
            node_number, value = pair
            return (graph.node_names[node_number], value)
        def map_conversion(adjacency_list_for_node):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama kali dijalankan 
#pada class map_conversion
            if adjacency_list_for_node is None:
                return None
            return map(convert_to_names, adjacency_list_for_node)
        return [map_conversion(adjacency_list_for_node)
                for adjacency_list_for_node in adjacency_list]

    def get_adjacency_matrix(self):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama kali dijalankan 
#pada class get_adjacency_matrix(sebuah variabel yang menyatakan kelas itu sendiri).
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        max_index = self.find_max_index()
        adjacency_matrix = [[0] * (max_index) for _ in range(max_index)]
        for edg in self.edges:
            from_index, to_index = edg.node_from.value, edg.node_to.value
            adjacency_matrix[from_index][to_index] = edg.value
        return adjacency_matrix

    def find_max_index(self):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama kali dijalankan 
#pada class get_max_index(sebuah variabel yang menyatakan kelas itu sendiri).
        """Return the highest found node number
        Or the length of the node names if set with set_node_names()."""
        if len(self.node_names) > 0:
            return len(self.node_names)
        max_index = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value
        return max_index

    def find_node(self, node_number):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama kali dijalankan 
#pada class find_node(sebuah variabel yang menyatakan kelas itu sendiri pada class node_number).
        "Return the node with value node_number or None"
        return self._node_map.get(node_number)

    def _clear_visited(self):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama kali dijalankan 
#pada class clear_visited(sebuah variabel yang menyatakan kelas itu sendiri).
        for node in self.nodes:
            node.visited = False
#visited digunakan untuk mengambil / mengeset data dari negara yang dikunjungi

    def dfs_helper(self, start_node):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama kali dijalankan 
#pada class dfs_helper(sebuah variabel yang menyatakan kelas itu sendiri pada class start_node).
        """TODO: Write the helper function for a recursive implementation
        of Depth First Search iterating through a node's edges. The
        output should be a list of numbers corresponding to the
        values of the traversed nodes.
        ARGUMENTS: start_node is the starting Node
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the traversed node values (integers).
        """
        ret_list = [start_node.value]
        start_node.visited = True
        for edge in start_node.edges:
            if edge.node_to.visited == False:
                ret_list += self.dfs_helper(edge.node_to)
        return ret_list

#DFS
    def dfs(self, start_node_num):
    #keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama kali dijalankan 
#pada class dfs(sebuah variabel yang menyatakan kelas itu sendiri pada class start_node_num).
#Algoritma DFS (Depth First Search) adalah salah satu algoritma yang digunakan untuk pencarian jalur.
        """Outputs a list of numbers corresponding to the traversed nodes
        in a Depth First Search.
        ARGUMENTS: start_node_num is the starting node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        self._clear_visited()
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node)

    def dfs_names(self, start_node_num):
 #keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama kali dijalankan 
#pada class dfs_names(sebuah variabel yang menyatakan kelas itu sendiri pada class start_node_num).
        """Return the results of dfs with numbers converted to names."""
        return [self.node_names[num] for num in self.dfs(start_node_num)]

#BFS
    def bfs(self, start_node_num):
 #keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama kali dijalankan 
#pada class bfs(sebuah variabel yang menyatakan kelas itu sendiri pada class start_node_num).
#bfs atau Breadth-first search adalah algoritma yang melakukan pencarian secara melebar yang mengunjungi simpul 
#secara preorder yaitu mengunjungi suatu simpul kemudian mengunjungi semua simpul yang bertetangga dengan simpul 
#tersebut terlebih dahulu.
        """ Create an iterative implementation of Breadth First Search
        iterating through a node's edges. The output should be a list of
        numbers corresponding to the traversed nodes.
        ARGUMENTS: start_node_num is the node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        node = self.find_node(start_node_num)
        self._clear_visited()
        q = queue.queue()
        ret_list = [node.value]
        node.visited = True
        while len(ret_list) < len(self.nodes):
#while digunakan untuk perulangan pada len.
            for edge in node.edges:
                if edge.node_to.visited == False:
                    edge.node_to.visited = True
                    ret_list.append(edge.node_to.value)
                    q.put(edge.node_to)
            node = q.get()

        return ret_list

    def bfs_names(self, start_node_num):
#keyword yang digunakan untuk menyatakan suatu fungsi pada program yang pertama kali dijalankan 
#pada class bfs_names(sebuah variabel yang menyatakan kelas itu sendiri pada class start_node_num).
        """Return the results of bfs with numbers converted to names."""
        return [self.node_names[num] for num in self.bfs(start_node_num)]

graph = Graph()
#class Graph digunakan untuk merepresentasikan objek-objek diskrit dan hubungan antara objek-objek tersebut. 

graph.set_node_names(('Mountain View',   # 0
                      'San Francisco',   # 1
                      'London',          # 2
                      'Shanghai',        # 3
                      'Berlin',          # 4
                      'Sao Paolo',       # 5
                      'Bangalore'))      # 6
#nama-nama negara yang melakukan antrian.
graph.insert_edge(51, 0, 1)     # MV <-> SF
graph.insert_edge(51, 1, 0)     # SF <-> MV
graph.insert_edge(9950, 0, 3)   # MV <-> Shanghai
graph.insert_edge(9950, 3, 0)   # Shanghai <-> MV
graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
graph.insert_edge(9900, 1, 3)   # SF <-> Shanghai
graph.insert_edge(9900, 3, 1)   # Shanghai <-> SF
graph.insert_edge(9130, 1, 4)   # SF <-> Berlin
graph.insert_edge(9130, 4, 1)   # Berlin <-> SF
graph.insert_edge(9217, 2, 3)   # London <-> Shanghai
graph.insert_edge(9217, 3, 2)   # Shanghai <-> London
graph.insert_edge(932, 2, 4)    # London <-> Berlin
graph.insert_edge(932, 4, 2)    # Berlin <-> London
graph.insert_edge(9471, 2, 5)   # London <-> Sao Paolo
graph.insert_edge(9471, 5, 2)   # Sao Paolo <-> London
# (6) 'Bangalore' is intentionally disconnected (no edges)
# for this problem and should produce None in the
# Adjacency List, etc.

import pprint
#import digunakan untuk memanggil file lain di dalam satu module yang berbeda.
pp = pprint.PrettyPrinter(indent=2)

print ("Edge List")
#print digunakan untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks pada 
#Class "Edge List".
pp.pprint(graph.get_edge_list_names())

print ("\nAdjacency List")
#print digunakan untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks pada 
#Class "\nAdjacency List".
pp.pprint(graph.get_adjacency_list_names())

print ("\nAdjacency Matrix")
#print digunakan untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks pada 
#Class "\nAdjacency Matrix".
pp.pprint(graph.get_adjacency_matrix())

print ("\nDepth First Search")
#print digunakan untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks pada 
#Class "\nDepth First Search".
pp.pprint(graph.dfs_names(2))

# Should print:
# Depth First Search
# ['London', 'Shanghai', 'Mountain View', 'San Francisco', 'Berlin', 'Sao Paolo']

print ("\nBreadth First Search")
#print digunakan untuk mencetak atau menampilkan objek ke perangkat keluaran (layar) atau ke file teks pada "\nBreadth First Search".
pp.pprint(graph.bfs_names(2))
# test error reporting
# pp.pprint(['Sao Paolo', 'Mountain View', 'San Francisco', 'London', 'Shanghai', 'Berlin'])

# Should print:
# Breadth First Search
# ['London', 'Shanghai', 'Berlin', 'Sao Paolo', 'Mountain View', 'San Francisco']
