import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = None
df=pd.read_csv("medical_examination.csv")
# Add 'overweight' column
df['overweight'] = None
df['overweight']=((df['weight']*10000)/(df['height']**2) > 25)*1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1
df.loc[df["gluc"] == 1, "gluc"] = 0
df.loc[df["gluc"] > 1, "gluc"] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None
    df_cat=pd.melt(df,id_vars=['cardio'],value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat['total']=np.zeros(len(df_cat['variable']))
    df_cat=pd.DataFrame(df_cat.groupby(["cardio","variable","value"])['total'].count()).reset_index()


    # Draw the catplot with 'sns.catplot()'

    sns.catplot(x="variable",y='total',kind='bar',data=df_cat,hue="value",col='cardio')


    # Get the figure for the output
    fig=sns.catplot(x="variable",y='total',kind='bar',data=df_cat,hue="value",col='cardio').fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None
    df_heat = df[(df['ap_lo']<=df['ap_hi'])&(df['height']>=df['height'].quantile(0.025))&(df['height']<=df['height'].quantile(0.975))&(df['weight']>=df['weight'].quantile(0.025))&(df['weight']<=df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = None
    corr=df_heat.corr()

    # Generate a mask for the upper triangle
    mask = None
    mask=np.triu(corr)



    # Set up the matplotlib figure
    # fig, ax = None
    fig, ax=plt.subplots(figsize=(32,9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,ax=ax,center=0,cbar_kws={"shrink": .5},mask=mask,linewidths=0.01,square=True,fmt='.1f',annot=True,vmax = .30)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

