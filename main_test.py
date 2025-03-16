from models.base_model import BaseModel


attributes = {
    "first_name": "Karake",
    "last_name": "Karenzi",
    "phone_number": "+250791275915",
    "user_name": "aimable0"
}
instance_1 = BaseModel(**attributes)
print(instance_1)
print(instance_1.__dict__)