import matplotlib.pyplot as plt

with open("filename", 'r') as f:
    lines = f.readlines()

time_intervals = []
throughput = []
for line in lines:
    time_str = line.split()[0]

    time_intervals.append((time_str))

    input_str = line.split()[1]
    throughput.append(input_str)

time_intervals = time_intervals[1:-1]
time_list = list(map(float, time_intervals))
throughput = throughput[1:-1]
throughput_list = list(map(float, throughput))

plt.plot(time_list, throughput_list, color='brown')
plt.xlabel('Time')
plt.ylabel('Throughput')
plt.title('Throughput vs Time')
plt.show()

