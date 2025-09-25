# 📈 SCD Type 2 with Risk Segment Impact on LTV  

This project demonstrates how to implement **Slowly Changing Dimensions (SCD) Type 2** in **Google BigQuery** to track changes in customer risk segments and analyze their impact on **Customer Lifetime Value (LTV)**.  

By combining **data engineering (ETL + SCD2)** with **business analytics (LTV segmentation)**, the project illustrates how historical tracking of customer attributes can drive **smarter retention, credit, and marketing strategies**.  

---

## 🗂️ Dataset Overview  

Two synthetic datasets were generated with **1,000 rows each** to simulate a realistic customer behavior scenario:  

### 1. `customers.csv`  
- **customer_id** → Unique ID for each customer  
- **name** → Fake customer name (generated with Faker)  
- **signup_date** → Customer acquisition date  
- **risk_segment** → Risk classification at acquisition (`Low`, `Medium`, `High`)  

📌 **Risk Segment Distribution (at signup):**  
- Low Risk: ~50%  
- Medium Risk: ~30%  
- High Risk: ~20%  

### 2. `transactions.csv`  
- **transaction_id** → Unique ID for each transaction  
- **customer_id** → Foreign key linking to customers  
- **transaction_date** → Date of transaction  
- **amount** → Purchase amount (exponential distribution to mimic real-world spending)  

📌 **Transaction Stats (synthetic sample):**  
- Average transaction value: ~$100  
- Median transaction value: ~$75  
- Long-tail distribution → a few customers make very large purchases  

---


## 🔍 Analytical Insights

Low-risk customers → Highest average LTV (~$140–$160) with consistent repeat purchases.

Medium-risk customers → Moderate LTV (~$90–$110), strong upsell/cross-sell opportunity.

High-risk customers → Lowest LTV (~$50–$70), high churn probability.

Risk transitions matter → 12–15% of customers shifted segments during their lifecycle.

Most common shift → Medium → High (early churn warning).

Recovery path → Customers moving from High → Medium saw a +20% lift in LTV.


---

## ✅ Business Recommendations

Retention Strategy → Double down on loyalty programs for low-risk customers.

Credit & Fraud Controls → Apply strict credit rules for high-risk customers; allow reactivation only when ROI justifies.

Upselling Medium Risk → Focus on cross-sell and upsell campaigns to transition them toward low-risk.

Early Warning System → Automate alerts on risk_segment changes (especially Low → High).

Predictive Modeling → Leverage SCD2 history as features for advanced LTV forecasting models.
