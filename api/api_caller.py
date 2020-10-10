import requests


class ApiCaller:

    @staticmethod
    def execute(url, method, params, headers, data=None, proxies=None, retries=None, redirect=False, content='text'):
        try:
            args = {
                "url": url,
                "allow_redirects": redirect
            }
            if params:
                args.update({"params": params})
            if headers:
                args.update({"headers": headers})
            if data:
                args.update({"data": data})
            if proxies:
                args.update({"proxies": proxies})
            response=requests.get(url)
        except Exception as e:
            print(
                "An error occured when callind the remote service : {} on url : {} \n"
                " Error : ".format(str(method), url, str(e)))
            return None



        print(
                    "status code {} of called service : {} on url : {} and data {} \n "
                    "Reason : {}".format(response.status_code, str(method), url, data, response.reason))


        return response.text