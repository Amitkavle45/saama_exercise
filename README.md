# saama_exercise


# Saama Excercise Use-Case 1

It is a Scenario based Excercise, The Tasks which we have to perform 
are as follows
1. Data Cleanning
2. Changing DataTypes as per our requirements
3. Finally applying bussiness logic & transformations as mentioned in the final output Screenshot


# 
* The input file format on which we are working is '.csv'  
   it looks like


## 

![App Screenshot](https://raw.githubusercontent.com/Amitkavle45/saama_exercise/main/raw_SBIN.png)

## After loading the above file using Glue crawler output in Athena looks like

![App Screenshot](https://raw.githubusercontent.com/Amitkavle45/saama_exercise/main/sbin_athena.png)
# Final output 
## we have to Transform above file 
## as shown below in Summary Layer

![App Screenshot](https://raw.githubusercontent.com/Amitkavle45/saama_exercise/main/Image_20230102_193027_243.png)
## Tools used  

1. S3
2. AWS Glue
3. AWS Athena


## Data Pipeline 

## S3 --> Glue crawler --> Glue Job --> S3

## Step 1

* Reading Data (SBIN.csv) from S3 Using glue crawler
* Data Cleanning using glue job
* Removing extra special characters from columns like (")
* Store Cleaned file on S3 

## Code For Glue job

* Refer :- clean_sbin_job.py

## After Running above job successfully
* Check once file gets Cleaned or not
* For that we have to create another table using glue crawler

## Output should look like

![App Screenshot](https://raw.githubusercontent.com/Amitkavle45/saama_exercise/main/cleaned_sbin.png)

We can see The quotes from 'scripname' column gets removed  
as well as the DataType of 'Date' column we have to change into date from string

##  Transformation Applied on the Cleaned SBIN.csv

*  Creating New Column for Week Number
*  Creating New Column for Year
*  Grouping The Week_Num & Year columns
*  Creating Start_Date & End_Date Columns
*  Aggrigate the required columns ie. Open,High,Low

## For the above Transformations 
Refer :- Transformed_sbin.py

# Final Step
* Join transformed DataFrame to Cleaned DataFrame to get Expected output.
* Store Final output on S3 location.
Output Should look like

![App Screenshot](https://raw.githubusercontent.com/Amitkavle45/saama_exercise/main/Final_sbin.png)

### To Get the above output
Refer :- final_sbin.py


## Thank You !
