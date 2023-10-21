import copy
from island import Island
from data_structures.heap import MaxHeap


class IslandNode:
    def __init__(self, island: Island, crew: int):
        crew_used = min(crew, island.marines)
        self.island = island
        earned_money = crew_used * island.money / max(1, island.marines)
        self.score = (2 * (crew - crew_used)) + earned_money

    def __ge__(self, other):
        return self.score >= other.score

    def __gt__(self, other):
        return self.score > other.score

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    The solution uses a max heap to figure out the optimal islands to choose
    based on the score given in the created IslandNode class. The island
    that's considered the best is then designated crew members to attack
    that island. The values of islands are changed each day depending on
    whether they've been attacked. All the functions used from the max heap
    class have a complexity of O(1) best and worst case, and the function
    simulate_day has a complexity of O(n), therefore the solution has an
    overall time complexity of O(n).
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Student-TODO: Best/Worst Case
        time complexity of O(1) both best and worst case
        """
        self.islands = []
        self.n_pirates = n_pirates

    def add_islands(self, islands: list[Island]):
        """
        Student-TODO: Best/Worst Case
        complexity of O(1) * compf for deepcopy
        """
        self.islands.extend(copy.deepcopy(islands))

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Student-TODO: Best/Worst Case
        time complexity of O(n), as no nested loops however could
        vary depending on the complexity of the IslandNode class
        functions.
        """
        islands = MaxHeap(len(self.islands))
        results = []

        for island in self.islands:
            islands.add(IslandNode(island, crew))

        for pirate in range(0, self.n_pirates):
            score = 0
            crew_sent = 0
            best_island = None

            if len(islands):
                """
                figure out the score of each island to determine the optimal
                island to plunder and have the values change with each day
                """
                best_island_node = islands.get_max()
                best_island = best_island_node.island

                crew_sent = min(best_island.marines, crew)
                score = best_island_node.score

                # If an island has remaining money, put it back on the Heap
                best_island.money -= crew_sent * best_island.money / best_island.marines
                best_island.marines = max(0, best_island.marines - crew_sent)

                if best_island.money > 0:
                    islands.add(IslandNode(best_island, crew))

            # if more beneficial to skip an island than plundering it, skip it
            score_if_skipping = 2 * crew

            if score_if_skipping > score:
                crew_sent = 0

            results.append((best_island, crew_sent))

        return results

