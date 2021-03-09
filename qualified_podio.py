def podio_olimpico(tempo_chegada1,tempo_chegada2,tempo_chegada3,nome_corredor1,nome_corredor2,nome_corredor3):

    if tempo_chegada1 < tempo_chegada2 and tempo_chegada1 < tempo_chegada3:
        primeiro_lugar = tempo_chegada1
    elif tempo_chegada2 < tempo_chegada1 and tempo_chegada2 < tempo_chegada3:
        primeiro_lugar = tempo_chegada2   
    else:
        primeiro_lugar = tempo_chegada3
    if tempo_chegada1 > tempo_chegada2 and tempo_chegada1 > tempo_chegada3:
        ultimo_lugar = tempo_chegada1
    elif tempo_chegada2 > tempo_chegada1 and tempo_chegada2 > tempo_chegada3:
        ultimo_lugar = tempo_chegada2   
    else:
        ultimo_lugar = tempo_chegada3
    if tempo_chegada1 > tempo_chegada2 and tempo_chegada1 < tempo_chegada3:
        segundo_lugar = tempo_chegada1
    elif tempo_chegada2 > tempo_chegada1 and tempo_chegada2 < tempo_chegada3:
        segundo_lugar = tempo_chegada2   
    else:
        segundo_lugar = tempo_chegada3

        print(f"1 - {nome_corredor1} - {primeiro_lugar} minutos\n"
        f'2 - {nome_corredor2} - {segundo_lugar} minutos\n'
        f'3 - {nome_corredor3} - {ultimo_lugar} minutos\n'
            )
        
tempo_chegada1 = 120
tempo_chegada2 = 90
tempo_chegada3 = 110
nome_corredor1 = "Ronaldo"
nome_corredor2 = "Wanderlei Cordeiro de Lima"
nome_corredor3 = "Eliud Kipchoge"

podio_olimpico(tempo_chegada1,tempo_chegada2,tempo_chegada3,nome_corredor1,nome_corredor2,nome_corredor3)