# Map reduce for word count
from multiprocessing import Pool

pool = Pool(5)  # Use 5 Thread

def divide_chunks(list_data, number_chunck): 

    # looping till length list_data 
    for i in range(0, len(list_data), number_chunck):  
        yield list_data[i:i + number_chunck]

def map_word_count(text_list):
  dic_count = dict()
  for item in text_list:
    if item in dic_count.keys():
      dic_count[item] += 1
    else:
      dic_count[item] = 1
  
  return(dic_count)

def split_dict(dict_data, number_split):
  for i in range(0, len(dict_data), number_split):
    yield dict(list(dict_data.items())[i: i+number_split])

def reducing(dict_word):
  dic_count = dict()
  for key, val in dict_word.items():
    dic_count[key] = sum(val)
    
  return(dic_count)

sentence =   '''
A MapReduce program is composed of a map procedure, 
which performs filtering and sorting (such as sorting 
students by first name into queues, one queue for each name), 
and a reduce method, which performs a summary operation 
(such as counting the number of students in each queue, 
yielding name frequencies).
'''

# 1. Clean special character and change to lower case
sentence_clean = ''.join(text.lower() for text in sentence if text.isalnum() or text.isspace())
word_list = sentence_clean.split()

# 2. Split data to each chuncks
number_split = 5
chuncks = divide_chunks(word_list, int(len(word_list)/number_split))

# 3. Map data in each chuncks and count
list_count1 = pool.map(map_word_count, chuncks)

# 4. Shuffle data
dic_shuffle = dict()
for dict_word in list_count1:
  for key, val in dict_word.items():
    if key in dic_shuffle.keys():
      dic_shuffle[key].append(int(val))
    else:
      dic_shuffle[key] = [int(val)]

list_count2 = split_dict(dic_shuffle, number_split)

# 5. Reduce word count
list_count3 = pool.map(reducing, list_count2)

# 6. Combine
result = dict()
for dict_count in list_count3:
  result.update(dict_count)

print(result)