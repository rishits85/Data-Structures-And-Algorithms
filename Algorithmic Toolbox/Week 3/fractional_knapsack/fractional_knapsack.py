# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	value = 0.
	unit_val = []
	max_unit_val = 0
	amount = 0
	# write your code here
	for i in range(0,len(weights)):
		# print(i)
		unit_val.append(values[i]/weights[i])

	while capacity > 0:
		i = unit_val.index(max(unit_val))
		print(type(i))
		max_val_cap = capacity[i]
		value = max_val_cap * values[i]
		capacity - max_val_cap
		unit_val.pop(i)
		capacity.pop[i]
		value.pop[i] 

	print(value)
	# print(unit_val)
	# print(max(unit_val))
	return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    # print(values)
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
