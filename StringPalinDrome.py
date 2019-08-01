'''Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input:s1 = "abo" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").


Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False


Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''
from collections import defaultdict

def two_map_solution(s1, s2):
	def map_to_dictionary(s):
		my_dict = {}
		for char in 'qwertyuiopasdfghjklzxcvbnm':
			my_dict[char] = 0
		for char in s:
			my_dict[char] += 1
		return my_dict
	if len(s2) < len(s1):
		return False

	stringMap1 = map_to_dictionary(s1)
	stringMap2 = map_to_dictionary(s2[0:len(s1)])

	for i in range(len(s2) - len(s1)):
		if stringMap1 == stringMap2:
			return True
		else:
			stringMap2[s2[i]] -= 1
			stringMap2[s2[i+len(s1)]] += 1

	return False

print(two_map_solution('ab', 'aboo')) # True
print(two_map_solution('abo', 'eidbaooo')) # True
print(two_map_solution('ab', 'eidboaoo')) # False

print(test)
'''
Big O Analysis:
	if s1 is size N and s2 is size M, mapping the strings is N + N = 2N
	the for loop is (M - N), thus bigO is M+N
'''

'''Also possible to do with just one map. See default dictionary count'''




