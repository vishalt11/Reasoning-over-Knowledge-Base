def freebase():
	fo = open("data/Freebase/train.txt", "r")
	entity1 = {}
	entity2 = {}
	relation = {}
	common_entity = {}
	count = 0
	for i in fo:
		count += 1
		#print count
		a = i.split("\t")
		a[2] = a[2][:-1]
		#sprint a
		if a[0] not in entity1:
			#entity1.append(a[0])
			entity1[a[0]] = 1

		if a[2] not in entity2:
			#entity2.append(a[2])
			entity2[a[2]] = 1

		if a[1] not in relation:
			#relation.append(a[1])
			relation[a[1]] = 1

		if a[0] not in common_entity:
			#common_entity.append(a[0])
			common_entity[a[0]] = 1

		if a[2] not in common_entity:
			#common_entity.append(a[2])
			common_entity[a[2]] = 1

	print len(entity1)
	print len(entity2)
	print len(relation)
	print len(common_entity)

	fo = open("freebase_entity1.txt","w")
	for i in entity1:
		fo.writelines(i)
		fo.writelines("\n")

	fo = open("freebase_entity2.txt","w")
	for i in entity2:
		fo.writelines(i)
		fo.writelines("\n")

	fo = open("freebase_relation.txt","w")
	for i in relation:
		fo.writelines(i)
		fo.writelines("\n")

	fo = open("freebase_common_entity.txt","w")
	for i in common_entity:
		fo.writelines(i)
		fo.writelines("\n")


def wordnet():
	fo = open("data/Wordnet/train.txt", "r")
	entity1 = {}
	entity2 = {}
	relation = {}
	common_entity = {}
	count = 0
	for i in fo:
		count += 1
		#print count
		a = i.split("\t")
		a[2] = a[2][:-1]
		#sprint a
		if a[0] not in entity1:
			#entity1.append(a[0])
			entity1[a[0]] = 1

		if a[2] not in entity2:
			#entity2.append(a[2])
			entity2[a[2]] = 1

		if a[1] not in relation:
			#relation.append(a[1])
			relation[a[1]] = 1

		if a[0] not in common_entity:
			#common_entity.append(a[0])
			common_entity[a[0]] = 1

		if a[2] not in common_entity:
			#common_entity.append(a[2])
			common_entity[a[2]] = 1

	print len(entity1)
	print len(entity2)
	print len(relation)
	print len(common_entity)

	fo = open("wordnet_entity1.txt","w")
	for i in entity1:
		fo.writelines(i)
		fo.writelines("\n")

	fo = open("wordnet_entity2.txt","w")
	for i in entity2:
		fo.writelines(i)
		fo.writelines("\n")

	fo = open("wordnet_relation.txt","w")
	for i in relation:
		fo.writelines(i)
		fo.writelines("\n")

	fo = open("wordnet_common_entity.txt","w")
	for i in common_entity:
		fo.writelines(i)
		fo.writelines("\n")

freebase()
wordnet()
