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
    if random.randint(1, 100) <= val:
        return True
    else:
        return False


def find_word(words, letters):
    pos = []

    pos.append([random.randint(0,3), random.randint(0,3)])
    word = letters[pos[0][0]][pos[0][1]]
    num_valid_words = 0
    valid_words = []

    count = 0
    while True:
        if rand(100 + (3 * 3) - (len(word) * 3) + (num_valid_words * 10)):
            for i in range (180):
                new_pos = [random.randint(0,3), random.randint(0,3)]
                if abs(new_pos[0] - int(pos[count][0])) <= 1 and abs(new_pos[1] - int(pos[count][1])) <= 1 and new_pos not in pos:
                    pos.append(new_pos)
                    word = word + letters[new_pos[0]][new_pos[1]]
                    break
            else:
                return valid_words
            
            if word in words:
                num_valid_words += 1
                if len(word) >= 4:
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
    valid_words = set()
    timer = st.empty()

    while (t.time() - start_time) < runtime:
        remaining = runtime - (t.time() - start_time)
        timer.write(f"Time remaining: {round(remaining, 2)}s")

        found = find_word(words, letters)
        valid_words.update(found)

    sorted_words = sorted(valid_words, key=len, reverse=True)

    st.write(sorted(sorted_words))
    

def main():
    st.title("Word Hunt Bot")

    words = set(remv())

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