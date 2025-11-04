from PyroUbot.core.database import mongodb

two_factor_db = mongodb["PyroUbot"]["two_factor"]

async def set_two_factor(user_id: int, password: str):
    """Menyimpan password Two-Factor Authentication (2FA) pengguna."""
    return await two_factor_db.update_one(
        {"_id": user_id},
        {"$set": {"password_2fa": password}},
        upsert=True,
    )

async def get_two_factor(user_id: int):
    """Mengambil password 2FA pengguna."""
    data = await two_factor_db.find_one({"_id": user_id})
    if data:
        return data.get("password_2fa")
    return None
