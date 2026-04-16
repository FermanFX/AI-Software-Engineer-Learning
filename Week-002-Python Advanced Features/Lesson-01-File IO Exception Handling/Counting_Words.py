with open('text.txt', 'r') as f:
    contents = f.readlines()

count = {}
for line in contents:
    # Substitute non-alphabetic characters for space
    clean_line = ''.join([c if c.isalpha() else ' ' for c in line])
    # Clean whitespace and lowercase
    clean_line = clean_line.strip().casefold()
    
    if clean_line:
        for word in clean_line.split(' '):
            if word:
                if count.get(word, False):
                    count[word] += 1
                else:
                    count[word] = 1

# Transform dictionary into a list and sort by count (descending)
count = list(count.items())
count.sort(reverse=True, key=lambda x: x[1])

# Display results
for c in count:
    print(c[0], ':', c[1])

#Outputs
# python : 4
# hello : 3
# is : 2
# for : 2
# world : 1
# everyone : 1
# this : 1
# a : 1
# test : 1
# file : 1
# counting : 1
# words : 1
# great : 1
# text : 1
# processing : 1
# let : 1
# s : 1
# count : 1
# how : 1
# many : 1
# times : 1
# each : 1
# word : 1
# appears : 1
# and : 1
# again : 1