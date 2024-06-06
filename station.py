zones={

    "abc":"c",
    "klo":"c",
    "cde":"b",
    "ijk":"b",
    "efg":"a",
    "ghi":"a"

}
src=['abc',"efg","ghi"]
dest=['klo','ijk',"abc"]
l=[]
for i in range(len(src)):
    ans=""
    if zones[src[i]] == zones[dest[i]]:
        ans+=zones[src[i]]
    else:
        if ord(zones[src[i]]) == ord(zones[dest[i]])-1 or ord(zones[src[i]]) == ord(zones[dest[i]])+1:
            ans+=zones[src[i]]
            ans+=zones[dest[i]]
            l.append(ans)
        else:
            l.append("abc")

    

print(l)