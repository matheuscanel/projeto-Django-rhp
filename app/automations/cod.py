import sqlite3
import pyautogui
import time
import datetime
 
#obter a data e hora atuais
data_atual = datetime.datetime.now()
 
pyautogui.PAUSE = 0.5
 
conn = sqlite3.connect(r'C:\Users\60925\Desktop\projeto Django\db.sqlite3')

cursor = conn.cursor()
 
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='app_medicos'")
tabela_existe = cursor.fetchone()
 
cursor.execute('SELECT cpf, nome, cracha, data_nascimento, sexo, estado_civil, raca, estado_nascimento, cidade_nascimento, cep, grau_de_instrucao, estado_civil FROM "app_medicos"')
 
dados = cursor.fetchall()
 
for cpf, nome, cracha, data_nascimento, sexo, estado_civil, raca, estado_nascimento, cidade_nascimento, cep, grau_de_instrucao, estado_civil in dados:  # Desempacotando diretamente as variáveis cpf e nome
 
    pyautogui.hotkey('win', 'r')
    pyautogui.write("https://rhp.nydusrh.com/default.aspx#/Dashboard/Index.aspx")
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.press('enter')
    time.sleep(5)
    #adm pessoal
    pyautogui.press('tab', 4)
    pyautogui.press('enter')
    time.sleep(5)
    #admissão
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)
    #colaborador
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)
    #funcionario-pessoa fisica
    pyautogui.press('tab', 7)
    pyautogui.press('enter')
    time.sleep(5)
    #cadastro de pessoa - novo
    pyautogui.press('tab', 2)
    pyautogui.press('enter')
 
    time.sleep(10)
    pyautogui.typewrite(cpf)
    pyautogui.press('tab')
    time.sleep(5)
 
    pyautogui.press('tab', 2)
    pyautogui.typewrite(nome)
    time.sleep(5)
 
    pyautogui.press('tab')
    pyautogui.typewrite(cracha)
    time.sleep(5)
    pyautogui.press('tab')
 
    pyautogui.typewrite(data_nascimento)
    pyautogui.press('tab')
    time.sleep(10)
 
    #sexo
    pyautogui.press('tab', 5)
    pyautogui.press('enter')
    pyautogui.typewrite(sexo)
    pyautogui.press('enter')
    time.sleep(8)
 
    #tratamento
    pyautogui.press('tab', 7)
    pyautogui.press('enter')
    pyautogui.press('down', 3)
    pyautogui.press('enter')
    pyautogui.press('tab')
 
    #estado civil
    pyautogui.press('enter')
    pyautogui.typewrite(estado_civil)
    pyautogui.press('enter')
    pyautogui.press('tab')
 
    #raça
    pyautogui.press('enter')
    pyautogui.typewrite(raca)
    pyautogui.press('enter')
    pyautogui.press('tab', 4)
   
    #grau de instrução
    pyautogui.press('enter')
    pyautogui.typewrite(grau_de_instrucao)
    pyautogui.press('enter')
    time.sleep(5)
 
    if grau_de_instrucao == 'Ph.D.':
        pyautogui.press('tab', 15)
    else:
        pyautogui.press('tab', 17)
 
    #nacionalidade
    pyautogui.press('enter')
    pyautogui.typewrite('Brasileiro')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
 
    #estado de nascimento
    pyautogui.typewrite(estado_nascimento)
    time.sleep(5)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('tab', 19)
 
    #cidade de nascimento
    pyautogui.typewrite(cidade_nascimento)
    time.sleep(4)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.press('tab', 2)
 
    #CEP
    cep_str = str(cep)
 
    for char in cep_str:
        pyautogui.typewrite(char)
        time.sleep(0.4)
       
    time.sleep(5)
   
    time.sleep(3)
 
    pyautogui.press('tab', 10)
    time.sleep(2)
    pyautogui.press('tab', 10)
    time.sleep(2)
    pyautogui.press('tab', 10)
    time.sleep(2)
    pyautogui.press('tab', 10)
    time.sleep(2)
    pyautogui.press('tab', 10)
    time.sleep(2)
    pyautogui.press('tab', 10)
    time.sleep(2)
    pyautogui.press('tab',5 )
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(20)
 
 
    #ADMISSÃO
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write("https://rhp.nydusrh.com/default.aspx#/Dashboard/Index.aspx")
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.press('enter')
    time.sleep(5)
    #adm pessoal
    pyautogui.press('tab', 4)
    pyautogui.press('enter')
    time.sleep(5)
    #admissão
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)
    #colaborador
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)
    #externo
    pyautogui.press('tab', 6)
    pyautogui.press('enter')
    time.sleep(5)
    #admissão
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)
    #colaborador externo - novo
    pyautogui.press('tab', 2)
    pyautogui.press('enter')
    time.sleep(5)
    #dados - pessoa fisica
    pyautogui.press('tab')
    pyautogui.typewrite(cpf)
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
 
    #data de admissão
    pyautogui.typewrite(data_atual.strftime("%d/%m/%Y"))
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('tab', 4)
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('tab', 4)
    pyautogui.press('enter')
    time.sleep(10)
   
 
# Fechar a conexão com o banco de dados
conn.close()