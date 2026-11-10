colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts1 = [(color,size) for color in colors for size in sizes]

tshirts2 = [(color,size) for size in sizes for color in colors]
print("tshirt1 = ", tshirts1)
print("tshirt2 = ", tshirts2)