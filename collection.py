# list
a=[1,2,3,4,2]

a.append(11)

a.insert(0,12)
a.pop(0)
b=[11,22,31,41,21]

a.extend(b)



# tuple
# cannt modify

t=(1,2,3)
u=list(t)


# set
s={1,2,3,4,1}
s.add(10)


# dictionary

d={
    "name":"demo",
    "age":30,
    "place":"tirupattur",
    "skills":["c","c++","java"]
}

d["age"]=29

d["scl"]="dsh"

d.update({"cgpa":64})

print(d)