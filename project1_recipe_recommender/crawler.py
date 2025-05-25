import json
import requests
from bs4 import BeautifulSoup

from utils import Recipe, save_recipes_to_json


def crawl_recipes(food_name_list: list[str]):
    recipe_list = []
    for food_name in food_name_list:
        recipe_id = get_recipe_id(food_name)
        if recipe_id == "":
            continue
        try:
            url = f"https://www.10000recipe.com/recipe/{recipe_id}"
            response = requests.get(url)
            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            recipe_info = json.loads(soup.find(attrs={'type':'application/ld+json'}).text)
            # print(recipe_info)

            # TODO: recipe_info 값을 파싱해서 재료와 설명을 추출
            ingredient_list = []
            instruction = ""
            # TODO

            recipe = Recipe(food_name, ingredient_list, instruction)
            recipe_list.append(recipe)
        except:
            continue

    # TODO: 실제 실행 시에는 파일 이름을 recipes.json 으로 변경
    save_recipes_to_json(recipe_list, "sample_recipes.json")
    # TODO


# 요리 이름으로 검색한 뒤 첫 번째 recipe의 id를 반환하는 함수
def get_recipe_id(food_name: str) -> str:
    url = f"https://www.10000recipe.com/recipe/list.html?q={food_name}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return ""
        soup = BeautifulSoup(response.text, "html.parser")
        recipe_list = soup.find_all(attrs={"class":"common_sp_link"})
        recipe_id = recipe_list[0]["href"].split("/")[-1]
        return recipe_id
    except:
        return ""


if __name__ == "__main__":
    # TODO: 실제 실행시에 수집하고 싶은 요리 이름을 list 형태로 작성
    food_name_list = ["김치찌개", "된장찌개"]
    # TODO
    
    crawl_recipes(food_name_list)
