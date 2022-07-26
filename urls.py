# The code below is for creating all url endings that return status response 200. 
# Final result is 8 lists. 

#These are the unique URLs that identify a specific photo album. There are 8 albums total. 
a1 = 'https://isc01.gradimages.com/GIT2021/06/50358706/00101/' # The album number for a1 is 00101
a2 = 'https://isc01.gradimages.com/GIT2021/06/50358706/00102/' # The album number for a2 is 00102
b1 = 'https://isc01.gradimages.com/GIT2021/06/50358706/00201/' # The album number for b1 is 00201
b2 = 'https://isc01.gradimages.com/GIT2021/06/50358706/00202/' # The album number for b2 is 00202
c1 = 'https://isc01.gradimages.com/GIT2021/06/50358706/00301/' # The album number for c1 is 00301
c2 = 'https://isc01.gradimages.com/GIT2021/06/50358706/00302/' # The album number for c2 is 00302
d1 = 'https://isc01.gradimages.com/GIT2021/06/50358706/00701/' # The album number for d1 is 00701
d2 = 'https://isc01.gradimages.com/GIT2021/06/50358706/00702/' # The album number for d2 is 00702

# These are the number of photos in each album. (hardcoded, found manually)
a1_end = 524 
a2_end = 654                                                   
b1_end = 531
b2_end = 510
c1_end = 487
c2_end = 500
d1_end = 81
d2_end = 57

# This is the ending. It will be the same for all URLs
ending = '.jpg?preset=p'

# An accessible url example would be 
    # a1 + a1_end(with zero padding) + ending 
    # https://isc01.gradimages.com/GIT2021/06/50358706/00101/0524.jpg?preset=p

#All that has to be done now is to create a range from 0001 to 0[end], turn it into a string, and add it to the prefix and ending.
a1_urls = [a1+str(i).zfill(4)+ending for i in range(1,a1_end+1)] # len 524
a2_urls = [a2+str(i).zfill(4)+ending for i in range(1,a2_end+1)] # len 634
b1_urls = [b1+str(i).zfill(4)+ending for i in range(1,b1_end+1)] # len 531
b2_urls = [b2+str(i).zfill(4)+ending for i in range(1,b2_end+1)] # len 510
c1_urls = [c1+str(i).zfill(4)+ending for i in range(1,c1_end+1)] # len 487
c2_urls = [c2+str(i).zfill(4)+ending for i in range(1,c2_end+1)] # len 500
d1_urls = [d1+str(i).zfill(4)+ending for i in range(1,d1_end+1)] # len 81
d2_urls = [d2+str(i).zfill(4)+ending for i in range(1,d2_end+1)] # len 57
