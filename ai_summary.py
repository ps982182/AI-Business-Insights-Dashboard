def generate_ai_summary(results):

    summary = []

    summary.append(
        f"Total sales across all regions reached ${results['total_sales']:,}."
    )

    summary.append(
        f"The best selling product was {results['top_product']}."
    )

    top_region = results["region_sales"].idxmax()

    summary.append(
        f"The {top_region} region generated the highest sales."
    )

    return summary