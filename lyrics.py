def grade_checker(grade):
    if grade >= 90 and grade <= 100:
        return "edi ikaw na ang bright"
    elif grade >= 80 and grade <= 89:
        return "congrats naka line of 8 ka! "
    elif grade >= 75 and grade <= 79:
        return "bawi nalang next sem/grading"
    elif grade >= 101:
        return "mura man kag gi ango2 wala may grado nga ing ana ka dako"
    else:
        return "better luck next time"
    
grade = int(input("Pila imo grade karun sem/grading: "))
print(grade_checker(grade))
    
    