from fastapi import FastAPI
from routes import home,wrapper
app = FastAPI()

app.include_router(home.router)
app.include_router(wrapper.router,prefix='/in')

# Include the greeting router at "/greet" path and the items router at "/items" path
# app.include_router(greeting.router, prefix="/greet", tags=["greeting"])
# app.include_router(items.router, prefix="/items", tags=["items"])
