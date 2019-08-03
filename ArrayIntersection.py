#Given two arrays a1 and a2, return intersecting elements. Treat intersected elements as used
a1 = [1, 3, 3, 5]
a2 = [2, 3, 3, 3, 8]
# def array_intersect(a1, a2):
# 	result = []
# 	for element in a1:
# 		if element in a2:
# 			a2.remove(element)
# 			result.append(element)
# 	return result

# print(array_intersect(a1, a2))

def one_pass_intersect(a1, a2):
	i = 0
	j = 0
	result = []
	if len(a1) is 0 or len(a2) is 0:
		return result
	while i < len(a1) and j < len(a2):
		if a2[j] > a1[i]:
			i += 1
		elif a2[j] is a1[i]:
			result.append(a1[i])
			i += 1
			j += 1
		else:
			j += 1
		print(str(i) + ',' + str(j) + ',' + str(result))
	return result

print(one_pass_intersect(a1, a2))