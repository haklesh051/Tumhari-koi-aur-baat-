import aiosqlite
import os

DB_PATH = "thumbs.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS thumbs(user_id INTEGER PRIMARY KEY, msg_id INTEGER)"
        )
        await db.commit()

async def df_thumb(user_id, msg_id):
    """Insert or update thumbnail record"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR REPLACE INTO thumbs(user_id, msg_id) VALUES(?, ?)",
            (user_id, msg_id)
        )
        await db.commit()

async def del_thumb(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM thumbs WHERE user_id = ?", (user_id,))
        await db.commit()

async def thumb(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT msg_id FROM thumbs WHERE user_id = ?", (user_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                class Obj: pass
                o = Obj()
                o.msg_id = row[0]
                return o
            return None
