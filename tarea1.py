"""EJERCICIO N°1 WEYMAR VILLCAORUÑO """
tiempo = int(input("Intro el tiempo para llevar a cabo tu proceso: "))
tarea_seg = int(input("Intro los segundos: "))
if tarea_seg>=0 and tarea_seg<=60:
    tarea_min = int(input("Intro los minutos: "))
    if tarea_min>=0 and tarea_min<=60:
        tarea_hor = int(input("Intro la hora: "))
        if tarea_hor>=0 and tarea_hor<=24:
            print(tarea_seg,"s. ",tarea_min,"min. ",tarea_hor,"hrs. ")
            total_time = 0
            tarea_min = tarea_min * 60
            tarea_hor = tarea_hor * 60
            total_time = tarea_seg + tarea_min + tarea_hor
            res = tiempo - total_time
            print("El tiempo para hacer el proceso es de: ",tiempo,"segundos y el tiempo del proceso es: ",total_time,"segundos")
            if res>=0:
                print("El tiempo es suficiente.",res,"segundos restantes")
            else:
                print("El tiempo no es suficiente.")
        else:
            print("Minutos fuera de rango")
    else:
        print("Horas fuera de rango")
else:
    print("Segundos fuera de rango.")