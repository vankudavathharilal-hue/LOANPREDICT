import streamlit as st


MAX_LOAN_AMOUNT = 100_000
MIN_CIBIL_SCORE = 650


st.set_page_config(
    page_title="Loan approval check",
    page_icon=":material/account_balance:",
    layout="centered",
)

st.title("Loan approval check")
st.caption("Simple sample assessment for loans up to ₹1,00,000.")

with st.form("eligibility_check", border=True):
    applicant_name = st.text_input("Applicant name", max_chars=80)
    score_col, amount_col = st.columns(2)
    with score_col:
        cibil_score = st.number_input(
            "CIBIL score",
            min_value=300,
            max_value=900,
            value=700,
            step=25,
            help="Use the + and − controls to change the score by 25 points.",
        )
    with amount_col:
        loan_amount = st.number_input(
            "Loan amount (₹)",
            min_value=25_000,
            max_value=MAX_LOAN_AMOUNT,
            value=25_000,
            step=25_000,
            format="%d",
            help="Use the + and − controls to change the amount by ₹25,000.",
        )
    loan_duration = st.selectbox(
        "Loan duration (months)",
        [6, 12, 18, 24, 36, 48, 60],
        index=1,
    )
    st.caption(
        f"Assessment guide: scores of {MIN_CIBIL_SCORE}+ meet this demo's "
        "sample threshold. This is not a lender decision."
    )
    submitted = st.form_submit_button("Check eligibility", type="primary")

if submitted:
    if not applicant_name.strip():
        st.error("Enter the applicant name to see the assessment.")
    else:
        with st.container(border=True):
            st.subheader("Assessment")
            st.write(f"Applicant: **{applicant_name.strip()}**")
            amount_col, duration_col, score_col = st.columns(3)
            amount_col.metric("Loan amount", f"₹{loan_amount:,.0f}")
            duration_col.metric("Duration", f"{loan_duration} months")
            score_col.metric("CIBIL score", f"{cibil_score}")
            if cibil_score >= MIN_CIBIL_SCORE:
                st.success(
                    f"Meets the sample score threshold ({MIN_CIBIL_SCORE}+). "
                    "The application may be reviewed by a lender."
                )
            else:
                st.warning(
                    f"Does not meet the sample score threshold "
                    f"({MIN_CIBIL_SCORE}+). A lender may decline the application."
                )

st.caption("Demo only — this is not a credit check or loan approval.")
