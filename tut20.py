# def average(a=9,b=1):
#   print("The average is",(a+b)/2)
# average(5)
# average(b=9,a=21)

def average(*numbers):
    sum=0
    for i in numbers:
        sum =sum+1
        print("Average is:",sum/len(numbers))
        average(5,6,7,1)