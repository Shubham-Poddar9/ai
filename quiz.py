import random, requests, html


URL = "https://opentdb.com/api.php?amount=10&category=9&type=multiple"

def quiz():
    try:
        questions=requests.get(URL).json()["results"]
    
    except:
        print("unable to get question")
        return
    
    score=0
    print("welcome to the quiz\n")
    for i,q in enumerate(questions,1):
        qn=html.unescape(q['question'])
        ans=html.unescape(q["correct_answer"])
        opts=[html.unescape(x)for x in q["incorrect_answers"]]+[ans]
        random.shuffle(opts)
        print(f"q{i}.{qn}")

        for n,op in enumerate(opts,1):
            print(f"{n}.{op}")

        while True:
            try:
                choice=int(input("enter your choice from 1 to 4 option :- "))
                if 1<=choice <=4:
                    break

            except:
                pass
            print("no option ")

        if opts[choice-1]==ans:
            print("correct answer whooooooooo! \n")
            score += 1
        else:
            print("the option is wrong but the correct answer is :- ","\n",ans)

    print("your total score is ",score/len(questions))
    print("you got ",(score/len(questions)*100) , "%")

quiz()



