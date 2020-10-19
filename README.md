# Election_Results
 
## Project Overview
Contracted by the Colorado Board of Elections to develop an automated auditing system to certify the results of a recent local congressional election.  Project deliverables include the following:  

  1. Tabulate and report the total number of votes cast.
  2. Obtain a complete list of candidates who received votes.
  3. Calculate and report the total number of votes each candidate received.
  4. Calculate and report the percentage of votes each candidate received.
  5. Determine and report the winner of the election based upon popular vote.
  6. Calculate and report the voter turnout for each county. 
  7. Calculate and report the percentage of votes from each county.
  8. Report the county with the highest turnout.
  
  
## Resources
Data Source: election_results.csv
Software:  Python (3.7.6) and Visual Studio Code (1.50.1)


## Election Audit Results




## Election Audit Summary

Using Python, generate vote count report to certify local election. ...



============================================================
## Appendix A: Election Audit Readout





## Appendix B: Python Code



# Objectives / Data Needed to Retrieve
#   1. Total number of votes cast
#   2. A complete list of candidates who received votes
#   3. Total number of votes each candidate received
#   4. Calculate the percentage of votes each candidate received
#   5. Determine the winner of the election based upon popular vote

# Challenge Objectives
#   6. The voter turnout for each county
#   7. The percentage of votes from each county out of the total count
#   8. The county with the highest turnout

# Deliverables
#   1. The Election Results Printed to the Command Line
#   2. The Election Results Saved to a Text File
#   3. A written Analysis of the Election Audit (README.md)



# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

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

# Initialize Candidate Options List 3.5.2; Declare an empty dictionary to hold the candidates:votes 3.5.3
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}


# Track the winning candidate, vote count and percentage 3.5.5
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
county_largest_turnout = ""
county_largest_count = 0


# Read the csv and convert it into a list of dictionaries 3.4.3
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header 3.4.4
    header = next(reader)



    # For each row in the CSV file. 3.5.1
    for row in reader:

        # Add to the total vote count  3.5.1
        total_votes = total_votes + 1

        # Get the candidate name from each row. 3.5.2
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count. 3.5.3
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count 3.5.4
        candidate_votes[candidate_name] += 1




        # 4a: Write a decision statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1




# Save the results to our text file. 3.6.1
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal) 3.6.1
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)



    # 6a: Write a repetition statement to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        votes_county = county_votes[county_name]

        # 6c: Calculate the percent of total votes for the county.
        county_percentage = float(votes_county)/float(total_votes)*100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {county_percentage:.1f}% ({votes_county:,})\n")
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write a decision statement to determine the winning county and get its vote count.
        if (votes_county > county_largest_count):

            # If true then set....
            county_largest_count = votes_county
            
            # Set the winning_candidate equal to the candidate's name 3.5.5
            county_largest_turnout = county_name



    # 7: Print the county with the largest turnout to the terminal.
    print()

    county_largest_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {county_largest_turnout}\n"
        f"-------------------------\n"
        f" \n")

    print(county_largest_summary)


    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(county_largest_summary)

    # Iterate through the candidate list.  Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage 3.5.4
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal. 3.6.2
        print(candidate_results)

        #  Save the candidate results to our text file. 3.6.2
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate. 3.5.5
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal) 3.5.5
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)


