# Programação com Python

## Importando Módulos 

Para tratementos de dados especiais como as bibliotecas **math** e **string**.

A **importação é feita no bloco principal que inicializa quando recebemos um trigger de start**, através do método **onInput_onStart**.

```Python
class MyClass(GeneratedClass):
   def __init__(self):
      #construtor herdado de GeneratedClass
      GeneratedClass.__init__(self)

   def onLoad(self):
      #método de inicialização, para carregar recursos de sistema
      pass

   def onUnload(self):
      #método de limpeza
      pass

   def onInput_onStart(self):
      import math #IMPORTAÇÃO DE BIBLIOTECA MATH
      self.tan = math.tan(p)
      self.onStopped(self.tan)
      pass

   def onInput_onStop(self):
      self.onUnload() #recomendada para realizar a limpeza e encerrar o funcionamento da caixa por completo
      pass
```

## Script Padrão 

Esse é o script padrão que surge em qualquer box de script de Python no Choregrape:

```Python
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        #construtor padrão, vindo da classe pai Generated CLass
    
    def onLoad(self):
        #inicializações que precisam do sistema
        pass

    def onUnload(self):
        #limpeza de strings, caixas de memória, etc
        pass

    def onInput_onStart(self):
        #self.onStopped() #lógica principal ativada quando recebe start
        pass

    def onInput_onStop(self):
        #para quando recebe stop

        self.onUnload() #é recomendado utilizar a caixa de limpeza como está parado
        self.onStopped() #confirma que parou
```

Note que o script acima possui a **classe chamada MyClass**. Essa classe já **possui alguns métodos por padrão** e herda características de **GeneratedClass**.

**GeneratedClass** é uma classe gerada automaticamente com a execução de um comportamento. Ela inclui informações necessárias de entrada (inputs, outputs, parâmetros) que podem ser úteis por você para utilizar no script. 

### Métodos da MyClass padrão:
1. **__init__(self)** é o construtor, passando self como parâmetro e usando o método construtor padrão da **GeneratedClass**

2. **onLoad()** é o método chamado quanto a caixa/comportamento é carregada no sistema. É ideal para inicializar conexões, carregar recursos pesados, configurar variáveis que precisam do sistema já pronto.  

3. **onUnload()** método que faz a limpeza da caixa antes de sair, liberando strings, objetos, fechar conexões abertas, parar threads em execução, etc... É crucial para evital qualquer tipo de **memory leak**.

4. **onInput_onStart** é o método será chamado quando um sinal de entrada onStart é recebido
 

Dado o fato de que **MyClass** herda de **GeneratedClass**, você pode utilizar TODAS AS **FUNÇÕES BUILT-IN** no script.

## Funçções Built In

**1. Inputs**
**2. Output**
**3. Parâmetros**
**4. Timeline**
**5. Carregar e descarregar eventos**
**6. Recursos**
**7. Proxies**
**8. Sistema de Arquivos** 
**9. Logs**
**10. Tratamento de Exceções**


### 1. Inputs

Os métodos que correspondem ao Input de na box devem ser definidos com a seguinte sintaxe: 

**onInput_<input_name>**


## Movimentos Básicos 

### Postura
#### Stand Up (Levantar)

Código em Python: 

```Python

class MyClass(GeneratedClass):
    def __init__(self):
        #construtor, passando como false o auto output, portanto preciso especificar manualmente
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        self.nTries = 0 #atribui como zero o n° inicial de tentativas
        self.postureService = self.session().service("ALRobotPosture") #usa métodos para aplicar postura nos métodos de postura do robô
        pass

    def onUnload(self):
        self.postureService.stopMove() #aplica métodos para parar de mover quando encerrar

    def onInput_onStart(self):

        #lógica para que, se o número de tentativas for diferente do máximo, ele continue tentando
        if(self.nTries != self.getParameter("Maximum of tries")):
            self.nTries = self.getParameter("Maximum of tries")
            self.postureService.setMaxTryNumber(self.nTries)

        result = self.postureService.goToPosture(self.getParameter("Name"), self.getParameter("Speed (%)")/100.)

        #lógica do resultado usando métodos sucess e failure, por isso há duas saídas na box
        if(result):
            self.success()
        else:
            self.failure()
        pass

    def onInput_onStop(self):
        self.onUnload() #método usado para encerrar e parar qualquer movimento quando obtemos sucesso ou falha na tentativa de aplicar postura
        pass
```

#### Sit Down (Sente-se)

```Python
class MyClass(GeneratedClass):
    #construtor
    def __init__(self):
        GeneratedClass.__init__(self, False) #passa o parâmetro false para termos que especificar manualmente o resultado

    #carrega a aplicação de postura da classe GeneratedClass que possui um método "postureService"
    def onLoad(self):
        self.postureService = self.session().service("ALRobotPosture")
        pass

    #método para parar os movimentos após o encerramento
    def onUnload(self):
        self.postureService.stopMove()

    #método iniciado com um input
    def onInput_onStart(self):
        result = self.postureService.goToPosture(self.getParameter("Name"), self.getParameter("Speed (%)")/100.) #passa o nome do método e o parâmetro de velocidade que ele usará para levantar

        if(result): #testando o valor do resultado
            self.success() #usa o método sucess, se for bem sucedido, iremos aplicar a postura
        else: 
            #se tivermos falha, não aplicamos a postura p ficar sentado
            self.failure()
        pass

    #método de encerramento com um input
    def onInput_onStop(self):
        self.onUnload() #recomendado usar para o robô não continuar se movendo 
        pass
```

### Dança e Saudações