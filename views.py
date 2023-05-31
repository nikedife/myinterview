from django.shortcuts import render
import random
# Create your views here.

import matplotlib.pyplot as plt
import datetime
import pymongo

#1
def simulate_profit_loss(request):
    value = random.uniform(-100, 100)  # Simulating profit or loss between -10 and 10 dollars
    context = {
        'value':value
    }
    return render(request,'index.html',context)

#2
# Store the data in the MongoDB collection
client = pymongo.MongoClient("mongodb://localhost:27017/") # Connect to MongoDB
db = client["traders"] # Create a database
collection = db["trader_data"] # Create a collection and Configure necessary data fields in settings

#3
def create_user_dashboard(request):
    timestamps = []
    profits = []
    for _ in range(60): # Simulating data for 1 hour (60 minutes)
        profit_loss = simulate_profit_loss(request)
        timestamps.append(datetime.datetime.now())
        profits.append(profit_loss)


        data = {
                "timestamp": timestamps,
                "profit_loss":  profits
           }

        collection.insert_one(data)


        plt.plot(timestamps, profits)
        plt.xlabel("Time")
        plt.ylabel("Profit/Loss")
        plt.show()

        return render(request,'userdash.html', data)
        #Dashboard
        #User dashboard


#4
def create_admin_dashboard(request):
    trader_data = collection.find() # Retrieve all trader data from the collection

    for data in trader_data:
        print(f"Timestamp: {data['timestamp']}, Profit/Loss: {data['profit_loss']}")
        #Admin dashboard
        context = {
            'Timestamp': {data['timestamp']},
            'Profit/Loss': {data['profit_loss']}
        }

        return render(request, 'adminuser.html', context)
    #