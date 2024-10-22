# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
mostvotes = 0

# Define lists and dictionaries to track candidate names and vote counts
vote_count = {}
candidatelist = []

# Winning Candidate and Winning Count Tracker
Winning_candidate = ''
winning_count = 0


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        

        # Add a vote to the candidate's count
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1

lines = "-------------------------\n"

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    Title = f'Election Results\n'
    print(Title)
    print(lines)
    txt_file.write(Title)
    txt_file.write(lines)

    # Print the total vote count (to terminal)
    totalvote = f'Total Votes: {total_votes}\n'
    print(totalvote)
    print(lines)
    
    # Write the total vote count to the text file
    txt_file.write(totalvote)
    txt_file.write(lines)


    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in vote_count.items():
        

        # Get the vote count and calculate the percentage
        percent = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > mostvotes:
            mostvotes = votes
            winner = candidate

        # Print and save each candidate's vote count and percentage
        candidatevotes = f'{candidate}: {percent: .3f}% ({votes})\n'
        print(candidatevotes)
        txt_file.write(candidatevotes)
        
    print(lines)
    txt_file.write(lines)

    # Generate and print the winning candidate summary
    winnerwinner = f'Winner: {winner}\n'
    print(winnerwinner)

    # Save the winning candidate summary to the text file
    txt_file.write(winnerwinner)
    print(lines)
    txt_file.write(lines)