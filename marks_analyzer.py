
**Code (marks_analyzer.py)**  
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("marks.csv")  # columns: Name, Marks

print("Average:", df["Marks"].mean())
print("Highest:", df["Marks"].max())
print("Lowest:", df["Marks"].min())

plt.hist(df["Marks"], bins=10, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
