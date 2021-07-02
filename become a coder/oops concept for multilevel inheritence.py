class Telephone:
    def __init__(self):
        print("calls")
class Moblie(Telephone):
    def __init__(self):
        super().__init__()
        print("SMS,Wireless,basic games")

class SmartMoblie(Moblie):
    def __init__(self):
        super().__init__()
        print("Videos, Camera, Games, Movies.. sooo")


m1=SmartMoblie()

    
