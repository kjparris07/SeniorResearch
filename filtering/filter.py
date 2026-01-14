with open('excluded-participants.csv') as file:
    excluded = file.read().split('\n')

applicantsPath = input('Enter path to applicants csv:  ')
with open(applicantsPath) as file:
    applicants = file.read().split('\n')

ineligible = []
eligible = applicants
for a in applicants:
    if a in excluded:
        ineligible.append(a)
        eligible.remove(a)

if len(ineligible) > 0:
    print("\nIneligible Applicants:")
    for i in ineligible:
        print(i)

cont = input("\nWould you like to generate an email list? (y/n):  ").lower()

if cont == 'y':
    doodlePath = input("Enter path to doodle csv:  ")

    with open(doodlePath) as file:
        registered = file.read().split('\n')
    
    emailList = ''
    for a in eligible:
        if a not in registered:
            emailList += a + ', '
    
    emailList = emailList[:-2]
    print()
    print(emailList, '\n')