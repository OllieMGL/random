def test(guess, num):
    c = num + guess
    return(c)
    
c = 10
d = 10
while True:
    a = input("Please put in an input for \"a\" : ")
    c = test(int(a),c)
    print(c)