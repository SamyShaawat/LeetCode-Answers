class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(heights, names))
        people.sort(reverse=True, key=lambda x: x[0])
        sorted_names = [name for height, name in people]
        return sorted_names


        