
import pandas as pd
import numpy as np

data = pd.read_csv("web-test/popbycountry.csv", delimiter="|")
df = pd.DataFrame(data, columns=[
                  "Country (or dependency)", "Population(2020)", "Land Area (Km²)"])
population = [str.replace(",", "") for str in df['Population(2020)']]
area = [str.replace(",", "") for str in df["Land Area (Km²)"]]
population_np = np.array(population).astype(float)
area_np = np.array(area).astype(float)
popsum = 0
areasum = 0
for i in range(16, len(population)):
    popsum += population_np[i]
    areasum += area_np[i]

population_trimmed = [population_np[i] for i in range(16)]
population_trimmed.append(popsum)
country_trimmed = [df["Country (or dependency)"][i] for i in range(16)]
country_trimmed.append("Others")
area_trimmed = [area_np[i] for i in range(16)]
area_trimmed.append(areasum)

row = list(zip(country_trimmed, population_trimmed, area_trimmed))
columns = [
    "Country (or dependency)", "Population(2020)", "Land Area (Km²)"]

op_df = pd.DataFrame(row, columns=columns)
op_df = op_df.sort_values(by="Population(2020)", ascending=False)

op_df.to_csv("web-test/popbycountry-converted.csv", index=False)
