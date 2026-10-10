# Loan approval check

A small Streamlit demo for a simple personal-loan eligibility pre-check. Enter
a CIBIL score, a loan amount up to ₹1,00,000, and a loan duration in months.
The app does not request or display PAN details.

The assessment is illustrative only: it uses a score threshold of 650 and is
not connected to a credit bureau or lender.

## Run

```powershell
.\.venv\Scripts\Activate.ps1
streamlit run app.py
```

Or install the dependencies with `pip install -r requirements.txt` before
running the app.
