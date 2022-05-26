def find_anagram(str1, str2):
    # [assignment] Add your code here
    sorted_1=sorted(str1)
    sorted_2=sorted(str2)
    if sorted_1==sorted_2:
    #if sorted (earth)== sorted (heart):
        return True
    #print ("True")
    return False
    #print ("False")
print(find_anagram("earth","heart"))
