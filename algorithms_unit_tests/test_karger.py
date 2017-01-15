import unittest

from algorithms.karger import contract_nodes, count_edges, make_edges, make_nodes, min_cut


class Test_MinCut(unittest.TestCase):
    def test_basic_min_cut(self):
        test_matrix = [[1, 2, 3], [2, 1, 3, 4], [3, 1, 2, 4], [4, 2, 3]]
        expected_cut = 2

        actual_cut = min_cut(test_matrix)

        self.assertEqual(expected_cut, actual_cut)


class Test_MakeNodes(unittest.TestCase):
    def test_make_nodes(self):
        test_matrix = [[1, 2, 3], [2, 1, 3, 4], [3, 1, 2, 4], [4, 2, 3]]
        expected_nodes = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}

        actual_nodes = make_nodes(test_matrix)

        self.assertEqual(expected_nodes, actual_nodes)


class Test_MakeEdges(unittest.TestCase):
    def test_make_edges(self):
        test_nodes = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
        expected_edges = [(1, 2), (1, 3), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 2),
                          (4, 3)]

        actual_edges = make_edges(test_nodes)

        self.assertEqual(expected_edges, actual_edges)

    def test_parallel_edges(self):
        test_nodes = {1: [2, 2, 4], 2: [1, 1, 3, 4], 4: [2, 3]}
        expected_edges = [(1, 2), (1, 2), (1, 4), (2, 1), (2, 1), (2, 3), (2, 4), (4, 2), (4, 3)]

        actual_edges = make_edges(test_nodes)

        self.assertEqual(expected_edges, actual_edges)


class Test_ContractNodes(unittest.TestCase):
    def setUp(self):
        self.nodes = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}

    def test_nodes_are_contracted(self):
        contract_nodes(self.nodes, (1, 3))

        self.assertEqual(3, len(self.nodes))

    def test_contract_nodes_1_2(self):
        expected_nodes = {1: [3, 3, 4], 3: [1, 1, 4], 4: [1, 3]}

        actual_nodes = contract_nodes(self.nodes, (1, 2))

        self.assertEqual(expected_nodes, actual_nodes)

    def test_contract_nodes_1_3(self):
        expected_nodes = {1: [2, 2, 4], 2: [1, 1, 4], 4: [1, 2]}

        actual_nodes = contract_nodes(self.nodes, (1, 3))

        self.assertEqual(expected_nodes, actual_nodes)

    def test_contract_nodes_2_4(self):
        expected_nodes = {1: [2, 3], 2: [1, 3, 3], 3: [1, 2, 2]}

        actual_nodes = contract_nodes(self.nodes, (2, 4))

        self.assertEqual(expected_nodes, actual_nodes)

    def test_contract_nodes_double_self_loops(self):
        test_nodes = {2: [3, 3, 4], 3: [2, 2, 4], 4: [2, 3]}

        expected_nodes = {3: [4, 4], 4: [3, 3]}

        actual_nodes = contract_nodes(test_nodes, (3, 2))

        self.assertEqual(expected_nodes, actual_nodes)

    def test_contract_nodes_satellite_after_middle_merge(self):
        test_nodes = {1: [3, 3], 3: [1, 1, 4, 4], 4: [3, 3]}

        expected_nodes = {1: [4, 4], 4: [1, 1]}

        actual_nodes = contract_nodes(test_nodes, (4, 3))

        self.assertEqual(expected_nodes, actual_nodes)


class Test_CountEdges(unittest.TestCase):
    def test_count_edges(self):
        test_nodes = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2]}

        expected_count = 5

        actual_count = count_edges(test_nodes)

        self.assertEqual(expected_count, actual_count)

    def test_parallel_edges(self):
        test_nodes = {1: [2, 2, 4], 2: [1, 4], 4: [2]}

        expected_count = 4

        actual_count = count_edges(test_nodes)

        self.assertEqual(expected_count, actual_count)
