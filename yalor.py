

#allows a user to check if a certain year correspondes to the release year of 
#any taylor album


def is_album_taylor(intyear):
    try:
        albums = ["2006 - Taylor Swift", "2008-Fearless"]
        for album in albums:
            words = album.split("-")
            albumyr = int(words[0].strip())
        
            print(albumyr)
            print(intyear)

            if albumyr == intyear:
                return True
            else:
                return False
    except:
        print("enter valid")



is_album_taylor(2006)

def tricky_loop(1st):
    for i in range(len(1st)): #0, 1, 2
        1st[i] += i #1 + 0, 
        if 1st[i] % 2 == 0: #
        1st.append(1st[i] + 1)

nums = 1, 2 , 3 
