
import math

# bis 100 weil die 100. Zahl nicht existiert in der Liste
natuerlicheZahlen = [x for x in range(10, 100)]
# bis 51 weil die 51te Zahl nicht existiert in dieser Liste
fiftyNumbers = [x for x in range(-50, 51) if x % 2 == 0]
# bis 10 weil die 10te Zahl nicht existiert in dieser Liste
quadratZahlen = [x * x for x in range(-9, 10)]
# bis 6 weil die 6te Zahl nicht existiert in dieser Liste
# https://stackoverflow.com/a/1361789/5896378
equation = [2 * math.copysign(math.pow(abs(x), 2), x) -
            4*x + 6 for x in range(-5, 6)]
print(equation)
