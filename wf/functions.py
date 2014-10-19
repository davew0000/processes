

def createOrder(models):
	return 1
	
def approveOrder(models):
	order = models[0]
	order.approved = True
	order.save()
	return 1

def receiveOrder(models):
	order = models[0]
	order.received = True
	order.save()
	return 1