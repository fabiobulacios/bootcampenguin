import rodi
import time

robot = rodi.RoDI()
try:

    while True:

        linea = robot.sense()
        print(linea)
        print(linea[0])
        print(linea[1])
        time.sleep(0.5)
        if linea[0]<800 and linea[1]<800:
            distancia = robot.see() 
            if distancia > 10: 
                robot.move_left()
                robot.move_stop()
                time.sleep(0.1)
                time.sleep(0.2)
                robot.sing(3000, 800)
            else:
                robot.move(100,100)
                robot.move_forward()
            
        else:
            robot.move_backward()
            time.sleep(0.5)
            robot.move_stop()

except KeyboardInterrupt:
    print("Finalizado")
    robot.move_stop()