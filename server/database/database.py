import motor.motor_asyncio

MONGO_DETAILS = "mongodb+srv://EvokeMongoUser:EvokeMongoPass@cluster0.f8bvq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.myFirstDatabase

users_collection = database.get_collection("users")

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["userName"],
        "password": user["password"]

    }

# Retrieve all students present in the database
async def retrieve_users():
    users = []
    async for user in users_collection.find():
        users.append(user_helper(user))
    return users