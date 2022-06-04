import random 

num = input('enter the number of melli codes:')
first_3_number = input('enter the first 3 number :')

melli_code = ''
turns = 0
new_rest = ''




with open('password&username.txt','w') as f:

    while turns !=int(num):
        turns+=1
        rest_7_numbers = random.choices([1,2,3,4,5,6,7,8,9,0],k=7)
        for i in rest_7_numbers:
            new_rest +=str(i)
        melli_code = first_3_number+new_rest
        f.write(f'{melli_code}\n')
        meli_code = ''
        new_rest =''
        rest_7_numbers = ''
    


    