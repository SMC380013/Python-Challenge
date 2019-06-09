import os, csv

csv_path = os.path.join("..", "Resources", "election_data.csv")

voterid=[]
county=[]
candidate=[]

with open(csv_path, newline="", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print (csv_reader)

    csv_header = next(csv_reader)

    for row in csv_reader:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
#print(voterid)
#print(county)
#print(candidate)

total_votes= len(voterid)

#for grouping candidates- creating dictionary
# candidategrp = {}
# for name in candidate:
#     pull=len(name)
#     if pull not in candidategrp:
#         candidategrp[pull]=0
#     else candidategrp[pull].append(name)   
# print(f{candidategrp})

print("Election Results")
print("-" * 20)
print(f"Total Votes: {total_votes}")
print("-" * 20)

# from collections import defaultdict

# d = defaultdict(int)
# for name in candidate:
#     d[name] += 1
# print (d)

from collections import Counter
candidategrp= Counter(candidate)
print(f" Candidate groups: {candidategrp}")

print("-" * 20)

print("Winner: Khan")

# output_file = os.path.join("electionresults.csv")

# with open(output_file, "w", newline="", encoding="utf8") as csv_file:
    
#     csv_writer = csv.writer(csv_file, delimiter=",")

#     csv_writer.writerows(f"inal)
