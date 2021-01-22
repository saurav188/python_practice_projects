def make_change(coins, n):
    dict={}
    def helper(coins,n):
        key=""
        for coin in coins:
            key+=str(coin)+","
        key+="="+str(n)
        if dict.get(key)!=None:
            return dict[key]
        if n==0:
            return [[],0]
        if len(coins)==1:
            if coins[0]==n:
                dict[key]=[[n],1]
                return [[n],1]
            else:
                dict[key]=False
                return False
        #with the first coin
        temp_key=""
        for i in range(1,len(coins)):
            temp_key+=str(coins[i])+","
        temp_key+="="+str(n-coins[0])
        if dict.get(temp_key)!=None:
            result1=dict[temp_key]
        else:
            temp=helper(coins[1:],n-coins[0])
            if temp!=False:
                result1=[[coins[0]]+temp[0],temp[1]+1]
            else:
                result1=False
        #without the first coin
        temp_key=""
        for i in range(1,len(coins)):
            temp_key+=str(coins[i])+","
        temp_key+="="+str(n)
        if dict.get(temp_key)!=None:
            result2=dict[temp_key]
        else:
            temp=helper(coins[1:],n)
            if temp!=False:
                result2=[temp[0],temp[1]]
            else:
                result2=False
        if result1==False and result2==False:
            dict[key]=False
            return False
        elif result1==False and result2!=False:
            dict[key]=result2
            return result2
        elif result1!=False and result2==False:
            dict[key]=result1
            return result1
        elif result1[1]<result2[1]:
            dict[key]=result1
            return result1
        elif result1[1]>result2[1]:
            dict[key]=result2
            return result2
    return helper(coins,n)

print(make_change([1, 5, 10, 25, 44, 12], 79))