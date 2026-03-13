import pandas as pd

def generate_report(results, insights):

    metrics = {
        "Metric": [
            "Total Sales",
            "Best Selling Product",
            "Top Performing Region"
        ],
        "Value": [
            results["total_sales"],
            results["top_product"],
            results["region_sales"].idxmax()
        ]
    }

    metrics_df = pd.DataFrame(metrics)

    insights_df = pd.DataFrame({
        "Business Insights": insights
    })

    return metrics_df, insights_df