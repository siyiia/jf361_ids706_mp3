# jf361_ids706_mp3
[![CICD](https://github.com/siyiia/jf361_ids706_mp3/actions/workflows/cicd.yml/badge.svg)](https://github.com/siyiia/jf361_ids706_mp3/actions/workflows/cicd.yml)


 ## Project Introduction
This project is to create `Polars` descriptive statistics script.

## Project Requirments
- Python script using `Polars` for descriptive statistics
- Read a dataset (CSV or Excel)
- Generate summary statistics (mean, median, standard deviation)
- Create at least one data visualization

## Project Setup
1. **Read a CSV file** The first step is to read the dataset using `Polars`. This allows you to load the data into a DataFrame for further analysis:
    ```
   import polars as pl
   df = pl.read_csv(file_path)
   ```
2. **Analyze Summary Statistics**: `Polars` provides a convenient method `describe()` to generate summary statistics such as count, mean, standard deviation (std), minimum, and maximum for each numeric column in the dataset.
   ```angular2html
    analysed_data = df.describe()
    print(analysed_data)
    ```
3. **Visualizing the Data**: Histograms are generated for each numeric column. The detailed code of `create_visualization()` method is in the `src/main.py` file.
4. **Generate a Report**: The summary statistics and visualizations are compiled into a Markdown report. The detailed code of `create_summary_report()` method is in the `src/main.py` file.
5. **Generate a Report via CI/CD**: 
   1. In GitHub repo `Setting` -> `Actions` -> `General`, granting `Read and write permissions` allows workflows to modify your repository
   2. In `CICD.yml` file, add following code to push a dictionary to a repository
      ```angular2html
      - name: push report
        run: |
          if [ -n "$(git status --porcelain)" ]; then
            git config --local user.email "push_report@test.com"
            git config --local user.name "Push Report"
            git add .
            git commit -m "Add visualization and summary report" 
            git push
          else
            echo "No changes to commit"
          fi
      ```


## Project Output
The markdown summary report is under the `output` dictionary with name `summary_report.md`. You can find them here [Summary Report](./output/summary_report.md).