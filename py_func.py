

def pascal(n):
    pascal_start = [[1], [1,1]]
    if n == 1:
        print(pascal_start[0])
    elif n == 2:
        return pascal_start
    else:
        while len(pascal_start) < n:
            new_row = [1]
            for num in range(len(pascal_start[-1])):
                if num != len(pascal_start[-1])-1:
                    new_row.append(pascal_start[-1][num] + pascal_start[-1][num+1])
                else:
                    new_row.append(1)
            pascal_start.append(new_row)
        return pascal_start


print(pascal(2))      
    

def num_within(num, min, max):

    if (num >= min and num <= max):
        return True
    else: 
        return False

print(num_within(1, 2, 3), num_within(3, 1, 1000))


def nth_fibbonacci(n):
  if n<= 0:
    print("Incorrect input")
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return nth_fibbonacci(n-1)+nth_fibbonacci(n-2)


def rev_string(phrase):
    new_phrase = []
    phrase = list(phrase)
    for i in range(len(phrase)):
        new_phrase.append(phrase[-1-i])
    print(''.join(new_phrase))


rev_string('peanuts')


def mul_list(*args):
    iterator = 1
    for num in args:
        iterator *= num
    return iterator

print(mul_list(1, 2, 3,4))
