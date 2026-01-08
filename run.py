import os

# Root project folder
PROJECT_NAME = "shopping-app"

# Folder structure
folders = [
    f"{PROJECT_NAME}/server/config",
    f"{PROJECT_NAME}/server/controllers",
    f"{PROJECT_NAME}/server/routes",
    f"{PROJECT_NAME}/client/src/api",
    f"{PROJECT_NAME}/client/src/pages",
    f"{PROJECT_NAME}/client/src/components",
]

# Files to create
files = [
    f"{PROJECT_NAME}/server/config/db.js",
    f"{PROJECT_NAME}/server/controllers/product.controller.js",
    f"{PROJECT_NAME}/server/controllers/order.controller.js",
    f"{PROJECT_NAME}/server/routes/product.routes.js",
    f"{PROJECT_NAME}/server/routes/order.routes.js",
    f"{PROJECT_NAME}/server/server.js",
    f"{PROJECT_NAME}/server/package.json",
    f"{PROJECT_NAME}/server/.env",

    f"{PROJECT_NAME}/client/src/api/axios.js",
    f"{PROJECT_NAME}/client/src/pages/Home.jsx",
    f"{PROJECT_NAME}/client/src/pages/Cart.jsx",
    f"{PROJECT_NAME}/client/src/pages/Checkout.jsx",
    f"{PROJECT_NAME}/client/src/pages/TrackOrder.jsx",
    f"{PROJECT_NAME}/client/src/pages/Admin.jsx",
    f"{PROJECT_NAME}/client/src/components/ProductCard.jsx",
    f"{PROJECT_NAME}/client/src/components/Navbar.jsx",
    f"{PROJECT_NAME}/client/src/App.jsx",
    f"{PROJECT_NAME}/client/src/main.jsx",
    f"{PROJECT_NAME}/client/package.json",
    f"{PROJECT_NAME}/client/.env",
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    with open(file, "w") as f:
        f.write("")

print("✅ Project structure created successfully!")
