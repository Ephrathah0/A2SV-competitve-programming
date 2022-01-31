class Solution:
    def sortSentence(self, s: str) -> str:
        answer = []
        x = s.split(" ")
        x.sort(key = lambda i : int(i[-1]))
        for i in x:
            if i[-1].isdigit():
                answer.append(i[:len(i)-1])
        return " ".join(answer)
