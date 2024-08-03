   json1 = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
   json2 = [{'id': 101, 'age': 30}, {'id': 102, 'age': 25}]

   for item1, item2 in zip(json1, json2):
       print(item1, item2)
   