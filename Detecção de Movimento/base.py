import cv2
import tkinter as tk
from tkinter import ttk
import time  

def calculaDiferenca(img1, img2, img3):
    """
    Captura o movimento pela subtração de pixel dos frames.
    """
    d1 = cv2.absdiff(img3, img2)
    d2 = cv2.absdiff(img2, img1)
    imagem = cv2.bitwise_and(d1, d2)
    _, imagem = cv2.threshold(imagem, 60, 255, cv2.THRESH_BINARY)
    return imagem

def liga(selected_camera):
    """
    Inicia a detecção de movimento utilizando a câmera selecionada. Salva as capturas de movimentos em 'C:\Imagens Deteccao/'.
    """
    janela = "Tela de Captura"
    janela2 = "Tela Normal"
    i = 1

    cv2.namedWindow(janela, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(janela2, cv2.WINDOW_AUTOSIZE)

    webcam = cv2.VideoCapture(selected_camera)

    ultima = cv2.cvtColor(webcam.read()[1], cv2.COLOR_RGB2GRAY)
    penultima = ultima
    antepenultima = ultima

    fotos_tiradas = 0  # Contador de fotos tiradas

    while True:
        ret, frame = webcam.read()

        antepenultima = penultima
        penultima = ultima
        ultima = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        cv2.imshow(janela, calculaDiferenca(antepenultima, penultima, ultima))
        cv2.imshow(janela2, frame)

        if sum(sum(calculaDiferenca(antepenultima, penultima, ultima))):
            print(sum(sum(calculaDiferenca(antepenultima, penultima, ultima))))
            nome = 'image' + str(i)
            print(nome)
            cv2.imwrite('C:\\\Imagens\\' + nome + '.jpg', frame)
            
            fotos_tiradas += 1  # Incrementa o contador de fotos tiradas

            # if fotos_tiradas >= 100:
            #     break  # Sai do loop após tirar 100 fotos

            i += 1

        k = cv2.waitKey(30) & 0xFF
        if k == 27:
            webcam.release()
            cv2.destroyWindow(janela)
            cv2.destroyWindow(janela2)
            break


# Função para iniciar a detecção de movimento com a câmera selecionada
def iniciar_detecao():
    selected_camera = camera_combobox.get()  # Obtém a câmera selecionada a partir da lista suspensa
    liga(int(selected_camera))  # Converte para inteiro e inicia a detecção de movimento

# Cria a janela principal
janela = tk.Tk()
janela.title("Detector de Movimento")
janela.geometry('450x450')

# Adiciona um rótulo e um botão à janela
label = tk.Label(janela, text="Para Desligar a Detecção de Movimento Pressione 'Esc'.")
label.pack(pady=10)

botao = tk.Button(janela, text="Ligar Detector de Movimento", command=iniciar_detecao)
botao.pack()

# Adiciona um rótulo e uma lista suspensa (combobox) à janela
label = tk.Label(janela, text="Selecione a câmera:")
label.pack(pady=10)

# Obtém a lista de dispositivos de câmera disponíveis
available_cameras = []
for i in range(10):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        available_cameras.append(i)
        cap.release()

camera_combobox = ttk.Combobox(janela, values=available_cameras)
camera_combobox.pack()

# Inicia a interface gráfica
janela.mainloop()
