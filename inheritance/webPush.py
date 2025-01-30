class WebPush:
    def __init__(self, platform, optin:bool, gFrequencyCapping, startDate, endDate, language, pushType):
        self.platform = platform
        self.optin = optin
        self.gFrequencyCapping = gFrequencyCapping
        self.startDate = startDate
        self.endDate = endDate
        self.language = language
        self.pushType = pushType

    def sendPush(self):
        print(self.pushType + " Gönderildi",end="\n\n")




class TriggerPush(WebPush):

    def __init__(self, platform, optin:bool, gFrequencyCapping, startDate, endDate, language, pushType,triggerPage:str):
        super().__init__(platform, optin, gFrequencyCapping, startDate, endDate, language, self.__class__.__name__)
        self.triggerPage=triggerPage
        

class BulkPush(WebPush):

    def __init__(self, platform, optin:bool, gFrequencyCapping, startDate, endDate, language, pushType,sendDate:int):
        super().__init__(platform, optin, gFrequencyCapping, startDate, endDate, language, self.__class__.__name__)
        self.sendDate=sendDate

class SegmentPush(WebPush):

    def __init__(self, platform, optin:bool, gFrequencyCapping, startDate, endDate, language, pushType,segmentName:str):
        super().__init__(platform, optin, gFrequencyCapping, startDate, endDate, language, self.__class__.__name__)
        self.segmentName=segmentName

class PriceAlertPush(WebPush):

    def __init__(self, platform, optin:bool, gFrequencyCapping, startDate, endDate, language, pushType, priceInfo:int,discountRate:float):
        super().__init__(platform, optin, gFrequencyCapping, startDate, endDate, language, self.__class__.__name__)
        self.priceInfo=priceInfo
        self.discountRate=discountRate

    def discountedPrice(self):
        response = (self.priceInfo/100) * (100-self.discountRate)
        return response
        

class InstockPush(WebPush):

    def __init__(self, platform, optin:bool, gFrequencyCapping, startDate, endDate, language, pushType,stockInfo:bool):
        super().__init__(platform, optin, gFrequencyCapping, startDate, endDate, language, self.__class__.__name__)
        self.stockInfo = stockInfo
        
    def stockUpdate(self):
        self.stockInfo = not self.stockInfo
        return self.stockInfo


wPush1 = WebPush(platform="Chrome", optin=True, gFrequencyCapping=3, startDate="2024-01-01", endDate="2025-02-12", language="tr", pushType="Bulk-Push")

inStockPush = InstockPush(platform=wPush1.platform, optin=wPush1.optin, gFrequencyCapping=wPush1.gFrequencyCapping, startDate=wPush1.startDate, endDate=wPush1.endDate, language=wPush1.language, pushType=wPush1.pushType,stockInfo=False)
inStockPush.sendPush()
print(inStockPush.stockUpdate(),end="\n\n")

priceAlertPush = PriceAlertPush(platform=wPush1.platform, optin=wPush1.optin, gFrequencyCapping=wPush1.gFrequencyCapping, startDate=wPush1.startDate, endDate=wPush1.endDate, language=wPush1.language, pushType=wPush1.pushType,priceInfo=100,discountRate = 25)
priceAlertPush.sendPush()
print(priceAlertPush.discountedPrice(),end="\n\n")

segmentPush = SegmentPush(platform=wPush1.platform, optin=wPush1.optin, gFrequencyCapping=wPush1.gFrequencyCapping, startDate=wPush1.startDate, endDate=wPush1.endDate, language=wPush1.language, pushType=wPush1.pushType,segmentName="kullanıcı bazlı")
segmentPush.sendPush()

bulkPush = BulkPush(platform=wPush1.platform, optin=wPush1.optin, gFrequencyCapping=wPush1.gFrequencyCapping, startDate=wPush1.startDate, endDate=wPush1.endDate, language=wPush1.language, pushType=wPush1.pushType,sendDate=1)
bulkPush.sendPush()

triggerPush = TriggerPush(platform=wPush1.platform, optin=wPush1.optin, gFrequencyCapping=wPush1.gFrequencyCapping, startDate=wPush1.startDate, endDate=wPush1.endDate, language=wPush1.language, pushType=wPush1.pushType,triggerPage="cart")
triggerPush.sendPush()



