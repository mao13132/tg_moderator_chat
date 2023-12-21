# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
async def check_link(text_msg):
    if text_msg is None:
        return False

    try:
        tex_message_lower = text_msg.lower()
    except Exception as es:
        print(f'check_link Ошибка при уменьшения регистра у tex_message "{text_msg}" ошибка "{es}"')

        return True

    if 'http:' in tex_message_lower or 'https:' in tex_message_lower:
        return True

    return False
