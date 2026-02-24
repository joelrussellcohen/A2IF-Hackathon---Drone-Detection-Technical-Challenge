# This script is intended to help test your submission for the drone detection hackathon.
# A similar script will be used to evaluate your submission during the judging process,
# and you can use it as a reference for how to structure your code.

# Test 1
{ time python3 count_drones.py --input_1 "Sample challenge 1 (muted).mp4" > output.csv ; } 2> time.csv

# Test 2
{ time python3 count_drones.py --input_2 "Sample challenge 2 (muted).mp4" >> output.csv ; } 2>> time.csv

# Test 3
{ time python3 count_drones.py --input_3 "Sample challenge 3 (muted).mp4" >> output.csv ; } 2>> time.csv

# # Calculate scores
# python score.py --counts true_counts.txt --output output.csv --time time.csv > final_score.csv