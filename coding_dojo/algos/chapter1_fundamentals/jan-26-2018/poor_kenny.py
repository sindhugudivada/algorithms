def whathappentoday(probability):
    if probability <= 0.10:
	print "volcanos"
    elif probability >0.1 and probability <= 0.25:
	print "tsunami"
    elif probability > 0.25 and probability <= 0.45:
	print "earthquake"
    elif probability > 0.45 and probability <= 0.70:
	print "blizzards"
    elif probability > 0.70 and probability <= 1:
	print "meteors"




if __name__=='__main__':
    whathappentoday(0.3)
