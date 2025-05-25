from utils import recommend_recipe


ingredient_input = input("재료를 입력하세요 (여러 개는 쉼표로 구분): ")
ingredient_list = [i.strip() for i in ingredient_input.split(",") if i.strip()]

# TODO: 실제 실행 시에는 파일 이름을 recipes.json 으로 변경
recommendation = recommend_recipe("sample_recipes.json", ingredient_list)
# TODO

print(f"\n[추천 레시피 - {recommendation.food_name}]")
print(f"\n[설명]\n{recommendation.instruction}\n")
