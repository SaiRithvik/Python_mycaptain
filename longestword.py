def longest_word():
	list1 = (input("enter the list of words:"))
	list2 = list(list1.split(","))

	a = len(list2)

	longest = len(list2[0])

	for i in range(a):
		if(len(list2[i])>longest):
			longest = len(list2[i])

	print(longest)

longest_word()
