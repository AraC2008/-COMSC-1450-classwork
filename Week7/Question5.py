import math
def evaluate_advanced_piecewise(x):
    if x > 0:
        result = math.sqrt(math.log10(x) + math.exp(x))*math.cos(math.radians(x))
    elif x == 0:
        result = 0.0
    else:
        result = math.log(math.fabs(x))+math.pow(math.fabs(x),3)
    return result
def main():
    x = float(input("Enter a value for x: "))
    answer = evaluate_advanced_piecewise(x)
    print("Result:",round(answer,2))
main()