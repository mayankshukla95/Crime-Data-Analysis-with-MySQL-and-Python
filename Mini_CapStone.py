import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

conn = pymysql.connect(
    host='localhost',
    user='root',
    password="95095",
    db='test'
)
query = "select * from crime_data"
df = pd.read_sql(query, conn)

# Let's Know About Are DataFrame
df.info()

"""Please Run Program One-By-One After Commenting Out Another Questions."""


def question1():
    plt.figure(figsize=(10, 5))  # LAT, LON
    sns.scatterplot(x=df['LAT'], y=df['LON'], hue=df['Vict_Sex'])
    plt.title("Geographical Hotspots For Reported Crimes")
    plt.grid(linestyle="-")
    return plt.show()


question1()


def question2():
    def age_group(row):
        if row['Vict_Age'] < 18:
            return "0-17"
        if 18 <= row['Vict_Age'] <= 30:
            return '18-30'
        if 30 < row['Vict_Age'] <= 45:
            return '31-45'
        if 45 < row['Vict_Age'] <= 65:
            return '46-65'
        else:
            return '65+'

    df['Age_Group'] = df.apply(age_group, axis=1)

    yay = df.Age_Group.value_counts()
    yay1 = yay.reset_index().rename(columns={'index': 'unique_values', 0: 'counts'})
    print(yay1)

    plt.figure(figsize=(10, 5))
    sns.barplot(x=yay1['Age_Group'], y=yay1['count'])
    plt.title("Distribution Of Victim Ages In Reported Crimes")
    return plt.show()


#question2()


def question3():
    yay = df.Vict_Sex.value_counts()
    yay1 = yay.reset_index().rename(columns={'index': 'unique_values', 0: 'counts'})
    print(yay1)

    plt.figure(figsize=(10, 5))
    sns.barplot(x=yay1['Vict_Sex'], y=yay1['count'])
    plt.title("Gender-wise Crime Rates of Victims")
    return plt.show()


#question3()


def question4():
    yay = df.Location.value_counts()
    yay1 = yay.reset_index().rename(columns={'index': 'unique_values', 0: 'counts'})
    top10 = yay1.head(10)
    print(top10)

    plt.figure(figsize=(15, 4))
    sns.lineplot(x=top10['count'], y=top10['Location'])
    plt.xlabel("Crime_Count ----->")
    plt.ylabel("Location")
    plt.title("Top 10 Crime Hotspots ")
    return plt.show()


#question4()


def question5():
    yay = df.Crm_Cd.value_counts()
    yay1 = yay.reset_index().rename(columns={'index': 'unique_values', 0: 'counts'})
    top10 = yay1.head(10)
    print(top10)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    sns.boxplot(yay1['count'], orient="h", ax=axes[0])
    axes[0].set_title("BoxPlot")
    sns.barplot(x=top10['Crm_Cd'], y=top10['count'], ax=axes[1])
    axes[1].set_title("BarPlot Top 10 Crime Count")
    return plt.show()


#question5()


conn.close()
