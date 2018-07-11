

with open("snli_1.0_dev.txt", "rb") as f1, open("dev_X.txt", "wb") as f2, open("dev_y.txt", "wb") as f3:
 	i=0
 	for row in f1:
 		i+=1
 		if i==1:
 			continue
		else:
			col=row.strip().split('\t')
			f2.write(col[5]+'\t'+col[6]+'\n')
			f3.write(col[0]+'\n')

