from typing import List


class Solution:
    def djikstra_algo(self, input, node_count, source, destination):
        # build the adjancency matrix
        node_mapper = dict()
        reverse_mapper = dict(

        )
        result_map = dict()
        adj_matrix = [[None for x in range(0, node_count)] for y in range(0, node_count)]
        for i in range(0, node_count):
            node_mapper.update(**{
                chr(65 + i): i
            })
            reverse_mapper.update(**{
                str(i): chr(65 + i)
            })
            result_map.update(
                **{
                    chr(65 + i): {
                        'cost': None,
                        'previous': None
                    }
                }
            )
        for i in input:
            source, destination, weight = i
            adj_matrix[node_mapper[source]][node_mapper[destination]] = weight
            adj_matrix[node_mapper[destination]][node_mapper[source]] = weight

        visited_nodes = [

        ]
        current_node = source
        while visited_nodes!=node_count:
            # find the adjacent nodes
            self.visit_node(adj_matrix, current_node, node_mapper, result_map, reverse_mapper, visited_nodes)


    def visit_node(self, adj_matrix, current_node, node_mapper, result_map, reverse_mapper, visited_nodes):
        current_node_pool = adj_matrix[node_mapper[current_node]]

        if current_node in result_map and result_map[current_node].get('cost') is None:
            result_map[current_node]['cost'] = 0

        for index, i in enumerate(current_node_pool):
            if i is None:
                continue
            # calculate node distance and update it accordingly
            current_cost = result_map[current_node]['cost'] + i

            if reverse_mapper[str(index)].get('cost') is None or reverse_mapper[str(index)].get('cost') > current_cost:
                reverse_mapper[str(index)]['cost'] = current_cost
                reverse_mapper[str(index)]['previous'] = current_node

            self.visit_node(
                adj_matrix, reverse_mapper[str(index)], node_mapper, result_map, reverse_mapper, visited_nodes
            )

            visited_nodes.append(reverse_mapper[str(index)])
        visited_nodes.append(current_node)




test_cases = [
    [
        ['E', 'C', 5],
        ['B', 'C', 5],
        ['E', 'B', 2],
        ['D', 'E', 5],
        ['D', 'B', 2],
        ['A', 'B', 6],
        ['A', 'D', 1],
    ]
]

for t in test_cases:
    s = Solution().djikstra_algo(t, 5, 'A', 'C')
    print(t, s)
