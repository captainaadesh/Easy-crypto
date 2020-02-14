import random
import string


class EasyCrypto:
	def __init__(self, key):
		self.__all_char = string.ascii_letters+string.digits+string.punctuation+" "
		self.__key_split(key)
		self.__list_of_random_lists = list()
		self.__generate_random_lists()

	def __key_split(self, key):
		try:
			self.__seed, self.__number_of_lists = key.split(".")
			self.__number_of_lists = int(self.__number_of_lists)
		except:
			raise Exception('Invalid key.\nValid key format: <seed:[int/float/string]>.<no_of_lists:[int]>')
 
	def __generate_random_lists(self):
		random.seed(self.__seed)
		for i in range(self.__number_of_lists):
			temp = list(self.__all_char)
			random.shuffle(temp)
			self.__list_of_random_lists.append(''.join(temp))


	def __substitute(self, lista, listb, c):
		try:
			return listb[lista.index(c)]
		except: 
			return c

	def encrypt(self, text):
		final=""
		random_int = [random.randint(0,self.__number_of_lists-1) for x in range(len(text))]

		for (letter,l_num) in zip(text,random_int):
			temp = self.__substitute(self.__all_char, self.__list_of_random_lists[l_num], letter)
			final += temp
		return final

	def decrypt(self, text):
		final=""
		random_int = [random.randint(0,self.__number_of_lists-1) for x in range(len(text))]
		for (letter,l_num) in zip(text,random_int):
			temp = self.__substitute(self.__list_of_random_lists[l_num], self.__all_char, letter)
			final += temp
		return final
