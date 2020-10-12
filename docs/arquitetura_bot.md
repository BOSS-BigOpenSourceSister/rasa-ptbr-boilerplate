# Arquitetura do Rasa

No boilerplate são usadas diversas tecnologias que interagem entre si para obter um melhor resultado. Veja a arquitetura implementada:

![](https://user-images.githubusercontent.com/8556291/57933140-d8d66b80-7892-11e9-8d58-a7eda60b099b.png)

O usuário interage com a Boilerplate via Telegram, que manda as mensagens para o Rasa NLU através de
conectores, onde ele identifica a *intent*, e responde pelo Rasa Core, de acordo com as *stories* e *actions*. 

As *models* utilizadas para a conversação foram geradas pelo módulo *trainer* e depois transferidas para o bot, estes
modelos podem ser versionados e evoluídos entre bots.  
Os notebooks avaliam o funcionamento de acordo com o formato das *intents* e *stories*.

O elasticsearch coleta os dados da conversa e armazena para a análise feita pelo kibana, que gera gráficos para
avaliação das conversas dos usuários e do boilerplate.

## Bot

Este script foi configurado para construir as imagens genéricas necessárias para execução deste ambiente.

Caso seu projeto utilize este boilerplate e vá realizar uma integração contínua ou similar, é interessante criar um repositório para as imagens e substitua os nomes das imagens "lappis/bot", e "lappis/botrequirements" pelas suas respectivas novas imagens, por exemplo "<organização>/bot" em repositório público. 