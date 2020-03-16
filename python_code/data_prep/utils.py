def lower_columns(df, columns):
    for column in columns:
        df[column] = df[column].str.lower()
