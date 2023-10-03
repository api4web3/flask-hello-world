import os  # importing os module

def getKey():
    # value for env variable
    key = 'MONGO_DB'

    # invokinig os.getenv() with default= 'python/edpresso'
    value = os.getenv(key,default='False')
    return value

if __name__ == '__main__':
    getKey()
