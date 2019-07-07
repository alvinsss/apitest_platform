from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(1)
    def stream(self):
        # self.client.post("/is/api/v1/stream",
        #                  {"channel": "career", "city": "", "timestamp": "1558597097107", "pid": "demo", "pver": "1",
        #                   "signature": "7f1cd7b576c6c5dfe95dbc15f2ded442", "nonce": "884534810278962707",
        #                   "uuid": "7d9a9512faed32229ace24e30cc2969a", "request_num": "0", "action": "19",
        #                   "lbs": "%7B%7D", "isfirst": "1", "reg": "CN", "app_vname": "1.4.3",
        #                   "imei": "7b7e8fe7842c3d7f", "allow_stick": "0", "type": "1", "imsi": "", "isp": "0",
        #                   "gimei": "867200020646954", "oimei": "867200020646954",
        #                   "bid": "50d725b3aa31a704bf49464101cf6dd9", "net": "WIFI", "os": "Android", "app_vcode": "20",
        #                   "full_screen": "1", "openudid": "7b7e8fe7842c3d7f", "sdk_version": "3.0",
        #                   "resolution": "1080x1920", "device_brand": "Lenovo", "os_version": "6.0", "language": "zh-CN",
        #                   "model": "LenovoK50-t5", "osSDK": "23", "scene": "0", "dt": "Lenovo%20K50-t5" })

        par = "http://47.105.67.21/is/api/v1/stream?&channel=career&city=&timestamp=1558597097107&pid=demo&pver=1&signature=7f1cd7b576c6c5dfe95dbc15f2ded442&nonce=884534810278962707&uuid=7d9a9512faed32229ace24e30cc2969a&request_num=0&action=19&lbs=%7B%7D&isfirst=1&reg=CN&app_vname=1.4.3&imei=7b7e8fe7842c3d7f&allow_stick=0&type=1&imsi=&isp=0&gimei=867200020646954&oimei=867200020646954&bid=50d725b3aa31a704bf49464101cf6dd9&net=WIFI&os=Android&app_vcode=20&full_screen=1&openudid=7b7e8fe7842c3d7f&sdk_version=3.0&resolution=1080x1920&device_brand=Lenovo&os_version=6.0&language=zh-CN&model=LenovoK50-t5&osSDK=23&scene=0&dt=Lenovo%20K50-t5"
        self.client

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000