# Split list on nulls
input_vals = [1, 5, None, 7, 2, 9, None, 4]
output_vals = []
holder = []

for num in input_vals:
    if num is not None:
        holder.append(num)
    else:
        output_vals.append(holder)
        holder = []
if len(holder) > 0:
    output_vals.append(holder)

print(output_vals)
