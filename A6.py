
QUESTIONS=[
    "Do you have sore throat?",
    "Do you have running nose?",
    "Do you have stuffy nose?",
    "Are you noticing any unexplained sweating?",
    "Do you have fever?",
    "Do you have cough?",
    "Are you getting tired without exerting yourself",
    "Do you have headache?",
    "Do you have itchy throat?",
]
THRESHOLD={
    'MILD':30,
    'SEVERE':50,
    'EXTREME':75
}

def Expertsys(questions,threshold):
    score=0
    for question in questions :
        print(question,"Y/N")
        ans=input(">")
        if ans.lower()=='y':
            print("Rate it on the scale 1-10")
            ip=int(input(">"))
            while( int(ip)<1 or int(ip)>10):
                print('Enter correct val')
                ip=int(input('>'))
            score+=int(ip)

    print()
    print()
    if score>=threshold['EXTREME']:
        print('You are suffereing through extreme covid')
    elif score >= threshold['SEVERE']:
        print('You are suffereing through severe covid')
    elif score>=threshold['MILD']:
        print('You are suffereing through mild covid')
    else:
        print("you are safe")

if '__main__'==__name__:
    print("covid expert system")
    Expertsys(QUESTIONS,THRESHOLD)