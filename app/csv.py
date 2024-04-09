# import csv
# from io import StringIO, BytesIO
# import asyncio
# import os


# # Create csv file
# output = StringIO()
# writer = csv.writer(output)
# for row in all_static:
#     writer.writerow(row)
# csv_data = output.getvalue()
# output.close()


# # csv file to download
# file_name = f"Admin-{datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M')}.csv"
# buffered_input_file = types.input_file.BufferedInputFile(file=csv_data.encode(), filename=file_name)
# try:
#     await bot.send_document(chat_id=chat_id, document=buffered_input_file)
#     await bot.answer_callback_query(callback_query.id)
# except:
#     print(f"Error sending documentb Admin stat")