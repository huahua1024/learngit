#do_if

age = int(input('please input your age:'))

if age >=18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')
	
########################################################
height = 1.75
weight = 70.5
BMI = weight/(height*height)

if BMI<18.5:
	print('BMI低于18.5：过轻')
elif BMI<25:
	print('BMI 18.5-25：正常')
elif BMI<28:
	print('BMI25-28：过重')
elif BMI<32:
	print('BMI28-32：肥胖')
else:
	print('BMI高于32：严重肥胖')