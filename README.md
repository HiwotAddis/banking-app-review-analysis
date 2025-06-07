# Banking App Review Analysis

### Data Collection
- Used `google-play-scraper` to collect user reviews from three banking apps: CBE, BOA, and Dashen.
- Extracted fields: `review`, `rating`, `date`, `bank`, and `source`.
- Collected 400+ reviews per app (~1200+ total).

### Preprocessing
- Removed duplicate reviews.
- Dropped rows with missing critical fields (review, rating, date, bank).
- Normalized dates to `YYYY-MM-DD`.
- Exported a cleaned dataset to `data/cleaned_reviews.csv`.

### Tools Used
- Python
- pandas
- google-play-scraper
- Git/GitHub
