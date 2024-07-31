# from models.user import User
# from core.database import db

# async def get_user_by_username(username: str) -> Optional[User]:
#     user = await db.users.find_one({"username": username})
#     return User(**user) if user else None

# async def create_user(user: User) -> User:
#     existing_user = await get_user_by_username(user.username)
#     if existing_user:
#         raise ValueError("Le nom d'utilisateur est déjà utilisé.")
    
#     await db.users.insert_one(user.dict())
#     return user
