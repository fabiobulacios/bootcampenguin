import rodi
import time

robot = rodi.RoDI()
"""
pasos = 0
while pasos <= 3:
    pasos = pasos + 1
    robot.move_forward()
    time.sleep(2)
    robot.move_right()  
    time.sleep (0.5)
    

robot.move_left()  
time.sleep (3)
robot.move_stop()
#######

for movimiento in range(4):
    robot.move_forward()
    time.sleep(2)
    robot.move_right()  
    time.sleep (0.5)
 """


print("El siguiente obstaculo está a " , robot.see(), "cm")

""" variable = 3
while True:
    print(robot.see(), "centimetros") """

""" try:         #intentar esto
    while True: 
        print(robot.see(), "centimetros") #cuenta sin parar a que distancia se encuentra de un obstaculo
        if robot.see() > 8:     #cuando robot.see() sea mayor a 8 cm Rodi anda gracias a la accion siguiente
            robot.move_forward() #se le ordena a Rodi que mientras se cumpla lo anterior Rodi ande hacie el frente sin drama
        
        else: 
            robot.move_left() #si robot.see() es menor a 8 se cumple lo siguiente
            time.sleep(0.5) # al encontrar un obstaculo a 8 o menos cm Rodi gira a la izquierda y sigue andado mientras no
            #haya un obstaculo
            

except KeyboardInterrupt:# se puede detener a Rodi con ctrl+c para finalizar sus acciones
    print("Finalizado")
    robot.move_stop() """
    

    #Hacer que Rodi busque un objeto movil y lo persiga y cuando lo encuentre lo empuje

""" import random 

while True:                         #Sirve para alternar los colores del Rodi
    x= random.randint(0,255)
    y= random.randint(0,255)
    z= random.randint(0,255)
    time.sleep(0.05)
    robot.pixel(x,y,z) """



""" try:                                        #codigo para batalla
    while True:
        distancia = robot.see() 
        print(distancia," cm")

        if distancia > 10: 
            robot.move(-50,50)
            robot.move_stop()
            time.sleep(0.1)
            robot.move(5,5)
            time.sleep(0.2)
        else:
            robot.move(100,100)
            robot.move_forward()

        
except KeyboardInterrupt:
    print("Finalizado")
    robot.move_stop()  """


#robot.sing(3000, 800)

#SEGUIDOR DE LINEA
while True:

    linea = robot.sense()
    print(linea)
    print(linea[0])
    print(linea[1])
    time.sleep(0.5)
    if linea[0]<800 and line[1]<800:
        
