import pandas as pd

df = pd.read_csv("Reddit Dataset.csv",encoding="ISO-8859-1") 
df_s = pd.DataFrame(columns=df.columns) # S for same, No need tie-breaking
df_c = pd.DataFrame(columns=df.columns) # Chloe as the tie breaker
df_y = pd.DataFrame(columns=df.columns) # Me as the tie breaker
df_r = pd.DataFrame(columns=df.columns) # Robbie as the tie breaker

def filter(startRow, endRow, col1, col2, tieBreaker):
    global df_s # declare global
    global df_c
    global df_y
    global df_r
    for i in range (startRow,endRow):
        if(df.at[i,col1].lower() == df.at[i,col2].lower()):
            df.at[i,'final topic'] = df.at[i,col1].lower()
            df_s = df_s.append(df.iloc[i])
        else:
            if (tieBreaker == "Topic (Robbie)"):
                df_r = df_r.append(df.iloc[i])
            elif (tieBreaker == "Topic (Yunyi)"):
                df_y = df_y.append(df.iloc[i])
            else:
                df_c = df_c.append(df.iloc[i])

# order: start row (inclusive), end row (exclusive), 2 annotators + tie breaker
filter(1,251,"Topic (Robbie)","Topic (Yunyi)","Topic (Chloe)") 
filter(251,499,"Topic (Robbie)","Topic (Chloe)","Topic (Yunyi)") 
filter(499,749,"Topic (Yunyi)","Topic (Chloe)","Topic (Robbie)") 
filter(749,999,"Topic (Yunyi)","Topic (Robbie)","Topic (Chloe)") 
filter(999,1249,"Topic (Chloe)","Topic (Robbie)","Topic (Yunyi)") 
filter(1249,1501,"Topic (Chloe)","Topic (Yunyi)","Topic (Robbie)") 


# Combine df_y, df_c and df_r
df_d = df_y.append(df_c)
df_d = df_d.append(df_r)

#Combine df_d and df_s into one outfile
df_out = df_d.append(df_s)

# Write the data frames into csv
df_out.to_csv('filtered Reddit Dataset.csv')









