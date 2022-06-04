
#- - - - - - - 
first_three = input('enter first tree nums :')
nums = ['0','1','2','3','4','5','6','7','8','9',]


num_list = []
for i in nums:
    
    for e in nums:
        
        for l in nums:
            for s in nums :
                for h in nums :
                    for g in nums :
                        for r in nums:
                            num_list.append(first_three+i+e+l+s+h+g+r)
                            

with open('pass.txt','w') as f:
    for q in num_list:
        f.write(f'{q}\n')
print('done')