#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

# read the content
with open("project_01.txt") as f:
   content = f.readlines()

# make a list of lists
content = [x.rstrip() for x in content]        # remove trailing whitespace
content = [x.split(", ") for x in content]     # split based on comma

# create and fill the dictionary
d = dict()
for info_list in content:
    for movie in info_list[1:]:
        try:
            d[movie[:-7]].append(info_list[0])
        except KeyError:
            d[movie[:-7]] = [info_list[0]]

# check whether the movie keys exist in the dictionary
def check_movies(movie1     : str, 
                 movie2     : str,
                 movie_dict : dict) -> None:
    
    # test whether the movie exists
    try:
        movie_dict[m1]
        movie_dict[m2]
    except KeyError:
        print("The defined movies are not found in our dictionary")
    

# part a    
movies = str(input("Movies to compare:\n"))
if "&" in movies:
    m1, m2 = movies.split(" & ")
    check_movies(m1, m2, d)
    print("Union of these two movies:\n{}".format(set(d[m1]).union(set(d[m2]))))
elif "|" in movies:
    m1, m2 = movies.split(" | ")
    check_movies(m1, m2, d)
    print("Intersection of these two movies:\n{}".format(set(d[m1]).intersection(set(d[m2]))))
elif "-" in movies:
    m1, m2 = movies.split(" - ")
    check_movies(m1, m2, d)
    print("Symmetric difference of these two movies:\n{}".format(set(d[m1]).symmetric_difference()(set(d[m2]))))
    
# part b
co_actors = []
actor     = str(input("Actor:\n"))

for l in d.values():
    if actor in l:
        l.remove(actor)
        co_actors.extend(l)

# print the co-actors
print("{}'s co-actors:\n".format(actor))
[print(actor) for actor in co_actors]
