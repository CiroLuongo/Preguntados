import pygame 
from datos_preguntados import lista
from CONSTANTES import *
'''
Nombre: Ciro
Apellido: Luongo
Ejercicio: Preguntados 
'''

pregunta = ""
respuesta_a = ""
respuesta_b = ""
respuesta_c = ""
corecta = ""
posicion_pregunta = 0
posicion_imagen = [30,100]
lista_preguntas = []
lista_respuestas_a = []
lista_respuestas_b = []
lista_respuestas_c = []
lista_correctas = []
puntaje = 0
intentos = 2 

for e_lista in lista:
    lista_preguntas.append(e_lista["pregunta"])
    lista_respuestas_a.append(e_lista['a'])
    lista_respuestas_b.append(e_lista['b'])
    lista_respuestas_c.append(e_lista['c'])
    
pregunta = ""
respuesta_a = ""
respuesta_b = ""
respuesta_c = ""
correcta = ""

pygame.init()

pantalla = pygame.display.set_mode([600 , 600])
pygame.display.set_caption("Preguntados")

imagen = pygame.image.load("preguntados.webp")
imagen = pygame.transform.scale(imagen,(100,100))

#definir textos
fuente = pygame.font.SysFont("Arial", 25)
texto_siguiente_pregunta = fuente.render(("Siguiente pregunta"),True, (0,0,0))
texto_reiniciar = fuente.render(("Reiniciar"),True,(0,0,0))
texto_pregunta = fuente.render(str(pregunta), True, (0,0,0))
texto_respuesta_a = fuente.render(str(respuesta_a),True, (0,0,0))
texto_respuesta_b = fuente.render(str(respuesta_b),True, (0,0,0))
texto_respuesta_c = fuente.render(str(respuesta_c),True, (0,0,0))
texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
texto_correcta = fuente.render(" ",True,COLOR_VERDE)
texto_a = fuente.render('A',True, (0,0,0))
texto_b = fuente.render('B', True, (0,0,0))
texto_c = fuente.render('C', True, (0,0,0))
texto_incorrecta = fuente.render(" ",True,COLOR_ROJO)
texto_final = fuente.render("",True,COLOR_BLANCO)
texto_sin_intentos = fuente.render("",True,COLOR_ROJO)

flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(posicion_click)
            #Escribo las condiciones para el boton de "siguiente pregunta"
            if (posicion_click[0] > 380 and posicion_click[0] < 580) and (posicion_click[1] > 20 and posicion_click[1] < 70):
                pregunta = lista_preguntas[posicion_pregunta]
                texto_pregunta = fuente.render(str(pregunta), True, (0,0,0))

                pygame.draw.rect(pantalla,COLOR_VERDE,(40,100,100,30))
                respuesta_a = lista_respuestas_a[posicion_pregunta]
                texto_respuesta_a = fuente.render(str(f"A_ {respuesta_a}"),True, (0,0,0))

                respuesta_b = lista_respuestas_b[posicion_pregunta]
                texto_respuesta_b = fuente.render(str(f"B_ {respuesta_b}"),True, (0,0,0))

                respuesta_c = lista_respuestas_c[posicion_pregunta]
                texto_respuesta_c = fuente.render(str(f"C_ {respuesta_c}"),True, (0,0,0))

                texto_correcta = fuente.render("",True,COLOR_VERDE) 
                
                if posicion_pregunta < len(lista_preguntas):
                    posicion_pregunta += 1
                elif posicion_pregunta > len(lista_preguntas):
                    posicion_pregunta = 0
                
            #Escribo las condiciones para el boton de "Reiniciar"    
            if (posicion_click[0] > 150 and posicion_click[0] < 320) and (posicion_click[1] > 19 and posicion_click[1] < 69):
                posicion_pregunta = 0
            
                pregunta = ""
                texto_pregunta = fuente.render(str(pregunta), True, (0,0,0))
                
                respuesta_a = " "
                texto_respuesta_a = fuente.render(respuesta_a,True, (0,0,0))

                respuesta_b = " "
                texto_respuesta_b = fuente.render(respuesta_b,True, (0,0,0))

                respuesta_c = ""
                texto_respuesta_c = fuente.render(respuesta_c,True, (0,0,0))
                
                texto_correcta = fuente.render("",True,COLOR_VERDE)
                texto_incorrecta = fuente.render("",True,COLOR_ROJO)

                puntaje = 0
                texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))

                intentos = 2 
                texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))

                texto_sin_intentos = fuente.render(" ",True,(COLOR_BLANCO))
    
            #Realizo las condiciones en cada pregunta dependiendo que letra sea la respuesta correcta
            if posicion_pregunta == 1 :
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
            elif posicion_pregunta == 2 :
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))

            elif posicion_pregunta == 3:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
            
            elif posicion_pregunta == 4:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))

            elif posicion_pregunta == 5:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))

            elif posicion_pregunta == 6:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))

            elif posicion_pregunta == 7:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))

            elif posicion_pregunta == 8:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
            elif posicion_pregunta == 9:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
        
            elif posicion_pregunta == 10:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))

            elif posicion_pregunta == 11:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
            
            elif posicion_pregunta == 12:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))

            elif posicion_pregunta == 13:
                
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))

            elif posicion_pregunta == 14:
                
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))

            
            elif posicion_pregunta == 15:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
            
            elif posicion_pregunta == 16:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))

            elif posicion_pregunta == 17:
                if  ((posicion_click[0] > 415 and posicion_click[0] < 440) and (posicion_click[1] > 375 and posicion_click[1] < 404)): 
                    texto_correcta = fuente.render("CORRECTA",True,COLOR_VERDE)
                    puntaje += 10
                    texto_puntaje = fuente.render(f"Score: {puntaje}",True, (0,0,0))
                    texto_incorrecta = fuente.render("", True, COLOR_ROJO)
                    texto_final = fuente.render("GRACIAS POR JUGAR!!",True, COLOR_BLANCO)
                    intentos = 2
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif (posicion_click[0] > 470 and posicion_click[0] < 495) and (posicion_click[1] > 375 and posicion_click[1] < 404): 
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
                
                elif(posicion_click[0] > 525 and posicion_click[0] < 550) and (posicion_click[1] > 375 and posicion_click[1] < 404):
                    texto_correcta = fuente.render("",True,COLOR_VERDE)
                    texto_incorrecta = fuente.render("INCORRECTA", True, COLOR_ROJO)
                    intentos -= 1
                    texto_intentos = fuente.render(f"Intentos: {intentos}",True,(0,0,0))
            
            if intentos == 0:
                texto_sin_intentos = fuente.render("SIN INTENTOS. Reinicie para volver a jugar",True,COLOR_BLANCO)
                
    pantalla.fill((COLOR_CELESTE))
    pantalla.blit(imagen,(30,30))
    pygame.draw.rect(pantalla,COLOR_VERDE,(415,376,27,30))
    pygame.draw.rect(pantalla,COLOR_VERDE,(470,376,27,30))
    pygame.draw.rect(pantalla,COLOR_VERDE,(525,376,27,30))
    pygame.draw.rect(pantalla, COLOR_BLANCO, (150,20,170,50))
    pantalla.blit(texto_reiniciar,(190,29))
    pygame.draw.rect(pantalla, COLOR_BLANCO, (380,20,200,50))
    pantalla.blit(texto_siguiente_pregunta,(400,29))
    pantalla.blit(texto_pregunta,(15,250))
    pantalla.blit(texto_respuesta_a,(40,300))
    pantalla.blit(texto_respuesta_b,(40,370))
    pantalla.blit(texto_respuesta_c,(40,440))
    pygame.draw.rect(pantalla,COLOR_GRIS,(140,170,105,35))
    pantalla.blit(texto_puntaje,(150,170))
    pygame.draw.rect(pantalla,COLOR_GRIS,(390,170,113,35))
    pantalla.blit(texto_intentos,(400,170))
    pantalla.blit(texto_correcta, (400,311))
    pantalla.blit(texto_a,(421,378))
    pantalla.blit(texto_b,(476,378))
    pantalla.blit(texto_c,(531,378))
    pantalla.blit(texto_incorrecta,(400,458))
    pantalla.blit(texto_final,(200,525))
    pantalla.blit(texto_sin_intentos,(130,520))
    pygame.display.flip()

pygame.quit()
#Entregado