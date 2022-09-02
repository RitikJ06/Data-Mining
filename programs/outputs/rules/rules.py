def findDecision(obj): #obj[0]: Outlook, obj[1]: Temp, obj[2]: Humidity, obj[3]: Windy
	# {"feature": "Outlook", "instances": 14, "metric_value": 0.122, "depth": 1}
	if obj[0]>0:
		# {"feature": "Humidity", "instances": 10, "metric_value": 0.1, "depth": 2}
		if obj[2]<=0:
			# {"feature": "Temp", "instances": 5, "metric_value": 0.1172, "depth": 3}
			if obj[1]>1:
				return 0.3333333333333333
			elif obj[1]<=1:
				return 0
			else: return 0.0
		elif obj[2]>0:
			# {"feature": "Windy", "instances": 5, "metric_value": 0.2, "depth": 3}
			if obj[3]<=False:
				return 1
			elif obj[3]>False:
				return 0.5
			else: return 0.5
		else: return 0.8
	elif obj[0]<=0:
		return 1
	else: return 1.0
