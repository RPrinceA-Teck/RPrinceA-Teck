__author__ = "✍️ Anass El Adroui"
__license__ = "📜 Ce projet est sous licence MIT"
__version__ = "🔢 0.0.0"
__maintainer__ = "👨‍🔧 Anass El Adroui"
__email__ = "📧 eadraoui.anas@gmail.com"
__Date__ = "📅 28/06/2024"

import PySimpleGUI as sg
import os
class Calc:
    def __init__(self):
        pass
    
    def estimate(self, nbr_sent_received, nbr_wattch, nbr_sp, nbr_deleted, size):
        estimation =[]
        self.Total = nbr_sent_received + nbr_wattch + nbr_sp
        estimation.append(self.Total)
        self.Cfootprint_e = nbr_sent_received * 0.3 + nbr_wattch * 4 + nbr_sp * 50
        estimation.append(self.Cfootprint_e)
        self.Cfootprint_stockage = self.Total *10
        estimation.append(self.Cfootprint_stockage)
        self.distancee = self.Total *102/1.609
        estimation.append(self.distancee)
        self.Cfootprint_wattch = nbr_wattch * 551*0.454/102
        estimation.append(self.Cfootprint_wattch)
        self.consomm_e = nbr_wattch * 62 /102
        estimation.append(self.consomm_e)
        self.bottle_e = nbr_wattch * 3048 /102
        estimation.append(self.bottle_e)
        self.fly_e = nbr_wattch * 10 * 1.609 /102
        estimation.append(self.fly_e)
        self.dry_cyclee = nbr_wattch * 138/102
        estimation.append(self.dry_cyclee)
        self.email_deleted = nbr_deleted * 244/30
        estimation.append(self.email_deleted)
        self.sizes = size * 0.24 / 1000
        estimation.append(self.sizes)
        return estimation

sg.theme('dark green 1')
layout = [[sg.Text('Combien de E-mails(text) reçus et envoyés chaque jour ?', font=("Verdana", "10", "bold")), sg.Push(), sg.Input(key='-nbr_sent_received-')],
          [sg.Text('Combien de E-mails avecattachement envoyés et reçus chaque jour ?',font=("Verdana", "10", "bold")), sg.Push(), sg.Input(key='-nbr_wattch-')],
          [sg.Text('Combien de E-mails brouillons et spams (inclus les réseaux sociaux et promotions) sont collectés dans votre boîte chaque jour ?',font=("Verdana", "10", "bold")), sg.Push(), sg.Input(key='-nbr_sp-')],
          [sg.Text('Combien de E-mails supprimés dans votre boîte chaque jour ?',font=("Verdana", "10", "bold")), sg.Push(), sg.Input(key='-nbr_deleted-')],
          [sg.Text('Quelle est la taille en ton E-mails en Moctets ?',font=("Verdana", "10", "bold")), sg.Push(), sg.Input(key='-size-')],
          [sg.T(' '*8), sg.Button('Calculer'), sg.Button('Quitter'), sg.Button('Références'), sg.Button('A propos...')]]
window = sg.Window('Calculer Empreinte Carbone de ton Email', layout, font='Calibri 10', default_element_size=(25,1), use_custom_titlebar=True, keep_on_top=True)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quitter':
        os._exit(os.EX_OK)
    elif event == 'Références':
        window.disappear()
        sg.popup('1. Carbon Literacy Project: https://www.carbonliteracy.com/ \n',
                 '2. Good Calculators; https://goodcalculators.com/carbon-footprint-calculator/ \n',
                 '3. Eco-Friendly Email Calculator; https://www.emailcarbon.com/ \n',
                 'PySimpleGUI Version', sg.version,  grab_anywhere=True, keep_on_top=True)
        window.reappear()
    elif event == 'A propos...':
        sg.popup('Anass\n', 'E-mail id: eadraoui.anas@gmail.com', sg.version,  grab_anywhere=True, keep_on_top=True)
        window.reappear()
    elif event == 'Calculer':
        user = Calc()
        results = user.estimate(nbr_sent_received = int(values['-nbr_sent_received-']),
                       nbr_wattch=int(values['-nbr_wattch-']),
                       nbr_sp=int(values['-nbr_sp-']),
                       nbr_deleted=int(values['-nbr_deleted-']),
                       size=int(values['-size-']))

        window.disappear()
        
        msg1 ="1)🚗 Avec {} CO2e on peut rouler avec une voiture jusqu'à {} Km qui correspond à {} fois d'aller-retour de Casablanca jusqu'à Rabat.\n".format(results[1], int(results[3]), int(results[3]*333/59940.3))
        msg2 ="2)✈️ Avec {} CO2e on peut voyager par avion jusqu'à {}.\n".format(results[1], results[5])
        msg3 ="4)🍾 Avec {} CO2e on peut jeter {} bouteilles avec un message dans l'océan.\n".format(results[1], results[5])
        msg4 ="5)🍔 Avec {} CO2e c'est l'équivalent de ce qui est dégagé par la consommation de {} hamburgers.\n".format(results[1], results[3])
        msg5 ="6)♻️ Avec {} CO2e c'est l'équivalent de {} cycle de séchage d'une machine à laver.\n".format(results[1], results[6])
        msg6 ="7)📊 {} E-mails stockées, c'est l'équivalent de {} CO2e et de {} sac plastiques.".format(results[0], results[8] ,results[0])
        msg7 ="8)🔋 {} E-mails supprimés, c'est économiser {} de consommation.\n".format(int(values['-nbr_deleted-']), results[7])
        msg8 ="9)💡 {} E-mails avec pièce jointe, c'est comme allumer {} pendant 1h.\n".format(int(values['-nbr_wattch-']), int(values['-nbr_wattch-']))
        sg.popup(msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, font=("Verdana", "10", "bold"), grab_anywhere=True, keep_on_top=True)
        window.reappear()

    window.close()


if __name__ == '__main__':
    Calc()

