# 📈 SCD Type 2 with Risk Segment Impact on LTV  

This project demonstrates how to implement **Slowly Changing Dimensions (SCD) Type 2** in **Google BigQuery** to track changes in customer risk segments and analyze their impact on **Customer Lifetime Value (LTV)**.  

By combining **data engineering (ETL + SCD2)** with **business analytics (LTV segmentation)**, the project illustrates how historical tracking of customer attributes can drive **smarter retention, credit, and marketing strategies** by dimensional modeling and analytical enrichment. 

---

## 🗂️ Dataset Overview  

Two synthetic datasets were generated with **1,000 rows each** to simulate a realistic customer behavior scenario:  

### 1. `customers.csv`  
- **customer_id** → Unique ID for each customer  
- **name** → Fake customer name (generated with Faker)  
- **signup_date** → Customer acquisition date  
- **risk_segment** → Risk classification at acquisition (`Low`, `Medium`, `High`)  


### 2. `transactions.csv`  
- **transaction_id** → Unique ID for each transaction  
- **customer_id** → Foreign key linking to customers  
- **transaction_date** → Date of transaction  
- **amount** → Purchase amount (exponential distribution to mimic real-world spending)  


### 3. Data Products
- **First Layer** → Raw ingestion of customer risk updates and transactions

- **Second Layer** → Dimensional modeling with fact_transactions and dim_customer_risk (SCD2)

- **Third Layer** → Aggregations and analytical outputs (LTV segmented by risk)

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

#### Retention Strategy 
**Insight**: Customers in this segment show the highest LTV and strong retention, making them the most valuable group. The marginal cost of retention is low compared to the lifetime return.  
**Recommendation**: Invest in loyalty programs, exclusive perks, and tailored engagement initiatives to maximize their long-term value.  


#### Credit & Fraud Controls 
**Insight**: High-risk customers generate the lowest LTV and display higher churn probability, with retention costs often exceeding potential ROI.  
**Recommendation**: Apply strict credit limits, strengthen fraud monitoring, and minimize retention investment—focusing resources only when the expected return justifies it.  


#### Upselling Medium Risk 
**Insight**: Medium-risk customers maintain a moderate LTV but represent the largest growth opportunity. Historical patterns show that customers who moved from High → Medium increased their LTV by +20%.  
**Recommendation**: Prioritize cross-sell and upsell campaigns, product bundles, and targeted promotions to transition these customers toward the low-risk segment.  


#### Early Warning System 
**Insight**: Transitions such as Medium → High are frequent and strongly associated with declining LTV, serving as early churn signals.  
**Recommendation**: Implement real-time alerts on risk_segment changes, especially when customers move to higher risk levels, enabling proactive measures such as renegotiations, discounts, or dedicated support.  

