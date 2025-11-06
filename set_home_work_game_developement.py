soccer= {"leon","micheal","luke","ezekiel"}
badminton={"domenik","luke","robbie","emmanuel"}

print("Who played badminton and soccer ?")
players= soccer & badminton
print(players)
print("Who played badminton or soccer but not both ?")
bystanders= soccer ^  badminton
print(bystanders)
print("who played badminton only ?")
one_sport= badminton - soccer
print(one_sport)
