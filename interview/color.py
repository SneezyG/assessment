

"""
--- ALGORITHM:
Scrape the colors off the html page.
Then calculate the mean, median and others using the frequency of the colors because all these statistical measures are only possible on numbers variables and not string variable like color.
"""


from bs4 import BeautifulSoup
from collections import Counter
import statistics
import psycopg2

print("\n")

# Open the HTML file
with open('question.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

table_row = soup.find_all('tr')
row_len = len(table_row)

rows_data = ""


index = 0
for row in table_row:
  index += 1
  # get the color text off the <td> tags
  data = row.find_all('td')[1].get_text()
  # append the color text to rows_data(a string variable)
  if index == row_len:
    rows_data += data
  else:
    rows_data += data + ", "


# create list of colours
color_list = rows_data.split(", ")

# create a map of colours and their frequency
color_obj = dict(Counter(color_list))
print(color_obj, "\n")


# getting the mode
mode_color = max(color_obj, key=color_obj.get)
mode_frequency = color_obj[mode_color]
print("Mode color:", mode_color)
print("Frequency:", mode_frequency, '\n')



# getting the median
sorted_colors = sorted(color_list)
median_color = statistics.median(sorted_colors)
print("Median color:", median_color, '\n')



# getting the mean and variance using colour frequency.
mean_frequency = statistics.mean(color_obj.values())
variance_frequency = statistics.variance(color_obj.values())
print("Mean frequency:", mean_frequency)
print("Variance of frequency:", variance_frequency, '\n')


# probability that a color is red
red_prob = color_obj['RED'] / sum(color_obj.values())
print("Red colour probability:", red_prob, '\n')




"""
saving colors and their frequency to database
"""

# connecting to the database
conn = psycopg2.connect(
    dbname="database_name",
    user="username",
    password="password",
    host="host",
    port="port"
)
cur = conn.cursor()

# Create a table
cur.execute("""
    CREATE TABLE IF NOT EXISTS color_frequency (
        id SERIAL PRIMARY KEY,
        color VARCHAR(50) NOT NULL,
        frequency INTEGER NOT NULL
    )
""")
conn.commit()

#Insert data into the table
for color, frequency in color_frequencies.items():
    cur.execute("INSERT INTO color_frequency (color, frequency) VALUES (%s, %s)", (color, frequency))
conn.commit()

# Close cursor and connection
cur.close()
conn.close()

