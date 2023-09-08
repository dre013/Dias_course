country_code = [('10','USA'),('2','India'),('3''Ukraine')]

vote = {                                                    # Доработка хэш-функции
	10:'USA',
	2:"India",
	3:"Ukraine"
}

def search(list_i,key):
	if key in list_i:
		return list_i[key]
			
print(search(vote,2))