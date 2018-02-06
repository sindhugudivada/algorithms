def accurategrades(score):
    if score < 60:
	print "score:" +str(score)+ ".grade:F"
    elif score >=60  and score <=69 :
	print "score:"+str(score)+".grade:D"
    elif score >70  and score <=79 :
	print "score:"+str(score)+".grade:C"
    elif score >80  and score <= 89 :
	print "score:"+str(score)+".grade:B"
    elif score >=90:
	print "score:"+str(score)+".grade:A"




if __name__=='__main__':
    lettergrade(90)
