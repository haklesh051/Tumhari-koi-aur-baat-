import os

# Dummy DB functions
async def df_thumb(user_id, msg_id):
    # yaha normally DB me save karte
    # abhi ke liye skip kar dete
    return True

async def del_thumb(user_id):
    # DB se thumb delete karna hota
    return True

async def thumb(user_id):
    # DB se thumb fetch karna hota
    return None
