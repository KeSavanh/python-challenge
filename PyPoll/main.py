# Dependencis
import os
import csv
#open file path
election_path = os.path.join('election_data.csv')
#open csv reader
with open(election_path, 'r') as election:
    election_reader = csv.reader(election, delimiter=',')
#skip headers
    next(election_reader)
#create lists 
    voters = []
    counties = []
    candidates_list = []
    votes_candidate = []
    percent_vote_list = []
# add rows into lists created
    for row in election_reader:
        voters.append(row[0])
# count votes from voters list
        total_votes = len(voters)
# assign candidate list and calculate vote numbers
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            index = candidates_list.index(row[2])
            votes_candidate.append(1)
        else:
            index = candidates_list.index(row[2])
            votes_candidate[index] += 1
# find percent of votes for candidates
    for v in votes_candidate:
        percent = round(((v/total_votes)*100), 3)
        percent_vote_list.append(percent)
    for c in range(len(candidates_list)):
        candidate_names = (candidates_list[c])
        candidate_percents = (percent_vote_list[c])
        candidate_votes = (votes_candidate[c])
        # print(str(candidate_names), ":", str(candidate_percents), str(candidate_votes))
                               
                                
#find the maximum votes 
    win_candidate = max(votes_candidate)
# find the winner who has maximun votes
    winner = str(candidates_list[votes_candidate.index(win_candidate)])
# Report
#export to txt file 
#split in 3 parts
analysis_report = os.path.join("..", "Analysis/PyPollReport.txt")
pypollreport = open(analysis_report, "w")
part1 = ["Election Results", "--------------------------", 
            f"Total Votes: {str(total_votes)}",
             "--------------------------"]      
#line3 = str(f"Total Votes: {str(total_votes)}")
#line5 = str(candidate_names), ":", str(candidate_percents), str(candidate_votes)
pypollreport.write('\n'.join(part1)) 
pypollreport.write('\n')
for c in range(len(candidates_list)):
    candidate_names = (candidates_list[c])
    candidate_percents = (percent_vote_list[c])
    candidate_votes = (votes_candidate[c])
    part2 = f"{str(candidate_names)}: {str(candidate_percents)}% ({str(candidate_votes)})"
    pypollreport.write('{}\n'.format(part2))
part3 = ["--------------------------", 
        f"Winer: {str(winner)}", 
        "--------------------------"]    
pypollreport.write('\n'.join(part3)) 
                                                 