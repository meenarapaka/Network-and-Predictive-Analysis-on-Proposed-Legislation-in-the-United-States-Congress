# Network-and-Predictive-Analysis-on-Proposed-Legislation-in-the-United-States-Congress
In this project, we perform network analysis legislators from the past 50 decades and try to create a model to predict the legislative outcome of some bill introduced to the US Congress.
In our study, we extracted data from historical legislative records from ProPublica Data-store and transferred these to a RDBMS via our Extract-Transform-Load (ETL) process. 
The ETL process used employs Python’s Element Tree library to extract Legislative Metadata and placed this in a SQL database. Once there, we built a predictive model using the data returned in our SQL queries, combined with historical political information and network analysis from Gephi.
