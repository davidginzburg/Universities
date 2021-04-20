import pandas as pd

def main():
    """
    This script will generate the empty universities_data.csv file
    """
    universities_data = pd.DataFrame(columns=['alpha_two_code', 'country', 'web_pages', 'domains', 'name', 'state_province'])
    universities_data.to_csv('universities_data.csv', encoding = 'utf-8-sig', index = False)

if __name__ == '__main__':
    main()