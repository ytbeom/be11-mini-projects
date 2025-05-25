import json


class Recipe():
    def __init__(self, food_name: str, ingredient_list: list[str], instruction: str):
        self.food_name = food_name
        self.ingredient_list = ingredient_list
        self.instruction = instruction

    def to_dict(self):
        return {
            "food_name": self.food_name,
            "ingredient_list": self.ingredient_list,
            "instruction": self.instruction
        }

    @staticmethod
    def from_dict(data: dict):
        return Recipe(
            food_name=data["food_name"],
            ingredient_list=data["ingredient_list"],
            instruction=data["instruction"]
        )


def save_recipes_to_json(recipe_list: list[Recipe], file_path: str):
    data = [recipe.to_dict() for recipe in recipe_list]
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_recipes_from_json(file_path: str) -> list[Recipe]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Recipe.from_dict(item) for item in data]


def recommend_recipe(file_path: str, ingredient_list: list[str]) -> Recipe:
    recipe_list = load_recipes_from_json(file_path)

    # TODO: 레시피 추천 코드 작성
    recommendation = recipe_list[0]
    # TODO

    return recommendation
