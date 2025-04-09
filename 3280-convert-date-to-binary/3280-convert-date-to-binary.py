class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.split("-")
        print(date)
        for i in range(len(date)):
            date[i] = bin(int(date[i]))[2:]
            # print(date[i])
        # print(date)

        return "-".join(date)
        