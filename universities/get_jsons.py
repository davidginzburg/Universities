class Get_universities:
    def __init__(self,url):
        self.url = url
        
    def get_universities_info(self):
        """
        This func reach to the given url and returns list of university objects

        Recives: nothing
        Returns: list, university object
        """
        #built-in packages
        import json         
        #downloaded packages
        import requests
        #built packages
        from universities.University import University
        response = requests.get(self.url, headers={'Content-Type':'application/json'})
        json_data = json.loads(response.text)
        universities_list = []        
        for jsonn in json_data:
            universities_list.append(University(*[value for key,value in jsonn.items()])) 
        return universities_list