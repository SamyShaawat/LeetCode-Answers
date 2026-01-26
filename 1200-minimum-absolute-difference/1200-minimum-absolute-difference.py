class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        result = []

        i, j = 0, 1
        n = len(arr)
        mindiff = arr[j] - arr[i]

        result.append([arr[i], arr[j]])
        i += 1
        j += 1

        while j < n:
            diff = arr[j] - arr[i]

            if diff < mindiff:
                mindiff = diff
                result.clear()
                result.append([arr[i], arr[j]])
            elif diff == mindiff:
                result.append([arr[i], arr[j]])

            i += 1
            j += 1

        return result