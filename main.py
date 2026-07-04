import streamlit as st
import time as t
import random 

def remv():

    with open("freq-word.txt", "r") as f:
        text = f.read()

    words = text.split()
    filtered_words = []
    for i in range (len(words)):
        if len(words[i]) >= 3:
            filtered_words.append(words[i])

    with open("output.txt", "w") as f:
        f.write(" ".join(filtered_words))

    return filtered_words




def convert(pos, letters):
    word = ""
    for i in range (len(pos)):
        word = word + str(letters[pos[i][0]][pos[i][1]])
    return word

def find_neighbors(pos, count):
    neighbors = []
    x, y = pos[count][0], pos[count][1]
    for m in range (-1, 2):
        for n in range (-1, 2):
            newx, newy = x + m, y + n
            if 0 <= newx < 4 and 0 <= newy < 4 and not (n == 0 and m == 0):
                new = [newx, newy]
                if new not in pos:
                    neighbors.append(new)
    return neighbors

def find_word(words, letters):
    pos = []
    pos.append([random.randint(0,3), random.randint(0,3)])

    count = 0
    while True:
        

        neighbors = find_neighbors(pos, count)
        #st.write(neighbors, count)
        if len(neighbors) > 0:
            pos.append(random.choice(neighbors))
        else:
            break


        word = convert(pos, letters) 
        if word in words:
            return word
             
        if len(word) > 10:
            break


        count += 1

            



def search(words, runtime, letters):
    #st.write(letters)

    start_time = t.time()
    valid_words = []
    time_left = st.empty()
    while (t.time() - start_time) < runtime:
        time_left.write(f"Time left: {round(runtime - t.time() + start_time, 1)}")
        val = find_word(words, letters)
        if val not in valid_words:
            valid_words.append(val)
        #st.write("SEARCHING")
        #t.sleep(1)

    if None in valid_words:
        valid_words.remove(None)
    
    st.write(sorted(valid_words, key=len, reverse=True))
    

def main():
    st.title("Word Hunt Bot")

    words = remv()

    #st.write(words)
    NULL = 0
    rows = [NULL, NULL, NULL, NULL]
    with st.form("grid_input"):
        for i in range (4):
            rows[i] = (st.text_input(f"Row {i + 1}", key=f"row_{i}"))

        runtime = st.slider("Amount time given to search", 5, 75)
        runtime = int(runtime)

        submit = st.form_submit_button()

        if submit:
            letters = []
            for i in range (4):
                letters.append(list(rows[i]))

            #st.write(letters)

            search(words, runtime, letters)
    

if __name__ == "__main__":
    main()