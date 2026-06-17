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

def rand(val):
    if random.randint(0, 100) <= val:
        return True
    else:
        return False


def find_word(words, letters):
    pos = []

    pos.append([random.randint(0,3), random.randint(0,3)])
    word = letters[pos[0][0]][pos[0][1]]
    num_valid_words = 0
    valid_words = []

    while True:
        count = 0
        if rand(100 + (3 * 3) - (len(word) * 3) + (num_valid_words * 8)):
            while True:
                new_pos = [random.randint(0,3), random.randint(0,3)]
                if abs(new_pos[0] - int(pos[count][0])) <= 1 and abs(new_pos[1] - int(pos[count][1])) <= 1 and len(list(dict.fromkeys(pos.append(new_pos)))) == len(pos):
                    pos.append(new_pos)
                    word = word + letters[new_pos[0]][new_pos[1]]
                    break
            
            if len(word) >= 4 and word in words:
                num_valid_words += 1
                valid_words.append(word)
                
                #if rand(90):
                #    pass
                #else:
                #    break

            count += 1
        else:
            break

    return valid_words



def search(words, runtime, letters):
    #st.write(letters)

    start_time = t.time()
    valid_words = []
    while (t.time() - start_time) < runtime:
        val = find_word(words, letters)
        if val not in valid_words:
            valid_words.append(val)
        #st.write("SEARCHING")
        #t.sleep(1)
    
    st.write(valid_words)
    

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