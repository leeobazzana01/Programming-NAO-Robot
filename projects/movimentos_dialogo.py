#SENTAR 

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        self.postureService = self.session().service("ALRobotPosture")
        pass

    def onUnload(self):
        self.postureService.stopMove()

    def onInput_onStart(self):
        result = self.postureService.goToPosture(self.getParameter("Name"), self.getParameter("Speed (%)")/100.)
        if(result):
            self.success()
        else:
            self.failure()
        pass

    def onInput_onStop(self):
        self.onUnload() #~ it is recommanded to call onUnload of this box in a onStop method, as the code written in onUnload is used to stop the box as well
        pass



#TOQUE NA CABEÇA
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        #~ puts code for box initialization here
        pass

    def onUnload(self):
        #~ puts code for box cleanup here
        pass

    def onInput_onStart(self, p):
        if(p > 0):
            self.onStopped() #~ activate output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #~ it is usually a good idea to call onUnload of this box in a onStop method, as the code written in onUnload is used to finish the working of the box as well
        pass

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        #~ puts code for box initialization here
        pass

    def onUnload(self):
        #~ puts code for box cleanup here
        pass

    def onInput_onStart(self, p):
        if(p > 0):
            self.onStopped() #~ activate output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #~ it is usually a good idea to call onUnload of this box in a onStop method, as the code written in onUnload is used to finish the working of the box as well
        pass

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        #~ puts code for box initialization here
        pass

    def onUnload(self):
        #~ puts code for box cleanup here
        pass

    def onInput_onStart(self, p):
        if(p > 0):
            self.onStopped() #~ activate output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #~ it is usually a good idea to call onUnload of this box in a onStop method, as the code written in onUnload is used to finish the working of the box as well
        pass

# GO TO POSTURE (LEVANTAR)

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        self.nTries = 0
        self.postureService = self.session().service("ALRobotPosture")
        pass

    def onUnload(self):
        self.postureService.stopMove()

    def onInput_onStart(self):
        if(self.nTries != self.getParameter("Maximum of tries")):
            self.nTries = self.getParameter("Maximum of tries")
            self.postureService.setMaxTryNumber(self.nTries)

        result = self.postureService.goToPosture(self.getParameter("Name"), self.getParameter("Speed (%)")/100.)
        if(result):
            self.success()
        else:
            self.failure()
        pass

    def onInput_onStop(self):
        self.onUnload() #~ it is recommanded to call onUnload of this box in a onStop method, as the code written in onUnload is used to stop the box as well
        pass

#HELLO 
class MyClass(GeneratedClass):
  def __init__(self):
    GeneratedClass.__init__(self, False)

  def onLoad(self):
    self.bIsRunning = False;
    self.leds = ALProxy("ALLeds")

  def onUnload(self):
    self.onInput_onStop(); # will stop current loop execution

  def onInput_onStart(self):
    #self.logger.info( self.getName() + ": start - begin" );

    if( self.bIsRunning ):
      #print( self.getName() + ": already started => nothing" );
      return;

    self.bIsRunning = True;
    self.bMustStop = False;

    rDuration = 0.2;
    self.leds.post.fadeRGB( "FaceLedsTop", 0xff00ff, rDuration );
    self.leds.post.fadeRGB( "FaceLedsInternal", 0xff00ff, rDuration );
    self.leds.post.fadeRGB( "FaceLedsBottom", 0xff00ff, rDuration );
    self.leds.fadeRGB( "FaceLedsExternal", 0xff00ff, rDuration );

    while( not self.bMustStop ):
      rTime = 0.1;
      self.leds.post.fadeRGB( "FaceLedsTop", 0xffffff, rTime );
      self.leds.fadeRGB( "FaceLedsBottom", 0xffffff, rTime );
      if( self.bMustStop ):
        break;
      rTime = 0.3
      self.leds.post.fadeRGB( "FaceLedsTop", 0xff00ff, rTime );
      self.leds.fadeRGB( "FaceLedsBottom", 0xff00ff, rTime );


    # end while
    self.bIsRunning = False;
    self.onStopped();

  def onInput_onStop(self):
    self.bMustStop = True; # will stop current loop execution

#LOCALIZED TEXT (SELECIONAR LINGUAGEM)
# /!\ Generated content. Do not edit!
class MyClass(GeneratedClass):
    def __init__(self):
        try: # disable autoBind
            GeneratedClass.__init__(self, False)
        except TypeError: # if NAOqi < 1.14
            GeneratedClass.__init__( self )

        self.sentences = {
            "Chinese" : " 你喜欢吃巧克力吗？ ",
            "English" : " Hello. I am Jarivs, an Artificial Intelligence Powered robot inspired on Tony\'s Startk creation. Can i help you sir? ",
            "French" : " Aimes-tu le chocolat ? ",
            "German" : " Mögen Sie Schokolade? ",
            "Italian" : " Ti piace il cioccolato? ",
            "Japanese" : " チョコレートが好きですか ",
            "Korean" : " 당신은 초콜렛을 좋아합니까? ",
            "Portuguese" : " Gostas de chocolate? ",
            "Brazilian" : " Boa tarde. Eu sou o Jarvis, um robô Integrado com Inteligência Artificial inspirado no filme do homem de Ferro. Estou pronto para responder a qualquer pergunta. . Posso ajudar você?  ",
            "Spanish" : " ¿Te gusta el chocolate? ",
            "Arabic" : " هل تحب الشوكولاته؟ ",
            "Polish" : " Lubisz czekoladę? ",
            "Czech" : " Máš rád čokoládu? ",
            "Dutch" : " Hou je van chocolade? ",
            "Danish" : " Kan du lide chokolade? ",
            "Finnish" : " Pidätkö suklaasta? ",
            "Swedish" : " Gillar du choklad? ",
            "Russian" : " Вы любите шоколад? ",
            "Turkish" : " Çikolata sever misin? ",
            "MandarinTaiwan" : " 你喜歡吃巧克力嗎？ ",
        }

    def onLoad(self):
        self.tts = self.session().service("ALTextToSpeech")

    def onInput_onStart(self):
        sDefaultLang = self.tts.getLanguage()
        self.onStopped(self.sentences[sDefaultLang])

# SAY TEXT (PRA FALAR)
import time

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        self.tts = self.session().service('ALTextToSpeech')
        self.ttsStop = self.session().service('ALTextToSpeech') #Create another service as wait is blocking if audioout is remote
        self.bIsRunning = False
        self.ids = []

    def onUnload(self):
        for id in self.ids:
            try:
                self.ttsStop.stop(id)
            except:
                pass
        while( self.bIsRunning ):
            time.sleep( 0.2 )

    def onInput_onStart(self, p):
        self.bIsRunning = True
        try:
            sentence = "\RSPD="+ str( self.getParameter("Speed (%)") ) + "\ "
            sentence += "\VCT="+ str( self.getParameter("Voice shaping (%)") ) + "\ "
            sentence += str(p)
            sentence +=  "\RST\ "
            id = self.tts.pCall("say",str(sentence))
            self.ids.append(id)
            self.tts.wait(id)
        finally:
            try:
                self.ids.remove(id)
            except:
                pass
            if( self.ids == [] ):
                self.onStopped() # activate output of the box
                self.bIsRunning = False

    def onInput_onStop(self):
        self.onUnload()
    
# DELAY 
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        self.delayed = []

    def onUnload(self):
        self.cancelDelays()

    def cancelDelays(self):
        cancel_list = list(self.delayed)
        for d in cancel_list:
            d.cancel()

    def cleanDelay(self, fut, fut_ref):
        self.delayed.remove(fut)

    def triggerOutput(self):
        self.timerOutput()

    def onInput_onStart(self):
        import qi
        import functools
        delay_future = qi.async(self.triggerOutput, delay=int(self.getParameter("Timeout (s)") * 1000 * 1000))
        # keep the async operation in an array for cancel
        # and remove it when it is finished in the callback
        self.delayed.append(delay_future)
        bound_clean = functools.partial(self.cleanDelay, delay_future)
        delay_future.addCallback(bound_clean)

    def onInput_onStop(self):
        if self.getParameter("Trigger timerOutput if cancelled") and self.delayed:
            self.timerOutput()
        self.onUnload()

# MAIS UM TATICLE HEAD
#
#
#
#
#

#SET LANGUAGE RECOGNITION
# /!\ Generated content. Do not edit!
# -*- coding: utf-8 -*-
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)
        self.setTTS = False
        self.setASR = True
        self.setDialog = False
        self.language = "English"

    def getService(self, serviceName, humainName):
        service = None
        try:
            service = self.session().service(serviceName)
        except:
            self.logger.warn("%s is not available, language setting cannot be applied to %s." % (serviceName, humainName))
        return service

    def onLoad(self):
        if self.setTTS:
            self.tts = self.getService("ALTextToSpeech", "speech")
        if self.setASR:
            self.asr = self.getService("ALSpeechRecognition", "recognition")
        if self.setDialog:
            self.dialog = self.getService("ALDialog", "dialog")

    def setLanguage(self, service, serviceName):
        try:
            if service is None:
                return False
            service.setLanguage(self.language)
            return True
        except Exception as e:
            self.logger.error("Could not set language %s for %s: %s" % (self.language, serviceName, e))
            return False

    def onInput_onSet(self):
        res = True
        if self.setTTS:
            res = self.setLanguage(self.tts, "ALTextToSpeech") and res
        if self.setASR:
            res = self.setLanguage(self.asr, "ALSpeechRecognition") and res
        if self.setDialog:
            res = self.setLanguage(self.dialog, "ALDialog") and res

        if res:
            self.onReady()
        else:
            self.logger.error("Language %s could not be set for one or more services." % self.language)
            self.onError()

# SPEECH RECOGNITION


class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        try:
            self.asr = self.session().service("ALSpeechRecognition")
        except Exception as e:
            self.asr = None
            self.logger.error(e)
        self.memory = self.session().service("ALMemory")
        from threading import Lock
        self.bIsRunning = False
        self.mutex = Lock()
        self.hasPushed = False
        self.hasSubscribed = False
        self.BIND_PYTHON(self.getName(), "onWordRecognized")

    def onUnload(self):
        from threading import Lock
        self.mutex.acquire()
        try:
            if (self.bIsRunning):
                if (self.hasSubscribed):
                    self.memory.unsubscribeToEvent("WordRecognized", self.getName())
                if (self.hasPushed and self.asr):
                    self.asr.popContexts()
        except RuntimeError, e:
            self.mutex.release()
            raise e
        self.bIsRunning = False;
        self.mutex.release()

    def onInput_onStart(self):
        from threading import Lock
        self.mutex.acquire()
        if(self.bIsRunning):
            self.mutex.release()
            return
        self.bIsRunning = True
        try:
            if self.asr:
                self.asr.pushContexts()
            self.hasPushed = True
            if self.asr:
                self.asr.setVocabulary( self.getParameter("Word list").split(';'), self.getParameter("Enable word spotting") )
            self.memory.subscribeToEvent("WordRecognized", self.getName(), "onWordRecognized")
            self.hasSubscribed = True
        except RuntimeError, e:
            self.mutex.release()
            self.onUnload()
            raise e
        self.mutex.release()

    def onInput_onStop(self):
        if( self.bIsRunning ):
            self.onUnload()
            self.onStopped()

    def onWordRecognized(self, key, value, message):
        if(len(value) > 1 and value[1] >= self.getParameter("Confidence threshold (%)")/100.):
            self.wordRecognized(value[0]) #~ activate output of the box
        else:
            self.onNothing()


# SWITCH  CASE 
# /!\ Generated content. Do not edit!
class MyClass(GeneratedClass):
    def __init__(self):
        try: # disable autoBind
          GeneratedClass.__init__(self, False)
        except TypeError: # if NAOqi < 1.14
          GeneratedClass.__init__( self )

    def onInput_onStart(self, p):
        p = self.typeConversion(p)
        if(p == self.typeConversion("yes")):
            self.output_1(p)
        elif(p == self.typeConversion("no")):
            self.output_2(p)
        else:
            self.onDefault()

    def typeConversion(self, p):
        try:
            p = float(p)
            pint = int(p)
            if( p == pint ):
                p = pint
        except:
            p = str(p)
        return p


# #LOCALIZED TEXT PARA ENTENDER INGLÊS 
# /!\ Generated content. Do not edit!
class MyClass(GeneratedClass):
    def __init__(self):
        try: # disable autoBind
            GeneratedClass.__init__(self, False)
        except TypeError: # if NAOqi < 1.14
            GeneratedClass.__init__( self )

        self.sentences = {
            "Chinese" : " 你喜欢吃巧克力吗？ ",
            "English" : " Understood. I am here in case you need information ",
            "French" : " Aimes-tu le chocolat ? ",
            "German" : " Mögen Sie Schokolade? ",
            "Italian" : " Ti piace il cioccolato? ",
            "Japanese" : " チョコレートが好きですか ",
            "Korean" : " 당신은 초콜렛을 좋아합니까? ",
            "Portuguese" : " Gostas de chocolate? ",
            "Brazilian" : " Boa tarde. Eu sou o Jarvis, um robô Integrado com Inteligência Artificial inspirado no filme do homem de Ferro. Estou pronto para responder a qualquer pergunta. . Posso ajudar você?  ",
            "Spanish" : " ¿Te gusta el chocolate? ",
            "Arabic" : " هل تحب الشوكولاته؟ ",
            "Polish" : " Lubisz czekoladę? ",
            "Czech" : " Máš rád čokoládu? ",
            "Dutch" : " Hou je van chocolade? ",
            "Danish" : " Kan du lide chokolade? ",
            "Finnish" : " Pidätkö suklaasta? ",
            "Swedish" : " Gillar du choklad? ",
            "Russian" : " Вы любите шоколад? ",
            "Turkish" : " Çikolata sever misin? ",
            "MandarinTaiwan" : " 你喜歡吃巧克力嗎？ ",
        }

    def onLoad(self):
        self.tts = self.session().service("ALTextToSpeech")

    def onInput_onStart(self):
        sDefaultLang = self.tts.getLanguage()
        self.onStopped(self.sentences[sDefaultLang])


#SAI TEXT 

import time

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        self.tts = self.session().service('ALTextToSpeech')
        self.ttsStop = self.session().service('ALTextToSpeech') #Create another service as wait is blocking if audioout is remote
        self.bIsRunning = False
        self.ids = []

    def onUnload(self):
        for id in self.ids:
            try:
                self.ttsStop.stop(id)
            except:
                pass
        while( self.bIsRunning ):
            time.sleep( 0.2 )

    def onInput_onStart(self, p):
        self.bIsRunning = True
        try:
            sentence = "\RSPD="+ str( self.getParameter("Speed (%)") ) + "\ "
            sentence += "\VCT="+ str( self.getParameter("Voice shaping (%)") ) + "\ "
            sentence += str(p)
            sentence +=  "\RST\ "
            id = self.tts.pCall("say",str(sentence))
            self.ids.append(id)
            self.tts.wait(id)
        finally:
            try:
                self.ids.remove(id)
            except:
                pass
            if( self.ids == [] ):
                self.onStopped() # activate output of the box
                self.bIsRunning = False

    def onInput_onStop(self):
        self.onUnload()

# OPÇÃO 1 SE RECONHECER E OUVIR NO
# GO TO SIT DOWN POSIÇÃO 
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        self.postureService = self.session().service("ALRobotPosture")
        pass

    def onUnload(self):
        self.postureService.stopMove()

    def onInput_onStart(self):
        result = self.postureService.goToPosture(self.getParameter("Name"), self.getParameter("Speed (%)")/100.)
        if(result):
            self.success()
        else:
            self.failure()
        pass

    def onInput_onStop(self):
        self.onUnload() #~ it is recommanded to call onUnload of this box in a onStop method, as the code written in onUnload is used to stop the box as well
        pass

# continuar para as ações de PENSAR E FALAR AO MESMO TEMPO, PRA RESPONDER
#COLOCAR NUM LOOP PARA ENQUANTO ESTIVER FALANDO, FAZER ESSES MOVIMENTOS 
