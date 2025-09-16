from locust import HttpUser, task, between

class DigiKalaUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_product(self):
        self.client.get(
            "https://api.digikala.com/v2/product/17833952/?_rch=db340a7f7c4f",
            headers={
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
                'origin': 'https://www.digikala.com',
                'priority': 'u=1, i',
                'referer': 'https://www.digikala.com/',
                'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
                'x-web-client': 'desktop',
                'x-web-optimize-response': '1'
            },
            cookies={
                'tracker_glob_new': 'bixtmrH',
                '_ga': 'GA1.1.811662629.1753259620',
                'ab_test_experiments': '%5B%22229ea1a233356b114984cf9fa2ecd3ff%22%2C%22db7b11075496e04f0a6ef0d3a02d5264%22%2C%224905b18f64695e6dbfd739d20a4ae2c0%22%2C%22f0fd80107233fa604679779d7e121710%22%2C%2237136fdc21e0b782211ccac8c2d7be63%22%5D',
                'Digikala:General:Location': 'VllOY014RUVOc254OVJxNDA0K1FDQT09%26UWZiUmhHWXJCRFgwZmdVTndLRk5ZV1hxY2ZNdlZvRHpQUlNLSC8xK1d6eE50K20zNEd3UjR2aDZTeTh0amVERm93cHB4R3c1Umd6Q2RVbGRVcEtNMEE9PQ~~',
                'TS01b6ea4d': '01023105911cb911d39c28b8d4e0e220ba09b3b58921526178e7c92e519ff57f7ef444a53e3fb684507e38f8666b94b6309afc402ce78a327a635e367c0f0c9a566dc56f997e051f83142b7cb14b9c3964ff1ca73b',
                '_sp_ses.13cb': '*',
                'tracker_session': '9QOKSJc',
                'TS01c77ebf': '0102310591f90f24e20b9d91f8c9149c4ded41ba742bd8f4bb2c0dbb785569bcb57329ea3913e0f9cb2169757080291c075a4a67f3373024d7011f409d8fca7321dbf99ea1',
                '_ga_QQKVTD5TG8': 'GS2.1.s1758024482$o7$g1$t1758024534$j8$l0$h0',
                '_sp_id.13cb': '0d217210-3f09-40f7-9f3e-1a39eddd7402.1753259619.6.1758025330.1757943942.02bb89d1-578f-4983-bc99-54a1791f32b8.e120a459-f18d-4e6e-8ef0-68d4dbb00c73.3a9994e1-c610-4bfe-98ef-67e4541d3073.1758024481145.47'
            }
        )

