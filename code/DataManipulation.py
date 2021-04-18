'''
Simply python file that formats the data properly for the 
DMak software that was used. 

The required format was a text file. 
'''

# Open files
data = open("data.csv", "r")
new_file = open("formatted-data.txt", 'w')

# Traverse data rows, add formatted rows to new file
lines = data.readlines()
line_count = 0

for line in lines:
	if line_count != 0:
		formatted_line = line.replace(",", " ")
		formatted_line = formatted_line.strip()
		new_file.write(formatted_line)
	line_count += 1
print(f"Processed {line_count} lines.")

