# Objectives / Data Needed to Retrieve
#   1. Total number of votes cast
#   2. A complete list of candidates who received votes
#   3. Total number of votes each candidate received
#   4. Total number of votes each candidate received
#   5. Total number of votes each candidate received



#Add Dependencies: Modules-csv (work with csv files) and os(view operating system when don't know file path) 3.4.2
import csv
import os




# Assign a variable for the file to load and the path. (module:os, sub module: os.path, funtion: join)
# join - joins file path components together) 3.4.2
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.  3.4.3
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter 3.5.1
total_votes = 0

# Initialize Candidate Options List 3.5.2
candidate_options = []

# Declare an empty dictionary to hold the candidates:votes 3.5.3
candidate_votes = {}

# Winning Candidate and Winning Count Tracker 3.5.5
winning_candidate = ""
winning_count = 0
winning_percentage = 0




# Open the election_results and read the file.  3.4.3
with open(file_to_load) as election_data:

    # Read the file object with the reader function.  3.4.4
    file_reader = csv.reader(election_data)

    # Read and print the header row. 3.4.4
    headers = next(file_reader)
    print(headers)


    # Print each row in the CSV file 3.5.1
    for row in file_reader:
        # Add to the total vote count 3.5.1
        total_votes += 1

        # Print the candidate name for each row 3.5.2
        candidate_name = row[2]



        # If the candidate name does not match any existing candidate in candidate_options
        if candidate_name not in candidate_options:

            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.  3.5.3
            candidate_votes[candidate_name] = 0

        # Add votes to the candidates 3.5.4
        candidate_votes[candidate_name] += 1



# Determine the percentage of votes for each candidate by looping through the counts. 3.5.4

#Iterate through the candidate list.    
for candidate_name in candidate_votes:

    # Retrieve vote count of a candidate. 3.5.4
    votes = candidate_votes[candidate_name]

    # Calculate the percentage of votes. 3.5.4
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    

    # Determine winning vote count and candidate 3.5.5

    # Determine if the votes are greater than the winning count. 3.5.5
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        # If true then set winning_count = votes and winning_percent = vote_percentage 3.5.5
        winning_count = votes
        winning_percentage = vote_percentage

        # Set the winning_candidate equal to the candidate's name 3.5.5
        winning_candidate = candidate_name



# Print winning candidate summary 3.5.5
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



