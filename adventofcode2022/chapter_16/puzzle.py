
import sys


'''


Get the "map" of all routes.

Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II

'''


def Node(node_index, sub_indexes):

	def __init__(self,node_index,sub_indexes):

		self.node_index = node_index
		self.sub_indexes = sub_indexes

		self.flow_rate = flow_rates[node_index]



def Tree(node_stuff):

	def __init__(self, node_stuff):

		self.node_stuff = node_stuff
		self.construct_tree()
		self.nodes = {}

	def construct_tree(self):

		for node_thing in node_stuff:

			node_index = node_thing[0]

			sub_indexes = node_thing[1]

			index_int = indexes[node_index]

			self.nodes[index_int] = Node(node_index)




connection_shit = []

flow_rates = {}

indexes = {}


def parse_input():

	stuff = sys.stdin.buffer.read().decode('ascii')
	lines = stuff.split("\n")

	for i, line in enumerate(lines):

		tokens = line.split(" ")

		valve_name = tokens[1]

		flow_rate_token = tokens[4]

		flow_rate = int(flow_rate_token[5:-1])

		flow_rates[valve_name] = flow_rate

		indexes[valve_name] = i

		connection_stuff = ''.join(tokens[9:])

		things = connection_stuff.split(", ")

		connection_shit.append(things)

	print("connection_shit: "+str(connection_shit))
	print("flow_rates: "+str(flow_rates))
	print("indexes: "+str(indexes))



def solve_puzzle():
	parse_input()




if __name__=="__main__":

	print("Result of puzzle: "+str(solve_puzzle()))
