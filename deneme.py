
import pickle
import pandas as pd
"""""""""
# initializing data to be stored in db
Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak','age': 21, 'pay': 40000}
Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak','age': 50, 'pay': 50000}

# database
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish

# For storing
# type(b) gives <class 'bytes'>;
b = pickle.dumps(db)

# For loading
myEntry = pickle.loads(b)
print(myEntry)


original_df = pd.DataFrame({"a": ((([[1, 2, 3],[11,22,33]],[[2],[2]]))), "b": (7,6)})
print(original_df)

d = pd.DataFrame()

for p in range(1,6):
    temp = pd.DataFrame(
        {
            'Player': (([[p]])),
            'f':(([[p+10]])),
        }
    )

    d = pd.concat([d, temp])
print(d)
"""
# Python code to illustrate
# working of try()
def divide(x, y):
	try:
		# Floor Division : Gives only Fractional
		# Part as Answer
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
	else:
	    pass
# Look at parameters and note the working of Program
divide(3, 2)

