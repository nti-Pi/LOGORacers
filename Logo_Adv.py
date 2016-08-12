print "Logo Clone."
import os
import pygame
import math
import random
pygame.init()
frame_counter = 1
x_initial = 250
y_initial = 250
x_final = 250
y_final = 250
vector = 0
unit = ""
value = ""
enter = False
name = raw_input("Please enter your full name and press enter. ")
class_name = raw_input("Please enter your class and section and press enter. ")
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Logo Clone.")
green = (0, 255, 0)
timer = 0
print_collision = False
settings = open(name + " " + class_name + ".txt", "w")
#print variables:
print_0 = pygame.image.load("print_0.png").convert()
print_1 = pygame.image.load("print_1.png").convert()
print_2 = pygame.image.load("print_2.png").convert()
print_3 = pygame.image.load("print_3.png").convert()
print_4 = pygame.image.load("print_4.png").convert()
print_5 = pygame.image.load("print_5.png").convert()
print_6 = pygame.image.load("print_6.png").convert()
print_7 = pygame.image.load("print_7.png").convert()
print_8 = pygame.image.load("print_8.png").convert()
print_9 = pygame.image.load("print_9.png").convert()
print_f = pygame.image.load("print_f.png").convert()
print_d = pygame.image.load("print_d.png").convert()
print_b = pygame.image.load("print_b.png").convert()
print_k = pygame.image.load("print_k.png").convert()
print_r = pygame.image.load("print_r.png").convert()
print_l = pygame.image.load("print_l.png").convert()
print_t = pygame.image.load("print_t.png").convert()
turn_counter = 0
print_collision_pic = pygame.image.load("print_collision.png").convert()
x_print = 5
vec_print = 5
printout = []
Done = False
victory = False
#try:
if 1 == 1:
    while not Done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Done = True
            if event.type == pygame.KEYDOWN:
                if pygame.K_b == event.key:
                    unit = unit + "b"
                    printout.append("b")
                elif pygame.K_k == event.key:
                    unit = unit + "k"
                    printout.append("k")
                elif pygame.K_f == event.key:
                    unit = unit + "f"
                    printout.append("f")
                elif pygame.K_d == event.key:
                    unit = unit + "d"
                    printout.append("d")
                elif pygame.K_r == event.key:
                    unit = unit + "r"
                    printout.append("r")
                elif pygame.K_l == event.key:
                    unit = unit + "l"
                    printout.append("l")
                elif pygame.K_t == event.key:
                    unit = unit + "t"
                    printout.append("t")
                elif pygame.K_1 == event.key:
                    value = value + "1"
                    printout.append("1")
                elif pygame.K_2 == event.key:
                    value = value + "2"
                    printout.append("2")
                elif pygame.K_3 == event.key:
                    value = value + "3"
                    printout.append("3")
                elif pygame.K_4 == event.key:
                    value = value + "4"
                    printout.append("4")
                elif pygame.K_5 == event.key:
                    value = value + "5"
                    printout.append("5")
                elif pygame.K_6 == event.key:
                    value = value + "6"
                    printout.append("6")
                elif pygame.K_7 == event.key:
                    value = value + "7"
                    printout.append("7")
                elif pygame.K_8 == event.key:
                    value = value + "8"
                    printout.append("8")
                elif pygame.K_9 == event.key:
                    value = value + "9"
                    printout.append("9")
                elif pygame.K_0 == event.key:
                    value = value + "0"
                    printout.append("0")
                elif pygame.K_RETURN == event.key:
                    enter = True
                    turn_counter += 1
                    printout = [""]
                elif pygame.K_SPACE == event.key: printout.append("")
                elif pygame.K_BACKSPACE == event.key:
                    unit = ""
                    value = ""
                    printout = [""]
                
        clock = pygame.time.Clock()
        clock.tick(30)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, green, (0, 0, 500, 5))
        pygame.draw.rect(screen, green, (0, 0, 5, 500))
        pygame.draw.rect(screen, green, (495, 0, 5, 500))
        pygame.draw.rect(screen, green, (0, 495, 500, 5))
        pygame.draw.rect(screen, (0, 0, 255), (438, 0, 62, 62))
        #outer ring:
        pygame.draw.lines(screen, green, False, [(438, 225), (438, 62), (62, 62), (62, 438), (438, 438), (438, 275)], 3)
        #middle ring:
        pygame.draw.lines(screen, green, False, [(124, 225), (124, 124), (376, 124), (376, 376), (124, 376), (124, 275)], 3)
        #inner ring:
        pygame.draw.lines(screen, green, False, [(314, 186), (186, 186), (186, 314), (314, 314), (314, 236)], 3)
        
        if vector == 0:
            pygame.draw.lines(screen, (255, 0, 0), True, [(x_final, y_final - 10), (x_final - 4, y_final), (x_final + 4, y_final)], 3)
        elif vector == 90:
            pygame.draw.lines(screen, (255, 0, 0), True, [(x_final + 10, y_final), (x_final, y_final - 4), (x_final, y_final + 4)], 3)
        elif vector == 180:
            pygame.draw.lines(screen, (255, 0, 0), True, [(x_final, y_final + 10), (x_final - 4, y_final), (x_final + 4, y_final)], 3)
        elif vector == 270:
            pygame.draw.lines(screen, (255, 0, 0), True, [(x_final - 10, y_final), (x_final, y_final - 4), (x_final, y_final + 4)], 3)
        else:
            pygame.draw.lines(screen, (255, 0, 0), True, [(x_final, y_final - 10), (x_final - 4, y_final), (x_final + 4, y_final)], 3)        
        
        if value == "":
            value = "0"
    
        while vector >= 360:
            vector = vector - 360
        while vector < 0:
            vector = vector + 360
    #For rt and lt
        if unit == "rt" and enter == True:
            enter = False
            unit = ""
            vector = vector + int(value)
            value = ""
        elif unit == "lt" and enter == True:
            enter = False
            unit = ""
            vector = vector - int(value)
            value = ""
            
    #This is for fd
        elif unit == "fd" and enter == True:
    #alternative with trig:
            if vector <= 90 and vector >= 0:
                x_final = x_initial + math.sin(math.radians(vector)) * int(value)
                y_final = y_initial - math.cos(math.radians(vector)) * int(value)
                value = ""
                unit = ""
                enter = False
            elif vector > 90 and vector <= 180:
                y_final = y_initial + math.sin(math.radians(vector - 90)) * int(value)
                x_final = x_initial + math.cos(math.radians(vector - 90)) * int(value)
                value = ""
                unit = ""
                enter = False
            elif vector > 180 and vector <= 270:
                y_final = y_initial + math.sin(math.radians(270 - vector)) * int(value)
                x_final = x_initial - math.cos(math.radians(270 - vector)) * int(value)
                value = ""
                unit = ""
                enter = False
            else:
                y_final = y_initial - math.cos(math.radians(vector - 270)) * int(value)
                x_final = x_initial - math.sin(math.radians(vector - 270)) * int(value)
                value = ""
                unit = ""
                enter = False
       
    #this is for bk               
        elif unit == "bk" and enter == True:
            if vector <= 90 and vector >= 0:
                x_final = x_initial - math.sin(math.radians(vector)) * int(value)
                y_final = y_initial + math.cos(math.radians(vector)) * int(value)
                value = ""
                unit = ""
                enter = False
            elif vector > 90 and vector <= 180:
                y_final = y_initial - math.sin(math.radians(vector - 90)) * int(value)
                x_final = x_initial - math.cos(math.radians(vector - 90)) * int(value)
                value = ""
                unit = ""
                enter = False
            elif vector > 180 and vector <= 270:
                y_final = y_initial - math.sin(math.radians(270 - vector)) * int(value)
                x_final = x_initial + math.cos(math.radians(270 - vector)) * int(value)
                value = ""
                unit = ""
                enter = False
            else:
                y_final = y_initial + math.cos(math.radians(vector - 270)) * int(value)
                x_final = x_initial + math.sin(math.radians(vector - 270)) * int(value)
                value = ""
                unit = ""
                enter = False
        elif enter == True:
            unit = ""
            value = "0"
            enter = False
        #Printing display:
        for character in range(len(printout)):
            if printout[character] == "f": screen.blit(print_f, (x_print + (character * 18), 510))
            elif printout[character] == "d": screen.blit(print_d, (x_print + character * 18, 510))
            elif printout[character] == "b": screen.blit(print_b, (x_print + character * 18, 510))
            elif printout[character] == "k": screen.blit(print_k, (x_print + character * 18, 510))
            elif printout[character] == "r": screen.blit(print_r, (x_print + character * 18, 510))
            elif printout[character] == "l": screen.blit(print_l, (x_print + character * 18, 510))
            elif printout[character] == "t": screen.blit(print_t, (x_print + character * 18, 510))
            elif printout[character] == "0": screen.blit(print_0, (x_print + character * 18, 510))
            elif printout[character] == "1": screen.blit(print_1, (x_print + character * 18, 510))
            elif printout[character] == "2": screen.blit(print_2, (x_print + character * 18, 510))
            elif printout[character] == "3": screen.blit(print_3, (x_print + character * 18, 510))
            elif printout[character] == "4": screen.blit(print_4, (x_print + character * 18, 510))
            elif printout[character] == "5": screen.blit(print_5, (x_print + character * 18, 510))
            elif printout[character] == "6": screen.blit(print_6, (x_print + character * 18, 510))
            elif printout[character] == "7": screen.blit(print_7, (x_print + character * 18, 510))
            elif printout[character] == "8": screen.blit(print_8, (x_print + character * 18, 510))
            elif printout[character] == "9": screen.blit(print_9, (x_print + character * 18, 510))    
        vector = str(vector)
        for number in range(len(vector)):
            if str(vector)[number] == "0": screen.blit(print_0, (vec_print + number * 18, 535))
            elif vector[number] == "1": screen.blit(print_1, (vec_print + number * 18, 535))
            elif vector[number] == "2": screen.blit(print_2, (vec_print + number * 18, 535))
            elif vector[number] == "3": screen.blit(print_3, (vec_print + number * 18, 535))
            elif vector[number] == "4": screen.blit(print_4, (vec_print + number * 18, 535))
            elif vector[number] == "5": screen.blit(print_5, (vec_print + number * 18, 535))
            elif vector[number] == "6": screen.blit(print_6, (vec_print + number * 18, 535))
            elif vector[number] == "7": screen.blit(print_7, (vec_print + number * 18, 535))
            elif vector[number] == "8": screen.blit(print_8, (vec_print + number * 18, 535))
            elif vector[number] == "9": screen.blit(print_9, (vec_print + number * 18, 535))
        vector = int(vector)
        if print_collision == True:
            screen.blit(print_collision_pic, (5, 560))
            timer += 1
        if timer == 20:
            print_collision = False

        #COLLISION
        if x_initial >= 186 and x_initial <= 314 and y_initial >= 186 and y_initial <= 314:
            if not(y_final >= 186 and y_final <= 236 and x_final >= 314 and x_final <= 376) and not (x_final >= 186 and x_final <= 314 and y_final >= 186 and y_final <= 314): 
                print_collision = True
                x_final = 250
                y_final = 250
                vector = 0
        elif x_initial >= 124 and x_initial <= 376 and y_initial >= 124 and y_initial <= 376:
            if not(x_final <= 376 and x_final >= 124 and y_final <= 376 and y_final >= 124 and not (x_final >= 186 and x_final <= 314 and y_final >= 186 and y_final <= 314)) and not (x_final >= 62 and x_final <= 124 and y_final >= 225 and y_final <= 275):        
                print_collision = True
                x_final = 250
                y_final = 250
                vector = 0
        elif x_initial >= 62 and x_initial <= 438 and y_initial >= 62 and y_initial <= 438:
            if not(x_final <= 438 and x_final >= 62 and y_final <= 438 and y_final >= 62 and not (x_final >= 124 and x_final <= 376 and y_final >= 124 and y_final <= 376)) and not (x_final >= 438 and x_final <= 500 and y_final >= 225 and y_final <= 275):        
                print_collision = True
                x_final = 250
                y_final = 250
                vector = 0
        elif x_final > 500 or x_final < 0 or y_final > 500 or y_final < 0:
                print_collision = True
                x_final = 250
                y_final = 250
                vector = 0
                
        #VICTORY
        if x_final >= 438 and y_final <= 62:
            Done = True
            victory = True
        x_initial = x_final
        y_initial = y_final

        frame_counter = frame_counter + 1
        
        pygame.display.flip()
    pygame.quit()
#except:
    
else:
    pygame.quit()
    print "CRASH"

if victory == True:
    print "YOU WIN!"
    print (frame_counter / 30), "is number of seconds."
    save = (str(frame_counter / 30) + str(turn_counter))
    settings.write(str(frame_counter / 30))
else:
    print "You quit."
settings.close()

    
