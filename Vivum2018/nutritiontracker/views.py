from django.shortcuts import render
import requests

import datetime

def renderAll(request):
	if not request.user.is_authenticated:
		return render(request, 'nutritiontracker/index.html', {'error': 'You must be signed in to view this page.'})
	else:
		falseUser = FalseUser.objects.get(user=request.user)
		if (falseUser.height == -1):
			return render(request, 'nutritiontracker/index.html', {'displayForm': 'True'})
		else:
			resultsDict = {calGol: falseUser.calorieGoal, calDate: falseUser.calorieDate}
			return render(request, 'nutritiontracker/index.html', {'resultsDict': resultsDict})

def submitFood(request):
	if request.POST:
		falseUser = FalseUser.objects.get(user=request.user)
		
		endpoint = 'https://api.edamam.com/api/food-database/parser'
		param = {'ingr': request.POST['food'], 'app_id': 'f9e2673a', 'app_key': '98567a484e370e9f073756bf971463e8'}
		r = requests.get(url=endpoint, params = param)
		j = r.json()

		rData = {name: request.POST['food'], cals: (j['parsed'][0]['food']['nutrients']['ENERC_KCAL'] * int(request.POST['qty']))/100}
		resultsDict = {calGol: falseUser.calorieGoal, calDate: falseUser.calorieDate, recipeFound: rData}
		return render(request, 'nutritiontracker/index.html', {'resultsDict': resultsDict})
	else:
		return render(request, '404.html')

def updateDetails(request):
	cur_false_user = FalseUser.objects.get(user=request.user)

	if request.method == 'POST':
		try:
			age = request.POST['age']
			height = request.POST['height']
			weight = request.POST['weight']
		except:
			return render(request, 'nutritiontracker/index.html', {error: 'You have left one or more fields blank.'})
		else:
			BMR = 10 * weight - 5 * age
			if cur_false_user.gender == 'M':
				BMR += 6.25 * height + 5
			else:
				BMR += 6.25 * height - 161

			cur_false_user.age=age,
			cur_false_user.height=height,
			cur_false_user.weight=weight,
			cur_false_user.calorieGoal=BMR*7
			cur_false_user.calorieDate= datetime.date.today() + datetime.timedelta(days=7)

			cur_false_user.save()

			return renderAll(request)
	else:
		return render(request, '404.html')