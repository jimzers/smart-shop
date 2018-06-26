
#ORGANIZING TEXT FILE DATA INTO OBJECT AND ATTRIBUTES 

fle = "C:clothesdata.txt"
f = open(fle)
text = f.read()
with open(fle) as f:
	clothelist = [line.split() for line in f]

for lst in clothelist:
	Clothing(clothing_name = lst[0], store_name = lst[1], clothing_type = lst[2], clothing_price = lst[3], clothing_style = lst[4], clothing_url = lst[5], clothing_image = lst[6], friendly = lst[7])

#SEARCH
def search():
	budget = document.ClothingSearch.budget.value
	clothetype = document.ClothingSearch.type.value
	clothepreference = document.ClothingSearch.preference.value
	friendliness = document.ClothingSearch.friendly.value
	for clothe in Clothing.objects.all():
		searchlist = []
		if budget >= clothe.clothing_price and clothetype == clothe.clothing_type and clothepreference == clothe.clothing_style:
			if friendliness == clothe.friendly:
				searchlist.append(clothe)
				#for obj in searchlist:
					#RETURN OBJECTIMAGE + URL IN SEARCHRESULTS HTML FILE
			else:
				searchlist.append(clothe)
				#for obj in searchlist:
					#RETURN OBJECTIMAGE + URL IN SEARCHRESULTS HTML FILE
				


