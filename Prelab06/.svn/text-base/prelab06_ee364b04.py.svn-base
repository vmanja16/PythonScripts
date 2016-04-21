import re

# QUESTION 1
string11=" AAAA "
string12=" A "
pattern1 = " A{2,5} "
match1 = re.search(pattern1, string11)
match2 = re.search(pattern1, string12)
if match1: print("{} matched pattern {}!".format(string11,pattern1))
if match2: print("{} matched pattern {}!".format(string12,pattern1))

# QUESTION 2
string21="Herecomesthe12.35kl;j;negative-12.35dj;lad"
pattern2 = r"-?[0-9]*\.[0-9]+"
# matches [.99 01.999 -1.1 etc] not integers/chars
sub = re.sub(pattern2,"float", string21)
print(sub)

# QUESTION 3
string21="Herecomesthe12.35kl;j;negative-12.35dj;lad"
pattern2 = r"-?[0-9]*\.[0-9]+"
sub = re.subn(pattern2, "float", string21)
print(sub[1])

# QUESTION 4
string4="12jkld;jafl;d-12jda;lsfja5dk;alsf6dafj;14"
pattern4 = r"-?[0-9]+"
integers=re.findall(pattern4, string4)
print(sum([int(x) for x in integers]))

# QUESTION 5
string5="EE364EE364EE364"
pattern5 = r"EE364"
newstring5 = re.sub(pattern5, "EE461", string5, 1)
print(newstring5)

# QUESTION 6

IPV4 = r"(?P<IP>(((0*[0-1]?[\d]{0,2})|(0*[2][0-5]{0,2}))\.){3}(([2][0-5]{0,2})|([0-1]?[\d]{0,2})))"
match=re.search(IPV4, "123.123.123.123")
if match:
    print(match.group("IP"), "--VALID IP")

# QUESTION 7

# a) Search string input for the letter 'e', ignore case
# b) Match the strvar "input" to any set of characters followed
#    by "is a" followed by any character till a new line
#    Place "is a" and the characters on either side into groups
# c) Same as part B, but name the first group as "First",
#    the "is a" as "Second" and the last group as "Third"
#    They can be called as match.group("First") etc..
# d) Search for substrings in input matching "I" followed by
#    "like" ten or more times, followed by "you" one for
#    two times. Group the "I", the "likes", and "you"
#    separately

