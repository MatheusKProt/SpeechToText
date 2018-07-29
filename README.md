# SpeechToText  
  
Este bot para telegram tem a função principal de transformar os seus áudios em texto utilizando a API de Serviços Cognitivos da Azure, plataforma de cloud da Microsoft.  
  
## Configuração  
  
Primeiramente, você deverá obter as respectivas chaves de acesso aos serviços cognitivos seguindo os passos dos tutoriais abaixo. Após ter todas as chaves, você deverá editar o arquivo [main](https://github.com/MatheusKProt/SpeechToText/blob/master/main.py) e adicionar a chave gerada pelo serviço da microsoft no campo `BING_TOKEN` e a chave gerada pelo telegram no campo `TELEGRAM_TOKEN`.

## Demonstação
![](https://i.imgur.com/PRJ6fmQl.jpg)

## Criar um recurso de Fala no Azure

Para adicionar um recurso do serviço de Fala à sua conta do Azure, execute estas etapas.

1. Entre no [portal do Azure](https://ms.portal.azure.com/) usando sua conta Microsoft.
2. Clique em **Criar um recurso** (o ícone **+** verde) na parte superior esquerda do portal.![](https://i.imgur.com/aj5hehJ.png)
3. Na janela Nova, procure por **Bing Speech**.![enter image description here](https://i.imgur.com/dafkRqn.png)
4. Nos resultados da pesquisa, clique em "Bing Speech".
5. Clique no botão **Criar** na parte inferior do painel do serviço de Fala.![enter image description here](https://i.imgur.com/HqO0tQy.png)
6. No painel Criar, insira:
	-  Um nome para o novo recurso.  O nome ajuda a distinguir entre várias assinaturas do mesmo serviço.
	-  Escolha a assinatura do Azure a qual o novo recurso está associado para determinar como os valores serão cobrados.
	-   Escolha o tipo de preços, F0 (assinatura gratuita limitada) ou S0 (assinatura padrão).  Clique em  **Exibir detalhes de preços completos**  para saber mais sobre preço e cotas de uso de cada tipo.
	-   Crie um novo grupo de recursos para esta assinatura de Fala ou a atribua a um grupo existente.  Os grupos de recurso ajudam você a manter suas diversas assinaturas do Azure organizadas.
	-   Escolha a região onde o recurso será usado.
	-   Clicar em **Criar.**<br>
![enter image description here](https://i.imgur.com/gVLgGgA.png)<br>
Talvez demore um pouco para criar e implantar o novo recurso de Fala.  O painel Início Rápido aparece com informações sobre o novo recurso.![enter image description here](https://i.imgur.com/p2CB756.png)
7. Clique no link  **Keys**  na Etapa 1 no painel Início Rápido para exibir suas chaves de assinatura.  Cada assinatura tem duas chaves; você pode usar uma delas em seu aplicativo.  Clique no botão ao lado de cada chave para copiá-la na área de transferência e colá-la no campo `BING_TOKEN`.

## Criar um bot no Telegram

1. Entre no [BotFather](https://telegram.me/botfather) usando o Telegram.![enter image description here](https://docs.microsoft.com/pt-br/azure/bot-service/media/channels/tg-stepvisitbotfather.png?view=azure-bot-service-3.0)
2. Crie um novo bot usando o comando `/newbot`.![enter image description here](https://docs.microsoft.com/pt-br/azure/bot-service/media/channels/tg-stepnewbot.png?view=azure-bot-service-3.0)
3. De um nome ao seu bot.![enter image description here](https://docs.microsoft.com/pt-br/azure/bot-service/media/channels/tg-stepnamebot.png?view=azure-bot-service-3.0)
4. De um username ao seu bot.![enter image description here](https://docs.microsoft.com/pt-br/azure/bot-service/media/channels/tg-stepusername.png?view=azure-bot-service-3.0)
5. Copie na área de transferência e cole no campo `TELEGRAM_TOKEN`.![enter image description here](https://docs.microsoft.com/pt-br/azure/bot-service/media/channels/tg-stepbotcreated.png?view=azure-bot-service-3.0)
