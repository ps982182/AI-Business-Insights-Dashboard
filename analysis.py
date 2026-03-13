import pandas as pd

def analyze_sales(df):

    # Total Sales 
    total_sales = df['sales'].sum()

    # Best Selling Product 
    top_product = df.groupby('product')['sales'].sum().idxmax()

    # Sales by Region 
    region_sales = df.groupby('region')['sales'].sum()

    # Monthly Sales Trend 
    monthly_sales = df.groupby('month')["sales"].sum()

    return {
        "total_sales": total_sales,
        "top_product": top_product,
        "region_sales": region_sales,
        "monthly_sales": monthly_sales
    }