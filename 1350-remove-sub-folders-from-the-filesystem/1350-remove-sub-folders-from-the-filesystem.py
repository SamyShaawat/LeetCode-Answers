class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        n = len(folder)
        # print(folder)
        result = [folder[0]]
        for i in range(1, n):
            last_folder = result[-1]
            last_folder += "/"

            if not folder[i].startswith(last_folder):
                result.append(folder[i])
        return result
            

        