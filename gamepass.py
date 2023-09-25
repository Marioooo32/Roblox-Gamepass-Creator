import requests
import tkinter as tk

def create_gamepass():
    game_id = game_id_entry.get()
    gamepass_name = gamepass_name_entry.get()
    auth_cookie = auth_cookie_entry.get()
    description = description_entry.get()
    price = price_entry.get()
    asset_id = asset_id_entry.get()

    url = f"https://api.roblox.com/groups/{game_id}/game-passes"

    headers = {
        "Content-Type": "application/json",
        "Cookie": auth_cookie
    }

    data = {
        "Name": gamepass_name,
        "Description": description,
        "PriceInRobux": int(price),
        "ProductId": game_id,
        "CurrencyType": 1,
        "CreatorType": "User",
        "IconImageAssetId": int(asset_id),
        "IconImageAssetVersionId": 0
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result_label.config(text="Gamepass created successfully!", fg="red")
    else:
        result_label.config(text="Failed to create gamepass.", fg="red")

# Create the GUI window
window = tk.Tk()
window.title("Gamepass Creator")
window.configure(bg="black")

# Set the window size and center it on the screen
window.geometry("400x350")
window.eval('tk::PlaceWindow . center')

# Create and position input labels and entry fields
game_id_label = tk.Label(window, text="Game ID:", fg="red", bg="black")
game_id_label.pack()
game_id_entry = tk.Entry(window)
game_id_entry.pack()

gamepass_name_label = tk.Label(window, text="Gamepass Name:", fg="red", bg="black")
gamepass_name_label.pack()
gamepass_name_entry = tk.Entry(window)
gamepass_name_entry.pack()

auth_cookie_label = tk.Label(window, text="Auth Cookie:", fg="red", bg="black")
auth_cookie_label.pack()
auth_cookie_entry = tk.Entry(window)
auth_cookie_entry.pack()

description_label = tk.Label(window, text="Description:", fg="red", bg="black")
description_label.pack()
description_entry = tk.Entry(window)
description_entry.pack()

price_label = tk.Label(window, text="Price in Robux:", fg="red", bg="black")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

asset_id_label = tk.Label(window, text="Asset ID:", fg="red", bg="black")
asset_id_label.pack()
asset_id_entry = tk.Entry(window)
asset_id_entry.pack()

# Create and position the create button
create_button = tk.Button(window, text="Create Gamepass", command=create_gamepass, bg="red", fg="black")
create_button.pack(pady=10)

# Create and position the result label
result_label = tk.Label(window, text="", fg="red", bg="black")
result_label.pack()

# Start the GUI event loop
window.mainloop()
