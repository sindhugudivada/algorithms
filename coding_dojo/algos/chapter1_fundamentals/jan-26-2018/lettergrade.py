def lettergrade(score):
    if score < 60:
	print "score:" +str(score)+ ".grade:F"
    elif score >=60  and score <=69:
	print "score:{}.grade{}".format(score,"D")
    elif score >70  and score <=79:
	print "score:{}.grade{}".format(score,"C")
    elif score >80  and score <= 89:
	print "score:{}.grade{}".format(score,"B")
    elif score >=90:
	print "score:{}.grade{}".format(score,"A")



if __name__=='__main__':
    lettergrade(1000)
