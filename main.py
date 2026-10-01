import pandas as pds

def main():
    
    df = pd.read_csv('tips.csv')
    
    
    print(" First 10 rows of tips.csv ")
    print(df.head(10))

if __name__ == "main":
    main()
