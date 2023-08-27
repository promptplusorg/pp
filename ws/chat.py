from string import Template
# from fastapi.templating import Jinja2Templates
import os
import logging

from fastapi.websockets import WebSocket

from fastapi import APIRouter
router = APIRouter()

print(os.getcwd())

chat = open("pp/templates/chatbot.html", "r")
src = Template(chat.read())
print(src)

# with open('foo.txt', 'r') as f:
#     src = Template(f.read())
#     result = src.substitute(d)
#     print(result)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print("BASE_DIR", BASE_DIR)
# TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
# print("TEMPLATE_DIR", TEMPLATE_DIR)
# templates = Jinja2Templates(directory=TEMPLATE_DIR)
# # templates = Jinja2Templates(directory="pp/templates")
# print("templates", templates)

# @router.websocket_route("/ws")


@router.websocket_route("/chatline")
async def websocket_endpoint_chatline(websocket: WebSocket):

    await websocket.accept()
    print("websocket.accept() accepted")

    logging.info("WebSocket connection established.")
    await websocket.send_text("promptplus_id: WebSocket Connected")

    try:

        from embedchain import App
        from dotenv import load_dotenv
        load_dotenv()
        ok = os.getenv('openai')
        os.environ["OPENAI_API_KEY"] = ok
        elon_musk_bot = App()

        from ..utilities import refresh_file
        path_to_sandbox_folder, file_list_in_sandbox = refresh_file()

        for i, file_name in enumerate(file_list_in_sandbox):
            file_path = os.path.join(path_to_sandbox_folder, file_name)
            try:
                print(i+1, file_path)
                elon_musk_bot.add(file_path, data_type='pdf_file')
                print(i+1, "added")
            except:
                pass

        while True:
            data = await websocket.receive_text()
            logging.info(f"Received WebSocket message: {data}")

            # prompt =
            # prompt = "<h1>"+data+"</h1>"
            # prompt = f"""<li class="max-w-4xl py-2 px-4 sm:px-6 lg:px-8 mx-auto flex gap-x-2 sm:gap-x-4">
            # <span class="flex-shrink-0 inline-flex items-center justify-center h-[2.375rem] w-[2.375rem] rounded-full border-2 border-yellow-400">
            # <span class="leading-none font-extrabold text-sm text-yellow-400">>_</span></span>
            # <div class="space-y-3 font-medium text-gray-800 dark:text-white">{data}</div></li>"""

            # await websocket.send_text(templates.TemplateResponse("chatbot.html", {"data": data}))
            # await websocket.send_text(templates.TemplateResponse("chatbot.html",  {"request": request, "data": data}))

            prompt = src.substitute({"data": data})
            print("prompt", prompt)
            await websocket.send_text(prompt)

            # do some lang chain here now
            # text = "How many companies does Elon Musk run?"
            text = data
            res = "error"
            try:
                print("text", text)
                # res = chat(text)
                # do you have embed files?
                res = elon_musk_bot.query(text)
                print("res", res)
                # ref_fmt = res
                # ref_fmt = "<h1>"+res+"</h1>"
                ref_fmt = f"""<li class="max-w-4xl py-2 px-4 sm:px-6 lg:px-8 mx-auto flex gap-x-2 sm:gap-x-4">
            <span class="flex-shrink-0 inline-flex items-center justify-center h-[2.375rem] w-[2.375rem] rounded-full border-2 border-green-500">
            <span class="leading-none font-extrabold text-sm text-green-500">id</span></span>
            <div class="space-y-3 font-medium text-gray-800 dark:text-white">{res}</div></li>"""
                await websocket.send_text(ref_fmt)
            except:
                await websocket.send_text(res)

    except WebSocketDisconnect as e:
        logging.warning(f"WebSocket disconnected with code: {e.code}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        # This will log the full traceback of the exception
        logging.error(traceback.format_exc())
        await websocket.send_text(f"Error: {e}")
