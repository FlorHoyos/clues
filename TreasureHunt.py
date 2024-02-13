import time
#beginning messages
def startingPoint():
    print("Hello Walter, glad to have you here, now enjoy this!")
    print("I've created clues for you.")
    print("I do enjoy my time with you by the way, now lets start!\n")

def theClues(clueNum, clueWord):
    print(f"Clue {clueNum}: {clueWord}")
    time.sleep(2)  # delay 

def answer(expected_answer):
    user_answer = input("Hey Walter, sabes la respuesta? ❤️ : ").lower()
    return user_answer == expected_answer.lower()    

def endPoint():
    print("\nCongratulations! Felicidades Amor!")
    print("Happy Valentine's Day! ❤️ Do you want to be mine forever? ;)")

def main():
    # clues and answers
    cluesResponse = [
        ("When we first connected What was the name of the app?", "hinge"),
        ("Our first kiss happened outside a restaurant. Which city was it?", "southlake"),
        ("For our second date, we enjoyed Japanese food. Name the Japanese restaurant.", "coco coichibanya"),
        ("I have a special word for you. What is the word I always call you?", "crazy"),
    ]
    # Display introduction
    startingPoint()

    # Start the treasure hunt
    for i, (clue, answer) in enumerate(cluesResponse, start=1):
        theClues(i, clue)

        while True:
            if answer(answer):
                print("Perfecto! we will continue, ready???.")
                time.sleep(1)
                break
            else:
                print("so close, but not close.")
        

    # Reveal the treasure
    print("\nlo ultimo!")
    theClues(len(cluesResponse) + 1, f"The hidden treasure is at ")
    endPoint()

if __name__ == "__main__":
    main()
