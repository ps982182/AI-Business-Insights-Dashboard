def answer_query(df, question):

    if question == "Which product has the highest sales?":
        product = df.groupby("product")["sales"].sum().idxmax()
        return f"The product with the highest sales is {product}."

    elif question == "Which region has the highest sales?":
        region = df.groupby("region")["sales"].sum().idxmax()
        return f"The region generating the highest sales is {region}."

    elif question == "What are the total sales?":
        total = df["sales"].sum()
        return f"The total sales across the dataset are ${total:,}."

    elif question == "Which month had the highest sales?":
        month = df.groupby("month")["sales"].sum().idxmax()
        return f"The month with the highest sales is {month}."

    elif question == "Which product has the lowest sales?":
        product = df.groupby("product")["sales"].sum().idxmin()
        return f"The product with the lowest sales is {product}."

    else:
        return "No insight available."