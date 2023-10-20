from island import Island
from data_structures.bst import BinarySearchTree, BSTInOrderIterator

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117

    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        both best and worst case of O(1)
        """
        self.islands = islands
        self.crew = crew


    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        attack_list = []

        bst = BinarySearchTree()

        for island in self.islands:
            # depending on the ratio of marines to money determine which islands to attack and add to the list
            # use of max to prevent failure if money = 0
            ratio = island.marines / max(1, island.money)
            bst[ratio] = island

        in_nodes = [node.item for node in BSTInOrderIterator(bst.root)]

        remaining_crew = self.crew

        for island in in_nodes:
            if island.marines > remaining_crew:
                crew_sent = remaining_crew
            else:
                crew_sent = island.marines

            attack_list.append((island, crew_sent))
            remaining_crew -= crew_sent

        return attack_list

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
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

