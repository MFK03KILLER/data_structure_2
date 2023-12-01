def selection_sort_names(names):
    for i in range(len(names)-1):
        min_index = i
        for j in range(i+1, len(names)):
            if names[j]['Last Name'] < names[min_index]['Last Name']:
                min_index = j
            elif names[j]['Last Name'] == names[min_index]['Last Name']:
                if names[j]['First Name'] < names[min_index]['First Name']:
                    min_index = j
        names[i], names[min_index] = names[min_index], names[i]
    return names

# Example usage
names = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]

sorted_names = selection_sort_names(names)
print(sorted_names)
# bakhshe avale proje jahate sort kardan alephbaii
# ====================================================
#bakhshe dovome proje baraye sakhtan data haye random va baresi sorat mohasebe algorithm dar sorat taghir size vorodi data
import matplotlib.pyplot as plt
import random
import time

def selection_sort(people):
    n = len(people)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if people[j]['First Name'] < people[min_index]['First Name']:
                min_index = j
        people[i], people[min_index] = people[min_index], people[i]


def generate_random_data(n):
    data = []
    for _ in range(n):
        first_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        last_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        data.append({'First Name': first_name, 'Last Name': last_name})
    return data

def measure_sorting_time(data):
    start_time = time.time()
    selection_sort(data)
    end_time = time.time()
    return end_time - start_time


data_sizes = list(range(10, 1001, 10))
sorting_times = []

for size in data_sizes:
    data = generate_random_data(size)
    sorting_time = measure_sorting_time(data)
    sorting_times.append(sorting_time)


plt.plot(data_sizes, sorting_times)
plt.xlabel('Meghdar dade vorodi')
plt.ylabel('Zaman mohasebe(sanie)')
plt.title('modat zaman mohasebe VS tedad data vorodi | Ostad Eskandari')
plt.show()

