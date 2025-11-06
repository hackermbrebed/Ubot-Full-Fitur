from PyroUbot import *
from datetime import datetime, timedelta

#Callback handler untuk tombol free trial
@PY.CALLBACK("informasi_ubot")
async def free_trial_callback(client, callback_query):
    user_id = callback_query.from_user.id

    # Cek apakah user sudah pernah mendapat premium gratis
    free_users = await get_list_from_vars(client.me.id, "informasi_ubot")
    if user_id in free_users:
        return await callback_query.answer("mohon menung gua akan send txt informasi tetang gua", show_alert=False)

    # Tambahkan 1 hari premium
    now = datetime.now(timezone("Asia/Jakarta"))
    expired = now + timedelta(hours=5)

    await set_expired_date(user_id, expired)
    await add_to_vars(client.me.id, "PREM_USERS", user_id)
    await add_to_vars(client.me.id, "FREE_PREM_USERS", user_id)

    # Kirim pesan ke user dengan status free trial
    await callback_query.answer("mohon menung gua akan send txt informasi tetang gua", show_alert=False)
    
    # Kirim pesan dengan tombol inline    
    await bot.send_message(
        user_id,
        f"""
<blockquote><b>
❏ ɪɴꜰᴏʀᴍᴀꜱɪ ʙᴏᴛ🤖
├ ᴏᴡɴᴇʀ : @kingofudin
├ ᴄʜᴀɴɴᴇʟ ꜱᴜᴘᴘᴏʀᴛ : @udiens123
╰ ɢʀᴜᴘ ꜱᴜᴘᴘᴏʀᴛ : @yamazzakki
ʙᴏᴛ ɪɴɪ ᴅɪʙᴜᴀᴛ ᴘᴀᴅᴀ ᴛᴀɴɢɢᴀʟ 01 ɴᴏᴠᴇᴍʙᴇʀ 2025.</b></blockquote>
𝘗𝘰𝘸𝘦𝘳𝘦𝘥 𝘣𝘰𝘵 𝘣𝘺 𝕂𝕒𝕚𝕤𝕒𝕣 𝕌𝕕𝕚𝕟👑
""",
  )
  
