from collections import Counter   #counter makes a frequency dictionary that a particular list contain how many same type of words
def ana(input):
    input=input.split(" ")
    for i in range(0,len(input)):
        input[i]=''.join(sorted(input[i]))
        #since sorted function return list but we have to make string so 'a','n','t' become ant by join()
    print("sorted: ",str(input))
    frequencydic=Counter(input)
    print(max(frequencydic.values()))#.values returns keys and .elements() returns values

if __name__=="__main__":
    input="cars bikes arcs steer"
    ana(input)

