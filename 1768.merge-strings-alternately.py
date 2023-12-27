class Solution:
    def mergeAlternately(self, word1: str, word2: str):
        list = []
        index = 1
        merge_string = ""
        for str1 in word1:
            list.append(str1)
        for str2 in word2:
            list.insert(index,str2)
            index +=2
        for final_str in list:
            merge_string += final_str
        return merge_string
