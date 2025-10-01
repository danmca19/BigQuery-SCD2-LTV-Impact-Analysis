# 📈 SCD Type 2 with Risk Segment Impact on LTV  

This project demonstrates how to implement **Slowly Changing Dimensions (SCD) Type 2** in **Google BigQuery** to track changes in customer risk segments and analyze their impact on **Customer Lifetime Value (LTV)**.  

By combining **data engineering (ETL + SCD2)** with **business analytics (LTV segmentation)**, the project illustrates how historical tracking of customer attributes can drive **smarter retention, credit, and marketing strategies** by dimensional modeling and analytical enrichment. 

---

## 🎯 Why Use SCD Type 2?

SCD Type 2 is essential here because it ensures data integrity for historical analysis by allowing us to:

* **Track History:** Capture the temporal validity (`start_date` and `end_date`) for every risk segment a customer has held.
* **Enable Accurate Analysis:** Guarantee that every transaction (in the **`fact_transactions`**) is correctly tied to the **exact risk segment** the customer was in at the time of purchase.

### 🛠️ Architecture and Data Structure

The project follows a standard layered architecture to transform raw inputs into ready-to-use analytical data products:

| Layer | Key Components | Business Objective |
| :--- | :--- | :--- |
| **First Layer (Raw)** | Ingestion of `customers` and `transactions` | Collect daily risk updates and transaction records. |
| **Second Layer (Dimensional)** | **`fact_transactions`** and **`dim_customer_risk (SCD2)`** | Robust modeling to ensure historical traceability of risk status. |
| **Third Layer (Analytical)** | LTV Aggregations by Risk Segment | Deliver **actionable insights** directly to business teams. |

---

## 🗂️ Synthetic Dataset

We generated two synthetic datasets (1,000 rows each) to simulate a realistic customer lifecycle scenario:

| Dataset | Key Columns | Details |
| :--- | :--- | :--- |
| **`customers.csv`** | `customer_id`, `risk_segment`, `signup_date` | Simulates customer updates and changes in risk classification. |
| **`transactions.csv`** | `transaction_id`, `customer_id`, `amount` | Simulates purchase history and LTV accumulation. |

---

## 🔍 Key Analytical Insights and Discoveries

Analyzing the risk history revealed crucial trends for customer management:

| Segment / Transition | Average LTV (Estimated) | Business Implications |
| :--- | :--- | :--- |
| **Low-Risk** | $140 – $160 | Highest LTV, consistent retention, and low churn probability. |
| **Medium-Risk** | $90 – $110 | Critical opportunity for immediate **upsell/cross-sell** efforts. |
| **High-Risk** | $50 – $70 | Lowest LTV, highest churn probability, and elevated retention costs. |
| **Transition Medium → High** | 12–15% of customers | **Early Warning Signal:** Strongest indicator of LTV decline and imminent churn. |
| **Transition High → Medium** | **+20% LTV Lift** | Demonstrates the success of credit or retention recovery programs. |

---

## ✅ Actionable Business Recommendations

| Strategy | Project Insight | Recommendation |
| :--- | :--- | :--- |
| **Retention (Low-Risk)** | Most valuable customers with low marginal retention cost. | Invest in **loyalty programs** and exclusive perks to maximize their long-term value. |
| **Upselling (Medium-Risk)** | Largest growth opportunity. Recovered customers (High → Medium) show a +20% LTV increase. | Prioritize **cross-sell and upsell campaigns** designed to migrate this group to the Low-Risk segment. |
| **Credit & Fraud Control (High-Risk)** | Low LTV, high fraud risk, and retention costs often exceed potential ROI. | Apply **strict credit limits**, strengthen fraud monitoring, and minimize retention investment. |
| **Early Warning System** | The Medium → High transition is a frequent and critical churn signal. | Implement **real-time alerts** on risk\_segment changes to enable proactive measures, such as dedicated support or renegotiations. |
