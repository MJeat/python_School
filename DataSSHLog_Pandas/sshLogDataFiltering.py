import pandas as pd
# Dataframe = df


# 1. Load the CSV file into a DataFrame
df = pd.read_csv("ssh_logs_processed.csv")

# This function is the entry point of the script
def main():
        '''2. Display the basic information about the DataFrame and understanding its structure'''
        display_basic_info() 

        '''3. Find Top 10 Most Frequent IP Addresses'''
        find_top_ips()

        '''4. Find Top 10 Most Frequent Users'''
        find_top_users()

        ''' 5. Find Top 15 Most Attacked Countries'''
        find_top_countries()

        ''' 6. Remove Duplicates IPs Per Country'''
        #remove_duplicates_ips()

def display_basic_info():
    # This function displays basic information about the DataFrame
    print("===Data Set Overview===")
    print(f"\nData Set Information: {len(df)} lines")  # The Number of Logs
    print("Printing The First 3 Info To Get an Idea:")
    print(df.head(3))  # Display the first 3 rows of the DataFrame
    print("\nData Set Information:")
    print(df.info())  # Information about the DataFrame

def find_top_ips():
    print("\n" + "="*39)
    print("===Top 10 Most Frequent IP Addresses===\n")
    top_ips = df["IP"].value_counts().head(10)
    top_ips_df = top_ips.reset_index()
    top_ips_df.columns = ['IP', 'Attempts']  # Rename the columns
    print(top_ips_df.to_string(index=True))  # Print without pandas index

def find_top_users():
    print("\n" + "="*34)
    print("===Top 10 Most Common USERNAMES===\n")
    top_usrs = df["Username"].value_counts().head(10)
    top_usrs_df = top_usrs.reset_index()
    top_usrs_df.columns = ['Username', 'Attempts']  # Rename the columns
    print(top_usrs_df.to_string(index=True))  # Print without pandas index

    
    print("\n===Top 10 Most Common PASSWORDs===\n")
    top_passwd = df["Password"].value_counts().head(10)
    top_passwd_df = top_passwd.reset_index()
    top_passwd_df.columns = ['Password', 'Attempts']  # Rename the columns
    print(top_passwd_df.to_string(index=False))  # Print without pandas index

def find_top_countries():
    print("\n" + "="*36)
    print("===TOP 15 MOST ATTACKED COUNTRIES===\n")
    top_countries = df["Country"].value_counts().head(15)
    top_countries_df = top_countries.reset_index()
    top_countries_df.columns = ['Country', 'Attempts']  # Rename the columns
    print(top_countries_df.to_string(index=True))  # Print without pandas index

def remove_duplicates_ips():
   print("\n" + "="*40)
   print("===REMOVING DUPLICATE IPS PER COUNTRY===\n")
   unique_ips_per_country = df.groupby('Country')['IP'].nunique().sort_values(ascending=False)
   unique_ips_per_country_df = unique_ips_per_country.reset_index()
   unique_ips_per_country_df.columns = ['Country', 'Unique_IPs']  # Rename the columns
   print(unique_ips_per_country_df.to_string(index=True))  # Print with pandas index

'''
The difference between find_top_countries and remove_ips_countries functions is that the former counts the total number of login attempts from each country, 
while the latter counts the number of unique IP addresses from each country. This distinction helps to understand not only where the most login attempts are coming from but also how many different sources (IP addresses) are involved in those attempts.

In simple terms:
- find_top_countries: Tells you which countries are making the most login attempts overall.
- remove_ips_countries: Tells you how many DIFFERENT (not the same or duplicates) IP addresses from each country are making those attempts.

'''

# Run the main function
main()