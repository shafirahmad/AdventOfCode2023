with open("aoc2023/data/day1.txt", "r") as f:
    lines = f.readlines()

sum = 0

for line in lines:
    left= 0
    right=0
    chars = list(line.strip())
    print(chars)
    # Find left
    for char in chars:
        print(char,end=">")
        if char in ['0','1','2','3','4','5','6','7','8','9']:
            
            left = char
            break

    print("  ",end="")
    for char in chars[::-1]:
        print(char,end="<")
        if char in ['0','1','2','3','4','5','6','7','8','9']:
            right = char
            break

    sum += int(left)*10 + int(right)
    print("\n",line,left,right,sum)

p1sum = sum

#Part 2 
nums = "zerohohoho one two three four five six seven eight nine".split()
digits = ['0','1','2','3','4','5','6','7','8','9']
sum=0
for line in lines:
    left= 0
    right=0
    
    newline = "  " + line.strip() + "  "
    chars = list(newline)
    #print(chars, len(chars))
    # Find left
    for i in range(2,len(chars)-1):
        #print(chars[i],end=">")
        if chars[i] in digits:
            left = chars[i]
            break
        found=False
        if (i > 3):
            str3 = chars[i-2]+chars[i-1]+chars[i]
            str4 = chars[i-3]+chars[i-2]+chars[i-1]+chars[i]
            str5 = chars[i-4]+chars[i-3]+chars[i-2]+chars[i-1]+chars[i]
            for j in range(10):
                if str3 == nums[j]: found = True
                if str4 == nums[j]: found = True
                if str5 == nums[j]: found = True
                if found:
                    left = digits[j]
                    #print("found: ", left, j, nums[j])
                    break
        if found:
            break    

    #Find Right
    for i in range(len(chars)-1,1,-1):
        #print(chars[i],end="<")
        if chars[i] in digits:
            right = chars[i]
            break
        found=False
        if (i < len(chars)-4):
            str3 = chars[i]+chars[i+1]+chars[i+2]
            str4 = chars[i]+chars[i+1]+chars[i+2]+chars[i+3]
            str5 = chars[i]+chars[i+1]+chars[i+2]+chars[i+3]+chars[i+4]
            for j in range(10):
                if str3 == nums[j]: found = True
                if str4 == nums[j]: found = True
                if str5 == nums[j]: found = True
                if found:
                    right = digits[j]
                    #print("found: ", right, j, nums[j])
                    break
        if found:
            break    

    sum += int(left)*10 + int(right)
    print(newline,left,right,sum)

p2sum=sum

print("Part1:", p1sum, "Part2:", p2sum)