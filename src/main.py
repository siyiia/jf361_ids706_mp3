import polars as pl
import matplotlib.pyplot as plt


def analyse_data(file_path):
    df = pl.read_csv(file_path)
    numeric_df = df.select(pl.col(pl.Float64, pl.Int64))
    stats_data = numeric_df.describe()
    return numeric_df, stats_data


def create_visualization(
    df, stats_data, output_file="./output/data_visualization.png", color="skyblue"
):
    num_cols = df.shape[1]
    _, axes = plt.subplots(num_cols, 1, figsize=(8, num_cols * 4))

    for i, col in enumerate(df.columns):
        data = df[col].to_numpy()
        ax = axes[i] if num_cols > 1 else axes
        ax.hist(data, bins=10, edgecolor="black", color=color)

        mean_val = stats_data[col][2]
        median_val = stats_data[col][6]

        ax.axvline(
            mean_val,
            color="red",
            linestyle="dashed",
            linewidth=2,
            label=f"Mean: {mean_val:.2f}",
        )
        ax.axvline(
            median_val,
            color="blue",
            linestyle="dotted",
            linewidth=2,
            label=f"Median: {median_val:.2f}",
        )

        ax.set_title(f"Histogram of {col}")
        ax.set_xlabel("Value")
        ax.set_ylabel("Frequency")
        ax.legend()

    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()


def create_summary_report(
    df, summary_statistics, output_file="./output/summary_report.md"
):
    markdown_content = "# Summary Report\n\n"
    markdown_content += "## Dataset Overview\n\n"
    markdown_content += "This dataset provides a comprehensive overview of various factors affecting student performance in exams.\n\n"
    markdown_content += "### First 5 Rows of the Dataset\n\n"
    markdown_content += df.head().to_pandas().to_markdown() + "\n\n"

    markdown_content += "## Summary Statistics\n\n"
    markdown_content += summary_statistics.to_pandas().to_markdown() + "\n\n"

    markdown_content += "## Data Visualization\n\n"
    markdown_content += "![Data Visualization](./data_visualization.png)\n\n"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)


if __name__ == "__main__":
    raw_data, summary_stats = analyse_data("./StudentPerformanceFactors.csv")
    create_visualization(raw_data, summary_stats)
    create_summary_report(raw_data, summary_stats)
