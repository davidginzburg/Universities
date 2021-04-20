from universities.get_jsons import Get_universities
import pandas as pd

def main():
    """
    This script will get all the universities data from the given url using the universities package,
    and will store all the unique universities into a csv file.
    This script will run once a day and update the csv file with the new unique universities.
    """

    #get the csv file into a data-frame
    universities_df = pd.read_csv('universities_data.csv', encoding = 'utf-8-sig')
    universities_names_list = universities_df['name'].tolist()

    #get list of university objects
    url = 'http://universities.hipolabs.com/search?country=Israel'
    api_universities = Get_universities(url)
    list_of_universities = api_universities.get_universities_info()

    #to see if we got new entities or not for exporting to csv later..
    is_new_entities = False

    for university in list_of_universities:
        if university.name not in universities_names_list:
            is_new_entities = True
            universities_df= universities_df.append(pd.DataFrame({
                'alpha_two_code': [university.alpha_two_code], 
                'country': [university.country],
                'web_pages': [str(university.web_pages)],
                'domains': [str(university.domains)],
                'name': [university.name],
                'state_province':[str(university.state_province)]}) , ignore_index = True)

    #export back to csv  if true
    if is_new_entities:         
        print('we got new entities!')                                     
        universities_df.to_csv('universities_data.csv', encoding = 'utf-8-sig', index = False)
    else:print('no new universities for now!')

if __name__ == '__main__':
    main()



