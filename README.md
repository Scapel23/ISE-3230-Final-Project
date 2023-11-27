# ISE-3230-Final-Project
Code for MILP Optimization 
The situation is as follows: 
Within the subway system, there are 7 trains categorized into two series:   Series A comprising Trains 1, 2, and 3, and Series B comprising Trains 4, 5, 6, and 7. 
To manage the impending evening rush hour congestion, the system requires maintenance and scheduling optimization for the trains. 
The evening rush hour spans three hours, segmented into the first, second, and third hours. 
Throughout this time, the subway system encounters an average demand of around 580 passengers per hour. 
Unmet passenger demand during this period can result in additional waiting costs. 
The required tasks: 
Train Maintenance Planning: Plan to replace at least one train from Series A for maintenance while selecting trains from Series B to ensure that 5 trains are 
operational each hour. 
Operational Costs and Passenger Demand: Consider the operational costs and passenger capacity of each train in different time slots, 
as well as the waiting costs for unmet passenger demand. 
Operating Restrictions for Series A Trains: Ensure that each train from Series A does not exceed a total of 2 hours of operation. 
Passenger Demand Fulfillment: Ensure that the demand of at least 250 passengers per hour is met. 
The goal is to design a cost-effective and efficient train operation plan that meets the passenger demand and maintenance requirements 
during the evening rush hour. 


The data used for the project is as follows:
cost = [Train 1[100, 110, 120], Train 2[110, 120, 125], Train 3[100, 115, 125],
        Train 4[150, 155, 165], Train 5[105, 120, 115], Train 6[130, 140, 145], Train 7[135, 145, 150]]



capacity = [Train 1[50, 50, 50], Train 2[60, 60, 60], Train 3[55, 55, 55],
            Train 4[70, 60, 65], Train 5[55, 40, 50], Train 6[60, 55, 60], Train 7[60, 55, 60]]
