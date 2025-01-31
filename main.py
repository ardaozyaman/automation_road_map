from classes.student import Person
from functions.questions import Questions as Ques
from inheritance.webPush import *


def runFunctions():
    ques = Ques()
    
    ques.q1Func(min=2, max=15, div=3)

    ques.q2Func(num=124)

    ques.examCalculate(vize1=30, vize2=30, final=30)


def runClasses():
    p = Person("irdo", "özyakup", "10", "tr", "kr")

    p.addAbility("ağzıyla araba sesi çıkarmak")

    p.printAllPersonData()


def runWebpushes():
    wPush1 = WebPush(
        platform="Chrome",
        optin=True,
        gFrequencyCapping=3,
        startDate="2024-01-01",
        endDate="2025-02-12",
        language="tr",
        pushType="Bulk-Push",
    )

    inStockPush = InstockPush(
        platform=wPush1.platform,
        optin=wPush1.optin,
        gFrequencyCapping=wPush1.gFrequencyCapping,
        startDate=wPush1.startDate,
        endDate=wPush1.endDate,
        language=wPush1.language,
        pushType=wPush1.pushType,
        stockInfo=False,
    )
    inStockPush.sendPush()
    print(inStockPush.stockUpdate(), end="\n\n")

    priceAlertPush = PriceAlertPush(
        platform=wPush1.platform,
        optin=wPush1.optin,
        gFrequencyCapping=wPush1.gFrequencyCapping,
        startDate=wPush1.startDate,
        endDate=wPush1.endDate,
        language=wPush1.language,
        pushType=wPush1.pushType,
        priceInfo=100,
        discountRate=25,
    )
    priceAlertPush.sendPush()
    print(priceAlertPush.discountedPrice(), end="\n\n")

    segmentPush = SegmentPush(
        platform=wPush1.platform,
        optin=wPush1.optin,
        gFrequencyCapping=wPush1.gFrequencyCapping,
        startDate=wPush1.startDate,
        endDate=wPush1.endDate,
        language=wPush1.language,
        pushType=wPush1.pushType,
        segmentName="kullanıcı bazlı",
    )
    segmentPush.sendPush()

    bulkPush = BulkPush(
        platform=wPush1.platform,
        optin=wPush1.optin,
        gFrequencyCapping=wPush1.gFrequencyCapping,
        startDate=wPush1.startDate,
        endDate=wPush1.endDate,
        language=wPush1.language,
        pushType=wPush1.pushType,
        sendDate=1,
    )
    bulkPush.sendPush()

    triggerPush = TriggerPush(
        platform=wPush1.platform,
        optin=wPush1.optin,
        gFrequencyCapping=wPush1.gFrequencyCapping,
        startDate=wPush1.startDate,
        endDate=wPush1.endDate,
        language=wPush1.language,
        pushType=wPush1.pushType,
        triggerPage="cart",
    )
    triggerPush.sendPush()
