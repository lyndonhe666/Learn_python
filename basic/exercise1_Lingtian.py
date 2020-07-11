import re

def add_salary(x):
    """
    x: original dictionary with only name and salary
    """
    new_dict={}
    new_dict['name']=x['name']
    new_dict['salary']=x['salary']
    new_dict['tax']=int(x['salary'])*0.1
    new_dict['income']=int(x['salary'])*0.9
    return new_dict


data="""name: Jack   ;    salary:  12000
 name :Mike ; salary:  12300
name: Luk ;   salary:  10030
  name :Tim ;  salary:   9000
name: John ;    salary:  12000
name: Lisa ;    salary:   11000"""
l1=[x.strip() for x in data.split("\n")]
pattern=re.compile('name\s*:\s*(?P<name>\w+)\s*;\s*salary:\s*(?P<salary>\d+)',re.S)
dict_list=[re.search(pattern, x).groupdict() for x in l1]
added_dict = [add_salary(x) for x in dict_list]
for new_dict in added_dict:
    print('name: {};\tsalary: {};\ttax: {};\tincome:{}'.format(new_dict['name'],int(new_dict['salary']),int(new_dict['tax']),int(new_dict['income'])))
