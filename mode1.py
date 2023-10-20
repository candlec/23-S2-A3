from island import Island
from data_structures.bst import BinarySearchTree, BSTInOrderIterator

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    This solution makes use of a binary search tree select_islands, with the nodes ordered
    via InOrder depending on the island’s ratio of marines to money, to help determine
    which island is the least profitable. It then traverses through the bst comparing the
    number of island marines to the remaining available crew appending both the given
    island and sent crew amount to a list which is returned. For example, using the
    islands: (name='A', money=400, marines=100), (name='B', money=300, marines=150),
    (name='C', money=100, marines=5), (name='D', money=350, marines=90),
    (name='E', money=300, marines=100), the ratios (keys) would respectably be
    0.25, 0.5, 0.05, 0.257, 0.333. Using InOrder the islands would be ordered as
    C, A, D, E, B and therefore the crew would be allocated in such a way.
    The solution has a complexity of O(n), BSTInOrderOperator has a complexity of O(n) where
    n is the size of the bst, select_islands additionally has two separate O(n) functions,
    however none of these are nested so it would have a complexity of O(n + n + n) which
    would just be O(n).
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        time complexity of O(1) for both best and worst case
        """
        self.islands = islands
        self.crew = crew


    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        time complexity of O(n) for both best and worst case
        """
        # list that will contian the islands to attack with the number of crew sent
        attack_list = []
        # create a bst
        bst = BinarySearchTree()

        # depending on the ratio of marines to money determine which islands to attack and add to the list
        for island in self.islands:
            # use of max to prevent failure if money = 0
            ratio = island.marines / max(1, island.money)
            # key is ratio and node is the island
            bst[ratio] = island

        in_nodes = [node.item for node in BSTInOrderIterator(bst.root)]
        remaining_crew = self.crew

        for island in in_nodes:
            if island.marines > remaining_crew:
                crew_sent = remaining_crew
            else:
                # sends an equal amount of crew to marines
                crew_sent = island.marines

            attack_list.append((island, crew_sent))
            # subtracts the crew that will perish from the total crew
            remaining_crew -= crew_sent

        return attack_list

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        time complexity of O(n x c) for both best and worst case
        """
        saved_crew_size = self.crew
        results = []

        for crew_size in crew_numbers:
            # run through self.select_islands with a given crew number
            self.crew = crew_size
            islands = self.select_islands()
            total = 0

            for node in islands:
                island = node[0]
                crew_to_send = node[1]
                total += (island.money * crew_to_send) / max(1, island.marines)

            results.append(total)

        self.crew = saved_crew_size

        return results

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        time complexity of O(1) for both best and worst case
        """
        island.money = new_money
        island.marines = new_marines

