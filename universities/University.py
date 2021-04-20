class University:
    def __init__(self, alpha_two_code, country, web_pages, domains, name, state_province):
        """
        alpa_two_code: str
        country: str
        web_pages: list of strings
        domain: list of strings
        name: str
        state_province: str    
        """
        self.alpha_two_code = alpha_two_code
        self.country = country
        self. web_pages = web_pages
        self.domains = domains
        self.name = name
        self.state_province = state_province          
        
    def __str__(self):
#         return str(self.__dict__)
        return """'alpha_two_code' : {},\n'country' : {},\n'web_pages' : {},\n'domains' : {}, \n'name' : {}, \n'state_province' : {}""".format(self.alpha_two_code, self.country, self.web_pages, self.domains, self.name, self.state_province)
        
     