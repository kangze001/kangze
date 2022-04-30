from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die(10)
die_3 = Die(20)

#hello world

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()+die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides+die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}

my_layout = Layout(title='掷一个D6、一个D10以及一个D20 50000次的结果',
                   xaxis=x_axis_config,
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10_d20.html')
