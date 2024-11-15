import pandas

data = pandas.read_csv("Squirrel_Data.csv")
furs = (data["Primary Fur Color"])
# .value_counts())
count_gray = len(data[furs == "Gray"])
count_cinnamon = len(data[furs == "Cinnamon"])
count_black = len(data[furs == "Black"])

new_data = {
    "color": ["gray", "cinnamon", "black"],
    "count": [count_gray, count_cinnamon, count_black]
}

csv = pandas.DataFrame(new_data)
csv.to_csv("new_data.csv")
