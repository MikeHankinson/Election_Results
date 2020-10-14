# Objectives / Data Needed to Retrieve
#   1. Total number of votes cast
#   2. A complete list of candidates who received votes
#   3. Total number of votes each candidate received
#   4. Total number of votes each candidate received
#   5. Total number of votes each candidate received

print("hello")


#Add Dependencies: Modules-csv (work with csv files) and os(view operating system when don't know file path) 3.4.2
import csv
import os

# Assign a variable for the file to load and the path. (module:os, sub module: os.path, funtion: join)
# join - joins file path components together) 3.4.2
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.  3.4.3
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the Election result and read the file.  3.4.3
with open(file_to_load) as election_data:

    print("hello2")
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    
