from repository import custom_repository
from collections import defaultdict



def fetch_sample_bookings():
    """
    Fetches sample bookings for demo
    """
    repository = custom_repository.Repository()
    bookings = repository.fetch_sample_bookings()
    return bookings


def search(capacity , startTime , endTime , Index):
    dic={}
    with open('database/booking.txt' ,'r') as DBdata:
        finalList =defaultdict(list)
        if capacity in DBdata and DBdata[capacity] >0:
            
            if startTime in DBdata and DBdata[startTime] > 0:
                
                if endTime in DBdata and DBdata[endTime] > 0:
                    
                    dic[Index].append(DBdata[hallname])
                    return finalList
                
                
        
        





